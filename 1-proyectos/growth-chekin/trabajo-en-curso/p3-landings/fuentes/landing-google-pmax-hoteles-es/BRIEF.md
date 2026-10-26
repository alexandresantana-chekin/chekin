# Plan de test: nueva landing para hoteles en Google Ads (España)

Autor: Alex Santana · Fecha: 21 oct 2026 · Actualizado: 22 oct 2026 · Estado: propuesta para aprobación (nada publicado)

---

## 1. Resumen
- **Qué:** cambiar **solo la landing** de la campaña de Google `SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN` por una nueva, orientada a hoteles y adaptada a lo que prometen sus anuncios.
- **Por qué:** es la PMax de Google que más gasta en España (10.639 € en 90 días) y su landing convierte entre el **0,22% y el 0,39%** de los clics. El formulario está al final de la página, hay 14 enlaces de salida y el mensaje no coincide con el anuncio.
- **Aviso:** las cifras de MQL, SQL y coste por SQL de esta campaña **no son fiables** por un fallo de etiquetado UTM (sección 9). No las usamos para justificar el test.
- **Cómo se demuestra:** test de una sola variable (la landing). Métrica principal: conversión de la landing (CRO). Después se traduce a SQL e ingresos.
- **Qué necesito:** aprobación del enfoque y 5 datos o accesos (sección 11).
- **Fase 2 (sección 13):** ya están hechas 4 landings más, una por ángulo de anuncio (Normativa, Ingresos, Inbox IA y Recepción), con la misma oferta y el mismo formulario. Se testan después de este test, no a la vez.

---

## 2. La campaña elegida
| Campo | Valor |
|---|---|
| Campaña | **SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN** |
| Tipo | Performance Max · España · segmento Hoteles · activa |
| Grupo de recursos | SB_ES_GOOGLE_PMAX_COMPETITORS |
| URL final actual | https://landing.chekin.com/chekin-hoteles (sin redirecciones) |

**Resultados del 21 jul al 18 oct 2026** (biblioteca de anuncios Chekin: Windsor.ai + HubSpot)

| Métrica | Valor |
|---|---|
| Gasto | 10.638,55 € |
| Impresiones / clics / CTR | 61.857 / 3.876 / 6,3% |
| Clics que llegan a cargar la página | 1.726 (44,5%) |
| Formularios en la propia landing (biblioteca) | 9 de 4.049 clics: **0,22%** |
| Formularios de Google con primera página `chekin-hoteles` (HubSpot, 21 jul – 21 oct) | 15 de 3.876 clics: **~0,39%** |
| Tipo de alojamiento de quien entró por `chekin-hoteles` (HubSpot) | 14 hotel/camping · 10 alquiler vacacional |
| MQL / SQL / ganados atribuidos a la campaña | 122 / 13 / 4 según la biblioteca. **No fiable:** mezcla leads de otras campañas (sección 9) |

Las métricas de Google (gasto, clics, impresiones) son fiables. Las de HubSpot atribuidas por UTM, no.

---

## 3. Público y oferta: prueba gratis de 14 días con contacto de un experto
- **Público:** hoteles y cadenas, no pequeños alojamientos. Un hotel con PMS y equipo de recepción necesita ayuda para conectar la integración. El pequeño alojamiento que prueba solo ya tiene otras campañas y landings (SES / alquiler vacacional).
- **Oferta:** "Prueba Chekin gratis 14 días" (los mismos 14 días que muestra el registro en dashboard.chekin.com). **El hotel deja sus datos y un experto en Chekin se pone en contacto con él para que lo use 14 días gratis**, y le ayuda con cualquier duda o problema, también al conectar su PMS.
- **Campos del lead (5):** nombre, teléfono, email, tipo de alojamiento y **número exacto de habitaciones** (campo numérico, no tramos: un hotel de 1 y uno de 19 no son lo mismo para ventas ni para la medición). Sin casilla de consentimiento obligatoria: bajo el botón se informa de que un experto le contactará por teléfono o email sobre su prueba (base: atender su solicitud, art. 6.1.b RGPD; **validar con legal/DPO**).
  - Cumple la promesa del anuncio ("Prueba Chekin Gratis"), que no se cambia.
  - CTA único: "Empieza tu prueba gratis". El formulario sigue captando los datos que ventas necesita.
  - **A tener en cuenta:** la landing actual pide "Hablar con un experto"; la nueva ofrece la prueba que promete el anuncio. La oferta forma parte de la variable "landing", así que el test mide el conjunto (mensaje, diseño y oferta), no cada elemento por separado.
