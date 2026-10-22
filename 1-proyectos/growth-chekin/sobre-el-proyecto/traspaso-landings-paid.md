# Traspaso · Landings de paid para Chekin (hoteles España → resto de países)

Autor: Alex Santana · Sesión de trabajo con Claude, 21–22 oct 2026
Para: proyecto «casa» de Chekin. Sube este archivo como conocimiento del proyecto y usa el bloque del final como instrucciones.

---

## 1. Qué es este proyecto
Sistema de landings para las campañas de pago de Chekin (Google Ads y Meta Ads), con los leads entrando en HubSpot.
- **Objetivo:** subir la conversión de la landing (CRO), bajar el CPL y, al final, conseguir más SQL y más ventas cerradas.
- **Orden de trabajo:** España → hoteles primero → luego el resto de España → Italia (hoteles primero) → siguientes países, siempre hoteles primero.
- **Fase 1 (test principal):** cambiar SOLO la landing de la campaña de Google `SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN` (grupo de recursos `SB_ES_GOOGLE_PMAX_COMPETITORS`, URL actual `landing.chekin.com/chekin-hoteles`). La landing se adapta a la campaña, no al revés: una sola variable, se mide la CRO y luego los ingresos. Alex tiene que poder defenderlo ante su responsable.
- **Fase 2 (idea de Carlos):** una landing por ángulo de anuncio. El hero repite la promesa del anuncio y enseña primero esa función; después, todo lo demás que hace Chekin. Más atrevida e interactiva por debajo del hero, dentro del design system.

## 2. Reglas de trabajo acordadas (respetarlas siempre)
- **Idioma:** español.
- **No publicar ni subir nada** (HubSpot, WordPress, Google Ads) sin el OK explícito de Alex. Notion y los enlaces de Claude sí están autorizados para revisión interna.
- **No inventar cifras, reseñas ni testimonios.** Solo datos oficiales de Chekin o casos publicados en chekin.com. Nada de reseñas con estilo de Google.
- **Google y Meta por separado:** una landing no sirve para los dos.
- **Coherencia anuncio ↔ landing:** mirar qué prometen los anuncios activos (titulares, imágenes, keywords) antes de diseñar.
- **Medir por página** (campo oculto `landing` + analítica de HubSpot), no por `utm_campaign`, mientras las UTM sigan rotas.
- **Público:** hoteles y cadenas, no pequeños alojamientos (esos ya tienen sus campañas de SES y alquiler vacacional).
- **Todo debe funcionar en móvil**, incluidas las calculadoras: el resultado tiene que quedar a la vista mientras se mueven los controles.
- **Los datos personales de HubSpot** solo se tratan en agregado.
- **Legal (DPO)** valida el texto bajo el formulario.
- **Seguridad:** el kit `mkgt-auto` incluye un `wp_api.py` con una contraseña de aplicación de WordPress escrita en el código. No usarla y pedir que se rote.

## 3. Oferta y formulario (iguales en todas las landings)
- **Oferta:** "Prueba Chekin gratis 14 días". El hotel deja sus datos y **un experto en Chekin** (no "experto en hoteles") se pone en contacto para que lo use 14 días gratis, y le ayuda con cualquier duda o problema. No usar "desde que dejas tus datos" ni "desde hoy". Son 14 días, como en dashboard.chekin.com/register (no 15).
- **5 campos obligatorios:** nombre, teléfono, email, tipo de alojamiento (`property_type`) y **número exacto de habitaciones** (`number_of_rooms`, campo numérico, sin tramos).
- **Sin casilla de consentimiento.** Nota bajo el botón: "Sin compromiso. Al enviar, un experto en Chekin te contactará por teléfono o email sobre tu prueba. Más información en la política de privacidad." Base: art. 6.1.b RGPD, a validar con el DPO.
- **Campos ocultos:** utm_source, utm_medium, utm_campaign, utm_term, utm_content, gclid, fbclid y `landing` (un valor por landing).
- **CTA único:** "Empieza tu prueba gratis".

