# 11. Lista de revisión antes de publicar

Marca cada punto. Si alguno no aplica a tu web (por ejemplo, no hay pagos), táchalo y anota por qué.
Las pruebas se hacen en local o en un entorno de pruebas; contra la web publicada, solo las que
**leen** (cabeceras, certificado, archivos expuestos).

## Cuentas y acceso

- ☐ Las contraseñas se guardan con Argon2id, scrypt, bcrypt o PBKDF2 con sal.
- ☐ Se rechazan las contraseñas filtradas o demasiado comunes, sin reglas de composición absurdas.
- ☐ El login tiene límite por IP y bloqueo temporal por cuenta.
- ☐ El login, el registro y la recuperación no revelan si un correo existe.
- ☐ Los administradores y el personal tienen segundo factor obligatorio.
- ☐ La cookie de sesión lleva `Secure`, `HttpOnly`, `SameSite` y, si se puede, el prefijo `__Host-`.
- ☐ La sesión caduca por inactividad y por duración total, y cerrar sesión la anula en el servidor.
- ☐ El valor de sesión cambia en cada login.
- ☐ Los enlaces de recuperación caducan en menos de una hora y sirven una sola vez.
- ☐ Cambiar la contraseña cierra todas las sesiones.
- ☐ Toda ruta privada comprueba la sesión y el rol **en el servidor**.
- ☐ Un usuario no puede ver ni cambiar objetos de otro cambiando un número (probado con dos cuentas).

## Navegador

- ☐ Todo va por HTTPS y `http://` redirige a `https://`.
- ☐ SSL Labs da una A o superior.
- ☐ HSTS activo.
- ☐ securityheaders.com y Mozilla Observatory dan una A.
- ☐ La CSP no tiene `'unsafe-eval'` ni `*` en `script-src` (y, si se puede, tampoco `'unsafe-inline'`).
- ☐ No se usa `innerHTML`, `dangerouslySetInnerHTML` ni `v-html` con datos de usuarios.
- ☐ Un `<script>` escrito en cualquier campo se ve como texto en la web, en el panel y en los correos.
- ☐ Las peticiones que modifican datos comprueban `Origin` o llevan token anti-CSRF.
- ☐ CORS solo permite orígenes concretos.

## Datos que entran

- ☐ Todos los formularios y rutas de la API validan en el servidor con un esquema.
- ☐ Los campos que no se esperan se rechazan.
- ☐ Ninguna consulta a la base de datos se construye juntando texto.
- ☐ Los archivos subidos: lista cerrada de tipos, comprobados por su contenido, tamaño máximo, nombre
  aleatorio, almacenamiento privado y descarga con enlace que caduca.
- ☐ Login, registro, recuperación, contacto, subidas e IA tienen límite de peticiones.
- ☐ El servidor no descarga direcciones que manda el usuario (o lo hace con lista cerrada).

## Pagos

- ☐ El importe lo calcula el servidor.
- ☐ La tarjeta se teclea en la página o los componentes de la pasarela.
- ☐ El pago se confirma solo por webhook con firma verificada.
- ☐ Un mismo aviso procesado dos veces no abona dos veces.
- ☐ Las disputas y los reembolsos avisan a una persona.
- ☐ La clave secreta de la pasarela solo está en el servidor.

## Secretos y configuración

- ☐ No hay secretos en el código ni en el historial de Git (gitleaks pasado sobre todo el historial).
- ☐ `.env` está en `.gitignore`.
- ☐ En el código del navegador no hay ninguna clave secreta.
- ☐ La aplicación no arranca en producción si falta un secreto.
- ☐ Debug, documentación automática de la API y mapas de código, apagados o no publicados.
- ☐ `/.env`, `/.git/config` y las copias dan 404 en la web publicada.
- ☐ La base de datos no es accesible desde internet.
- ☐ Existe una tabla de rotación de claves.

## Dependencias y cuentas

- ☐ El archivo de bloqueo está en Git y el servidor instala con `npm ci` (o equivalente).
- ☐ La auditoría de dependencias corre en cada cambio y bloquea las vulnerabilidades altas.
- ☐ No hay paquetes instalados que no se usen.
- ☐ Dominio, DNS, alojamiento, repositorio, pasarela y correo tienen segundo factor y dos
  administradores.
- ☐ El dominio de correo tiene SPF, DKIM y DMARC.

## Vigilancia y recuperación

- ☐ Se registran accesos, cambios sensibles, acciones de administración y dinero, sin datos sensibles.
- ☐ Hay avisos al correo o al móvil para los casos de la tabla del apartado 9.1.
- ☐ Hay copias automáticas y se ha probado a restaurar una.
- ☐ Hay un plan de respuesta escrito y se sabe cómo notificar una brecha a la AEPD.

## Si usa IA

- ☐ La clave del proveedor de IA solo está en el servidor.
- ☐ El modelo solo accede a lo que puede ver quien pregunta.
- ☐ Las respuestas del modelo se escapan antes de pintarlas.
- ☐ Hay límite de mensajes y tope de gasto.
- ☐ Se ha intentado romper el asistente y se han corregido los fallos en el código.
