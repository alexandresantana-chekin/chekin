# Hallazgos (solo crece)

Cada descubrimiento con datos: **fecha · qué · fuente y periodo · qué implica · estado**. Lo más nuevo arriba.
Regla: toda cifra lleva su periodo (Carlos trabaja con 90 días). Si un dato no es fiable, se dice.

---

## 22-10-2026

### H-08 · Por qué la PMax Vacational ES se queda en su landing y la Competitors no
- **Qué:** las dos PMax tienen textos de anuncio generados con los títulos de otras páginas (expansión de URL + textos automáticos). Google manda el clic a la página que más formularios saca. Vacational: su landing (página SES) convierte al 4,25% → no hay a dónde ir mejor (99,1% del tráfico se queda). Competitors: /chekin-hoteles convierte al 0,38% (carga 3,9 s, `lang="en"`, formulario al 93%) → Google desvía a plantillas (4–5%).
- **Dato fuerte:** el texto que más gasta en Competitors, "Plantilla SES Hospedajes" (título de la plantilla Word), = 1.066 clics y 4.636 €. Nadie lo escribió.
- **Fuente / periodo:** Biblioteca de anuncios (tabla por texto), 21 jul – 18 oct (90 días).
- **Implica:** el problema de Competitors es de configuración + landing débil, no solo de medición.
- **Estado:** [POR COMPROBAR en Google Ads] expansión y exclusiones, textos automáticos, objetivo de conversión, términos de búsqueda. Lunes 26 con Carlos.

### H-07 · La página SES es la landing de la PMax Vacational, no de Competitors
- **Qué:** /es/check-in-online-ses-hospedajes recibe 11.600 de los 11.707 clics de la PMax Vacational ES (99%). En la vista por landing suma 14.622 clics, 535 formularios (3,7%) de 4 campañas.
- **Fuente / periodo:** Biblioteca de anuncios, 90 días.
- **Implica:** los ~508 contactos "de Competitors" que entraban por la página SES en HubSpot eran casi seguro tráfico de Vacational mal etiquetado (UTM rotas).
- **Estado:** confirmado con la biblioteca (atribuye por ID de campaña de la URL).

### H-06 · Volumen frente a calidad: Vacational trae leads baratos, Competitors trae las ventas
| 90 días | Vacational ES | Competitors ES |
|---|---|---|
| Gasto | ~5.400 € | ~10.400 € |
| Formularios | 500 (~11 €/form) | 81 (~128 €/form) |
| SQL | 8 (1,6%) | 13 |
| Ganados | 0 | 4 |
- **Fuente / periodo:** Biblioteca de anuncios (funnel por campaña), 21 jul – 18 oct.
- **Implica:** mejorar la página SES sube volumen; para ventas, lo que importa es el tráfico de hoteles.

### H-05 · Reparto de clics por URL en todas las PMax (90 días)
| PMax | % a su landing configurada |
|---|---|
| PT Competitors, PT Vacational, GB Vacational, DE Vacational | 100% |
| ES Vacational | 99% |
| IT Competitors | 67% (29% a /modello/contrattoaffittoturistico) |
| ES Competitors | 41% (23 URLs) |
| IT Vacational | 30% (65% a /modello/contrattoaffittoturistico) |
- **Implica:** Italia atrae a gente que busca una plantilla de contrato; tenerlo en cuenta antes de las landings de IT.

### H-04 · 41% frente a 21%: no es un error, son periodos distintos
- **Qué:** % de clics de la PMax ES Competitors que llegan a /chekin-hoteles = 41% en 90 días (21 jul – 18 oct, export de Google Ads) y 21% en los últimos 30 (~190 clics, Windsor).
- **Implica:** el último mes llega menos tráfico a la landing de hoteles que la media → la expansión se lo está llevando cada vez más.

### H-03 · El test de /chekin-hoteles no sale en plazo
- **Qué:** con ~190 clics/mes a la landing (30 días), el A/B de 1.560–2.900 visitas por versión no sale.
- **Estado:** test **pausado** en el tracker con el motivo. Decidir con Carlos: acotar expansión / testear donde va el tráfico / landing por anuncio.

### H-02 · Las UTM de las PMax mezclan campañas
- **Qué:** 589 contactos con `utm_campaign = SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN`; /chekin-hoteles recibe 5 nombres de campaña distintos (incluido `{campaignname}`); las PMax Vacational ES/GB/DE casi no tienen contactos propios.
- **Fuente / periodo:** HubSpot, desde el 21 jul.
- **Implica:** MQL, SQL y coste por SQL por campaña en HubSpot **no son fiables**. Usar la biblioteca (ID de campaña) o medir por página.
- **Estado:** prioritario corregir la plantilla de seguimiento / sufijo de URL final de las PMax.

### H-01 · Fallos de las landings SES actuales
- **Página SES** (/es/check-in-online-ses-hospedajes): en móvil el título y el párrafo salen cortados; formulario fuera de la primera pantalla (móvil) y botón bajo el pliegue (portátil 14"); etiqueta sobre el título que no hace nada; dos CTA iguales al mismo sitio; 11 botones; 13.963 px en móvil; inputs a 15 px; "+50 integraciones" (oficial: +200 PMS).
- **Guía SES** (/es/guia/seshospedajes): formulario al final y de 7 campos; errata "en un proceso"; texto de 2024; enlaces de salida con UTM de otra campaña.
- **Fuente:** revisión en navegador a 1512×780 y 375×812.
- **Estado:** boceto v2 de la página SES hecho (`trabajo-en-curso/p3-landings/landing-ses-hospedajes-v2.html`); guía en espera. Detalle en `p3-landings/auditoria-ses/`.
