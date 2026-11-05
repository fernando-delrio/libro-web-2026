# 1. Cómo piensa un atacante

## La idea

Piensa en un taller con nave, oficina y almacén. El ladrón no entra por la puerta principal, que
tiene cerradura buena y está a la vista. Prueba la ventana del baño, la persiana que no baja del
todo, la llave que alguien deja debajo del felpudo o la furgoneta aparcada con las llaves puestas.
**No busca lo que está bien protegido: busca lo que se te ha olvidado.**

Con una web pasa igual. Casi nadie rompe el cifrado de una contraseña: es más fácil probar las
contraseñas filtradas de otra web, encontrar una dirección de administración sin proteger o leer una
clave que alguien dejó en el código.

## Cinco principios que lo ordenan todo

| Principio | Qué significa | En el taller |
|---|---|---|
| **No te fíes del navegador** | Todo lo que llega del navegador lo puede cambiar quien lo usa: precios, campos ocultos, permisos | El albarán que trae el cliente no vale: se mira en tu sistema |
| **Mínimo privilegio** | Cada persona, programa o clave tiene solo el permiso que necesita, y nada más | El aprendiz tiene llave del almacén, no de la caja fuerte |
| **Defensa en profundidad** | Varias capas; si una falla, la siguiente para el golpe | Cerradura, alarma y cámara, no solo cerradura |
| **Fallar cerrado** | Si algo da error, se niega el acceso, nunca se deja pasar «por si acaso» | Si la alarma se estropea, la puerta queda cerrada, no abierta |
| **Lo más simple posible** | Cada pieza que añades es una puerta más que vigilar | Menos puertas, menos cerraduras que revisar |

> **🧱 Fundamentos:** F11 Datos en la frontera · F12 Cliente, servidor y HTTP

## La superficie de ataque

Es la suma de **todas las puertas** por las que alguien puede intentar entrar:

- Cada página con formulario (contacto, registro, login, búsqueda).
- Cada dirección de la API que responde a peticiones.
- Cada archivo que se puede subir o descargar.
- Cada paquete de terceros que usa tu código.
- Cada cuenta de proveedor: dominio, alojamiento, correo, repositorio de código, pasarela de pago.
- Cada persona con acceso, y su correo.

**Reducir la superficie** (quitar lo que no se usa) suele proteger más que añadir protecciones nuevas.

## Modelo de amenazas en cuatro preguntas

Antes de construir algo importante, hazte estas cuatro preguntas (método de Adam Shostack, usado en
la industria). Basta con una hoja de papel:

1. **¿Qué estamos construyendo?** Dibuja las piezas: navegador, servidor, base de datos, servicios
   externos, y las flechas entre ellas.
2. **¿Qué puede salir mal?** Para cada flecha: ¿alguien podría leerla, cambiarla, hacerse pasar por
   otro o tumbarla?
3. **¿Qué vamos a hacer al respecto?** Una protección por cada riesgo que importe.
4. **¿Lo hemos hecho bien?** Una prueba que lo demuestre.

## Qué vale tu web para un atacante

Aunque tu web sea pequeña, interesa por:

- **Los datos personales** de tus clientes (correos, teléfonos, direcciones), que se venden.
- **Las contraseñas**, porque mucha gente repite la misma en todas partes.
- **El dinero**, si hay pagos o saldo.
- **Tu servidor**, para enviar spam, minar criptomonedas o atacar a otros desde él.
- **Tu reputación y tu dominio**, para engañar a tus clientes con correos que parecen tuyos.

La mayoría de los ataques son **automáticos**: un programa recorre miles de webs buscando el mismo
fallo. No hace falta que nadie te tenga manía para que te ataquen.
