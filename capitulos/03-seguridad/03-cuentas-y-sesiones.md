# 3. Cuentas, contraseñas y sesiones

## 3.1 Guardar contraseñas: el hash

### La idea

Imagina que en lugar de guardar las llaves de tus clientes guardas **un molde de cada una hecho de
forma que no se puede usar para fabricar la llave**. Cuando alguien trae una llave, haces un molde
nuevo y comparas: si coinciden, es la llave buena. Si te roban los moldes, no pueden abrir nada.

Eso es un **hash**: una huella de la contraseña que sirve para comprobarla pero no para recuperarla.

### Qué puede salir mal

- **Guardar la contraseña tal cual.** Si alguien copia la base de datos, tiene las contraseñas de
  todos tus usuarios, y como mucha gente repite contraseña, también las de su correo o su banco.
- **Cifrarla** (de forma reversible). Si se puede descifrar, quien robe la clave de cifrado las tiene
  todas. Las contraseñas no se cifran: se les hace un hash.
- **Usar un hash rápido** (MD5, SHA-1, SHA-256 a secas). Están pensados para ser rápidos, y un
  ordenador con tarjeta gráfica prueba miles de millones por segundo.
- **No usar sal.** La sal es un valor aleatorio distinto para cada usuario que se mezcla con la
  contraseña. Sin sal, dos usuarios con la misma contraseña tienen el mismo hash, y existen tablas
  precalculadas con millones de hashes.

### Cómo se hace bien

Se usa un algoritmo **lento a propósito**, con sal única por usuario. Valores recomendados por la
OWASP Password Storage Cheat Sheet:

| Algoritmo | Parámetros mínimos | Cuándo |
|---|---|---|
| **Argon2id** | 19 MiB de memoria, 2 pasadas, 1 hilo | Primera opción si tu lenguaje lo tiene |
| **scrypt** | N = 2^17, r = 8, p = 1 | Si no hay Argon2id |
| **bcrypt** | Coste 10 o más | Sistemas antiguos. Solo usa los primeros 72 bytes de la contraseña |
| **PBKDF2-HMAC-SHA256** | 600.000 iteraciones o más | Cuando se exige un algoritmo aprobado por normas oficiales (FIPS) |

Además:

- Compara los hashes **en tiempo constante**, para que el tiempo de respuesta no dé pistas.
- Guarda junto al hash el algoritmo y sus parámetros. Así puedes subirlos más adelante: cuando el
  usuario entre, se comprueba con los viejos y se guarda de nuevo con los nuevos.
- **No programes tu propio algoritmo.** Usa la librería estándar de tu lenguaje o una muy conocida.

**Para quien quiera ver código** (Python con `argon2-cffi`):

```python
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

# Los valores por defecto de argon2-cffi ya usan Argon2id y superan el mínimo de OWASP.
password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def is_password_correct(password: str, stored_hash: str) -> bool:
    outcome = attempt(
        lambda: password_hasher.verify(stored_hash, password),
        VerificationError,
        InvalidHashError,
    )
    return outcome.error is None
```

> **🧱 Fundamentos:** F14 Azar, huellas y cifrado · F7 Errores: lanzar en un sitio, recoger en otro

### Cómo comprobarlo

Mira la tabla de usuarios: ninguna contraseña se puede leer, todas empiezan por el nombre del
algoritmo (por ejemplo `$argon2id$`) y dos usuarios con la misma contraseña tienen valores distintos.

## 3.2 Qué contraseñas aceptar

La guía de identidad digital del NIST (instituto de normalización de EE. UU.), revisión 4 de 2025
(SP 800-63B-4), cambió varias costumbres que todavía se ven en muchas webs:

| Antes se hacía | Ahora se recomienda |
|---|---|
| Obligar a mayúsculas, números y símbolos | **No imponer reglas de composición.** Llevan a `Verano2026!` |
| Cambiar la contraseña cada 90 días | **No obligar a cambiarla** salvo si hay indicios de que se ha filtrado |
| Mínimo de 8 caracteres | **Mínimo de 15** si la contraseña es lo único que protege la cuenta; **8** si además hay segundo factor |
| Máximo de 16 o 20 caracteres | Aceptar **al menos 64** caracteres, espacios y emojis incluidos |
| Pregunta de seguridad («nombre de tu mascota») | **No usarlas** |
| Bloquear el pegado en el campo | **Permitir pegar**: así funcionan los gestores de contraseñas |

Y una obligación: **comprobar la contraseña contra una lista de contraseñas filtradas o muy comunes**
y rechazarla si aparece. Servicios como Have I Been Pwned lo permiten sin enviar la contraseña
completa (solo los primeros caracteres de su hash).

## 3.3 Segundo factor y llaves de acceso

### La idea

