# 10. Chuleta de parámetros

Valores de referencia a noviembre de 2026. Cada uno está explicado en su apartado.

## Contraseñas y acceso

| Tema | Valor recomendado | Fuente |
|---|---|---|
| Hash de contraseña | Argon2id (19 MiB, 2 pasadas, 1 hilo); si no, scrypt (N = 2^17, r = 8, p = 1), bcrypt (coste ≥ 10) o PBKDF2-HMAC-SHA256 (≥ 600.000 iteraciones) | OWASP Password Storage |
| Sal | Aleatoria y única por usuario (la ponen los algoritmos de arriba) | OWASP |
| Longitud mínima | 15 caracteres si es el único factor; 8 con segundo factor | NIST SP 800-63B-4 |
| Longitud máxima aceptada | 64 caracteres o más | NIST SP 800-63B-4 |
| Reglas de composición | Ninguna obligatoria | NIST SP 800-63B-4 |
| Caducidad periódica | No, solo si hay indicios de filtración | NIST SP 800-63B-4 |
| Lista de contraseñas filtradas | Sí, obligatorio comprobarla | NIST SP 800-63B-4 |
| Segundo factor | Llave de acceso (passkey) o app TOTP; obligatorio para administradores | NIST, OWASP |
| TOTP | 6 dígitos, paso de 30 s, margen de ±1 paso, sin reutilizar un código | RFC 6238 |
| Límite de login por IP | 5 a 10 intentos cada 15 minutos | Práctica habitual |
| Bloqueo por cuenta | 5 fallos seguidos → 10 a 15 minutos | Práctica habitual |
| Mensaje de error de login | Siempre el mismo, exista o no la cuenta | OWASP Authentication |

## Sesiones y enlaces

| Tema | Valor recomendado | Fuente |
|---|---|---|
| Token de sesión | Aleatorio seguro, 128 bits o más (32 bytes es lo habitual); en la base, solo su hash | OWASP Session Management |
| Inactividad | 2 a 5 min en alto valor; 15 a 30 min en riesgo bajo | OWASP Session Management |
| Duración máxima | Unas horas (4 a 12 h según el uso) | OWASP Session Management |
| Valor nuevo | En cada login y al cambiar de privilegios | OWASP |
| Cookie | `__Host-` + `Secure` + `HttpOnly` + `SameSite=Strict` (o `Lax`) + `Path=/`, sin `Domain` | MDN |
| Dónde no guardar la sesión | `localStorage` ni `sessionStorage` | OWASP |
| Enlace de recuperación | 15 a 60 minutos, un solo uso, anula los anteriores | OWASP Forgot Password |
| Enlace de confirmación de correo | 24 a 48 horas, un solo uso | Práctica habitual |
| Invitación de personal | 72 horas como máximo, un solo uso | Práctica habitual |

## Transporte y cabeceras

| Tema | Valor recomendado | Fuente |
|---|---|---|
| TLS | 1.2 como mínimo, 1.3 preferido; nota A en SSL Labs | Mozilla, SSL Labs |
| HSTS | Empezar en minutos; 6 meses (`15768000`); objetivo 1 año (`31536000`) | MDN, hstspreload.org |
| CSP | `default-src 'self'`; scripts con nonce o hash y `'strict-dynamic'`; `object-src 'none'`; `base-uri 'none'`; sin `'unsafe-inline'` ni `'unsafe-eval'` en scripts | Google, OWASP CSP |
| Marcos | `X-Frame-Options: DENY` y `frame-ancestors 'none'` | MDN |
| Tipo de archivo | `X-Content-Type-Options: nosniff` | MDN |
| Referencias | `Referrer-Policy: strict-origin-when-cross-origin` | MDN |
| Permisos del navegador | `Permissions-Policy` apagando lo que no uses | MDN |
| Ventanas | `Cross-Origin-Opener-Policy: same-origin` | MDN |
| Páginas privadas | `Cache-Control: no-store` | OWASP |
| CORS | Lista cerrada de orígenes exactos; nunca `*` con credenciales | MDN, OWASP |
| CSRF | `SameSite` + comprobar `Origin` + JSON obligatorio en la API (o token anti-CSRF en formularios) | OWASP CSRF |
| Nota de cabeceras | A en securityheaders.com y en Mozilla Observatory | — |

## Entrada de datos, archivos y pagos

| Tema | Valor recomendado | Fuente |
|---|---|---|
| Validación | En el servidor, con esquema, lista blanca, longitud máxima y campos de más rechazados | OWASP Input Validation |
| Consultas | Siempre parametrizadas | OWASP SQL Injection Prevention |
| Archivos: tipo | Lista cerrada, comprobado por los primeros bytes | OWASP File Upload |
| Archivos: almacenamiento | Fuera del servidor web, privado, con nombre aleatorio | OWASP File Upload |
| Archivos: descarga | Enlace firmado de 1 a 5 minutos tras comprobar el permiso | Práctica habitual |
| Pagos: importe | Calculado en el servidor | PCI DSS, pasarelas |
| Pagos: tarjeta | Página o componentes alojados por la pasarela (SAQ A) | PCI DSS v4.0.1 |
| Webhook | Firma verificada sobre el cuerpo original, tolerancia de 5 minutos, idempotente | Stripe |
| Límite de peticiones | Por ruta, por IP y por cuenta; respuesta 429 | OWASP API Security |

## Operación

| Tema | Valor recomendado | Fuente |
|---|---|---|
| Secretos | Variables de entorno; `.env` fuera de Git; la app no arranca sin ellos | OWASP Secrets Management |
| Escaneo de secretos | gitleaks o TruffleHog en todo el historial, en la CI y antes de subir | — |
| Dependencias | Archivo de bloqueo, `npm ci`, auditoría que bloquea vulnerabilidades altas | OWASP A03 |
| Debug y documentación de API | Apagados en producción | OWASP A02 |
| Base de datos | Sin acceso desde internet; usuario sin privilegios de administrador | OWASP |
| Copias | Regla 3-2-1, diarias, restauración probada | INCIBE, NIST |
| Brecha de datos personales | Notificar a la AEPD en 72 horas | RGPD, art. 33 |
| Cuentas de proveedores | Segundo factor obligatorio y dos administradores | — |
| Nivel de verificación | OWASP ASVS nivel 2 si hay cuentas o pagos | OWASP ASVS |
