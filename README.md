<div align="center">

# Libro Web 2026

### Todo lo que hay que tener en cuenta para hacer una web en 2026, explicado para que se entienda

[![Licencia: CC BY-NC 4.0](https://img.shields.io/badge/licencia-CC%20BY--NC%204.0-c2410c.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.es)
![Capítulos publicados](https://img.shields.io/badge/cap%C3%ADtulos-1%20de%2012-1c1c1e.svg)
![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow.svg)
![Idioma](https://img.shields.io/badge/idioma-espa%C3%B1ol-blue.svg)

**[📥 Descargar el capítulo 1: Seguridad (PDF)](pdf/libro-web-2026-01-seguridad.pdf)**

</div>

---

## Qué es

Un libro libre y gratuito, por capítulos, sobre **todo lo que rodea a una web profesional**: que sea
segura, legal, rápida, fácil de encontrar, accesible y que no se caiga. No enseña a programar: enseña
**qué hay que tener en cuenta y por qué**, para poder tomar buenas decisiones o revisar las que toman
otros.

Hoy casi cualquiera puede montar una web en una tarde, y cada vez más código lo escribe una IA. Lo
difícil ya no es escribirlo: es **saber si está bien**. Este libro es la lista de cosas que hay que
saber mirar.

## Para quién es

- **Quien empieza** en el desarrollo web y quiere ver el mapa completo, no solo el framework de moda.
- **Quien trabaja con IA** y necesita criterio para revisar lo que le entrega.
- **Quien encarga una web** (autónomos, pymes, equipos de marketing) y quiere saber qué pedir y qué
  preguntar al proveedor.
- **Quien ya programa** y quiere una chuleta actualizada con los valores concretos.

No hace falta saber programar para leerlo. El código que aparece es poco, corto y opcional.

## Cómo está escrito cada capítulo

Cada tema sigue siempre el mismo orden:

| Parte | Qué encontrarás |
|---|---|
| 💡 **La idea** | Una comparación con algo cotidiano para entender el concepto |
| ⚠️ **Qué puede salir mal** | El fallo o el ataque real, contado sin jerga |
| ✅ **Cómo se hace bien** | Lo que hay que hacer, con valores concretos y su fuente |
| 🔍 **Cómo comprobarlo** | Una prueba que puedes hacer tú para saber si está bien |

Y cada capítulo termina con una **chuleta de parámetros** y una **lista de revisión** para usar en tus
proyectos.

## Índice

| Nº | Capítulo | Estado |
|:-:|---|:-:|
| 1 | **[Seguridad](capitulos/01-seguridad/)** — ataques comunes, contraseñas, sesiones, cabeceras, pagos, secretos, dependencias, IA, copias y qué hacer si te atacan | ✅ [PDF](pdf/libro-web-2026-01-seguridad.pdf) |
| 2 | **Legal y privacidad en la UE** — RGPD, cookies, aviso legal y ley europea de accesibilidad | 🛠️ En desarrollo |
| 3 | **Rendimiento** — Core Web Vitals, peso del JavaScript, imágenes y caché | 🛠️ En desarrollo |
| 4 | **SEO técnico** — cómo te encuentran los buscadores y los asistentes con IA | 🛠️ En desarrollo |
| 5 | **Accesibilidad** — WCAG 2.2 en la práctica | 🛠️ En desarrollo |
| 6 | **Dominio, DNS, alojamiento y despliegue** | 🛠️ En desarrollo |
| 7 | **Fiabilidad** — por qué se cae una web, avisos, copias y recuperación | 🛠️ En desarrollo |
| 8 | **El correo de la web** — que no acabe en spam: SPF, DKIM y DMARC | 🛠️ En desarrollo |
| 9 | **Pagos online** — pasarelas, autenticación reforzada y lo que nunca hay que tocar | 🛠️ En desarrollo |
| 10 | **Elegir el stack y la arquitectura** sin complicarse | 🛠️ En desarrollo |
| 11 | **Calidad** — tests, revisiones y deuda técnica | 🛠️ En desarrollo |
| 12 | **Desarrollar con IA** — especificaciones, agentes y cómo revisar lo que te entregan | 🛠️ En desarrollo |

El índice puede cambiar mientras el libro crece. Los capítulos se publican cuando están terminados y
revisados, no antes.

## Capítulo 1: Seguridad

Lo que trae el primer capítulo:

1. Cómo piensa un atacante
2. Los diez fallos más comunes (OWASP Top 10:2025)
3. Cuentas, contraseñas y sesiones
4. El navegador: HTTPS, cabeceras, XSS, CSRF y CORS
5. Lo que entra: formularios, consultas, archivos y límites
6. Pagos online
7. Secretos, configuración y dependencias
8. Si tu web usa inteligencia artificial
9. Vigilar, copiar y reaccionar
10. **Chuleta de parámetros**
11. **Lista de revisión antes de publicar**
12. Fuentes

Puedes leerlo en el **[PDF](pdf/libro-web-2026-01-seguridad.pdf)** o directamente aquí en GitHub, en
la carpeta **[capitulos/01-seguridad](capitulos/01-seguridad/)**.

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
python herramientas/generar_pdf.py 01-seguridad  # solo uno
```

Si Chrome no está en su ruta habitual de Windows, indica dónde está con la variable `NAVEGADOR_PDF`.

## Estructura del repositorio

```
libro-web-2026/
├── capitulos/
│   └── 01-seguridad/     un archivo .md por apartado, en orden
├── herramientas/
│   ├── generar_pdf.py    Markdown → HTML → PDF
│   └── estilo_libro.css  diseño del PDF
├── pdf/                  los PDF listos para descargar
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