Una contraseña es **algo que sabes**. El segundo factor añade **algo que tienes** (el móvil, una llave
física) o **algo que eres** (huella, cara). Robar la contraseña ya no basta.

### Opciones, de más a menos seguras

| Método | Seguridad | Nota |
|---|---|---|
| **Llaves de acceso (passkeys) o llaves físicas** (WebAuthn / FIDO2) | Muy alta | **Resisten el phishing**: no funcionan en una web falsa. Es hacia donde va todo el sector |
| **Código de una app** (TOTP: Google Authenticator, Aegis, Authy…) | Alta | 6 dígitos que cambian cada 30 segundos. Si el usuario lo teclea en una web falsa, sirve unos segundos |
| **Código por SMS** | Media-baja | Mejor que nada, pero vulnerable a duplicados de SIM. Evítalo para cuentas importantes |
| **Código por correo** | Baja | Solo protege tanto como el correo |

### Cómo se hace bien

- **Obligatorio para el personal y los administradores.** Una cuenta de administrador sin segundo
  factor es la llave maestra de todas las demás.
- Al activarlo, entrega **códigos de recuperación** de un solo uso y guarda solo su hash.
- Si alguien usa un código de recuperación o desactiva el segundo factor, avísale por correo.
- Con TOTP, acepta como mucho un paso de margen (±30 segundos) y no aceptes el mismo código dos veces.

## 3.4 Sesiones y cookies

### La idea

Cuando entras en un hotel te dan una tarjeta para no enseñar el DNI en cada puerta. La **sesión** es
esa tarjeta: después del login, el navegador recibe un valor que demuestra que ya te identificaste.
Si alguien la copia, entra como tú hasta que caduque.

### Cómo se hace bien

- **Valor aleatorio y largo**: 128 bits de azar como mínimo (32 bytes es lo habitual), generado con el
  generador seguro del lenguaje, no con `random`.
- **En el servidor se guarda solo su hash**, igual que con las contraseñas. Si roban la base de
  datos, no pueden usar las sesiones.
- **Valor nuevo en cada login.** Si se reutiliza el anterior, un atacante puede plantar un valor
  antes de que la víctima entre y usarlo después (fijación de sesión).
- **Caducidad doble**: por inactividad y por duración total. Valores orientativos de OWASP: de 2 a 5
  minutos de inactividad en aplicaciones de alto valor (banca) y de 15 a 30 en las de riesgo bajo;
  la duración total, unas horas.
- **Cerrar sesión la anula en el servidor**, no solo borra la cookie del navegador.
- Al cambiar la contraseña, **se cierran todas las sesiones abiertas**.

> **🧱 Fundamentos:** F14 Azar, huellas y cifrado

### La cookie de sesión

Las cookies tienen atributos que el navegador obedece. Para una sesión, todos estos:

| Atributo | Qué hace | Si falta |
|---|---|---|
| `HttpOnly` | El JavaScript de la página no puede leerla | Un fallo de XSS roba la sesión |
| `Secure` | Solo viaja por HTTPS | Se puede leer en una wifi pública |
| `SameSite=Strict` o `Lax` | No se envía en peticiones que empiezan en otra web | Abre la puerta al CSRF (apartado 4) |
| Prefijo `__Host-` en el nombre | Obliga a `Secure`, `Path=/` y prohíbe `Domain` | Un subdominio comprometido puede plantar o pisar la cookie |
| Sin `Domain` | La cookie solo vale para ese dominio exacto | Viaja a todos los subdominios |

**Para quien quiera ver código.** Así se ve una cookie de sesión bien puesta en la respuesta del
servidor:

```
Set-Cookie: __Host-sesion=Q2hyb21lIHNlc3Npb24gdmFsdWU; Path=/; Secure; HttpOnly; SameSite=Strict
```

**No guardes la sesión en `localStorage`.** Cualquier script de la página puede leerlo, incluido uno
inyectado por un atacante.

## 3.5 Fuerza bruta y enumeración

### Qué puede salir mal

- **Fuerza bruta**: un programa prueba miles de contraseñas contra una cuenta.
- **Relleno de credenciales** (*credential stuffing*): prueba parejas de correo y contraseña filtradas
  de otras webs. Es el ataque más común contra los logins.
- **Enumeración**: la web responde distinto si el correo existe («contraseña incorrecta») o no
  («usuario no encontrado»). Así el atacante sabe a quién atacar, o que alguien es cliente tuyo.

### Cómo se hace bien

- **Límite por IP**: por ejemplo, 5 a 10 intentos cada 15 minutos. Se comprueba **antes** de calcular
  el hash, para que nadie agote la CPU del servidor.