- **Filtro de calidad:** el formulario pide tipo de alojamiento y número de habitaciones, en las propiedades que ya existen en HubSpot (`property_type`, `number_of_rooms`). Ventas puede priorizar y medimos qué parte de los leads son hoteles.

---

## 4. Diferencias entre la landing actual y la nueva
Medido en el navegador el 21 oct 2026, en una pantalla de portátil de 14" (1512×780).

| Criterio | Actual · `chekin-hoteles` | Nueva |
|---|---|---|
| H1 | "Toda la experiencia del huésped, en una sola plataforma" | "Automatiza la recepción de tu hotel" |
| ¿Repite el anuncio? | No: ni titulares ni imágenes | Sí: titulares "Automatiza tu Recepción", "Check-in Digital Hoteles", "Evita Multas"; réplicas de las imágenes SES "Reportado", "+55 € por reserva" e "inbox 03:00" |
| Imagen principal | Piscina con palmeras + llave digital (no sale en el anuncio) | Formulario + cifras; visuales del anuncio en las funciones |
| Formulario | A **6.870 px**, al **93%** de la página, fuera de la primera pantalla | A **185 px**, en la primera pantalla |
| Altura de la página | 7.374 px | 4.362 px (−41%) |
| Menú de navegación | Sí | No |
| Enlaces que sacan de la página | **14** (9 destinos distintos: calculadora, guía de hoteles, footer en inglés duplicado…) | **3** (solo privacidad y cookies) |
| Oferta | Hablar con un experto | Prueba gratis 14 días: deja sus datos y un experto en Chekin le contacta |
| Objetivos de conversión | 3 (demo, guía descargable, calculadora) | 1 (empezar la prueba gratis) |
| Textos de CTA distintos | Hablar con un experto · Aprende más · Saber más · Descubrir más · Calcula los números… · Acceder al contenido… | Un solo texto: "Empieza tu prueba gratis" |
| Mapa de integraciones | Chekin conectado a 6 PMS | El mismo mapa, con los logos oficiales (Mews, Opera Cloud, Cloudbeds, Little Hotelier, eviivo, Amenitiz) |
| Prueba social | +10.000 hoteles, +25M check-ins, +15 países, testimonio anónimo | +10.000 hoteles, +25M check-ins, **+20 países**, **+200 PMS**, **+47% reseñas 5★**, slider con los logos de clientes que publica chekin.com (Greystar, Holidu, Numa, limehome, Interhome, Node, Novasol) y, en lugar de la cita anónima, el **caso de éxito de Sweet Accommodations** (Barcelona y Sevilla, Cloudbeds: −80% de tiempo manual, +12.000 registros online/año) |
| Bloque de 8 funciones (pestañas) | Sí | Sí, con los mismos textos oficiales |
| Idioma declarado de la página | `en` (con contenido en español) | `es` |
| Palabras | 971 | 513 |
| Peso / peticiones | 677 KB / 82 | 62 KB / 3 (en local: en HubSpot aumentará con sus scripts) |

**El problema de fondo de la actual:** pide la acción al final de una página larga y antes ofrece muchas salidas. Encaja con una conversión de entre el 0,22% y el 0,39%.

---

## 5. La guía descargable: por qué divide el lead y cómo medirlo
**El problema.** La landing actual tiene dos caminos de captación:
1. **Demo:** formulario al final de la página.
2. **Guía "Customer Journey en hoteles":** enlace a otra página (`landing.chekin.com/guia-hoteles`), con su propio formulario.

Cada visita que se va a la guía es una visita que no pide demo. Además, el enlace lleva `utm_campaign=SB_ES_GOOGLE_PMAX_COMPETITORS…`, así que esa conversión se atribuye a la campaña aunque ocurra en otra página. Es uno de los motivos de que los datos estén mezclados.

**Cómo medirlo en la landing actual (línea base, antes de cambiar nada):**

| Métrica | Cómo se obtiene |
|---|---|
| Visitas a `chekin-hoteles` | Analytics de la página en HubSpot |
| Formularios de demo | Envíos del formulario "Del check-in al check-out \| Chekin Hoteles: Paid-Spain-Hoteles-2026" en esa página |
| Salidas a la guía | Visitas a `guia-hoteles` con origen `chekin-hoteles` (HubSpot o GA4) |
| Formularios de la guía | Envíos del formulario de la guía de contactos que vienen de `chekin-hoteles` |
| Calidad por camino | % de MQL→SQL y SQL→ganado de los leads de la demo frente a los de la guía |

