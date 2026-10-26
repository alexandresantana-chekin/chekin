# Hallazgos (solo crece)

Cada descubrimiento con datos: **fecha · qué · fuente y periodo · qué implica · estado**. Lo más nuevo arriba.
Regla: toda cifra lleva su periodo (Carlos trabaja con 90 días). Si un dato no es fiable, se dice.

---

## 26-10-2026

### H-21 · PMax Vacational IT: la landing alloggiati sí saca formularios (17), y el 98% de los clics por título va a títulos de «contrato»
- **Qué:** en la Biblioteca de anuncios, la PMax Vacational IT tiene 1.676 clics, 52 formularios (3,1%) y 2.284 €. Por página: plantilla de contrato, 1.084 clics y **34 formularios (3,1%)**; `/it/check-in-online-alloggiati-web`, 501 clics y **17 formularios (3,4%)**. Google Ads cuenta 0 conversiones en alloggiati, pero sí convierte, incluso un poco mejor que la plantilla. Es la confirmación de H-18 (formulario como conversión secundaria). Los títulos «Modello Contratto Affitti Brevi» (1.814 clics, 2.777 €) y «Contratto Affitto Turistico» (472 clics) se llevan casi todos los clics de títulos de la campaña (2.286 de 2.330) y mandan todos a la plantilla. En HubSpot: 52 MQL (36 de alquiler vacacional, 5 de hoteles) → 4 SQL → 1 deal → 1 cliente; 5 trials.
- **Fuente / periodo:** artifact «Biblioteca de anuncios» (data.json, extraído el 19/10): Google Ads y GA4, 21 jul – 18 oct 2026 (90 días); formularios por página y embudo de HubSpot por MQL en el mismo periodo. Las cargas de GA4 (762 de 1.676 clics, 45%) no son comparables entre campañas: van del 3% al 96%, así que no se usan para sacar conclusiones.
- **Implica:** el boceto «IT resto» (affitti brevi) tiene que recoger a quien busca el contrato, porque es lo que trae el tráfico. Si alloggiati pasa a conversión principal, la PMax dejaría de esquivarla. Calidad baja: 4 SQL de 52 MQL (7,7%), frente a los 105 Qualified MQL de Italia del plan de noviembre (H-19).
- **Estado:** para revisar con el boceto IT resto (26/10).

### H-20 · Chekin Connect: 3 de los 5 eventos terminados no tienen ningún lead, y parte de los leads son pruebas internas
- **Qué:** de los 5 eventos terminados entre el 21 y el 25/10, **3 tienen 0 leads** (Tu Alquiler Asturias, Cloudbeds PT, Avvapro Sevilla). Los otros 2 suman 5 leads: The TOPO Connect, 4 (Marta); Scale Fest, 1 (Pablo). Entre los contactos de The TOPO Connect están el email de la propia Marta y el de Carlos, así que es probable que algunos sean pruebas. Ninguno de los 5 estaba en HubSpot hasta el reenvío del 26/10 (ahora 5 de 5, sin errores).
- **Fuente / periodo:** Supabase de Chekin Connect (tablas `events` y `leads`), eventos terminados del 21 al 25/10/2026. HubSpot, comprobado el 26/10.
- **Implica:** con estos datos no se puede medir lo que aportan los eventos. O los AEs no usan el QR, o no están asignados al evento en el panel [POR COMPROBAR con los AEs]. Hay que separar las pruebas de los leads reales antes de sacar conclusiones.
- **Estado:** tareas por evento creadas en Asana (Growth Daily › Alexandre). Preguntar a Marta y a los AEs.

### H-19 · Plan de noviembre de Snowball frente a las landings de Italia: Google es ~30% del presupuesto IT, no hay campaña de hoteles en Google y Search Intención IT no está en el plan
- **Qué:** el plan de noviembre de Snowball, preparado por Carlos, fija para Italia (paid) un mínimo de **105 Qualified MQL y 50 SQL**. Hoy llega a Qualified el **10,9%** de los MQL de Italia (jul–sep), así que harían falta **960 formularios** con la calidad actual. Google IT recibe **4.350 €** en noviembre: PMax Vacational 3.000 € (100 €/día), PMax Competitors 1.200 € (40 €/día) y Brand 150 €. El presupuesto de Italia es de ~14.250 € (Rental IT 9.750 € + Hoteles IT 4.500 €); el resto es Meta, fuera de P3. Snowball espera **0,7 Qualified** de PMax Vacational, con un coste histórico de 2.645 €/Qualified y 529 €/SQL, y **1,5** de PMax Competitors (756 €/Qualified, 302 €/SQL). **Las dos PMax IT se clasifican como *Rental IT*. No hay campaña de hoteles de Google en Italia:** los hoteles IT solo van por Meta (`SB_ITA_META_HOTELES_FORM_CK`). **`SB_IT_GOOGLE_SEARCH_INTENCION_CHEKIN` no aparece en el plan**, aunque fue la que mandó el 97,9% de su tráfico a questura y la única donde esa landing contó conversiones (H-17). El plan pide subir los Qualified MQL y SQL de HubSpot a Google y Meta como conversiones offline. Los €/día de partida no cuadran con el gasto real: el plan dice 94 €/día para Vacational, pero en 90 días gastó ~25 €/día (2.280 €).
- **Fuente / periodo:** «Snowball · Plan noviembre 2026.xlsx» (hojas 1–3; % Qualified jul–sep, costes históricos jun–oct según el propio plan). Comparado con Google Ads vía Windsor.ai, 21 jul – 18 oct (90 días), de H-18.
- **Implica:**
  1. El boceto «IT hoteles» va a recibir tráfico de alquiler vacacional. O se reorienta, o se pide a Snowball una campaña de hoteles en Google. Choca con la regla de P3 (público: hoteles y cadenas).
  2. La landing tiene que filtrar por tipo y tamaño de alojamiento (Micro no cuenta como Qualified), no solo captar más formularios.
  3. Para las conversiones offline, el formulario debe guardar el `gclid` en HubSpot [POR COMPROBAR]. Además, el formulario tiene que pasar a conversión principal (H-18).
  4. Preguntar a Snowball por Search Intención IT.
  5. Comprobar los €/día de partida con los últimos 30 días [POR COMPROBAR].
