# 7. Secretos, configuración y dependencias

## 7.1 Secretos: claves, contraseñas y tokens

### La idea

Un **secreto** es todo lo que da acceso a algo: la contraseña de la base de datos, la clave de la API
de correo, la clave secreta de la pasarela de pago, el token de una IA. Dejar uno en el código es como
**pegar la llave del almacén con celo en la puerta**: en cuanto el código sale de tu ordenador (un
repositorio, un compañero, una IA a la que se lo pasas), la llave sale con él.

### Cómo se hace bien

- **Los secretos van en variables de entorno**, nunca en el código. En local, en un archivo `.env`;
  en producción, en el panel del alojamiento.
- **El archivo `.env` nunca entra en Git.** Se añade a `.gitignore` el primer día. Se versiona un
  `.env.example` con los nombres de las variables y valores falsos.
- **La aplicación no arranca si falta un secreto obligatorio** en producción. Mejor un error claro al
  desplegar que una web que funciona a medias.
- **Los secretos no salen en los logs.** Muchos lenguajes tienen un tipo especial que se muestra como
  `**********` al imprimirlo (`SecretStr` en Pydantic, por ejemplo).
- **Una clave distinta por entorno**: desarrollo, pruebas y producción no comparten claves.
- **Mínimo privilegio también aquí**: si el servicio permite claves con permisos limitados, úsalas.

**Para quien quiera ver código** (Python con `pydantic-settings`):

```python
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", hide_input_in_errors=True)

    # Sin valor por defecto: si falta en el entorno, la aplicación no arranca.
    # SecretStr se muestra como '**********' en los logs y en los mensajes de error.
    database_url: SecretStr
    stripe_secret_key: SecretStr
```

> **🧱 Fundamentos:** F2 Variables y constantes · F11 Datos en la frontera

### El navegador no guarda secretos

**Todo lo que llega al navegador es público.** El código JavaScript de tu web se puede leer entero
con las herramientas del navegador, también lo que está «minificado». Por eso:

- En el código del navegador solo van valores que **no importa que se vean**: la dirección de tu API,
  la clave publicable de la pasarela, el identificador de la analítica, interruptores de funciones.
- Las llamadas a servicios que necesitan una clave secreta (enviar correos, consultar una IA, cobrar)
  **las hace tu servidor**, nunca el navegador directamente.
- Ojo con los frameworks: las variables con prefijo `VITE_`, `NEXT_PUBLIC_` o `REACT_APP_` **se meten
  en el código del navegador**. Nunca pongas un secreto en una de ellas.

### Cómo comprobarlo

Genera la versión de producción de la web y busca en la carpeta resultante palabras como `sk_`,
`secret`, `password`, `api_key`, `token`, `DATABASE_URL`. No debe aparecer nada.

## 7.2 Secretos en el historial de Git

### La idea

Git guarda **todas las versiones** de cada archivo. Si un día subiste una clave y al día siguiente la
borraste, **sigue en el historial**, y cualquiera con acceso al repositorio puede recuperarla. Hay
programas que recorren GitHub las 24 horas buscando claves recién publicadas: en minutos las prueban.

### Cómo se hace bien

- Pasa un buscador de secretos por **todo el historial**, no solo por la versión actual:
  **gitleaks** (`gitleaks git .`) o **TruffleHog**.
- Ponlo en la **integración continua** y en un **gancho antes de subir** (*pre-push* o *pre-commit*),
  para que una clave no llegue nunca al servidor.
- En GitHub, activa la **protección al subir** (*push protection*) del escaneo de secretos: bloquea el
  envío si detecta una clave conocida.

## 7.3 Si una clave se ha filtrado: rotar

Una clave que ha estado en Git, en un log, en un chat, en una captura de pantalla o en un correo **se
da por comprometida**, aunque creas que nadie la ha visto. El orden es:

1. **Generar una clave nueva** en el proveedor.
2. **Cambiarla** en el alojamiento (variables de entorno) y redesplegar.
3. **Anular la vieja** en el proveedor.
4. **Comprobar** que la vieja ya no funciona.
5. **Revisar los registros del proveedor** por si se usó mientras estuvo expuesta.
6. **Anotarlo**: qué clave, cuándo, cómo se filtró y qué se hizo.

**Borrar la clave del historial de Git no sustituye a rotarla.** Reescribir el historial puede
hacerse después, pero la clave ya se ha copiado: lo que la inutiliza es anularla.

Consejo: ten escrita una **tabla de rotación** con cada secreto (dónde se genera, dónde se cambia,
cómo se comprueba) antes de necesitarla. El día de la fuga no es momento de investigar.

## 7.4 Configuración de producción

### Qué apagar