Con esto calculamos:
- **Captación total** = (demo + guía) ÷ visitas.
- **Captación de demo** = demo ÷ visitas.
- **Fuga a la guía** = salidas a la guía ÷ visitas.

**Cómo se compara con la nueva (un solo formulario: el de la prueba gratis):**
- La nueva gana claramente si su **captación (formularios de prueba ÷ visitas) es mayor que la captación total de la antigua** (demo + guía).
- Si solo supera la captación de demo de la antigua, comparamos la **calidad**: un lead de guía suele ser de etapa temprana y pasa menos a SQL. Si eso se confirma, quitar la guía es mejor aunque haya menos formularios.
- La guía no se pierde: podría ser un test posterior, como segundo paso tras enviar el formulario (en la página de gracias), sin competir con la prueba gratis.

---

## 6. Qué cambia y qué no
- **Cambia:** solo el contenido de la landing.
- **No cambia:** anuncios, imágenes, vídeos, presupuesto, puja, audiencias, temas de búsqueda, expansión de URL final, ni la acción de conversión en Google Ads.
- **Cómo aplicarlo sin tocar Google Ads:** publicar la nueva **en la misma URL** `landing.chekin.com/chekin-hoteles`. La versión actual queda en el historial de revisiones de HubSpot y se puede restaurar en un clic. Así no hay revisión de anuncios ni reaprendizaje de la PMax.

---

## 7. Diseño del test
| | Opción A (preferida) | Opción B |
|---|---|---|
| Método | A/B de HubSpot en la misma URL, 50/50 aleatorio | Antes/después con periodos iguales |
| Requisito | Marketing Hub Professional o Enterprise (**a confirmar**) | Ninguno |
| Duración estimada | ~2,5 meses | ~5–6 semanas por periodo |
| Solidez | Alta | Media (estacionalidad, ajustes automáticos de la PMax) |

- **Métrica principal (CRO):** formularios enviados en la landing ÷ visitas a la landing (HubSpot). Se mide **por página, no por `utm_campaign`** (ver riesgo 1).
- **Secundarias:**
  - formularios ÷ clics de la campaña;
  - % de leads que son hotel;
  - MQL→SQL y SQL→ganado;
  - coste por SQL.
- **Muestra necesaria:** ~1.560 visitas por variante para detectar una subida del 0,22% al 1% (con base del 0,39%, ~2.900, porque la mejora relativa es menor) (95% de confianza, 80% de potencia). La campaña trae unos 1.300 clics al mes.
- **Criterio de éxito:** CRO mayor con significación estadística (p < 0,05) y MQL→SQL igual o mejor.
- **Disciplina:** anotar la fecha de inicio y no hacer otros cambios en la campaña durante el test. Si hay alguno, se apunta en un registro.

---

## 8. De conversión a ingresos
**Ingresos incrementales =** (CRO nueva − CRO actual) × visitas × % lead→SQL × % SQL→ganado × ticket medio.

- **Tasas lead→SQL y SQL→ganado:** las de la campaña no son fiables (sección 9). Hasta corregir las UTM, usar las tasas medias de hoteles en España de ventas.
- **Ticket medio de un hotel:** pendiente (sección 11).

**Ejemplo con 1.300 visitas al mes:** pasar del 0,22% al 1% son ~10 formularios más al mes. Si se confirmaran tasas como las que muestra la biblioteca (10,7% de MQL a SQL y 30,8% de SQL a ganado) serían ~1 SQL más y ~0,3 ganados más al mes, unos 4 hoteles más al año. El valor en euros depende del ticket. Es una ilustración, no una previsión.

---