## 4. Cifras oficiales que se pueden usar
+10.000 hoteles · +200.000 propiedades · +25M check-ins · +20 países · +200 PMS · −80% de tiempo en recepción · check-in en 3 min · +55 € de upsell medio por reserva · +47% de reseñas 5★.
**Inbox con IA** (página oficial /inbox-unificado/): 20× más rápido, ~10 s frente a 3–5 h del sector, 70% de preguntas repetitivas resueltas, +15% de conversión de upsell. La mensajería en las dos direcciones solo funciona con Cloudbeds, Amenitiz, Avantio, Guesty, Smoobu y Hospitable.
**No usar:** la valoración de Capterra (2,7/5 con 6 reseñas), los logos de Iberostar, Meliá y Barceló (no están en la web; solo con confirmación y logo oficial), ni el "+15 países" antiguo.

## 5. Las 5 landings (todas en estado Boceto)
| # | Landing | Ángulo | H1 | Elemento interactivo | Valor `landing` | Enlace |
|---|---|---|---|---|---|---|
| 1 | PMax Competitors (fase 1) | General | Automatiza la recepción de tu hotel | 8 funciones en pestañas + mapa de PMS | `pmax-competitors-es-v6-prueba14-contacto` | https://claude.ai/artifact/MNjzT6AykyJskR75SzasEc |
| 2 | El parte, sin ti | Normativa | Olvídate del portal del Ministerio | Calculadora de horas de parte + recorrido del parte en 4 pasos | `angulo-normativa-ses-hoteles-es-v1` | https://claude.ai/artifact/CXeYwzSb8QDeKUp8c4YsfT |
| 3 | Así se vende sola una reserva | Ingresos / upselling | Misma ocupación, +55 € por reserva | Añadir extras a una reserva + calculadora de ingresos | `angulo-ingresos-upselling-hoteles-es-v1` | https://claude.ai/artifact/4fDrhTjoJadYxYvW1YZ2Ux |
| 4 | Inbox IA | Inbox IA | Tu recepción también responde a las 3 de la mañana | Chat de madrugada + calculadora de horas | `angulo-inbox-ia-hoteles-es-v1` | https://claude.ai/artifact/Sd6hUVhNff1iwBXmq3ZcwC |
| 5 | Recepción | Recepción | Recupera horas en recepción | Simulador de la cola de la hora punta | `angulo-recepcion-hoteles-es-v1` | https://claude.ai/artifact/3PJSV3FSwNNK3GiU7yMTHn |

- **Enlaces:** son privados hasta que Alex los comparte desde el menú Share.
- **Visuales:** los logos son oficiales (Chekin, los clientes de la home de chekin.com y los PMS de la página de hoteles). Los móviles, chats y tarjetas son maquetas HTML que imitan los anuncios, no capturas del producto: cambiarlas por capturas reales si las hay.
- **Ejemplos ilustrativos:** los precios de los ejemplos (late check-out 18 €, parking 15 €, desayuno 12 €) y los valores iniciales de las calculadoras (p. ej. 6 min por check-in) son ilustrativos, no cifras de Chekin.
- **Caso de éxito:** se usa solo uno, Sweet Accommodations. En el Inbox, la cita publicada de Interhome (Operations Lead).

## 6. Design system de Chekin (resumen aplicado)
| Elemento | Regla |
|---|---|
| Azul principal | #385BF8 |
| Navy | #19194B / #161643 |
| Fuente | Proxima Nova; mientras llega, Montserrat como sustituto |
| H2 | Regular, 44 px |
| Botones | radio 12, anillo `0 0 0 3px rgba(56,91,248,.2)` |
| Tarjetas | sin borde, sombras con tinte azul |
| Degradado | uno por página |
| Prohibido | bento, chips flotantes, blur, bucles decorativos |
| Footer | navy |
| Fondos | alternar tonos por sección, no todo blanco |

**Pantalla de referencia:** portátil de 14" (1512×780): el formulario tiene que verse sin bajar. En móvil (375×812), sin scroll horizontal y con inputs de 16 px para que iOS no haga zoom.