- **Bloqueo por cuenta**: tras 5 fallos seguidos, la cuenta no admite intentos durante 10 o 15
  minutos, aunque vengan de otra IP. Se guarda en la base de datos para que sobreviva a un reinicio.
- **Mismo mensaje siempre**: «Correo o contraseña incorrectos». En el registro y en «olvidé mi
  contraseña», la misma respuesta exista o no el correo.
- **Mismo tiempo de respuesta**: si el correo no existe, calcula igualmente un hash falso. Si no, la
  diferencia de milisegundos lo delata.

**Para quien quiera ver código.** El mismo error en los dos casos, y una comparación aunque el correo
no exista:

```python
# Huella de una contraseña que nadie usa: se compara aunque el correo no exista,
# para que el tiempo de respuesta no delate qué correos tienen cuenta.
DUMMY_HASH = hash_password("this-password-belongs-to-no-account")


def stored_hash_of(user: User | None) -> str:
    if user is None:
        return DUMMY_HASH
    return user.password_hash


def authenticate(repository: UsersRepository, credentials: Credentials) -> User:
    user = repository.find_by_email(credentials.email)
    is_correct = is_password_correct(credentials.password, stored_hash_of(user))
    if user is None or not is_correct:
        raise InvalidCredentialsError()
    return user
```

> **🧱 Fundamentos:** F4 Guardas y retorno temprano · F3 Funciones

## 3.6 Enlaces de recuperación y confirmación

### La idea

Un enlace de «recupera tu contraseña» es una **llave temporal enviada por correo**. Tiene que servir
una sola vez, durar poco y no se puede adivinar.

### Cómo se hace bien

| Regla | Valor orientativo |
|---|---|
| Valor aleatorio largo, guardado como hash | 32 bytes, como la sesión |
| Recuperación de contraseña | **15 a 60 minutos** |
| Confirmación de correo | 24 a 48 horas |
| Invitación a una cuenta de personal | 72 horas como máximo |
| Un solo uso | Al usarlo, queda anulado |
| Pedir uno nuevo anula los anteriores | Solo vale el último |
| Al recuperar la contraseña | Se cierran todas las sesiones |

**Cuidado con el enlace del correo**: el dominio del enlace se escribe desde la configuración del
servidor, nunca a partir de la cabecera `Host` de la petición. Si no, un atacante puede pedir la
recuperación de tu cuenta haciendo que el enlace apunte a su web.

## 3.7 Permisos: quién puede hacer qué

### La idea

Que alguien haya entrado en el edificio no significa que pueda abrir todos los despachos. La
**autenticación** responde a «¿quién eres?»; la **autorización**, a «¿qué puedes hacer?». El fallo
número 1 de OWASP (A01) está en la segunda.

### Dos niveles de permisos

1. **Por función** (rol): un cliente no entra en `/admin`. Se comprueba en **el servidor**, en cada
   petición. Ocultar el botón en la pantalla no protege nada.
2. **Por objeto**: un cliente solo ve **sus** pedidos, facturas y archivos. Es el que más se olvida.
   Si la dirección es `/facturas/1002` y el servidor solo comprueba que hay sesión, cualquiera puede ir
   probando números. Este fallo se llama **IDOR** (referencia directa insegura a un objeto).

### Cómo se hace bien

- Cada consulta a la base de datos **filtra por el dueño** de la sesión: «la factura 1002 **de esta
  cuenta**», no «la factura 1002».
- Si el objeto no es suyo, responde **404** (no existe), no 403 (prohibido): así no confirmas que
  existe.
- Las rutas de administración: rol de administrador, segundo factor, fuera de los buscadores
  (`noindex`), sin enlaces desde la web pública y con cada acción anotada en un registro.
- **Por defecto, nada está permitido.** Cada ruta nueva nace cerrada y se abre a propósito.

**Para quien quiera ver código.** El dueño va **dentro de la consulta**, no en un `if` posterior: así
no se puede olvidar. Y `account_id` sale siempre de la sesión, nunca de lo que manda el navegador:

```python
def find_invoice(session: Session, account_id: int, invoice_id: int) -> Invoice:
    statement = (
        select(Invoice)
        .where(Invoice.id == invoice_id)
        .where(Invoice.account_id == account_id)
    )
    invoice = session.scalars(statement).one_or_none()
    if invoice is None:
        raise InvoiceNotFoundError()  # 404 también si existe pero es de otra cuenta
    return invoice
```

> **🧱 Fundamentos:** F13 Persistencia · F4 Guardas y retorno temprano

### Cómo comprobarlo

Crea dos cuentas, A y B. Con la sesión de A, pide uno por uno los recursos de B cambiando el número en
la dirección o en la petición. Todos deben responder 404. Repite con las peticiones que modifican
(editar, borrar) y comprueba que nada ha cambiado en la base de datos.
