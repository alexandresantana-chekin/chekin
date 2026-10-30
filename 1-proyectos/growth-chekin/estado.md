# Estado · actualizado 2026-10-28

## ▶ VIERNES 30/10
- **P7 · Respuesta al CEO sobre ShowMe:** documento «ShowMe: ¿ayuda de verdad?» (https://claude.ai/artifact/QBpRPWCufZe3HsZasYigyk), privado y sin enviar. Responde a las 3 preguntas con el informe v5 completo (H-58) y el corte mes a mes con Leopard (H-57). Faltan los vídeos y rehacer septiembre cuando Leopard cierre octubre.
- **P3 · Asana:** cerradas las 4 tareas de landings (ES resto, ES hoteles, IT hoteles, IT resto), cada una con un comentario a @Carlos con los IDs de las A y las B. Los A/B corren desde el 29/10. Portugal va dentro del comentario de ES resto. Sigue abierta «Registrar cada test en el tracker» (3/11).
- **Asana (11:28):** cerradas con comentario a @Carlos las 6 tareas de eventos (solo enseñaron su QR Marta, Rocco y Manuel), la subtarea de Cello «Reunir con Valery…» (Valery ya tuvo su reunión y espera a tener toda la documentación lista para enseñársela a posibles clientes de referidos) y «Corregir las UTM de las PMax» (Snowball las corrigió el 27/10).
- **P7 Portugal:** hoy el lote es de 150 (objetivo: 500 acumulados). A las 08:05, HubSpot marcaba 468 con `showme_pt_recovery` = true. Falta el comentario en Asana con la cifra final.
- **P3 · Seguimiento A/B (revisión automática del viernes):** informe en [seguimiento-ab/2026-10-30.md](trabajo-en-curso/p3-landings/seguimiento-ab/2026-10-30.md). Sin significación todavía; reparto A/B desigual el 29/10 y caída fuerte de clics en ES Vacational y PT.

## ▶ HECHO EL JUEVES 29/10 (resumen; detalle en hallazgos H-44 a H-52 y en p1-onboarding.md)
- **P7 Portugal:** workflow «ShowMe PreTrial -> Trial (Portugal)» creado y activado; los 9 leads corregidos (H-44). Recovery: 350 enrolados, comentado en Asana. Pedro respondió a las 3 preguntas (H-49): hay que corregir el borrador al CEO (quién entra, «converted»); los vídeos van después del 30/10.
- **P1 Onboarding:** funnel de 30 días (H-48), Clarity conectado y 500 grabaciones analizadas (H-46, H-47, H-50, H-51), tramos de tamaño (H-52). Dashboard renombrado a «Onboarding Chekin: del alta a la activación», con la sección nueva «Alta y onboarding». **Documento para Daniel:** https://claude.ai/artifact/2WEQKEeA2NfBKpybzB45gX · **Prototipos navegables:** portátil https://claude.ai/artifact/DfLw9HeJKddbpxHYRC6mLP · móvil https://claude.ai/artifact/CjcH5gMdon5qBKatXSLopN (lienzo de diseño: https://claude.ai/artifact/U8YpmnbK8qQrjdd3vssSUc). Los dos son privados: hay que compartirlos con Daniel.
- **P6 Cello:** resumen en `p6-cello.md` (H-45).
- **P3:** el A/B de España sigue en el paso 1 de 5 en «Martes 27».
- **Viernes 30:** Portugal (las dos últimas tandas), respuesta al CEO, mensaje a Daniel y revisar el workflow de `property_size`.

## ▶ EMPIEZA AQUÍ (jueves 29/10 · Carlos de vacaciones hasta el 3/11)
Lo de abajo de este bloque es el histórico. Horas: semana 26–30/10 ≈ 18 h → quedan ~2 h para jue–vie: priorizar.

**0. Portugal recovery:** hoy 29/10, lote de 100 (van 250). El viernes 30/10 se termina en dos tandas (primera hora y final del día, sueltos incluidos) y se comenta en Asana.

**1. Primero (5 min):** enviar a Pedro (ShowMe) las 3 preguntas: quién entra exactamente (1–3 viviendas, ¿algún filtro más?), si cuentan como convertidos los leads sin conversación, y cómo hacer altas de prueba sin contar. Borrador en `trabajo-en-curso/p7-showme-encargo-ceo.md`.

**2. Vence el 30/10:**
- **Encargo del CEO sobre ShowMe** (Asana gid 1219967710164778). Borrador de respuesta listo al final de `p7-showme-encargo-ceo.md`, sin enviar. Conclusión con pagos reales (H-43): ShowMe no sube la conversión a pago (ES 14,8% con vs 20,0% sin; IT igual mes a mes). Falta: vídeos (3 micro + 1 SMB; resolver teléfono y URL de registro) y respuesta de Pedro. Pendiente que Alex pase la frecuencia de contacto que conoce.
- **P3 · A/B en HubSpot (avanzado el 28/10 en el chat «Martes 27»):**
  - Foco en las PMax de Google con su landing principal como A y nuestro boceto como B: ES Vacational (SES v2), ES Competitors (hoteles v6), IT Vacational (Alloggiati v1, nueva), IT Competitors (Questura v5), PT Vacational (SIBA v1, nueva) y PT Competitors (check-in online PT v1, nueva). Mapa con enlaces en el histórico del 27/10, más abajo.
  - Las 6 A están publicadas y el plan de HubSpot **sí permite A/B** (Test → A/B test, 50/50, ganador manual). El conector de HubSpot ya lee landing pages.
  - La A española (page id 221464769047) es **un único bloque HTML** con el formulario real de HubSpot insertado (`e42c7acf…`). Plan: crear el A/B y en la variante B sustituir ese bloque por el HTML de la B, con el mismo formulario.
  - **Siguiente paso:** terminar el HTML de la variante B de España (SES) para HubSpot. Se estaba preparando cuando el ordenador se suspendió: retomar en el chat «Martes 27». Sin crear todavía el A/B en HubSpot (con OK de Alex).
  - Decisiones del 28/10 en `decisiones.md`: foco en 4 PMax, «Sin tarjeta de crédito. Activación inmediata.» en las 6 B, bloque interactivo de la A en las B, SEF/AIMA en Portugal.
- Propuesta CRO y plan de experimentación (Carlos, 30/10).
- KPI de activación con Daniel · qué cifra de MRR usamos · Óscar (Cálido) a Valery · Reverrr. Con ~2 h no cabe todo: mover en Asana con comentario lo que no se haga.

**3. Pendiente de enviar / responder:**
- **Sebastián (Snowball):** respuesta corta sobre automatizaciones HubSpot ↔ Meta/Google (eventos de conversión por lifecycle y auto tracking activos, H-32). Antes, mirar la pestaña *Audiences* de Anuncios en HubSpot.
- **Snowball:** Italia no tiene campaña de Meta de alquiler vacacional funcionando (H-34).
- **Isaac (Snowball):** ve el dashboard «Organic Lead Gen (SEO)» pero vacío (solo ve sus contactos). Decidir: «ver todos» en Contactos o envío programado por email. Comentario propuesto para Carlos en la tarea «Recordatorio: revisar con Isaac el dashboard de AEO / GEO» (sin publicar).

**4. Asana atrasado:** UTM de las PMax · mapa de tareas para Carlos (gid 1219818181506129) · 5 tareas de eventos (Marta y AEs).

**5. Seguridad, sin confirmar:** token de Supabase `chekin-connect-despliegue`, token de HubSpot, historial del terminal; contraseña de ShowMe en Slack; clave live de Stripe en Notion.

**6. Próximas fechas:** 29/10 Cello con Valery · 30/10 lo de arriba · 3/11 test SES v2, baseline de CR, tracker, Hasp, **medir de nuevo el recovery de Portugal** (H-56: enrolados frente a no enrolados, % que empieza la prueba; luego pago en Leopard) · 4/11 Italia resto · 5/11 Italia hoteles · 6/11 España hoteles lista, plan de Cello, revisión con Carlos · 10/11 test España hoteles.

**Dónde está cada cosa:** reglas en `/CLAUDE.md` · hallazgos en `hallazgos.md` (hasta H-43; ojo, dos sesiones escriben a la vez: comprobar el último número antes de añadir) · decisiones en `decisiones.md` · fichas en `trabajo-en-curso/` · ShowMe en `p7-showme.md` y `p7-showme-encargo-ceo.md` · landings en `trabajo-en-curso/p3-landings/`.

---

## Hecho
- P3: diagnóstico de la landing de PMax España Hoteles, deck de 14 diapositivas y tracker de tests creados.
- Casa `chekin` montada.
- Asana: tareas creadas en los 4 proyectos GTM (QR, Auditoría, Onboarding, Web). Faltan fechas de P1 tras la meet con Daniel.

## A medias
- **P2 · QR para eventos (AEs)** — web nueva activa (chekin-connect.vercel.app) y envío a HubSpot activo desde el 26/10 (ver «Lunes 26/10»). Pendiente: revisión final con Carlos (27/10), seguridad de tokens y seguimiento de eventos. [El escáner con Claude: ver histórico de P2]
- **P3 · Auditoría de landings y creatividades de paid** — todo el contexto está ya en la casa (traspaso, landings, fuentes, hallazgos). Pendiente:
  - Aprobación del plan (Carlos).
  - 22/10: Carlos propone una landing por anuncio (funcionalidad concreta primero, luego el resto de Chekin), más innovadoras. Se alinea en la reunión de growth check. Choca con la expansión de URL final activada en la PMax ES y con la conversión "cualquier formulario" (ver `trabajo-en-curso/p3-auditoria-paid.md`).
  - 5 landings en Boceto (PMax general + 4 ángulos: SES, upselling, Inbox IA, recepción) en `trabajo-en-curso/p3-landings/` y en la Biblioteca de landings de Notion. Siguiente: compartir los 5 enlaces, revisarlas con Carlos, montar la 1 en HubSpot con OK.
  - Test fase 1 **pausado** en el tracker (expansión de URL).
  - Formulario de HubSpot con 5 campos + ocultos; texto legal al DPO.
  - Ventas: qué recibe el hotel al enviar, cuándo le contacta el experto y si debe registrarse en el dashboard.
  - Sacar los términos de búsqueda de la PMax (Windsor.ai).
  - Producto: "120 PMS" → "+200" en el registro; confirmar Inbox IA para hoteles.
  - Corregir las UTM de las PMax (prioritario: plantilla de seguimiento / sufijo de URL final de Competitors y Vacational ES/GB/DE).
  - Confirmar si el plan de HubSpot permite A/B de landings.
  - Medir línea base: demo, guía y fuga.
  - Ticket medio de un hotel y su pipeline [€__].
  - Permiso para mostrar Iberostar, Meliá y Barceló; logos de PMS; fuente Proxima Nova.

## Pendiente
## Miércoles 28/10, hecho (sesión general)
- **Isaac (Snowball):** permiso de informes activado en HubSpot (asiento View-Only, sin coste); el dashboard es de Gabriel y está en «Everyone can view». Ve el dashboard pero vacío (solo «sus» contactos).
- **Portugal recovery:** lote de 100 → **250 acumulados** (HubSpot), comentado en Asana.
- **Mateo (Snowball):** preguntado por el A/B en Google; Snowball confirma que va en HubSpot.
- **Encargo del CEO sobre ShowMe:** tarea en Asana (30/10); análisis con/sin ShowMe (H-26 a H-30, con lifecycle Customer) corregido con el informe v5 de Carlos (H-42) y con pagos de Leopard (H-43); guion de vídeos, mensaje a Pedro y borrador de respuesta en `p7-showme-encargo-ceo.md`. ShowMe solo trabaja leads de 1 a 3 viviendas (Alexandre).
- **Brief «Landings de paid: antes y después»** republicado con estado al 28/10, Italia y páginas de gracias (https://claude.ai/artifact/BPBSyMM1PbQAmiKMijFNAq).
- **HubSpot ↔ Meta/Google:** cuentas de Google Ads y Meta conectadas con auto tracking; eventos de conversión por lifecycle activos hacia las dos (H-32); formularios de Meta entran solos (H-33; H-31 corregido); LinkedIn desconectado.
- **Leads de 7 días:** Meta 80 leads, cuadran con HubSpot (H-34); Google 4.535 € y 73 contactos nuevos (H-35).
- **P2:** tarea «Revisión final con Carlos y entrega a los AEs» cerrada con comentario a Carlos.
- El informe de Carlos «Landings…» de la biblioteca de anuncios (artifact 1qcX…) es una foto fija del 19/10, no se actualiza solo.

## Martes 27/10, hecho (resumen en curso)
- **P2 · Giulia sin acceso a chekin-connect:** cuenta y perfil bien (`giulia@chekin.com`, confirmada, activa), pero nunca había entrado: la contraseña provisional del 26/10 no valía. Contraseña nueva generada en Supabase (SQL) y probada por Alex. [POR COMPROBAR] Joan: mirar si tiene el mismo problema (`last_sign_in_at` vacío).
- **P7 · Portugal recovery (ShowMe):** 100 enrolados hoy → **150 acumulados** (comprobado en HubSpot: `showme_pt_recovery` = true; 50 el 26/10 + 100 el 27/10). Ritmo: 100 al día durante 5 días. Alex ha escrito a Pedro para pedir el desglose de resultados.
  - Medición: enrolados en HubSpot · contactados y respuestas, ShowMe · trial y MRR, HubSpot (`showme_trial_started_portugal`) + Leopard.
- **Asana (con OK de Alex):**
  - «Enrolar 100 leads de prueba de Portugal en ShowMe» (gid 1219770867648212): tarea única del recovery de PT; fecha 30/10; comentario con plan, acumulado, cómo se enrola y cómo se mide.
  - «Portugal: enrolar 50 clientes al día»: **eliminada** por decisión de Alex (sustituida por la anterior).
  - Cerradas con comentario a Carlos: alternativas de landing y CTAs; funnel de PostHog para Daniel (revisado hoy con Daniel, OK); mensaje a Snowball (hablado en la meet del 26/10, Snowball lo trabaja; **seguimiento el 28/10**).
- **Abiertas:** 5 tareas de eventos (TOPO Connect, Cloudbeds PT, Scale Fest, Avvapro Sevilla, Tu Alquiler Asturias); revisión final del QR con Carlos; UTM de las PMax; mapa de tareas para Carlos (vencen hoy).
- **P3 · Feedback de Valery sobre las landings (27/10):** le gustan (mensaje alineado con el anuncio, móvil arreglado, un solo CTA). Pendientes que salen de ahí:
  1. Guía SES y pack legal: tras el formulario el usuario **tiene que recibir el PDF** (la actual lleva a una thank you page con el enlace). Al montar en HubSpot, mantener thank you page con descarga y/o email. [POR COMPROBAR qué hace hoy el formulario]
  2. Responder a Valery si los formularios son los mismos de HubSpot. [POR COMPROBAR]
  3. Guest app: el boceto no es igual a la app real; Valery ofrece capturas reales: pedírselas.
  4. Poner **logos de los PMS** (se identifican más rápido). Logos recibidos y guardados en `trabajo-en-curso/p3-landings/logos/` (13 partners + 6 clientes). Las landings de rental (SES v2, guía, pack legal, guest app, affitti IT) no llevan logos todavía.
  - **Archivos descargables (comprobado en landing.chekin.com, 27/10):** ya en HubSpot: guía SES (`hubfs/Chekin_Guía_SES.Hospedajes.pdf`), parte de viajeros Word (`hubfs/Chekin-Modelo de parte de viajeros (Word).docx`), contrato alquiler vacacional (`hubfs/CONTRATO DE ALQUILER VACACIONAL.pdf`), factura (`hubfs/PLANTILLA FACTURA.pdf`) y contratto IT (`hubfs/Contratto Affitto Turistico.pdf`). Cada landing actual redirige a su thank you page con el enlace. Excel de registro de viajeros: también está en HubSpot (`hubfs/Chekin-Modelo de parte de viajeros.xlsx`, mismo archivo que pasó Alex el 28/10); ya enlazado en la página de gracias del pack.
  - **Enlaces de revisión actualizados (27/10):** guest app con capturas reales y logos https://claude.ai/artifact/6H23uPLZEJyBSbnVNWhTPP · SES v2 https://claude.ai/artifact/WSjWXPdZfVKVF781QqLdNK · guía v2 https://claude.ai/artifact/HWpa7NEiAcJAPwmYzvK1Uz · pack legal https://claude.ai/artifact/P8tf8sdAtaTqAXr8f7iZAj · affitti IT https://claude.ai/artifact/9JQowwwGyKbF2dZXhzF94x. Páginas de gracias (nuevas, privadas; en el visor de Claude los botones no descargan, en HubSpot sí): guía https://claude.ai/artifact/12J4bUSkMP47jiUWTSwQZX · pack https://claude.ai/artifact/FeF6rviuvLwbc1EkeeqGju · contratto IT https://claude.ai/artifact/JG3RSuqqz9JjLkTUrEWzDY. Fuentes en `trabajo-en-curso/p3-landings/` y `p3-landings/gracias/`.
  - **Formularios actuales (leído 28/10, sin tocar HubSpot):** guía 26d9814f, contrato 13e8319d, parte Word 58865ed4, factura 7aebfc15 y contratto IT 76da1bed piden lo mismo que los bocetos: nombre, email, teléfono, tipo de alojamiento y nº de alojamientos (+ `last_form_type` oculto). La guía además tiene empresa (opcional) y casilla de privacidad. Propuesta: reutilizar los formularios actuales; el pack legal (une 4) necesita elegir uno o crear uno nuevo. HubSpot, al final.
  - **28/10 · Snowball:** el A/B se hace en HubSpot (no en Google). Cada landing nueva = variante B de la actual, misma URL. Pendiente: reconectar el conector de HubSpot con permisos de landing pages (falló al leer formularios) y comprobar que el plan permite A/B.
  - P6: para partners, el enlace de Cello va asociado a una cuenta de Chekin; Valery lo aclarará (viernes).
- **P7 · Portugal (28/10):** 250 enrolados (26/10 50 · 27/10 100 · 28/10 100), comentario en Asana. Jueves 29/10: 100. Se termina el viernes 30/10 en dos tandas, una a primera hora y otra al final del día (incluidos los sueltos), y se ve cómo queda; la tarea mantiene su fecha, 30/10.
- **P3 · Foco en las 4 PMax (28/10):** variantes B listas para ES Vacational (SES v2), IT Competitors (Questura v4) y ES Competitors (hoteles v6). Nueva: **Alloggiati Web IT v1** (variante B de /it/check-in-online-alloggiati-web, PMax IT Vacational) https://claude.ai/artifact/7Tii5vGzn9mBiTjrwDm3ES (privado). H-36 y H-37 con URL finales, % de clics y conversión.
- **P3 · Portugal (28/10):** variante B de /pt/check-in-online-siba (PMax PT Vacational), mismo texto y estructura corregida según H-40: https://claude.ai/artifact/3evqPyLdFvBwt2Yx5DXtgM (privado). Fuera del orden de P3 (ES e IT primero).
- **P3 · Portugal (28/10):** variante B de /pt/check-in-online (PMax PT Competitors): https://claude.ai/artifact/1GvvvRc3sGZakekSwP2qKK (privado). Auditoría en H-41.
- **P3 · Mapa A/B de las PMax de Google (28/10)** — A = URL final actual en landing.chekin.com (las 6 responden 200); B = boceto nuestro:
  | Campaña | A (actual) | B (boceto) |
  |---|---|---|
  | ES PMax Vacational | /es/check-in-online-ses-hospedajes | SES v2 https://claude.ai/artifact/WSjWXPdZfVKVF781QqLdNK |
  | ES PMax Competitors | /chekin-hoteles | Hoteles v6 https://claude.ai/artifact/MNjzT6AykyJskR75SzasEc |
  | IT PMax Vacational | /it/check-in-online-alloggiati-web | Alloggiati v1 https://claude.ai/artifact/7Tii5vGzn9mBiTjrwDm3ES |
  | IT PMax Competitors | /it/ads/registrazione-ospiti-questura | Questura v5 https://claude.ai/artifact/7Jd3wwkK5AXQJ1fdHf1yZh |
  | PT PMax Vacational | /pt/check-in-online-siba | SIBA PT v1 https://claude.ai/artifact/3evqPyLdFvBwt2Yx5DXtgM |
  | PT PMax Competitors | /pt/check-in-online | Check-in online PT v1 https://claude.ai/artifact/1GvvvRc3sGZakekSwP2qKK |
  ✅ 28/10: Alex confirma en HubSpot que las 6 A están publicadas (ES Vacational = «Paid-Chekin-Compliance-GA-2026 (Spanish)»). ✅ El plan permite A/B: en el editor de la A española (page id 221464769047) sale «Test → A/B test» (variante manual, tráfico 50/50, eliges ganador). Sin crear todavía.
  ✅ 28/10 (tarde): el conector de HubSpot ya lee landing pages. La A española (221464769047) usa el tema @hubspot/session (Figtree); cabecera y pie salen del tema, y la zona de contenido (dnd_area) **no tiene módulos visibles por la API**: el cuerpo (hero, formulario, pestañas) está fuera de los módulos Alex lo comprueba: el cuerpo es **un bloque HTML** en el editor. El formulario se inserta dentro con hbspt.forms.create en `#ck-form-slot` (ES: formulario e42c7acf…). Plan: en la variante B se sustituye ese bloque HTML por el de la B, manteniendo el mismo formulario de HubSpot.
  ✅ 29/10: bloque HTML de la variante B de España listo para pegar en HubSpot: `trabajo-en-curso/p3-landings/hubspot/variante-b-es-ses.html` (mismo formulario e42c7acf de la A; CSS dentro de .chkb). Probado con el formulario real (sin enviar): botón a 550 px en portátil y 752 px en móvil, sin scroll horizontal.
  ✅ 29/10: bloques HTML de las otras 5 variantes B en `trabajo-en-curso/p3-landings/hubspot/` (es-hoteles, it-alloggiati, it-questura, pt-siba, pt-checkin-online), con formulario de HubSpot de 5 campos y prefijo del país por defecto (ES e42c7acf +34 · IT ca54cc24 +39 · PT 23a6aa7a +351); las A no se tocan (decisión de Alex: la B lleva las mejoras, por eso es un A/B). Probados a 1512×780 y 390 px: formulario cargado, sin scroll horizontal, sin errores. IDs de las A: ES SES 221464769047 · ES hoteles 217124968807 · IT Alloggiati 221484646818 · IT Questura 213710760063 · PT SIBA 221492326070 · PT check-in 177437110037. Ver H-54 (las A de IT y hoteles piden solo email).
  ✅ 29/10: **A/B ES Vacational creado** (A 221464769047 · B 225864333953). El cuerpo de estas páginas va en **Settings → Advanced → Head HTML** (no en un módulo). Claude ha subido la B por el conector (SET_METADATA headHtml, borrador, sin publicar). Logos de la B pasados a URLs públicas (hubfs y chekin.com) para que pese ~40 KB. Pendiente: revisión de Alex en la vista previa y publicar con su OK.
  ✅ 29/10: B de ES Vacational ajustada tras la vista previa (texto centrado, una sola flecha, Tipo/Nº a ancho completo, cifras en el hero en portátil). Alex la da por buena. Pendiente: Publish del test por Alex y hora de inicio.
  ✅ 29/10: **A/B ES hoteles creado** (A 217124968807 · B 225872837278). B subida por Claude al Head HTML (formulario e42c7acf, +34; 63 KB, logos por URL). Probada a 1512×780 y 390 px: botón visible sin bajar en los dos. Pendiente: vista previa de Alex y Publish.
  🟢 **29/10 ~11:50: A/B de ES Vacational y ES hoteles PUBLICADOS por Alex** (inicio del test; hora exacta [POR COMPROBAR], antes de las 11:52). Comprobado por Claude en navegador real: 10 visitas nuevas → ES 5 A / 5 B, hoteles 4 A / 6 B; la B en vivo carga el formulario de 5 campos con +34, sin cabecera ni pie del tema y sin scroll horizontal. Ojo: curl y Chrome sin interfaz (headless) reciben siempre la A (HubSpot deja fuera a los bots), así que para comprobarlo hay que usar un navegador real. Siguiente: IT Alloggiati (A 221484646818).
  ✅ 29/10: **A/B IT Vacational (Alloggiati) creado** (A 221484646818 · B 225876938077). B subida por Claude (formulario ca54cc24, +39), con la sección «Prima e dopo» recuperada (su script se había perdido al quitar el formulario de maqueta; lo mismo con las pestañas de Questura). Móvil compactado en las 4 B que quedan: botón dentro de la primera pantalla. Pendiente: vista previa y Publish por Alex.
  ✅ 29/10: «OK» de la tarjeta de Alloggiati cambiado por un check verde (Alex no entendía qué era). **A/B IT Competitors (Questura) creado** (A 213710760063 · B 225876940071), B subida por Claude (ca54cc24, +39, pestañas recuperadas). Pendiente: vista previa y Publish de las dos de Italia.
  🟢 **29/10 ~12:10: A/B de IT Alloggiati e IT Questura PUBLICADOS por Alex.** Comprobado en navegador real: Alloggiati 5 A / 5 B, Questura 6 A / 4 B (10 visitas cada uno; al minuto de publicar aún salía solo la A por la caché). Siguiente: Portugal (SIBA A 221492326070, check-in online A 177437110037).
  ✅ 29/10: **A/B PT Vacational (SIBA) creado** (A 221492326070 · B 225876941621). B subida por Claude (23a6aa7a, +351). Probada a 1512×780 y 390 px. Pendiente: vista previa y Publish de Alex; después PT check-in online (A 177437110037).
  ✅ 29/10: **A/B PT Competitors (check-in online) creado** (A 177437110037 · B 225876946233). B subida por Claude (23a6aa7a, +351). Con esto las 6 B están subidas. Pendiente: vista previa y Publish de las dos de Portugal; mañana comprobar el reparto de visitas de los 6 tests.
  ✅ 29/10: las dos B de Portugal compactadas a petición de Alex (la tarjeta se cortaba en el editor): título del formulario en una línea, sin «Introduzir um número», texto legal más pequeño. Botón a 584 px en pantalla de 700 px de alto.
  🟢 **29/10 ~12:25: los 6 A/B de las PMax de Google EN MARCHA** (Alex publica los de Portugal). Comprobado por Claude en navegador real, 8 visitas nuevas por página: ES SES 3A/5B · ES hoteles 5A/3B · IT Alloggiati 3A/5B · IT Questura 5A/3B · PT SIBA 1A/7B · PT check-in 5A/3B → las 6 sirven A y B. Siguiente: medir por página (envíos y leads que pasan a prueba/SQL), no solo envíos; primera revisión de reparto el 30/10.
  ⚠️ 29/10: H-53. La PMax ES Vacational pasó de ~900 a ~65 clics/día desde el 20/10 con el mismo gasto (CPC ~0,2 € → ~3 €). El A/B de ES Vacational recibirá ~30 visitas por variante al día. Preguntar a Carlos/Snowball qué se cambió el 20/10.
  📅 **Seguimiento de los 6 A/B (acordado con Alex, 29/10):** revisión **cada viernes** con los datos de la semana (clics de Windsor + visitas y envíos por variante en HubSpot + leads que pasan a prueba/SQL). 30/10: comprobar que funciona (reparto y envíos de la B). 6/11: primera tendencia (ES Vacational ~500 clics/semana → ~250 por variante). Cálculo orientativo para ES Vacational con la conversión histórica de la landing (3,7 %, HubSpot, 21/07–18/10, tráfico anterior al 20/10): para ver que la B dobla la conversión hacen falta ~600 visitas por variante (≈ 3 semanas al ritmo actual); para ver una mejora del 50 %, ~2.000 por variante (≈ 2 meses). La conversión con el tráfico posterior al 20/10 está [POR COMPROBAR].
  Sin tráfico de paid desde el 27/10 (eran URL de expansión): guía SES v2, guest app v2, pack legal, affitti IT y las 4 de «una landing por anuncio». Se guardan, no se usan en el A/B.
- Carlos se ha creado hoy «Informe ShowMe v5 con los datos nuevos» (vence 27/10) en el proyecto MRR + ShowMe.

## Lunes 26/10 (Tenerife con Carlos), hecho
- **P3 · Italia:** las 4 campañas de Google analizadas (H-18): 17 URL, pero 3 páginas se llevan el 94% de los clics, y el formulario de questura cuenta como conversión secundaria (101 en «todas las conversiones»). Cruce con el plan de noviembre de Snowball (H-19): Google es ~30% del presupuesto de Italia, no hay campaña de hoteles en Google IT y Search Intención IT no está en el plan. Los dos hallazgos están copiados en la ficha P3 de Notion. **Decidir con Carlos:** pasar el formulario a conversión principal, si el boceto «IT hoteles» se reorienta a alquiler vacacional y qué pasa con Search Intención IT.
- **P2 · Chekin Connect:**
  - Enlace para los AEs: https://chekin-connect.vercel.app/mi-perfil (versión nueva). No se pudo dar a la web nueva el nombre `qrsaleschekin.vercel.app`, porque no hay acceso a la cuenta personal de Vercel. La web antigua sigue funcionando con la versión anterior y la misma base de datos.
  - Contraseñas provisionales (con cambio obligatorio) para Giulia y Joan, generadas en el terminal de Alex. Rocco ya había entrado con su contraseña; el último script incluía también la suya [POR COMPROBAR si se ejecutó ese SQL]. Faltan en sus tarjetas: Giulia, Calendly y foto; Joan, teléfono, Calendly y foto; Pablo, foto.
  - **Envío a HubSpot activo:** app privada «Chekin Connect» (3 permisos de contactos y propietarios), token en Supabase y función desplegada. Sin propiedades nuevas: MQL Type solo si estaba vacío y Last MQL type siempre, con Event, Webinar o **Digital QR** (opción creada el 26/10). El evento concreto va en la nota. Probado con un contacto PRUEBA (borrado de la app; en HubSpot, a la papelera). Reenviados los 5 leads antiguos: 5 en HubSpot, 0 errores.
  - **Rutina «Chekin Connect · eventos terminados → Asana»** (L–V 9:00, modo Auto): crea en Growth Daily › Alexandre una tarea por evento terminado, con cifras y una subtarea por AE. Clave en el Llavero. Primeras 5 tareas creadas hoy. Documentación en `agentes-rutinarios/chekin-connect-eventos-terminados.md`.
- **Tarde del 26/10:**
  - **P3:** H-21 (PMax Vacational IT: alloggiati convierte al 3,4% aunque Ads le cuente 0). Análisis de competencia en `trabajo-en-curso/p3-competencia-landings.md`: Vikey, Partee y 9 más. A Carlos le gustan las 4 landings. Aplicado en IT hoteles (v4), IT resto (v3) y SES v2: «sin tarjeta y sin compromiso», «habla con un experto» (IT hoteles), los 3 portales en IT, el plazo legal y una línea de prueba social bajo el botón. Se mantienen los 5 campos; sin vídeos ni precio (¿~17 € con IVA? [POR COMPROBAR]).
  - **P3:** Alex trabaja de forma autónoma y habla directamente con Snowball (OK de Carlos). El mensaje a Snowball sigue sin enviar.
  - **MRR:** la fuente buena es LEOPARD (`mrr_leopard_eur` en HubSpot). Falta el traspaso con Carlos.
  - **P5:** OK de Carlos al GIF de la firma. Entregado.
  - **Portugal:** tarea en Growth Daily › Alexandre: 50 al día con Showme_PT_recovery = Yes. 26/10: 50 acumulados.
  - **P2:** los AEs están bien. The TOPO Connect: 2 leads reales y 2 pruebas (Asana corregida).
- **Final del 26/10:**
  - **P3 · Fechas en Asana (con un comentario en cada tarea):**
    - SES v2: montaje el 30/10 y lanzamiento el **3/11** (el 2/11 es festivo);
    - tracker y línea base de octubre: 3/11;
    - España hoteles: 6/11 y lanzamiento el 10/11;
    - **Italia hoteles: 4/11; Italia resto: 5/11** (adelantadas por Alex);
    - UTM: 27/10.
  - **P3 · Borrador para Snowball** (formulario como conversión principal en las PMax IT, con fecha del cambio) al final de `trabajo-en-curso/p3-pmax-que-cambiar.md`. **Sin enviar:** lo revisa y lo envía Alex. Conviene que salga esta semana, antes del 4/11.
  - **P7 · ShowMe:** proyecto nuevo de Alex. Contexto y pendientes en `trabajo-en-curso/p7-showme.md` (handoff a persona, la secuencia escribe a clientes que ya pagan, email de soporte, IVA en Italia, recovery de Portugal).
  - **Seguridad:** la contraseña de ShowMe está en texto plano en un DM de Slack (cuenta de Gabriel) y hay una clave live de Stripe en la página «STRIPE» de Notion. Hay que avisar para cambiarlas.
- **Pendiente de P2:**
  - **Seguridad:** revocar el token de Supabase `chekin-connect-despliegue` y rotar el token de HubSpot (los dos quedaron a la vista en el terminal). Tras rotar el de HubSpot, volver a guardarlo con `desplegar-hubspot-sync.sh`. Borrar `sbp_` y `pat-na1` del historial del terminal.
  - Preguntar a Marta cuáles de sus 4 leads de The TOPO Connect eran pruebas (aparecen su email y el de Carlos) y corregir la tarea de Asana. En la ficha de Carlos en HubSpot, Last MQL type ha pasado a «Event».
  - Asignar las subtareas de seguimiento a Marta y Pablo. Preguntar a los AEs por qué 3 de los 5 eventos tienen 0 leads (H-20).
  - ✅ (26/10, Alex) Enviados a Giulia y Joan su enlace y contraseña; Rocco ya tiene acceso. AEs avisados del enlace nuevo.
  - ✅ (27/10) Giulia no podía entrar: cuenta y perfil bien, pero la contraseña provisional del 26/10 no valía (nunca había iniciado sesión). Contraseña nueva generada en Supabase (SQL) y probada por Alex. [POR COMPROBAR] Joan: mirar si tiene el mismo problema (`last_sign_in_at` vacío).

## Asana al día (23/10, tarde)
- Growth Daily › Alexandre: tarea índice «Mapa de tareas de Alexandre: owner, fecha y «hecho»» (gid 1219818181506129), con todas las tareas abiertas enlazadas y un comentario a Carlos. Asana no permite añadir desde aquí una tarea existente a otro proyecto: por eso es un índice con enlaces, no tareas duplicadas.
- Cerradas con comentario: animación del logo, revisión de la configuración de PMax, app del QR en GitHub, «MRR: recibir el traspaso» (repetida) y «Arrancar web y CRO» (sustituida).
- «Hecho =» añadido en las tareas de P3, P2 y P1 que no lo tenían. Estado como comentario en cada tarea abierta. QR (revisión final) pasa al 27/10 y KPI de activación al 30/10.
- Experimento de Hasp: ahora es subtarea de la animación (3/11).
- **P6 · Cello (referidos) con Valery**, nuevo: tarea en Growth Daily › Alexandre con 4 subtareas (29/10, 30/10, 4/11 y 6/11) y ficha P6 en Notion. Plan para el 6/11.
- P3 Italia: bocetos de hoteles y resto, y brief «Landings de paid Italia: antes y después» (https://claude.ai/artifact/DrJ1sVouzZ6bQkZ4GcsRGz). H-17: las PMax IT no cuentan las conversiones de sus landings.

- **Antes del lunes 26 / en Tenerife con Carlos:**
  - Compartir con Carlos el brief [Landings de paid: antes y después](https://claude.ai/artifact/BPBSyMM1PbQAmiKMijFNAq) y los bocetos nuevos (guía v2, pack legal, guest app v2).
  - Pedir a Carlos la app privada de HubSpot (superadmin) y las 2 propiedades; guardar `HUBSPOT_TOKEN` en Supabase; prueba con un contacto "PRUEBA".
  - Enviar el mensaje a Snowball (borrador en `trabajo-en-curso/p3-pmax-que-cambiar.md`) tras hablar con Carlos.
  - Decidir con Carlos: Competitors ES (expansión de URL), fechas nuevas de P3, Clarity, test SES en Vacational.
  - Enseñar a Daniel el funnel (dashboard + PostHog) y pedirle grabaciones y eventos de activación.
  - Avisar a los AEs de la web nueva chekin-connect.vercel.app.
  - Comentarios en Asana mencionando a Carlos en las tareas del lunes que están hechas (con OK de Alex).
  - Comprobar /check-in-guestapp en un móvil real (sale en blanco en el emulador, H-16).
- **P5 · foto de perfil de Carlos (23/10):** `chekin-perfil-carlos-DEFINITIVA.gif` (foto → círculo azul desde el centro → check → vuelve la foto; 166 KB). Plantilla `make_gif_persona.py` para el resto del equipo. Falta que Carlos la suba desde el móvil y comprobarla.
- **P5 · 23/10:** Carlos quiere la **cuadrada para todo**. Comprobado: subida desde el móvil, se ve **animada como foto de perfil de Google**. La cuadrada no va en Vercel (decisión de Alex); Alex la adjunta en la tarea de Asana. Pendiente: experimento de Hasp (sender con GIF / sin GIF, tarea del 3/11).
- **P5 · versión cuadrada HECHA (22/10):** solo el check en blanco sobre azul #385BF8, se dibuja, zoom fuerte y vuelve, halo nítido y brillo paralelo al trazo largo del check. Archivos en `2-herramientas/firma-gmail/`: `chekin-firma-cuadrada-DEFINITIVA.gif` (200 px), `-400.gif` y `chekin-foto-perfil-google.png` (1024 px, fija). Script `make_gif_cuadrado.py ... zoom`. Comentario a Carlos en Asana (tarea "Animación del logo de Chekin para la firma de Gmail", Growth Daily) pidiendo OK. **Falta:** adjuntar los archivos en esa tarea (la herramienta de Asana no sube adjuntos: lo hace Alex), el OK de Carlos, subir el GIF a la URL pública y actualizar el paso a paso. Nota: el comentario se escribió antes del último ajuste del brillo; los archivos definitivos ya lo llevan.
- **Lunes 26/10:** viaje a Tenerife (TNF) a trabajar con Carlos, 8:00–20:00 aprox. (en Google Calendar). Temas para ver con él:
  - PMax ES: revisar en Google Ads expansión de URL y exclusiones, recursos de texto automáticos, objetivo de conversión ("cualquier formulario") y términos de búsqueda. Contexto en `trabajo-en-curso/p3-auditoria-paid.md` → "Por qué Vacational se queda…".
  - Decidir Competitors: acotar expansión / testear donde va el tráfico / landing por anuncio.
  - Test SES en Vacational: página actual vs v2 de Alex (`p3-landings/landing-ses-hospedajes-v2.html`); registrar en el tracker si lo aprueba.
  - Guía SES: **boceto v2 hecho (23/10)**, corto y con formulario arriba: https://claude.ai/artifact/HWpa7NEiAcJAPwmYzvK1Uz. Decidir lanzamiento (no a la vez que otro cambio en Competitors). Formulario con teléfono (23/10).
  - **Brief para compartir pantalla:** [Landings de paid: antes y después](https://claude.ai/artifact/BPBSyMM1PbQAmiKMijFNAq) (fuente en `trabajo-en-curso/p3-landings/brief-carlos/`). SES v2 publicada en https://claude.ai/artifact/WSjWXPdZfVKVF781QqLdNK. Compartir los enlaces con Carlos antes.
  - **Guest app** (/check-in-guestapp, 2.009 € en 90 días, la que más gasta; sale en blanco en móvil, H-16): boceto v2 https://claude.ai/artifact/6H23uPLZEJyBSbnVNWhTPP. Comprobar la pantalla en blanco en un móvil real.
  - **Pack legal** (une guía SES + 4 plantillas, 45% del gasto de Competitors ES en 90 días, H-15): boceto https://claude.ai/artifact/P8tf8sdAtaTqAXr8f7iZAj, con titular según el anuncio (`?recurso=`). Solo si se mantiene la expansión de URL.
  - **PMax:** qué cambiar (6 cambios, 4 decisiones) y borrador para Snowball en `trabajo-en-curso/p3-pmax-que-cambiar.md`.
  - **Clarity en las landings** (dos proyectos, `rrl7tp5b6k` y `rqlc6g9qhu`): ¿de quién son? Alex no tiene acceso; pedirlo (H-14).
  - **Fechas nuevas de P3** (el 27/10 no se llega): propuesta y 5 decisiones para Carlos en `trabajo-en-curso/p3-propuesta-fechas-26-10.md`. Con su OK, cambiar las fechas en Asana.
  - Traspaso del MRR automático y tareas de Growth Daily antes de sus vacaciones.
- **P5 · Animación del logo de Chekin para la firma de Gmail** (encargo de Carlos; proyecto Asana "GTM: Animación del logo para la firma de Gmail", entrega 27/10). **GIF definitivo (v5) publicado** en https://chekin-sales-card-navy.vercel.app/firma/chekin-firma.gif, paso a paso en `2-herramientas/firma-gmail/paso-a-paso-gmail.md` y ficha P5 en Notion. Falta: enviarlo a Carlos para revisión. GIF ligero 150–200 px, fondo blanco o transparente, en bucle, estilo del reel de Instagram que indica la tarea; alojado en URL pública + paso a paso para ponerlo en Gmail. Se envía a Carlos, que lo pasa a Ventas y Partnerships. Fecha: en Asana pone 22/10, en la descripción "martes 27, antes de las vacaciones de Carlos" [POR COMPROBAR cuál vale].
- **P1 · Onboarding de producto** — 23/10: dashboard con mapa de medición, funnel mes a mes con hueco (04/09–12/10) y "Cómo medir bien"; funnel guardado en PostHog (TyO9mkZy) y acción "Alta nueva" (172704). **No hay clics ni grabaciones** en el alta y la configuración (H-13): pedir a Daniel el lunes, con OK del DPO. Ver `trabajo-en-curso/p1-onboarding.md`. Reunión con Daniel hecha (22/10). **Para el lunes 26/10:** funnel con datos limpios de PostHog, mes a mes, ajustado con los datos históricos; marcar dónde entran variantes y dónde se dejó de medir, y proponer cómo medir bien a partir de ahora. ⚠️ El 26 es el día en Tenerife con Carlos: tenerlo listo el viernes 23. KPI de activación por definir con Daniel.
- **P4 · Web, CR y experimentos en WordPress** — el último en empezar.
- **MRR automático** — pasa a Alex (Growth Check 22/10). Pendiente: sesión de traspaso con Carlos, idealmente antes del 27/10. Asana: tarea en el proyecto de onboarding.
- **Antes del martes 27/10** (vacaciones de Carlos 28/10–3/11): mis tareas de *Growth Daily* con owner, fecha y definición de "hecho". Tarea en Asana, sección "Alexandre".
- P2 · Escáner de tarjetas (21/10) — **EN PAUSA (22/10, lo retoma Alex)**. Para cerrarlo: 1) clave de Anthropic de empresa + desplegar `scan-card`; 2) HubSpot: app privada, 2 campos, secreto y webhook; 3) probar en móvil con tarjetas reales; 4) pasar a la web real.
  - Hecho: migración `20261024_scan_leads.sql` **aplicada en Supabase** (comprobada). Versión de prueba en Vercel, cuenta nueva: https://chekin-sales-card-navy.vercel.app (despliega solo desde `main` de este repo). Escáner también en la vista de admins.
  - Lector con **Claude** programado (función `scan-card` en Supabase; respaldo: lector del móvil). Probado en local con respuesta simulada. Falta: clave `ANTHROPIC_API_KEY` de empresa en Supabase y desplegar la función.
  - Envío a **HubSpot** programado (función `hubspot-sync`). Falta: app privada y 2 campos en HubSpot, secreto y webhook en Supabase.
  - Web real `qrsaleschekin` (cuenta Vercel antigua `alexsantanajimenez-afk`): **desconectada de Git**, sigue funcionando con la versión de antes. No se ha tocado.
  - Contactos de prueba guardados con "PRUEBA" en comentarios: borrarlos.
