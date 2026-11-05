# 5. Lo que entra: formularios, consultas, archivos y límites

## 5.1 Validar en el servidor

### La idea

La validación del navegador (el campo que se pone rojo si el correo está mal) es **comodidad para el
usuario**, no seguridad. Es como el cartel de «prohibido el paso» en la puerta del almacén: orienta a
la gente honrada, pero no para a nadie. Cualquiera puede saltarse el navegador y enviar peticiones
directamente a tu servidor con lo que quiera.

### Cómo se hace bien

- **Toda entrada se valida en el servidor**, aunque ya se validara en el navegador.
- Se valida con un **esquema**: una descripción de qué campos se esperan, de qué tipo, con qué
  longitud máxima y con qué formato (Pydantic en Python, Zod en JavaScript, Bean Validation en Java…).
- **Lista blanca**, no lista negra: se dice qué se acepta, no qué se prohíbe. Lo que no está en la
  lista, fuera.
- **Rechazar campos que no se esperan.** Si alguien añade `"es_admin": true` al registro, debe dar
  error, no ignorarse ni, peor aún, guardarse.
- **Longitud máxima en todo**, también en los campos de texto libre. Un mensaje de 50 MB puede tumbar
  el servidor.
- **Mensajes de error limpios**: qué campo está mal y por qué, sin rutas de archivos, nombres de
  tablas ni trazas del código.

### Cómo comprobarlo

Con `curl` o con una herramienta como Bruno o Postman, envía a cada formulario: campos de más, textos
de 100.000 caracteres, un número donde va un texto, un correo sin `@`. Todo debe responder con un
error limpio (código 400 o 422), nunca con un 500.

## 5.2 Inyección: consultas parametrizadas

### La idea

Le dictas a un ayudante: «busca en el archivo la ficha de **Pérez**». Si un cliente se llama
`Pérez; y luego quema el archivo`, y el ayudante lo lee todo como una sola orden, tienes un problema.
La **inyección SQL** es eso: el dato del usuario se mezcla con la orden a la base de datos y acaba
formando parte de ella.

### Cómo se hace bien

Se separan siempre **la orden** y **los datos**. A eso se le llama consulta **parametrizada**: la
base de datos recibe la orden con huecos y, aparte, los valores que van en cada hueco. Nunca los
confunde.

**Para quien quiera ver código** (Python):

```python
# MAL: el texto del usuario pasa a formar parte de la orden
cursor.execute(f"SELECT * FROM usuarios WHERE correo = '{correo}'")

# BIEN: la orden lleva un hueco y el valor va aparte
cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
```

Los ORM (SQLAlchemy, Prisma, Django ORM, Hibernate…) parametrizan solos **mientras no construyas
texto a mano**. El riesgo vuelve en cuanto aparece una consulta «en crudo» montada con texto.

La misma idea vale para **otras inyecciones**: órdenes del sistema operativo (no construyas comandos
con datos del usuario), plantillas, LDAP o consultas a bases NoSQL.

### Cómo comprobarlo

Busca en el código consultas montadas con texto (`f"SELECT`, `+ "WHERE`, `.format(` cerca de SQL).
Y prueba a escribir `' OR '1'='1` y `'; DROP TABLE usuarios; --` en el login y en los buscadores: la
respuesta debe ser un error normal, nunca un 500 ni datos de otros.

## 5.3 Subida de archivos

### La idea

Recibir un archivo de un desconocido es como **recibir un paquete sin remite en el taller**: no lo
abres encima del banco de trabajo, no te fías de lo que pone la etiqueta y no lo guardas junto a las
herramientas.

### Qué puede salir mal

- Un archivo `.php` o `.jsp` subido como «foto» que luego el servidor **ejecuta**.
- Un archivo enorme que **llena el disco** o cuelga el servidor.
- Un nombre como `../../config/.env` que **sobrescribe** archivos del servidor.
- Un archivo con **virus** que luego abre tu personal.
- Un SVG o HTML subido como imagen que lleva **JavaScript** dentro (XSS).
- Archivos privados accesibles para cualquiera que **adivine la dirección**.

### Cómo se hace bien