## 9. Riesgos y limitaciones (conviene decirlos antes de empezar)
1. **Atribución contaminada.**
   - **Qué pasa:** de 589 contactos con `utm_campaign = SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN` desde el 21 jul, 508 entraron por la landing de alquiler vacacional SES, 28 por la de UK y 11 por la de Alemania. Solo 6 entraron por `chekin-hoteles`.
   - **Contraste:** con el nombre de las PMax Vacational solo hay 1 contacto (ES 0, GB 0, DE 1). Es muy probable que su tráfico se esté etiquetando con el nombre de Competitors ES.
   - **Además:** el tráfico de Google que llega a `chekin-hoteles` entra con 5 nombres de campaña distintos: `SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN`, `PMAXCOMPETITORS`, `blackfriday-ES-2025-11-pmax`, `24034590173` (ID) y `{campaignname}` (variable sin sustituir).
   - **Causa probable:** plantilla de seguimiento o sufijo de URL final compartido o desactualizado en Google Ads, y UTM arrastradas por enlaces internos como el de la guía.
   - **Consecuencia:** las cifras de MQL, SQL y coste por SQL por campaña no son fiables hasta corregirlo.
   - **Cómo lo manejamos:** medimos por página. Revisar las UTM no cambia la entrega de la campaña.
2. **Sin keywords.** No están en la biblioteca de anuncios ni en HubSpot (solo 1 de 589 contactos tiene `utm_term`). La landing se adapta a los recursos del anuncio, no a búsquedas reales. Pendiente: informe de términos de búsqueda de la PMax.
3. **Línea base pequeña y distinta según la fuente.** 9 formularios (biblioteca) o 15 (HubSpot, por primera página): entre el 0,22% y el 0,39%. Antes de lanzar hay que medirla con la analítica de la página en HubSpot.
4. **Expansión de URL final.** Si está activa, parte del tráfico no llega a ninguna de las dos landings. No se toca: se mide por página.
5. **Logos de clientes.** Se usan los 7 que Chekin ya publica en su home. Iberostar, Meliá y Barceló no aparecen en la web (una tira con ellos se retiró de /en/hotels/ en mayo de 2026): solo se añadirían con confirmación y logo oficial.

---

## 10. Próximos pasos
1. Aprobación de este plan.
2. Montar en HubSpot la nueva landing como variante (A/B) o como borrador en la misma URL, y conectar el formulario.
3. Medir la línea base de la sección 5 (demo, guía, fuga) con los datos actuales.
4. Lanzar el test y revisar cada 2 semanas sin tocar la campaña.
5. Informe final: CRO, calidad, SQL e ingresos. Decisión de mantener o volver atrás.
6. Fase 2: landings por ángulo, una por grupo de recursos de la PMax, contra la ganadora de la fase 1 (sección 13).

## 11. Qué necesito
- [ ] Plan de HubSpot (¿A/B de landings disponible?).
- [ ] Formulario de HubSpot para la nueva landing con: nombre, email, teléfono, `property_type`, `number_of_rooms`, UTM y gclid.
- [ ] Confirmación de ventas: qué recibe el hotel al enviar el formulario (cómo y cuándo recibe el acceso a la prueba de 14 días), cuándo le contacta el experto en Chekin y tiempo de respuesta.
- [ ] Ticket medio de un hotel (MRR o anual) y su pipeline en HubSpot.
- [ ] Opcional: confirmar si se pueden mostrar marcas hoteleras (Iberostar, Meliá, Barceló) y conseguir sus logos oficiales.
- [ ] **Prioritario:** revisar y corregir la plantilla de seguimiento / sufijo de URL final de las PMax (Competitors y Vacational ES/GB/DE) en Google Ads. No cambia la entrega de la campaña.
- [ ] Logos oficiales de PMS y fuente Proxima Nova.
- [ ] Para la fase 2: capturas reales del producto (Inbox, upselling, check-in) y confirmación de producto sobre el Inbox para hoteles.

## 12. Coherencia con el registro (dashboard.chekin.com/register, revisado el 21 oct 2026)
| Punto | Registro | Landing nueva | Estado |
|---|---|---|---|
| Días de prueba | 14 | 14 | Alineado |
| Uso del teléfono | "nunca para fines comerciales" | Informa de que un experto contactará sobre la prueba | Distinto propósito: validar con legal que no confunde |
| PMS integrados | "más de 120" | "+200" | Cifra oficial: **+200**. Pedir a producto que actualice el registro |
| Países | "más de 20" (informes policiales) | "+20" | Alineado |
| Campos | Email, contraseña, nombre, teléfono, tipo de inmueble | Nombre, teléfono, email, tipo, habitaciones | El experto le da acceso tras el contacto (confirmar con ventas si el hotel debe registrarse además en el dashboard) |

---

