# 9. Vigilar, copiar y reaccionar

## 9.1 Registro y vigilancia

### La idea

Una cámara que graba pero que nadie mira sirve para saber qué pasó, no para evitarlo. Un sistema de
alarma avisa en el momento. Una web necesita **las dos cosas**: un registro de lo que pasa y avisos
cuando pasa algo raro.

### Qué registrar

- **Accesos**: entradas correctas y fallidas, bloqueos de cuenta, cierres de sesión.
- **Cambios sensibles**: contraseña, correo, segundo factor, permisos y roles.
- **Acciones de administración**: quién hizo qué, sobre qué y cuándo.
- **Dinero**: pagos, reembolsos, disputas, ajustes manuales de saldo.
- **Errores de seguridad**: peticiones rechazadas por permisos, por origen, por límite de
  peticiones, avisos de pago con firma mala.

### Cómo se hace bien

- Cada línea con **fecha, quién, qué, sobre qué objeto y desde dónde**, y un **identificador de
  petición** para seguir un mismo caso por todo el sistema.
- **Sin datos sensibles en los registros**: ni contraseñas, ni tokens, ni números de tarjeta, ni más
  datos personales de los necesarios. La IP, truncada cuando sea posible.
- El **registro de auditoría** (acciones de administración y dinero) **no se puede modificar ni
  borrar**, tampoco por un administrador.
- **Conservación limitada**: lo que necesites y nada más, según la ley de protección de datos.

> **🧱 Fundamentos:** F7 Errores: lanzar en un sitio, recoger en otro

### Avisos que conviene tener

| Señal | Puede significar |
|---|---|
| Muchos logins fallidos en poco tiempo | Fuerza bruta o relleno de credenciales |
| Un pico de respuestas 401, 403 o 429 | Alguien está probando puertas |
| Un administrador nuevo o un cambio de rol | Una cuenta comprometida dando acceso a otra |
| Uso de un código de recuperación del segundo factor | Alguien ha perdido el móvil… o no |
| Avisos de pago con firma inválida | Alguien intenta fingir pagos |
| Disputas o reembolsos | Posible fraude con tarjetas robadas |
| Errores 500 en ráfaga | Un fallo, o alguien buscando uno |

Herramientas: un servicio de errores (Sentry, Rollbar, Bugsnag), un vigilante de disponibilidad
(UptimeRobot, Better Stack) y los registros de tu alojamiento. Los avisos importantes, al **correo o
al móvil**, no en un panel que nadie abre.

## 9.2 Copias de seguridad

### La idea

Proteger la base de datos también es **poder recuperarla**: un error al borrar, un fallo del
proveedor o un ataque que cifra tus datos (*ransomware*). Una copia que nunca has restaurado es una
esperanza, no una copia.

### La regla 3-2-1

- **3 copias** de los datos (la original y dos más),
- en **2 soportes o servicios distintos**,
- y **1 fuera** del sitio principal (otro proveedor u otra región).

### Cómo se hace bien

- **Copias automáticas** diarias como mínimo, con varios días de historial (si un error se descubre a
  la semana, la copia de ayer ya lo tiene).
- Si el proveedor lo permite, **recuperación a un momento concreto** (*point-in-time recovery*).
- **Copias que un atacante no pueda borrar** con las mismas credenciales de la web.
- **Prueba de restauración** periódica: restaura en una base aparte y arranca la web contra ella.
  Anota cuánto tardas: ese es tu tiempo real de recuperación.
- Copia también **los archivos subidos**, no solo la base de datos.
- Ojo con los **planes gratuitos**: muchos no incluyen copias o caducan a los pocos días.

## 9.3 Cuando pasa algo: plan de respuesta

### La idea

En el taller hay un extintor y todos saben dónde está **antes** del incendio. Un incidente de
seguridad se gestiona mucho mejor si ya sabes los pasos.

### Los pasos

1. **Contener**: cortar el acceso del atacante. Cerrar sesiones, desactivar cuentas, rotar claves,
   poner la web en mantenimiento si hace falta.
2. **Conservar pruebas**: no borres registros ni reinstales nada antes de copiar lo que necesitas
   para entender qué pasó.
3. **Entender**: ¿por dónde entró?, ¿desde cuándo?, ¿qué datos ha visto o cambiado?
4. **Arreglar** la causa, no solo el síntoma, y comprobar que no queda ninguna puerta trasera.
5. **Restaurar** desde una copia limpia si los datos se han dañado.
6. **Avisar** a quien corresponda (ver abajo).
7. **Aprender**: escribir qué pasó y qué se cambia para que no se repita. Sin buscar culpables.

### Obligaciones legales en la Unión Europea

Si el incidente afecta a **datos personales** (una brecha de seguridad, en términos del RGPD):

- Hay que **notificarlo a la autoridad de control** (en España, la **AEPD**) en un máximo de
  **72 horas** desde que se conoce, salvo que sea improbable que suponga un riesgo para las personas.
- Si el riesgo para las personas es **alto**, hay que **avisar también a los afectados**, en un
  lenguaje claro.
- Hay que **documentar** todas las brechas, incluso las que no se notifican.

En España, **INCIBE** ofrece ayuda gratuita en ciberseguridad a empresas y particulares en el
teléfono **017**.

Ten a mano, antes de necesitarlo: quién decide, a quién se llama (proveedor de alojamiento, gestoría,
abogado) y dónde está la información de contacto de cada uno.