| Regla | Cómo |
|---|---|
| Lista cerrada de tipos | Solo las extensiones que necesitas (por ejemplo `.jpg`, `.png`, `.pdf`) |
| Tipo comprobado por el contenido | Se leen los **primeros bytes** del archivo (su «firma»), no la extensión ni el `Content-Type` que manda el navegador |
| Tamaño máximo | Se corta en el servidor **antes** de recibir el archivo entero |
| Nombre interno aleatorio | El archivo se guarda con un identificador generado; el nombre original, si hace falta, solo en la base de datos |
| Fuera del servidor web | En un almacenamiento de objetos privado (tipo S3), nunca en una carpeta que la web sirva |
| Descarga controlada | Enlace firmado que caduca en minutos, emitido solo después de comprobar que el usuario tiene permiso |
| Imágenes reprocesadas | Volver a generar la imagen elimina contenido oculto y metadatos (por ejemplo, la ubicación GPS de una foto) |
| Antivirus | Si el personal va a abrir lo que suben los clientes |
| Cupos | Número de subidas por usuario y por hora |

### Cómo comprobarlo

Renombra un `.exe` a `.pdf` y súbelo: debe rechazarse. Sube un archivo un byte por encima del máximo:
debe rechazarse sin colgar nada. Usa el archivo de prueba **EICAR** (inofensivo, pero todos los
antivirus lo detectan) para comprobar el antivirus. Copia el enlace de descarga, espera a que
caduque o úsalo con otra cuenta: debe fallar.

## 5.4 Límite de peticiones

### La idea

Un mostrador atiende a una persona cada vez. Si alguien se pone a pedir mil cosas por minuto, se le
pide que espere. El **límite de peticiones** (*rate limiting*) protege contra la fuerza bruta, el
envío masivo de formularios, el abuso de servicios que te cuestan dinero (enviar correos, consultar
una IA) y parte de los intentos de tumbar la web.

### Cómo se hace bien

- **Cupos por ruta**, más estrictos donde más duele: login, registro, recuperación de contraseña,
  formulario de contacto, subida de archivos, llamadas a servicios de pago.
- **Por IP y por cuenta**, porque un atacante puede cambiar de IP.
- **Respuesta 429** («demasiadas peticiones») con un mensaje claro y, si puedes, la cabecera
  `Retry-After`.
- **La IP correcta.** Si tu web está detrás de un proxy o una CDN, la IP real llega en una cabecera.
  Usa la que tu proveedor **garantiza** que no puede falsificar el visitante. `X-Forwarded-For` tal
  cual suele poder inventarse, y entonces el atacante se salta el límite cambiándola.
- **Contador compartido.** Si guardas el contador en la memoria de un servidor y tienes varios, cada
  uno lleva su cuenta. Con más de un servidor, el contador va a una base de datos o a Redis.

### Contra los ataques masivos

Un límite en tu código no aguanta un ataque de denegación de servicio grande (DDoS). Para eso está la
protección de la red: la mayoría de alojamientos y CDN (Cloudflare, Fastly, AWS CloudFront…) la
incluyen. Comprueba qué ofrece la tuya.

## 5.5 SSRF: que tu servidor visite lo que no debe

### La idea

Le pides al recadero que te traiga un paquete de una dirección. Si el cliente le da la dirección
**de tu propia caja fuerte**, el recadero, que tiene llave, la abre. El **SSRF** ocurre cuando tu
servidor descarga una dirección que le pasa el usuario (una imagen por URL, una vista previa de un
enlace, un aviso a otra web) y el atacante le hace pedir direcciones internas: la base de datos, el
panel del alojamiento o el servicio de metadatos de la nube, que guarda credenciales.

### Cómo se hace bien

- Si puedes, **no descargues direcciones que manda el usuario**.
- Si hace falta: lista cerrada de dominios permitidos, solo `https`, y bloqueo de direcciones
  internas (`127.0.0.1`, `10.x`, `192.168.x`, `169.254.169.254`…) **después** de resolver el nombre,
  no antes.
- No sigas redirecciones automáticamente: una dirección permitida puede redirigir a una prohibida.
