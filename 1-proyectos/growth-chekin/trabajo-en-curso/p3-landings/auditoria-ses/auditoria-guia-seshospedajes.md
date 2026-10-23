# Auditoría · landing.chekin.com/es/guia/seshospedajes (22-10-2026) — EN ESPERA

Tráfico (90 días, 21 jul – 18 oct): 236 clics, 8 formularios (3,4%). Viene sobre todo de la **PMax Competitors ES** (202 clics, 7 forms); Search Intención 27; Vacational 7.
**No se toca mientras se decide/ejecuta el test de la PMax Competitors** (una sola variable por campaña).

## Fallos
1. Formulario al final: empieza a 1.823 px (portátil) / 2.337 px (móvil); el hero solo tiene "Descargar gratis" que baja al formulario.
2. Formulario enorme para descargar una guía: ~1.050 px de alto y 7 campos (nombre, email, prefijo, teléfono, empresa, tipo de alojamiento, nº de alojamientos).
3. Errata: "El registro de viajeros **en** un proceso obligatorio" (es "es").
4. Texto desactualizado: "obligatoria desde el pasado 2 de diciembre de 2024".
5. Enlaces de salida: a chekin.com con UTM de otra campaña (`utm_source=smarttravelnews…guide-smarttravelnews`) y a un formulario externo (`share.hsforms.com/…`).
6. Fuera del design system: tipografía Public Sans, sin logo de Chekin arriba.
7. `lang` vacío en la página.

## Mejora propuesta (cuando toque)
Formulario corto (nombre, email, tipo de alojamiento, nº) en el hero junto a la portada de la guía; quitar enlaces de salida; corregir textos; Montserrat y logo.

## Boceto v2 (23-10-2026) · `../landing-guia-ses-v2.html` · https://claude.ai/artifact/HWpa7NEiAcJAPwmYzvK1Uz
Decisión de Alex: desarrollarla ya, es la más fácil de ganar. Página corta, formulario al principio, sin foto en el hero; la portada y los temas de la guía pasan al bloque 2.
| | Actual | v2 |
|---|---|---|
| Botón de descarga (portátil 1512×780) | ≈1.823 px | 472 px |
| Botón de descarga (móvil 375×812) | ≈2.337 px | 717 px |
| Campos | 7 | 5 (nombre, email, prefijo + teléfono, tipo de alojamiento, nº de alojamientos) |
| Alto de página (portátil) | — | 1.637 px |
| Enlaces de salida | con UTM de otra campaña | solo legales |
Textos corregidos (errata, "obligatoria desde el 2 de diciembre de 2024"). Campo oculto `landing = guia-ses-es-v2-boceto`. **Pendiente:** portada real de la guía (ahora maqueta HTML), texto legal (DPO), conectar el formulario de HubSpot y la entrega del PDF. No lanzar a la vez que otro cambio en la PMax Competitors.

- 23/10: añadido el teléfono con prefijo (decisión de Alex).