## 13. Fase 2: una landing por ángulo de anuncio (propuesta de Carlos)
**Idea:** cada anuncio lleva a una landing que repite su promesa y enseña primero esa función. Después enseña el resto de lo que hace Chekin. Las 5 landings comparten la misma oferta (prueba gratis 14 días + contacto de un experto en Chekin), el mismo formulario de 5 campos y el mismo diseño, así que lo único que cambia entre ellas es el ángulo.

| # | Landing | Ángulo | H1 | Elemento interactivo | Campo `landing` (HubSpot) | Enlace |
|---|---|---|---|---|---|---|
| 1 | PMax Competitors (la del test de este plan) | General | "Automatiza la recepción de tu hotel" | 8 funciones en pestañas + mapa de PMS | `pmax-competitors-es-v6-prueba14-contacto` | https://claude.ai/artifact/MNjzT6AykyJskR75SzasEc |
| 2 | "El parte, sin ti" | Normativa | "Olvídate del portal del Ministerio" | Calculadora de horas de parte al mes + recorrido del parte en 4 pasos | `angulo-normativa-ses-hoteles-es-v1` | https://claude.ai/artifact/CXeYwzSb8QDeKUp8c4YsfT |
| 3 | "Así se vende sola una reserva" | Ingresos / upselling | "Misma ocupación, +55 € por reserva" | El visitante añade extras a una reserva + calculadora de ingresos al mes y al año | `angulo-ingresos-upselling-hoteles-es-v1` | https://claude.ai/artifact/4fDrhTjoJadYxYvW1YZ2Ux |
| 4 | "Tu recepción también responde a las 3 de la mañana" | Inbox IA | El mismo que el anuncio | Chat de madrugada: elige una pregunta de huésped y responde la IA + calculadora de horas | `angulo-inbox-ia-hoteles-es-v1` | https://claude.ai/artifact/Sd6hUVhNff1iwBXmq3ZcwC |
| 5 | "Recupera horas en recepción" | Recepción | "Recupera horas en recepción" | Simulador de la cola de la hora punta, sin Chekin y con Chekin | `angulo-recepcion-hoteles-es-v1` | https://claude.ai/artifact/3PJSV3FSwNNK3GiU7yMTHn |

- **Dónde están:** en Notion, en la base "Biblioteca de landings", cada una con su ficha, la vista previa y la columna "Enlace". Los enlaces son privados hasta que se comparten desde el menú Share de cada página.
- **Todas se ven bien en móvil:** en las calculadoras y en el chat, el resultado se queda a la vista mientras el visitante mueve los controles.
- **Cifras:** solo las oficiales de Chekin (+10.000 hoteles, +25M check-ins, +20 países, +200 PMS, −80% de tiempo en recepción, 3 min, +55 €, +47% de reseñas 5★; en el Inbox, 20× más rápido, ~10 s frente a 3–5 h, 70% de preguntas repetitivas y +15% de conversión de upsell). Los precios de los ejemplos (late check-out, parking, desayuno) y los valores iniciales de las calculadoras son ilustrativos.
- **Visuales:** los logos son oficiales. Los móviles, chats y tarjetas son maquetas en HTML que imitan los anuncios, no capturas del producto. Si hay capturas reales, conviene cambiarlas.

**Cómo testarlas sin romper el test de este plan:**
1. **Primero, el test de la sección 7** (landing 1 en la misma URL). No se mezcla con nada más hasta que termine.
2. **Después, una landing por ángulo y grupo de recursos.** En la PMax, cada grupo de recursos tiene su propia URL final. Un grupo por ángulo (Normativa, Ingresos, Inbox IA, Recepción), con sus recursos actuales, apuntando a su landing. Se compara contra la landing ganadora de la fase 1, que hace de control.
3. **Se mide igual:** CRO por página y el campo oculto `landing` en HubSpot, no `utm_campaign`, mientras las UTM no estén corregidas.
4. **Meta va aparte.** Los anuncios de Meta de hoteles en España llevan a un formulario instantáneo. Usar estas landings ahí es cambiar el destino del anuncio: es otro test, con su propia línea base.

**Cosas a validar antes de la fase 2:**
- Producto: que el Inbox con IA está disponible para hoteles y con qué PMS. La mensajería en las dos direcciones solo funciona con Cloudbeds, Amenitiz, Avantio, Guesty, Smoobu y Hospitable, no con los +200 PMS del check-in.
- Legal (DPO): el texto bajo el formulario, el mismo en las 5.
- Paid: qué recursos de cada grupo encajan con cada ángulo y si hay volumen suficiente por grupo (ver muestra necesaria en la sección 7).