| Qué | Por qué |
|---|---|
| Modo depuración (*debug*) | Enseña el código, las variables y las rutas cuando hay un error |
| Documentación automática de la API (`/docs`, `/swagger`, `/openapi.json`) | Es un mapa gratuito de todas tus rutas y campos |
| Mapas de código (`.map`) publicados | Permiten reconstruir tu código original. Si los usas para un servicio de errores, súbelos allí y bórralos de la web |
| Recarga automática del servidor (`--reload`, `watch`) | Es para desarrollo y consume recursos |
| Usuarios, contraseñas y datos de ejemplo | Una cuenta `demo` olvidada es una puerta abierta |
| Mensajes de error con detalle | El usuario ve un mensaje genérico; el detalle va al registro interno |

### Archivos que no deben estar a la vista

La web publicada solo debe servir lo que necesita el navegador. Comprueba que estas direcciones dan
**404**: `/.env`, `/.git/config`, `/backup.zip`, `/db.sqlite`, `/config.json`, `/phpinfo.php`,
`/.DS_Store`, `/README.md`, `/package.json` y cualquier carpeta de copias.

### La base de datos

- **Sin acceso desde internet**: solo desde tu servidor, por red privada o con una lista cerrada de
  IP permitidas.
- **El usuario de la aplicación no es administrador** de la base: puede leer y escribir sus tablas,
  pero no borrarlas ni crear usuarios.
- **Lo que no debe cambiar, que no pueda cambiar**: movimientos de dinero y registros de auditoría
  solo admiten añadir, nunca modificar ni borrar.
- **Cifrado en reposo** (casi todos los proveedores lo dan) y **conexión cifrada** (TLS) entre el
  servidor y la base.

## 7.5 Dependencias: el código de otros

### La idea

Una web moderna usa cientos de paquetes de terceros, y cada uno usa otros. Es como montar una máquina
con **piezas de cien proveedores distintos**: si uno te manda una pieza defectuosa o manipulada, va
dentro de tu máquina. Es el riesgo número 3 de OWASP en 2025 (A03).

### Por qué está en el podio

En **septiembre de 2025**, un atacante consiguió por phishing la cuenta del mantenedor de varios
paquetes de npm muy populares (entre ellos `chalk` y `debug`, con miles de millones de descargas a la
semana) y publicó versiones con código que robaba criptomonedas. Pocos días después apareció
**Shai-Hulud**, un «gusano» que se propagaba solo por cientos de paquetes de npm robando credenciales
de desarrolladores y publicando nuevas versiones infectadas con ellas.

### Cómo se hace bien

- **Archivo de bloqueo** (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`…) siempre en Git, e
  instalación **reproducible** en el servidor (`npm ci`, no `npm install`).
- **Auditoría automática** en cada cambio: `npm audit`, `pip-audit`, Dependabot o Renovate. Que bloquee
  el despliegue si hay una vulnerabilidad alta o crítica.
- **No actualizar a ciegas a la versión publicada hace una hora.** Algunos gestores permiten esperar
  unos días antes de aceptar una versión nueva (por ejemplo, `minimumReleaseAge` en pnpm): la mayoría
  de los paquetes secuestrados se detectan y retiran en ese tiempo.
- **Menos paquetes, menos riesgo.** Antes de instalar uno: ¿tiene mantenimiento?, ¿cuánta gente lo
  usa?, ¿lo puedo hacer en 30 líneas? Revisa de vez en cuando los que ya no usas y quítalos
  (`knip` o `depcheck` en JavaScript, `deptry` en Python).
- **Las acciones de la integración continua también son dependencias.** En GitHub Actions, fíjalas
  por su identificador de commit, no solo por versión (`@v4`), y da al flujo los permisos mínimos.
- **Cuidado con los nombres parecidos** (*typosquatting*): `reqeusts` en lugar de `requests`. Copia
  los nombres de la documentación oficial. Esto incluye los paquetes que te sugiere una IA:
  comprueba que existen y son los oficiales.

> **🧱 Fundamentos:** F16 Control de versiones

## 7.6 Las cuentas que hay alrededor de la web

Tu web es tan segura como **la cuenta más débil** que da acceso a ella:

| Cuenta | Qué controla |
|---|---|
| Registrador del dominio | Puede llevarse tu dominio y tu correo |
| DNS | Puede mandar tu web y tu correo a otro sitio |
| Alojamiento | Todo: código, base de datos, secretos |
| Repositorio de código | Puede meter código malicioso que se despliega solo |
| Pasarela de pago | El dinero |
| Correo | La recuperación de contraseña de todas las demás |

Para cada una: **segundo factor obligatorio** (mejor llave de acceso o app, no SMS), **al menos dos
administradores** (para no quedarte fuera si uno pierde el acceso), contraseñas en un **gestor de
contraseñas**, y la rama principal del repositorio **protegida** contra cambios directos.

Y protege tu dominio de correo con **SPF, DKIM y DMARC**: sin ellos, cualquiera puede enviar correos
que parecen tuyos a tus clientes.
