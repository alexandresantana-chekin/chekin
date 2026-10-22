# P3 · Auditoría de landing pages y creatividades de paid

El trabajo corre en el chat de Claude Code "Landing Page". Aquí solo estado y contexto.
**Contexto completo (traspaso del 22/10):** `../sobre-el-proyecto/traspaso-landings-paid.md` — oferta, formulario, cifras oficiales, design system, hallazgos y plan del test. Plan del test: `p3-landings/plan-test-landing-hoteles-es.md`.

## Las 5 landings (estado: Boceto) · archivos en `p3-landings/`
| # | Landing | Ángulo | H1 | Valor del campo `landing` | Archivo |
|---|---|---|---|---|---|
| 1 | PMax Competitors (fase 1) | General | Automatiza la recepción de tu hotel | `pmax-competitors-es-v6-prueba14-contacto` | `landing-pmax-competitors-hoteles-es.html` |
| 2 | El parte, sin ti | Normativa (SES) | Olvídate del portal del Ministerio | `angulo-normativa-ses-hoteles-es-v1` | `landing-ses-el-parte-sin-ti.html` |
| 3 | Así se vende sola una reserva | Ingresos / upselling | Misma ocupación, +55 € por reserva | `angulo-ingresos-upselling-hoteles-es-v1` | `landing-upselling-reserva-se-vende-sola.html` |
| 4 | Inbox IA | Inbox IA | Tu recepción también responde a las 3 de la mañana | `angulo-inbox-ia-hoteles-es-v1` | `landing-inbox-ia-recepcion-3am.html` |
| 5 | Recepción | Recepción | Recupera horas en recepción | `angulo-recepcion-hoteles-es-v1` | `landing-recepcion-recupera-horas.html` |

- Notion · Biblioteca de landings (dentro de la ficha P3): https://app.notion.com/p/9553538748a748528a94ece777a675c8
- Fase 1 = landing 1 en la URL actual. Fase 2 (idea de Carlos) = una landing por ángulo (2–5), cada una con su grupo de recursos de la PMax; nunca a la vez que la fase 1.
- Oferta en todas: "Prueba Chekin gratis 14 días" + un experto en Chekin contacta. Formulario de 5 campos (nombre, teléfono, email, tipo de alojamiento, nº exacto de habitaciones) + campos ocultos (UTM, gclid, fbclid, `landing`). CTA: "Empieza tu prueba gratis". Texto legal a validar por el DPO.

