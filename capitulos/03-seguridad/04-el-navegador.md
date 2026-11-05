# 4. El navegador: HTTPS, cabeceras, XSS, CSRF y CORS

## 4.1 HTTPS y HSTS

### La idea

Sin HTTPS, lo que viaja entre el navegador y tu web es una **postal**: cualquiera por el camino (la
wifi de una cafetería, un router comprometido) puede leerla y cambiarla. Con HTTPS es una **carta
cerrada y lacrada**: nadie la lee y, si alguien la abre, se nota.

### Cómo se hace bien

- **Todo** por HTTPS, no solo el login o el pago. Hoy los certificados son gratuitos (Let's Encrypt)
  y casi todos los alojamientos los ponen solos.
- Cualquier dirección `http://` **redirige** a `https://` con un código 301.
- **TLS 1.2 como mínimo**, mejor 1.3. Las versiones antiguas (SSL, TLS 1.0 y 1.1) desactivadas.
- **HSTS** (`Strict-Transport-Security`): una cabecera que le dice al navegador «durante este tiempo,
  entra aquí solo por HTTPS, aunque te pongan un enlace `http://`». Así se evita que alguien
  intercepte la primera visita.

| Valor de HSTS | Cuándo |
|---|---|
| `max-age=300` (5 minutos) | Al estrenarlo, para probar sin riesgo |
| `max-age=15768000` (6 meses) | Cuando todo funciona por HTTPS |
| `max-age=31536000` (1 año) | Objetivo final, y el mínimo para entrar en la lista de precarga |
| `includeSubDomains` | Solo si **todos** los subdominios tienen HTTPS |
| `preload` | Solo cuando estés seguro: salir de la lista de precarga tarda meses |

### Cómo comprobarlo

Pasa tu dominio por **SSL Labs** (ssllabs.com/ssltest): el objetivo es una **A**. Y desde la terminal:
`curl -I http://tudominio.es` debe devolver un 301 hacia `https://`.

## 4.2 Cabeceras de seguridad

### La idea

Las cabeceras son **instrucciones que tu servidor da al navegador** junto con cada página: «no me
metas dentro de otra web», «no adivines el tipo de archivo», «solo ejecuta scripts de mi dominio». Son
baratas de poner y paran ataques enteros.

### Las que toda web debería tener

| Cabecera | Valor recomendado | Qué evita |
|---|---|---|
| `Strict-Transport-Security` | Ver tabla anterior | Que alguien fuerce una visita sin cifrar |
| `Content-Security-Policy` | Ver apartado 4.3 | Que se ejecute código inyectado (XSS) |
| `X-Content-Type-Options` | `nosniff` | Que el navegador ejecute como script algo que no lo es |
| `X-Frame-Options` | `DENY` | Que otra web meta la tuya en un marco invisible para engañar al usuario (*clickjacking*) |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Que la dirección completa (con datos) viaje a otras webs |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | Que un script use la cámara, el micrófono o la ubicación |
| `Cross-Origin-Opener-Policy` | `same-origin` | Que una ventana de otra web manipule la tuya |
| `Cache-Control` | `no-store` en páginas con datos personales | Que una página privada quede guardada en un ordenador compartido |

### Cómo comprobarlo

Pasa tu web por **securityheaders.com** y por **Mozilla Observatory** (developer.mozilla.org/observatory).
El objetivo es una **A** en los dos.

## 4.3 XSS: código ajeno en tu página

### La idea

Un cliente deja una nota en el tablón del taller. Si en lugar de una nota deja **una orden que los
demás obedecen al leerla** («dale tus llaves al portador»), tienes un problema. El XSS (*cross-site
scripting*) es eso: un atacante consigue que tu web muestre **su código** a otros usuarios, y ese
código se ejecuta con los permisos de la víctima.

### Qué puede salir mal

Un usuario escribe en su nombre o en un comentario algo como
`<img src=x onerror="enviar(document.cookie)">`. Si tu web lo pinta tal cual en la página de otro
usuario o del administrador, ese código se ejecuta en su navegador: puede leer sus datos, hacer
acciones en su nombre o cambiar lo que ve.

### Cómo se hace bien

1. **Escapar al pintar.** Los frameworks modernos (React, Vue, Angular, Svelte) convierten `<` en
   `&lt;` automáticamente. El peligro está en las salidas de emergencia: `dangerouslySetInnerHTML`
   en React, `v-html` en Vue, `innerHTML` en JavaScript. **Evítalas.** Si de verdad necesitas pintar
   HTML de un usuario, límpialo antes con una librería específica (DOMPurify).
2. **Escapar también en los correos.** Los datos del usuario que van en un correo HTML se escapan
   igual que en la web.
3. **Política de seguridad de contenidos (CSP).** Es la red de seguridad: aunque se cuele un script,
   el navegador no lo ejecuta si no está autorizado.

**Para quien quiera ver código** (React):

```tsx
// MAL: el texto del usuario se interpreta como HTML
export const CommentText = ({ comment }: CommentProps) => (
  <p dangerouslySetInnerHTML={{ __html: comment.text }} />
)

// BIEN: React escapa el texto, y un <script> se ve como texto
export const CommentText = ({ comment }: CommentProps) => <p>{comment.text}</p>
```

### Una CSP estricta

La recomendación actual es autorizar los scripts con un **nonce** (un valor aleatorio distinto en
cada respuesta) o con su **hash**, en lugar de con una lista de dominios.

**Para quien quiera ver código:**

```
Content-Security-Policy:
  default-src 'self';
  script-src 'nonce-R4nd0m' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';
  frame-ancestors 'none'
```

| Si ves esto en una CSP | Significa |
|---|---|
| `'unsafe-inline'` en `script-src` | Cualquier script escrito en la página se ejecuta, también uno inyectado. Anula buena parte de la protección |
| `'unsafe-eval'` | Se puede ejecutar texto como código. Evítalo |
| `*` o `https:` en `script-src` | Se aceptan scripts de cualquier sitio |

**Consejo para empezar**: publica la CSP primero como `Content-Security-Policy-Report-Only`. El
navegador no bloquea nada, solo avisa de lo que bloquearía. Cuando no haya avisos, cambia a la
cabecera de verdad.

## 4.4 CSRF: que otra web actúe en tu nombre

### La idea

Firmas un documento en blanco y alguien lo rellena después. El **CSRF** (*cross-site request
forgery*) ocurre cuando visitas una web maliciosa mientras tienes la sesión abierta en la tuya, y esa
web hace que tu navegador envíe una petición a tu web (cambiar el correo, hacer un pago). El navegador
adjunta la cookie de sesión y tu servidor cree que lo pediste tú.

### Cómo se hace bien

Varias capas; con las dos primeras ya es muy difícil:

1. **Cookie con `SameSite=Strict` o `Lax`.** El navegador no la envía en peticiones que empiezan en
   otra web. Chrome y Edge aplican `Lax` por defecto desde 2020, pero Firefox y Safari no: ponlo
   siempre explícito.
2. **Comprobar la cabecera `Origin`** en todas las peticiones que modifican algo (`POST`, `PUT`,
   `PATCH`, `DELETE`): solo se aceptan las que vienen de tu dominio.
3. **Exigir `Content-Type: application/json`** en la API. Un formulario trampa de otra web no puede
   enviar ese tipo sin permiso de CORS.
4. **Token anti-CSRF** en formularios clásicos (no API): un valor secreto que la web pone en el
   formulario y el servidor comprueba.
5. **Nunca modificar nada con `GET`.** Un enlace o una imagen pueden lanzar un `GET` sin que el
   usuario haga nada.

**Para quien quiera ver código.** En FastAPI, como dependencia de las rutas que modifican datos:

```python
SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
JSON_CONTENT_TYPE = "application/json"


def content_type_of(request: Request) -> str:
    raw_content_type = request.headers.get("Content-Type", "")
    return raw_content_type.partition(";")[0].strip().lower()


def require_trusted_request(request: Request) -> None:
    if request.method in SAFE_METHODS:
        return
    if request.headers.get("Origin") not in settings.allowed_origins:
        raise ForbiddenOriginError()
    if content_type_of(request) != JSON_CONTENT_TYPE:
        raise ForbiddenOriginError()
```

> **🧱 Fundamentos:** F12 Cliente, servidor y HTTP · F4 Guardas y retorno temprano

**Excepción**: los avisos que te envían otros servicios (por ejemplo, la pasarela de pago) no vienen
de tu web. Se protegen con **firma**, no con `Origin` (apartado 6).

## 4.5 CORS: quién puede llamar a tu API desde el navegador

### La idea

Por defecto, el navegador no deja que una web lea respuestas de otra web distinta (la política del
mismo origen). **CORS** es la lista de excepciones: «a mi API puede llamarla esta web y esta otra».
Es una **puerta que abres tú**, no una protección que pones.

### Cómo se hace bien

- Lista **cerrada** de orígenes exactos (`https://www.tudominio.es`). Nunca `*` si la API usa cookies
  o datos privados.
- Nunca copiar automáticamente el `Origin` que llega como origen permitido: es lo mismo que `*`.
- Solo los métodos y cabeceras que de verdad usas.

### Cómo comprobarlo

```
curl -I -H "Origin: https://web-falsa.example" https://api.tudominio.es/algo
```

En la respuesta **no** debe aparecer `Access-Control-Allow-Origin`.
