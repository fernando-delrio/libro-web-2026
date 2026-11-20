# Plan del libro

Guion de los capítulos que vienen. Cada capítulo se publica cuando está escrito y revisado; hasta
entonces, este guion puede cambiar.

## Capítulo 1 · Fundamentos de la programación

**Objetivo:** que alguien que no ha programado nunca entienda las 16 ideas que aparecen en el resto
del libro, con una comparación cotidiana, un ejemplo en Python y otro en TypeScript, y dónde las va a
encontrar después.

Cada fundamento lleva: **la idea**, **cómo se ve en código**, **el error típico** y **dónde aparece
en el libro**.

| Código | Fundamento | Qué cuenta |
|:-:|---|---|
| F1 | Datos y tipos | Texto, números, sí/no, listas, diccionarios u objetos, y `null`/`None`. Por qué el tipo importa |
| F2 | Variables y constantes | `const`, nombres que explican, constantes en mayúsculas, no cambiar lo que hay dentro (crear uno nuevo) |
| F3 | Funciones | Entrada, salida, nombre verbo + objeto, 3 parámetros como máximo, funciones puras |
| F4 | Guardas y retorno temprano | Salir pronto en lugar de anidar; por qué sin `else` se lee mejor |
| F5 | Tablas en lugar de cadenas de if | Diccionarios de valores y de funciones (patrón Strategy) |
| F6 | Listas y recorridos | `map`, `filter`, `reduce`, comprensiones; cuándo sí un `for` |
| F7 | Errores | Lanzar con nombre, recoger en un solo sitio con `attempt()`, fallar cerrado |
| F8 | Estado con nombre | Un tipo unión o un `Enum` en vez de varios booleanos; máquinas de estados |
| F9 | Asincronía | Promesas, `async`/`await`, peticiones que tardan o fallan |
| F10 | Capas y responsabilidades | Vista, hook, servicio y modelo; organizar por funcionalidad |
| F11 | Datos en la frontera | Validar lo que entra y sanear lo que llega de la API con valores por defecto (`??`) |
| F12 | Cliente, servidor y HTTP | Petición y respuesta, métodos, códigos de estado, cabeceras, cookies, JSON |
| F13 | Persistencia | Tablas, consultas parametrizadas, transacciones, índices y migraciones |
| F14 | Azar, huellas y cifrado | Aleatoriedad segura, hash, cifrado, firma: qué es cada uno y cuándo se usa |
| F15 | Pruebas | Preparar-actuar-comprobar, caso bueno y caso de error, qué probar primero |
| F16 | Control de versiones | Git: commits pequeños, ramas, historial, y por qué un secreto subido no se borra |

## Capítulo 2 · Código que se lee

**Objetivo:** explicar por qué el código lo leen primero las personas y cómo conseguirlo aunque lo
escriba una IA. Se apoya en las 20 reglas de
[readfirst](https://github.com/fernando-delrio/readfirst), con un antes y un después de
cada una.

1. **Por qué importa**: el código se lee muchas más veces de las que se escribe; la IA escribe
   rápido, pero quien lo mantiene eres tú.
2. **Nombres que explican**: verbo + objeto, booleanos con `is`/`has`/`can`/`should`, sin
   abreviaturas ni `data`, `res` o `x`.
3. **Funciones cortas y con una sola tarea**: 20 líneas, 3 parámetros y un solo nivel de bloques.
4. **Sin `else`, ternarios ni `switch`**: guardas, funciones con nombre y tablas.
5. **Los errores en un solo sitio**: `attempt()` en Python y en TypeScript.
6. **Estados con nombre y sin parámetros booleanos**.
7. **Sin números ni textos mágicos**.
8. **Sin cambiar lo que ya existe**: crear valores nuevos en lugar de modificarlos.
9. **Comentarios solo para el porqué**, y cómo quitar el rastro típico de la IA.
10. **Capas**: cada pieza hace una cosa.
11. **Que lo vigile una máquina**: formateador, linter, test de estilo e integración continua.
12. **Pedirle código legible a una IA**: instrucciones del proyecto, revisores automáticos y el plugin
    readfirst.
13. **Refactorizar sin romper nada**: primero la prueba, y qué comprobar (prioridades, valores por
    defecto, casos excluyentes).
14. **Chuleta y lista de revisión de un cambio**.

## Después

Parte II (capítulos 4 a 12) y Parte III (13 y 14), según el índice del [README](README.md). Cada
capítulo nuevo usa los recuadros **🧱 Fundamentos** y sigue las reglas de readfirst en su código.