- **Estado:** para decidir con Carlos (26/10). Copiado en la ficha P3 de Notion (26/10, con OK de Alex).

### H-18 · Italia: el tráfico de las 4 campañas cae en 3 páginas, y la landing de hoteles sí convierte pero como conversión secundaria
- **Qué:** las 4 campañas IT apuntan a 17 URL distintas, pero 3 páginas se llevan el **94% de los 8.946 clics**: `/it/ads/registrazione-ospiti-questura` (5.383 clics), `/modello/contrattoaffittoturistico` (2.514) y `/it/check-in-online-alloggiati-web` (548). En cada campaña, una URL concentra entre el 65% y el 98% del tráfico (Search Intención 97,9%, Brand 98,1%). El resto son colas de 1–57 clics. **Nuevo frente a H-17:** en la PMax Competitors, la landing de questura tiene 0 conversiones pero **101,3 en «todas las conversiones»**. Lo mismo pasa con alloggiati en Vacational: 0 frente a 10. El formulario sí se registra, pero como acción secundaria, y la PMax no puja por ella. **Cruce con otros países:** Vacational IT manda 12 clics a páginas en inglés o de España (`/en/online-check-in`, `/ads/online-check-in-uk`, `/template/tenancycontractformat`, `/template/seshospedajesword`). Es el 0,7%, poco volumen. 6 de las 7 landings en italiano revisadas declaran `lang="en"` (solo alloggiati dice `it`). La de questura tiene el `<title>` de otra página: «Self Check-in de visu legale».
- **Fuente / periodo:** Google Ads vía Windsor.ai, 21 jul – 18 oct (90 días), por URL expandida, sin parámetros. Revisión con curl el 26/10.
- **Implica:** hay que rediseñar 3 páginas, no 21. Arreglar la acción de conversión (pasar el formulario a principal) es el cambio con más palanca y no toca el diseño. Cada +1 pp de conversión en los 3.288 clics de la PMax Competitors en questura serían ~33 formularios más en 90 días. El valor en MRR es [POR COMPROBAR: tasa lead→cliente y ticket en IT].
- **Estado:** resumen para Alex (26/10). Bocetos IT hoteles y resto ya cubren 2 de las 3 páginas. Decidir con Carlos la acción de conversión.

## 23-10-2026

### H-17 · Italia: Google Ads cuenta 0 conversiones en la landing de la PMax IT Competitors, pero en HubSpot entran contactos
- **Qué:** la PMax IT Competitors apunta a `landing.chekin.com/it/ads/registrazione-ospiti-questura`. En 90 días le llegaron **3.288 clics y 1.560 €, y Google Ads registra 0 conversiones**. En el mismo periodo, la plantilla de contrato `/modello/contrattoaffittoturistico` recibe 1.431 clics y 2.526 € de esa campaña y **sí cuenta 45 conversiones**. En HubSpot, **154 contactos** tienen esta landing como primera página desde el 21/07. La página sí tiene formulario en la primera pantalla («Contattaci», HubSpot, form `5ef250b9…`), declara `lang="en"` y usa cifras no oficiales: «50+ PMS», «4.8/5 Trustpilot», «87%», «100% conformità garantita», y testimonios de clientes de España.
- **Fuente / periodo:** Google Ads vía Windsor.ai, 21 jul – 18 oct (90 días), por URL expandida. HubSpot: contactos creados del 21/07 al 23/10, propiedad `hs_analytics_first_url` (primera página, no necesariamente la del formulario). Revisión en navegador el 23/10.
- **Matiz (mismo día):** en Italia hubo 4 campañas en esos 90 días, no 2. La de búsqueda `SB_IT_GOOGLE_SEARCH_INTENCION_CHEKIN` mandó 2.095 clics (3.928 €) a esta misma landing del 21/07 al 06/08, y ahí Google sí contó 6,7 conversiones. Después se paró: desde el 06/08 solo tiene clics sueltos. La cuarta, `SB_IT_GOOGLE_SEARCH_BRAND_CHEKIN`, sigue activa con poco volumen: 205 clics en 90 días, a `/it/ads/chekin`. Así que la conversión existe en la cuenta; lo que falla es que la PMax IT Competitors no la cuenta.
- **Implica:** lo más probable es que la PMax IT Competitors optimice hacia otro objetivo de conversión que no incluye este formulario [POR COMPROBAR en Ads: objetivos de conversión de la campaña]. La PMax no ve que la landing convierte y desvía el tráfico a la plantilla, que sí cuenta. Es el mismo mecanismo que H-08 en España. Arreglar la medición puede valer más que cambiar el diseño. Además, muchos contactos parecen alquiler vacacional, no hoteles [POR COMPROBAR el tipo de alojamiento en agregado].
- **Estado:** boceto de landing IT hoteles en curso (23/10). Para el lunes con Carlos: revisar las conversiones de la PMax IT en Google Ads.

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
