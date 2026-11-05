# 6. Pagos online

## La idea

En una tienda física, el precio lo marca **la caja**, no la etiqueta que trae el cliente en la mano.
Si el cliente pudiera escribir su propio precio, todo costaría un euro. En una web, todo lo que viene
del navegador es esa etiqueta: se puede cambiar.

## Qué puede salir mal

- **Precio manipulado**: la web manda al servidor «producto 7, precio 120 €». El atacante cambia el
  precio a 1 € antes de enviar.
- **Pago fingido**: el servidor da el pedido por pagado porque el navegador vuelve a la página de
  «gracias por tu compra», sin comprobar que el pago se completó.
- **Aviso de pago falso**: alguien envía a tu servidor un aviso inventado de «pago completado».
- **Doble abono**: la pasarela repite el mismo aviso (lo hacen a propósito si no respondes a tiempo)
  y tu servidor suma el saldo dos veces.
- **Datos de tarjeta en tu servidor**: si pasan por tu código, te obligan a cumplir la norma PCI DSS
  completa, que es muy exigente.

## Cómo se hace bien

### 1. El servidor calcula el importe

El navegador solo dice **qué** quiere comprar (identificadores y cantidades). El servidor busca los
precios en su base de datos, calcula descuentos, impuestos y gastos de envío, y crea el pago con ese
importe. Si el cliente manda un precio, se ignora.

### 2. La tarjeta no pasa por tu servidor

Usa la **página de pago alojada** por la pasarela (Stripe Checkout, Redsys, PayPal, Adyen…) o sus
componentes incrustados. El cliente teclea la tarjeta en la página de la pasarela; tú solo recibes un
identificador del pago. Así tu carga de cumplimiento PCI DSS es la mínima (el cuestionario más
corto, el **SAQ A**).

En Europa, la directiva PSD2 exige **autenticación reforzada** (SCA) en la mayoría de pagos con
tarjeta: el típico código o la confirmación en la app del banco. Las páginas alojadas de las
pasarelas ya lo gestionan.

### 3. El pago se confirma por webhook firmado

Un **webhook** es un aviso que la pasarela envía a tu servidor cuando pasa algo («pago completado»,
«reembolso», «disputa»). Es **la única fuente de verdad** del pago, no la vuelta del navegador.

| Regla | Por qué |
|---|---|
| **Verificar la firma** de cada aviso con el secreto del webhook | Cualquiera puede enviar peticiones a tu dirección; solo la pasarela conoce el secreto |
| Verificar sobre el **cuerpo original**, sin transformarlo | Si el código lee y reescribe el JSON antes, la firma ya no coincide |
| Rechazar avisos **antiguos** | Stripe usa por defecto una tolerancia de 5 minutos. Evita que alguien reenvíe un aviso viejo capturado |
| **Idempotencia**: guardar el identificador de cada evento procesado | Si llega dos veces, la segunda no hace nada |
| Responder rápido (código 2xx) y hacer el trabajo pesado después | Si tardas, la pasarela lo da por fallido y lo repite |
| Contrastar el importe y la moneda con el pedido | Que el pago completado corresponda de verdad a lo que se vendió |

El webhook es la única ruta de tu web que recibe peticiones que no vienen de tu navegador, así que no
puede usar la comprobación de `Origin` del apartado 4.4. **Su protección es la firma.**

**Para quien quiera ver código** (Python con la librería oficial de Stripe):

```python
evento = stripe.Webhook.construct_event(
    payload=cuerpo_original_en_bytes,
    sig_header=cabeceras["Stripe-Signature"],
    secret=SECRETO_DEL_WEBHOOK,
)
# Si la firma no es válida o el aviso es antiguo, lanza un error y no se abona nada.
```

### 4. Reembolsos y disputas

Una **disputa** (*chargeback*) es cuando el titular de la tarjeta reclama el cargo a su banco. Tu
servidor debe escuchar también esos avisos: avisar a una persona y, si hay saldo o servicio
pendiente, congelarlo hasta revisarlo.

### 5. Las claves de la pasarela

| Clave | Dónde puede estar |
|---|---|
| Clave **publicable** (en Stripe empieza por `pk_`) | Puede ir en el navegador |
| Clave **secreta** (en Stripe empieza por `sk_`) | Solo en el servidor, en una variable de entorno |
| Secreto del **webhook** (en Stripe empieza por `whsec_`) | Solo en el servidor |

Usa **claves restringidas** (con los permisos justos) cuando la pasarela las ofrezca, y el **modo de
pruebas** para todo el desarrollo.

## Cómo comprobarlo

- Cambia el importe en la petición desde las herramientas del navegador: el servidor debe ignorarlo.
- Envía un webhook sin firma o con la firma de otro secreto: rechazado, sin abono.
- Envía el mismo evento dos veces (la CLI de Stripe lo permite con `stripe trigger` y `stripe events
  resend`): un solo abono.
- Cierra el navegador justo después de pagar, sin volver a tu web: el pedido debe quedar pagado
  igualmente, porque lo confirma el webhook.
