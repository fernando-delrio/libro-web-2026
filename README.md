<div align="center">

# Libro Web 2026

### Todo lo que hay que tener en cuenta para hacer una web en 2026, explicado para que se entienda

[![Licencia: CC BY-NC 4.0](https://img.shields.io/badge/licencia-CC%20BY--NC%204.0-c2410c.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.es)
![Capítulos publicados](https://img.shields.io/badge/cap%C3%ADtulos-1%20de%2014-1c1c1e.svg)
![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow.svg)
![Idioma](https://img.shields.io/badge/idioma-espa%C3%B1ol-blue.svg)

**[📥 Descargar el capítulo 3: Seguridad (PDF)](pdf/libro-web-2026-03-seguridad.pdf)**

</div>

---

## Qué es

Un libro libre y gratuito, por capítulos, sobre **todo lo que rodea a una web profesional**: que sea
segura, legal, rápida, fácil de encontrar, accesible y que no se caiga. Y sobre **cómo escribir su
código para que lo entienda una persona**, aunque lo haya escrito una IA.

Hoy casi cualquiera puede montar una web en una tarde, y cada vez más código lo escribe una IA. Lo
difícil ya no es escribirlo: es **saber si está bien**. Este libro es la lista de cosas que hay que
saber mirar.

## Para quién es

- **Quien empieza** en el desarrollo web y quiere ver el mapa completo, no solo el framework de moda.
- **Quien trabaja con IA** y necesita criterio para revisar lo que le entrega.
- **Quien encarga una web** (autónomos, pymes, equipos de marketing) y quiere saber qué pedir y qué
  preguntar al proveedor.
- **Quien ya programa** y quiere una chuleta actualizada con los valores concretos.

No hace falta saber programar para leerlo. El código que aparece es corto y opcional.

## Cómo está escrito cada capítulo

Cada tema sigue siempre el mismo orden:

| Parte | Qué encontrarás |
|---|---|
| 💡 **La idea** | Una comparación con algo cotidiano para entender el concepto |
| ⚠️ **Qué puede salir mal** | El fallo o el ataque real, contado sin jerga |
| ✅ **Cómo se hace bien** | Lo que hay que hacer, con valores concretos y su fuente |
| 🔍 **Cómo comprobarlo** | Una prueba que puedes hacer tú para saber si está bien |
| 🧱 **Fundamentos** | Las ideas básicas de programación que usa ese apartado, con su código (F1, F2…) |

Y cada capítulo termina con una **chuleta de parámetros** y una **lista de revisión** para usar en tus
proyectos.

## Índice

### Parte I · Las bases

| Nº | Capítulo | Estado |
|:-:|---|:-:|
| 1 | **Fundamentos de la programación**: las 16 ideas básicas que aparecen en todo el libro (tabla de abajo) | 🛠️ En desarrollo |
| 2 | **Código que se lee**: cómo conseguir código legible para personas, aunque lo escriba una IA | 🛠️ En desarrollo |

### Parte II · Hacer una web

| Nº | Capítulo | Estado |
|:-:|---|:-:|
| 3 | **[Seguridad](capitulos/03-seguridad/)**: ataques comunes, contraseñas, sesiones, cabeceras, pagos, secretos, dependencias, IA, copias y qué hacer si te atacan | ✅ [PDF](pdf/libro-web-2026-03-seguridad.pdf) |
| 4 | **Legal y privacidad en la UE**: RGPD, cookies, aviso legal y ley europea de accesibilidad | 🛠️ En desarrollo |
| 5 | **Rendimiento**: Core Web Vitals, peso del JavaScript, imágenes y caché | 🛠️ En desarrollo |
| 6 | **SEO técnico**: cómo te encuentran los buscadores y los asistentes con IA | 🛠️ En desarrollo |
| 7 | **Accesibilidad**: WCAG 2.2 en la práctica | 🛠️ En desarrollo |
| 8 | **Dominio, DNS, alojamiento y despliegue** | 🛠️ En desarrollo |
| 9 | **Fiabilidad**: por qué se cae una web, avisos, copias y recuperación | 🛠️ En desarrollo |
| 10 | **El correo de la web**: que no acabe en spam (SPF, DKIM y DMARC) | 🛠️ En desarrollo |
| 11 | **Pagos online**: pasarelas, autenticación reforzada y lo que nunca hay que tocar | 🛠️ En desarrollo |
| 12 | **Elegir el stack y la arquitectura** sin complicarse | 🛠️ En desarrollo |

### Parte III · Trabajar bien

| Nº | Capítulo | Estado |
|:-:|---|:-:|
| 13 | **Calidad**: tests, revisiones y deuda técnica | 🛠️ En desarrollo |
| 14 | **Desarrollar con IA**: especificaciones, agentes y cómo revisar lo que te entregan | 🛠️ En desarrollo |

El índice puede cambiar mientras el libro crece. Los capítulos se publican cuando están terminados y
revisados, no antes. El guion de lo que viene está en **[PLAN.md](PLAN.md)**.

## Los fundamentos que recorren el libro

El capítulo 1 explica desde cero estas 16 ideas. El resto de capítulos las cita con un recuadro
**🧱 Fundamentos** cada vez que las usa, para que siempre sepas dónde repasarlas.

| Código | Fundamento | En una frase |
|:-:|---|---|
| F1 | **Datos y tipos** | Texto, números, sí/no, listas, fichas y la ausencia de valor |
| F2 | **Variables y constantes** | Poner nombre a un valor, y no cambiar lo que ya tiene nombre |
| F3 | **Funciones** | Una tarea con nombre: recibe algo y devuelve algo |
| F4 | **Guardas y retorno temprano** | Descartar primero lo que no vale y dejar el camino principal recto |
| F5 | **Tablas en lugar de cadenas de if** | Lo que cambia según un valor, escrito como una tabla |
| F6 | **Listas y recorridos** | Transformar, filtrar y sumar listas sin bucles a mano |
| F7 | **Errores: lanzar en un sitio, recoger en otro** | Quien falla avisa; quien coordina decide qué hacer |
| F8 | **Estado con nombre** | Un único estado («cargando», «listo», «error») en vez de varios sí/no |
| F9 | **Asincronía** | Esperar a algo que tarda (la red, el disco) sin congelarlo todo |
| F10 | **Capas y responsabilidades** | Cada pieza hace una cosa: pintar, coordinar, hablar con la API, transformar |
| F11 | **Datos en la frontera** | Todo lo que entra se valida y se limpia en la puerta |
| F12 | **Cliente, servidor y HTTP** | Peticiones, respuestas, métodos, códigos de estado y cabeceras |
| F13 | **Persistencia** | Bases de datos, consultas, transacciones y migraciones |
| F14 | **Azar, huellas y cifrado** | Valores imposibles de adivinar, hashes y cifrado, y para qué sirve cada uno |
| F15 | **Pruebas** | Preparar, actuar y comprobar: demostrar que algo funciona y que sigue funcionando |
| F16 | **Control de versiones** | Git: historial, commits, ramas, y por qué lo que subes se queda |

## El código del libro

Los ejemplos están en **Python** (servidor) y **TypeScript** (navegador) y siguen las reglas de estilo
**[readfirst](https://github.com/fernando-delrio/readfirst)**: *el código lo leen primero
las personas*. Es la misma forma de escribir que enseña el capítulo 2:

- nombres que explican qué hace cada cosa (en inglés), y comentarios solo para el porqué (en castellano);
- sin `else`, ternarios ni `switch`: guardas, funciones con nombre y tablas;
- funciones cortas (20 líneas y 3 parámetros como máximo) y un solo nivel de bloques;
- los errores se recogen en un solo sitio, con `attempt()`;
- un estado con nombre en lugar de varios booleanos, y sin números mágicos.

```python
# Lo que hay que hacer con cada aviso de la pasarela de pago, en una tabla.
HANDLER_BY_EVENT_TYPE = {
    "checkout.session.completed": credit_completed_payment,
    "charge.refunded": register_refund,
    "charge.dispute.created": freeze_disputed_account,
}


def apply_event(session: Session, event: stripe.Event) -> None:
    handler = HANDLER_BY_EVENT_TYPE.get(event.type)
    if handler is None:
        return
    handler(session, event)
```

## Fuentes y rigor

- Cada cifra y cada recomendación sale de una **fuente pública y reconocida** (OWASP, NIST, MDN,
  W3C, Google, organismos oficiales europeos y españoles), citada al final de cada capítulo.
- Cada capítulo indica **la fecha** de sus datos. En seguridad y en web las cifras cambian: si lees
  esto dentro de un año, comprueba la fuente.
- El libro se escribe con ayuda de inteligencia artificial y **el autor revisa cada capítulo** antes
  de publicarlo.

> **Aviso:** este libro es material divulgativo. No sustituye una auditoría de seguridad
> profesional ni el consejo de un abogado.

## Generar el PDF

Los capítulos se escriben en Markdown (un archivo por apartado) y el PDF se genera a partir de ellos.

Necesitas Python 3.11 o superior y Google Chrome:

```bash
pip install -r requirements.txt
python herramientas/generar_pdf.py               # todos los capítulos
python herramientas/generar_pdf.py 03-seguridad  # solo uno
```

Si Chrome no está en su ruta habitual de Windows, indica dónde está con la variable `NAVEGADOR_PDF`.

## Estructura del repositorio

```
libro-web-2026/
├── capitulos/
│   └── 03-seguridad/     un archivo .md por apartado, en orden
├── herramientas/
│   ├── generar_pdf.py    Markdown → HTML → PDF
│   └── estilo_libro.css  diseño del PDF
├── pdf/                  los PDF listos para descargar
├── PLAN.md               guion de los capítulos que vienen
├── LICENSE               texto legal de CC BY-NC 4.0
└── README.md
```

## Contribuir

¿Has encontrado un error, un dato desactualizado o algo que no se entiende? **[Abre un
issue](https://github.com/fernando-delrio/libro-web-2026/issues)** contando qué y dónde (capítulo y
apartado). Las sugerencias de temas para los próximos capítulos también son bienvenidas.

## Licencia

<a href="https://creativecommons.org/licenses/by-nc/4.0/deed.es"><img alt="Licencia Creative Commons BY-NC 4.0" src="https://licensebuttons.net/l/by-nc/4.0/88x31.png"></a>

Este libro se publica con licencia **[Creative Commons Atribución-NoComercial 4.0
Internacional (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.es)**.

| Puedes | Con estas condiciones |
|---|---|
| ✅ **Compartir**: copiarlo y redistribuirlo en cualquier medio o formato | **Atribución**: cita al autor, enlaza la licencia e indica si has hecho cambios |
| ✅ **Adaptar**: remezclarlo, transformarlo y crear a partir de él | **No comercial**: no puedes usarlo con fines comerciales (venderlo, ni total ni parcialmente) |

Cómo citarlo:

> *Libro Web 2026*, de Fernando del Río. Licencia CC BY-NC 4.0.
> https://github.com/fernando-delrio/libro-web-2026

El texto legal completo está en el archivo [LICENSE](LICENSE).

---

<div align="center">

Escrito por **[Fernando del Río](https://github.com/fernando-delrio)** · Edición 2026

Si te sirve, dale una ⭐ al repositorio: ayuda a que llegue a más gente.

</div>