- KPI: +30% conversion rate de las landings de paid en noviembre 2026 vs baseline de octubre. Fecha límite: 2026-11-30.
- Artifacts (privados):
  - Deck: [Test de landing hoteles España](https://claude.ai/artifact/Ge5ftUWvY1PfLUEMautShs)
  - Tracker: [Tests de landing Chekin](https://claude.ai/artifact/QoftN5oSqEFTFscpd5m4te)

## Alcance
- Se cambian solo las landings de **Google Ads**. **Meta** usa su propia plantilla de formulario: no se toca.
- Las mejoras se buscan en las campañas activas ahora y cada test se registra en el tracker.

## Primer test: España · Hoteles
- Campaña: `SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN` (Performance Max, activa).
- URL final: `landing.chekin.com/chekin-hoteles`.
- 21 jul – 18 oct 2026: 10.639 € de gasto · 61.857 impresiones · 3.876 clics (CTR 6,3%) · 44,5% de clics cargan la página · conversión de la landing 0,22–0,39%.
- Fuente: Google Ads vía Windsor.ai y HubSpot. MQL/SQL de la campaña no fiables por UTM.

## Diagnóstico de la landing actual (21-10-2026)
- Formulario al 93% del scroll.
- 14 enlaces de salida.
- 3 objetivos a la vez: demo, guía y calculadora.
- 0 message match con el anuncio en el hero.
- Carga: 3,9 s y 716 KB.

## Diseño del test
- Misma campaña y URL; solo cambia la página.
- Muestra: 1.560–2.900 visitas por variante. ~1.300 clics/mes → de 5 semanas a 2,5 meses.
- Revisión cada 2 semanas en el tracker.

## Hallazgo 22-10-2026: la PMax ES no manda el tráfico a chekin-hoteles
- Fuente: Google Ads vía Windsor, últimos 30 días (hasta 21/10). 913 clics, 72 conversiones (según Google), 2.794 €.
- **Expansión de URL final activada** (`FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION = OPTED_IN`). URL final del grupo de recursos: `chekin-hoteles`.
- Google reparte los clics entre 21 páginas. `chekin-hoteles`: 193 clics (21%), 0 conversiones, 266 €.
- El resto: plantillas SES Hospedajes Word (171 clics, 23,5 conv.), `/es/check-in-online-ses-hospedajes` (158, 18,2), guía SES (75, 2), guestapp (67, 7), otras plantillas, `/en/online-check-in`, `/precio`, `/legalidad`…
- HubSpot (200 contactos más recientes con UTM PMax Competitors, 12–22/10): 100 de 110 de la PMax ES entraron por `/es/check-in-online-ses-hospedajes`; ninguno por `chekin-hoteles`.
- Consecuencia: con ~190 clics/mes en `chekin-hoteles`, el A/B (1.560–2.900 visitas por variante) no sale en plazo. Decisión pendiente (Alex/Carlos): desactivar o acotar la expansión, o testear en las páginas que reciben el tráfico. Antes, mirar la calidad (MQL→SQL) de los contactos de plantillas.

### Calidad de los leads de la PMax ES (HubSpot, 22-10-2026)
- 589 contactos con `utm_campaign = SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN` creados desde el 21/07 (3 en agosto, 243 en septiembre, 343 en octubre). Página = primera página vista (`hs_analytics_first_url`).
- Todos pasan por MQL. Alguna vez SQL: 18 (3,1%); oportunidad: 9; clientes: 3. Etapa actual: Nurturing 276 (47%), Not ICP 169 (29%), MQL 130.
- `/es/check-in-online-ses-hospedajes`: 508 (86%) · SQL alguna vez 10 (2,0%) · Not ICP 157 (31%) · 1 cliente.
- Plantillas: 11 · SQL 2 · 0 oportunidades. `chekin-hoteles`: 6 · 0 SQL. Inglés/alemán (`/ads/online-check-in-uk`, `/de/`, `/en/`): 40 · 0 SQL · 8 Not ICP.
- Google Ads optimiza con una sola conversión: "SB - (MQL)Registro Landing Hubspot" (80 en 30 días). Cuenta cualquier formulario de landing, plantillas incluidas.
- Descuadre: Google atribuye ~40 conversiones/mes a páginas de plantillas, pero en HubSpot solo hay 11 contactos de plantillas con esta UTM en 3 meses [POR COMPROBAR: si esos formularios no guardan la UTM o el contacto ya existía].

## Biblioteca de anuncios: URLs servidas de verdad (22-10-2026, otro chat)
- La biblioteca usaba solo la URL configurada en el grupo de recursos; con la expansión de URL final Google lleva el clic a otras páginas. Ahora el reparto por landing de cada campaña de Google usa **las URLs que Google sirvió**, cruzadas con los formularios de HubSpot de cada URL.
- Cada ficha de PMax tiene una tabla nueva: qué titular o descripción lleva a qué URL y qué % de sus clics va a cada una (export de Google Ads, 21 jul – 18 oct, todas las PMax).
  - Ojo: en la tabla por titular un mismo clic cuenta para cada texto del anuncio; las filas no suman el total. El reparto real es la tabla de URLs.
- **ES PMax Competitors: a /chekin-hoteles va el 41% de los clics** (21 jul – 18 oct). Algunos titulares en inglés ("Online Check-in") llevan a /en/online-check-in.
- **IT PMax (Competitors y Vacational):** casi todo el tráfico atribuido a titulares viene de "Modello Contratto Affitti Brevi" y "Contratto Affitto Turistico" → /modello/contrattoaffittoturistico. Tenerlo en cuenta antes de diseñar las landings de Italia.
- **Dos cifras, dos periodos (aclarado 22/10):** 41% en los últimos 90 días (21 jul – 18 oct, export de Google Ads, el periodo que usa Carlos) y 21% / ~190 clics en los últimos 30 días (Windsor). El último mes llega menos tráfico a /chekin-hoteles que la media de 90 días.

## Tracker (22-10-2026)
- Test ES · Hoteles pasado a **Pausado** en el tracker, con el motivo (expansión de URL, ~190 clics/mes a chekin-hoteles) y la propuesta de Carlos (una landing por anuncio). Se reactiva o se rehace cuando se decida con Carlos.
- El deck sigue diciendo "~1.300 clics/mes" para el test: desactualizado.

## Pendiente
Ver `estado.md` → "A medias".