## 7. Hallazgos de datos (HubSpot, desde el 21 jul 2026)
- **Atribución contaminada:** 589 contactos con `utm_campaign = SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN`. Primera página: 508 en `es/check-in-online-ses-hospedajes`, 28 en la de UK, 11 en la de DE y solo 6 en `chekin-hoteles`. Con el nombre de las PMax Vacational ES/GB/DE casi no hay contactos (0/0/1). Lo más probable es que su tráfico se etiquete con el nombre de Competitors.
- **`chekin-hoteles`:** 24 contactos de primera página llegan con 5 nombres de campaña distintos: `SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN`, `PMAXCOMPETITORS`, `blackfriday-ES-2025-11-pmax`, `24034590173` y `{campaignname}`. 14 son hotel/camping y 10 alquiler vacacional.
- **Línea base de CRO** de la landing actual: 0,22–0,39%.
- **Consecuencia:** MQL, SQL y coste por SQL por campaña NO son fiables. No usarlos para justificar el test (se corrigió una afirmación anterior de "818 €/SQL").
- **Sin keywords:** solo 1 de 589 contactos tiene `utm_term`. Falta el informe de términos de búsqueda de la PMax (Windsor.ai está conectado y podría sacarlo).
- **Comparativa** (medida a 1512×780):

| | Actual `chekin-hoteles` | Nueva |
|---|---|---|
| Formulario | a 6.870 px (93% de la página) | a 185 px |
| Altura de la página | 7.374 px | 4.362 px |
| Enlaces de salida | 14 | 3 |
| Objetivos de conversión | 3 | 1 |
| Idioma declarado | `en` | `es` |

- **Muestra del test:** ~1.560–2.900 visitas por variante. La campaña trae ~1.300 clics al mes. Con A/B de HubSpot son ~2,5 meses.
- **Registro (dashboard.chekin.com/register):** 14 días · "más de 120 PMS" (pedir a producto que lo pase a +200) · "más de 20 países" · el teléfono "nunca para fines comerciales" (validar con legal que no choca con el contacto del experto).

## 8. Anuncios de referencia por ángulo (biblioteca de anuncios)
- **Recepción:**
  - Meta, activo: "Recupera horas en recepción" (`SB_ESP_META_HOTELES_FORM_CK`, IMG4). Va a formulario instantáneo.
  - Google: titulares "Automatiza tu Recepción", "Check-in en 3 Minutos", "−80% Tiempo en Recepción", "Sin colas en recepción".
- **Inbox IA:** imagen "Tu recepción también responde a las 3 de la mañana".
- **Normativa y upselling:** imágenes "Reportado" (SES) y "+55 € por reserva".
- **Meta hoteles España:** sus anuncios usan formulario instantáneo, así que llevarlos a una landing es otro test distinto.

## 9. Dónde está cada cosa
- **Notion · Biblioteca de landings:** https://app.notion.com/p/9553538748a748528a94ece777a675c8 (dentro de "P3 · Auditoría de landing pages y creatividades de paid"). Una ficha por landing con vista previa, H1, ángulo, campo de HubSpot, notas y la columna "Enlace".
- **Diapositivas para el responsable:** https://claude.ai/artifact/Ge5ftUWvY1PfLUEMautShs (15 diapositivas, incluida la fase 2).
- **Tracker de tests A/B** por país y segmento, con revisiones cada 2 semanas: https://claude.ai/artifact/QoftN5oSqEFTFscpd5m4te. Test sembrado: `es-hoteles-pmax-competitors`, estado "plan".
- **Biblioteca de anuncios** (fuente de los anuncios activos): https://claude.ai/artifact/1qcXvUZssjTNi3CzyJXSyG
- **En Descargas del Mac:**
  - `plan-test-landing-hoteles-es.md` (el plan completo)
  - `landing-pmax-competitors-hoteles-es.html`
  - `landing-ses-el-parte-sin-ti.html`
  - `landing-upselling-reserva-se-vende-sola.html`
  - `landing-inbox-ia-recepcion-3am.html`
  - `landing-recepcion-recupera-horas.html`
  - Los HTML son de archivo único: se abren con doble clic.
- **Las carpetas de trabajo** de esta sesión (plantillas, assets, guion de exportación) solo existen mientras exista la sesión. Lo importante ya está copiado en Descargas y en Notion.

