# 2. Los diez fallos más comunes

## La idea

OWASP (Open Worldwide Application Security Project) es una fundación sin ánimo de lucro que, cada
pocos años, analiza miles de aplicaciones reales y publica la lista de los diez fallos de seguridad
más frecuentes y dañinos: el **OWASP Top 10**. Es la referencia que usa todo el sector. La edición
vigente es la de **2025**.

Piensa en ella como la lista de las diez averías que más ve un taller: no son todas las posibles,
pero si revisas estas diez, evitas la mayoría de los problemas.

## La lista de 2025

| Código | Nombre oficial | Qué es, sin jerga | Ejemplo |
|---|---|---|---|
| **A01** | Broken Access Control | Alguien hace o ve algo que no le corresponde | Cambias `/pedidos/1001` por `/pedidos/1002` en la dirección y ves el pedido de otro cliente |
| **A02** | Security Misconfiguration | Algo mal configurado o con los valores de fábrica | El panel de administración con usuario `admin` y contraseña `admin`; mensajes de error que enseñan el código |
| **A03** | Software Supply Chain Failures | Un fallo que llega por el código o las herramientas de otros | Un paquete que usa tu web es secuestrado y su nueva versión roba claves |
| **A04** | Cryptographic Failures | Datos sensibles sin cifrar o mal cifrados | Contraseñas guardadas tal cual en la base de datos; una página sin HTTPS |
| **A05** | Injection | El atacante cuela órdenes dentro de un dato | Escribir código en el campo «nombre» que luego se ejecuta en la base de datos o en el navegador de otro |
| **A06** | Insecure Design | El fallo está en el diseño, no en el código | Una recuperación de contraseña que pregunta «¿nombre de tu mascota?» |
| **A07** | Authentication Failures | Fallos al comprobar quién eres | Login sin límite de intentos; sesiones que no caducan nunca |
| **A08** | Software or Data Integrity Failures | Se acepta algo sin comprobar que no ha sido manipulado | Una actualización que se instala sin verificar su firma; un aviso de pago sin firma |
| **A09** | Security Logging & Alerting Failures | Te atacan y no te enteras | No se guarda quién entró ni cuándo; nadie recibe un aviso con 500 logins fallidos |
| **A10** | Mishandling of Exceptional Conditions | Errores mal gestionados que abren la puerta | Si falla la comprobación de permisos, el programa deja pasar en vez de cortar |

## Qué ha cambiado respecto a 2021

- **La cadena de suministro (A03) es nueva y entra directamente en tercer lugar.** Refleja los
  ataques de 2024 y 2025 contra paquetes de código muy usados (lo verás en el apartado 7).
- **La gestión de errores (A10) es nueva.** Muchos fallos graves no vienen de un ataque ingenioso,
  sino de un caso raro que el programa no esperaba.
- **SSRF** (cuando el servidor visita una dirección que le pasa el atacante) ya no tiene categoría
  propia: pasa a formar parte de A01.
- **El control de acceso (A01) sigue siendo el primero.** Es el fallo más común en aplicaciones
  reales.

## Cómo usar esta lista

No es una lista de comprobación cerrada: es un **mapa de riesgos**. Para revisar una web punto por
punto, OWASP tiene otra guía más detallada, el **ASVS** (Application Security Verification
Standard), con requisitos concretos en tres niveles:

| Nivel ASVS | Para qué tipo de web |
|---|---|
| **1** | Cualquier web. Lo mínimo que todas deberían cumplir |
| **2** | Webs con cuentas de usuario, datos personales o pagos. La mayoría de las webs de empresa |
| **3** | Banca, sanidad, infraestructuras críticas |

Si tu web tiene cuentas o pagos, el objetivo razonable es el **nivel 2**.
