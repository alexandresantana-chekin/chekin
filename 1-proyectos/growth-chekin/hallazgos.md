# Hallazgos (solo crece)

Cada descubrimiento con datos: **fecha · qué · fuente y periodo · qué implica · estado**. Lo más nuevo arriba.
Regla: toda cifra lleva su periodo (Carlos trabaja con 90 días). Si un dato no es fiable, se dice.

---

## 23-10-2026

### H-16 · /check-in-guestapp: la página donde más gasta Competitors ES sale en blanco en móvil
- **Qué:** 377 clics, 2.009 € y 10 formularios (2,7%) en 90 días: más gasto que /chekin-hoteles (1.916 €). En móvil (375×812), **el titular sigue con opacidad 0 a los 6 s** de cargar: solo se ve el botón fijo "Probar Chekin gratis". En portátil aparece tras 1–2 s, pero el botón "Enviar" queda cortado en el borde (iframe 279–807 px con pantalla de 780). Cifras no oficiales ("50+ integraciones", "★ 4.8", "hasta 1 hora por reserva", "cero riesgo de multas"), oferta "activación inmediata", `lang="en"`, 7.116 px (portátil) y 11.076 px (móvil). El tráfico llega por el anuncio automático "Guestapp Chekin" (408 clics, H-08).
- **Fuente / periodo:** Biblioteca de anuncios, 21 jul – 18 oct (90 días); revisión en navegador el 23/10 [POR COMPROBAR la pantalla en blanco en un móvil real: puede ser cosa del emulador].
- **Implica:** si se confirma, quien llega desde el móvil no ve nada: explicaría parte de la conversión baja con el gasto más alto.
- **Estado:** boceto v2 hecho (https://claude.ai/artifact/6H23uPLZEJyBSbnVNWhTPP) y en el brief para Carlos.

### H-15 · La guía y las 4 plantillas se llevan el 45% del gasto de la PMax Competitors ES, y ya tienen el formulario arriba
- **Qué:** guía SES, contrato de alquiler vacacional, plantilla SES Word, plantillas SES y modelo de factura suman **1.357 clics, 51 formularios (3,8%) y 4.704 €** de los 10.384 € de la campaña (45%). Las plantillas ya ponen el formulario al lado del titular (por eso convierten al 2,9–5,0% frente al 0,38% de /chekin-hoteles), pero el botón queda por debajo de la primera pantalla (contrato: 939 px en 1512×780), la página declara `lang="en"` y tiene 6 enlaces de salida. Las landings de plantillas **sí muestran banner de cookies** con opciones (esenciales, analíticas, marketing): matiza H-14.
- **Fuente / periodo:** Biblioteca de anuncios, 21 jul – 18 oct (90 días); revisión en navegador el 23/10.
- **Implica:** si se mantiene la expansión de URL, unificar estas cinco páginas en un pack es la mejora de más volumen. Calidad baja (plantillas: 2 SQL, 0 oportunidades desde el 21/07).
- **Estado:** boceto del pack legal hecho (https://claude.ai/artifact/P8tf8sdAtaTqAXr8f7iZAj) y en el brief para Carlos. Depende de la decisión del lunes sobre la expansión.

### H-14 · Las landings ya tienen Microsoft Clarity (dos proyectos), y el alta del dashboard no tiene banner de cookies
- **Qué:** en `landing.chekin.com/chekin-hoteles` se cargan dos etiquetas de Clarity por Google Tag Manager (`GTM-PK7Q9R9`), con los proyectos `rrl7tp5b6k` y `rqlc6g9qhu`. Es decir, **puede que ya haya grabaciones y mapas de calor de las landings de paid**. Además cargan GA4, dos cuentas de Google Ads, Meta, Reddit, Amplitude y HubSpot. La página tiene un script de banner de cookies de HubSpot, pero en el navegador del panel no se mostró [POR COMPROBAR en una ventana privada]. En `dashboard.chekin.com/register` no aparece ningún banner de cookies.
- **Fuente / periodo:** revisión en navegador, 23/10/2026.
- **Implica:** para P3 no hace falta instalar nada: hay que pedir acceso a esos proyectos de Clarity (¿de Snowball o de Chekin?). Para grabar en el producto, primero hace falta un banner de consentimiento en el dashboard.
- **Estado:** preguntar a Carlos y a Snowball de quién son y pedir acceso. Consentimiento: DPO.

### H-13 · En el alta y la configuración no se ve nada de lo que hace el cliente
- **Qué:** en `dashboard.chekin.com` (`/register*` y `/setup*`) no hay clics (`$autocapture`), clics de rabia, clics muertos, salidas de página ni errores desde el 13/10, y las grabaciones están desactivadas (`session_recording_opt_in: false`). Solo hay páginas vistas y los eventos a medida del onboarding.
- **Fuente / periodo:** PostHog, eventos del 13 al 23/10/2026.
- **Implica:** sabemos en qué paso se cae la gente (sobre todo al conectar el PMS), pero no por qué. Para P1 hacen falta grabaciones y clics en esas páginas.
- **Estado:** propuesta para Daniel: grabaciones solo en esas URL, campos enmascarados, más autocapture, clics de rabia y errores. Antes, OK del DPO y revisar el consentimiento de cookies.

### H-12 · Corrige H-11: PostHog no cuenta ni las altas con Google antes del 21/10 ni el alta antigua
- **Qué:** del 13 al 23/10 PostHog registra **61 altas nuevas**: 38 con email (`auth_registration_succeeded`) y 23 con Google (`auth_social_succeeded` con `created = true`, evento que solo existe desde el 21/10). Además, **96 personas** llegan a `/register/accommodation-type` (pantalla del alta antigua) sin ningún evento de alta ni variante.
- **Comprobado:** el otro proyecto de PostHog ("Chekin - Dashboard") no tiene eventos; ningún otro dominio tiene eventos de alta del dashboard antes del 13/10 (solo `dashboard-ng.chekintest.xyz`, pruebas); Google Analytics ve tráfico en `/register` y en `/register/accommodation-type` en las mismas fechas.
- **Fuente / periodo:** PostHog, eventos del 13 al 23/10/2026; GA4 vía Windsor, 13–22/10 y agosto de 2026.
- **Implica:** el 16% de H-11 no vale (contaba solo email y comparaba con agosto). Lo que sí se sostiene: PostHog cuenta solo una parte de las altas, y la parte que falta es sobre todo el alta antigua. [POR COMPROBAR con producto: si en `/register/accommodation-type` la cuenta ya está creada.]
- **Estado:** dashboard corregido (fila de octubre con email + Google y aviso del alta antigua). Estimación del 16% retirada.

### H-11 · PostHog solo ve una de cada seis altas propias (estimación)
- **Qué:** PostHog registra 38 personas con `auth_registration_succeeded` del 13 al 23/10 (≈3,5 al día). La base de la app tenía 686 altas propias (origen DASHBOARD) en agosto (≈22 al día). Si el ritmo de altas no ha caído, PostHog capta en torno al **16%** de las altas.
- **Fuente / periodo:** PostHog, eventos del 13 al 23/10/2026; base de la app sincronizada, altas de agosto de 2026. No hay ningún periodo en que las dos fuentes midan a la vez: es una estimación [POR COMPROBAR con la sincronización arreglada].
- **Implica:** el funnel de PostHog de octubre no es el de todas las altas, sino el de quien pasa por los flujos que envían eventos (rebuilt y beta). Legacy no envía el registro. Cualquier tasa de PostHog vale para comparar variantes, no para dar el total.
- **Estado:** ❌ corregido por H-12 (no contaba las altas con Google y la comparación con agosto no se sostiene). Retirado del dashboard.

### H-10 · PostHog no tiene nada del dashboard antes del 13/10: hay un hueco del 04/09 al 13/10 sin ninguna fuente
- **Qué:** en `dashboard.chekin.com` el primer evento de PostHog, incluida la página vista, es del **13/10/2026**: no hay histórico del alta en PostHog. Por eventos: `$pageview` y `auth_registration_succeeded` desde el 13/10, `pms_connect_succeeded` desde el 14/10, `onboarding_variant_assigned` desde el 14/10 y `onboarding_setup_completed` desde el 15/10. La base de la app sincronizada (Postgres) se para el 04/09.
- **Fuente / periodo:** PostHog, eventos de 2025-01-01 a 2026-10-23, host `dashboard.chekin.com`.
- **Implica:** el funnel mes a mes solo se puede montar con dos fuentes que no se tocan. De enero al 3 de septiembre: base de la app (alta → vivienda → reserva → huésped). Desde el 13/10: eventos de PostHog (registro → onboarding → PMS). **Del 04/09 al 12/10 no hay datos en ninguna**, y los pasos de una fuente no son los de la otra.
- **Estado:** para la reunión del lunes 26 con Daniel. Arreglo: sincronización de Postgres (ingeniería) y eventos de vivienda y reserva creadas en PostHog.

### H-09 · Coste de oportunidad del onboarding en ARR a 12 meses (alta propia 2026)
- **Qué:** valor de un cliente a 12 meses = 39,76 al mes × 12 × 78,5% de retención a un año = **374** (LTV de vida completa: 2.219). Con ese valor, las altas propias de 2026 sin marzo (5.694, de ene a 3 sep) dejan de aportar unos **580.000 de ARR a 12 meses**: 388.000 en el paso alta → vivienda (≈1.037 clientes), 94.000 en vivienda → reserva (≈252) y 98.000 en reserva → huésped (≈261).
- **Fuente / periodo:** Stripe (MRR y clientes a 12/10, retención de las suscripciones de 2024 que duraron más de 31 días) y base de la app en PostHog (altas del 01/01 al 03/09/2026 sin marzo, estado a 04/09). Moneda de Stripe [POR COMPROBAR].
- **Implica:** el paso que más ARR deja escapar es registrar la primera vivienda: 2 de cada 3 euros del coste. Es una cota alta: supone que quien se queda pagaría como quien sigue, y el campo de pago (`has_paid`) tiene rarezas (agosto) [POR COMPROBAR con Daniel].
- **Estado:** en el dashboard "Funnel de activación Chekin" con selector de horizonte (12 meses o vida completa).

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