## 10. Plan del test (fase 1, resumen)
- **Cambio:** solo la landing. Se publica en la misma URL `landing.chekin.com/chekin-hoteles`, así que no hay revisión de anuncios ni reaprendizaje. La versión actual se restaura desde el historial de HubSpot.
- **Método A (preferido):** A/B de HubSpot 50/50 en la misma URL. Requiere Marketing Hub Professional o Enterprise, a confirmar.
- **Método B:** antes/después con periodos iguales.
- **Métricas:** la principal es formularios ÷ visitas de la landing. Secundarias: % de leads hotel, MQL→SQL, SQL→ganado y coste por SQL.
- **Criterio de éxito:** p < 0,05 y MQL→SQL igual o mejor.
- **Disciplina:** no tocar la campaña durante el test.
- **Ingresos:** (CRO nueva − CRO actual) × visitas × % lead→SQL × % SQL→ganado × ticket medio.
- **Fase 2:** un grupo de recursos de la PMax por ángulo, apuntando a su landing, contra la ganadora de la fase 1. Nunca a la vez que la fase 1.

## 11. Pendiente
**De Alex o de otros equipos:**
- [ ] Aprobación del plan por su responsable.
- [ ] Plan de HubSpot: ¿hay A/B de landings?
- [ ] Formulario de HubSpot con los 5 campos y los campos ocultos.
- [ ] Ventas: qué recibe el hotel al enviar el formulario, cuándo le contacta el experto y si además debe registrarse en el dashboard.
- [ ] Ticket medio de un hotel y su pipeline.
- [ ] **Prioritario:** corregir la plantilla de seguimiento o el sufijo de URL final de las PMax (Competitors y Vacational ES/GB/DE).
- [ ] Fuente Proxima Nova y capturas reales del producto.
- [ ] Producto: actualizar "120 PMS" en el registro y confirmar el Inbox con IA para hoteles.
- [ ] DPO: texto del formulario.
- [ ] Ejemplo del índice del otro proyecto, para adaptar un plan de 20 h/semana (Alex lo iba a pasar).

**Siguiente trabajo:**
- [ ] Compartir los 5 enlaces con el equipo.
- [ ] Revisar las landings con Carlos.
- [ ] Montar la landing 1 en HubSpot cuando haya OK.
- [ ] Sacar los términos de búsqueda de la PMax (Windsor.ai).
- [ ] Después: España resto (alquiler vacacional) e Italia hoteles.

---

## Instrucciones sugeridas para el proyecto «casa»
Pégalas en las instrucciones del proyecto:

> Trabajo en Growth/CRO de Chekin (software de check-in para hoteles y alquiler vacacional). Respóndeme en español. Proyecto activo: landings de paid (Google Ads y Meta Ads → HubSpot), por país y con hoteles primero. Empezamos por España y seguimos con Italia. El contexto completo está en "TRASPASO-landings-paid-chekin.md".
>
> Reglas:
> 1. No publiques ni subas nada (HubSpot, WordPress, Ads) sin mi OK explícito.
> 2. No inventes cifras, reseñas ni testimonios: usa solo las cifras oficiales del traspaso y los casos publicados en chekin.com.
> 3. Google y Meta van por separado, y la landing se adapta al anuncio, no al revés. Una sola variable por test.
> 4. Mide por página y por el campo `landing`, no por `utm_campaign`, hasta que se arreglen las UTM.
> 5. Oferta: "Prueba Chekin gratis 14 días" y un experto en Chekin contacta al hotel. Formulario de 5 campos: nombre, teléfono, email, tipo de alojamiento y nº exacto de habitaciones.
> 6. Respeta el design system de Chekin: #385BF8, navy #19194B, Proxima Nova (o Montserrat), un solo degradado, sin bento, blur ni chips flotantes. Todo responsive: en un portátil de 14" el formulario se ve sin bajar, y en móvil se ve bien, calculadoras incluidas.
> 7. Antes de afirmar algo sobre datos, compruébalo y dime de dónde sale. Si un dato no es fiable, dilo.
