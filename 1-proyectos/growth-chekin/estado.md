# Estado · actualizado 2026-10-23

## Hecho
- P3: diagnóstico de la landing de PMax España Hoteles, deck de 14 diapositivas y tracker de tests creados.
- Casa `chekin` montada.
- Asana: tareas creadas en los 4 proyectos GTM (QR, Auditoría, Onboarding, Web). Faltan fechas de P1 tras la meet con Daniel.

## A medias
- **P2 · QR para eventos (AEs)** — fichas hechas; falta un retoque: el lector del escáner con IA de visión vía API (opción B, ver abajo). Bloqueado: se espera la decisión de Carlos sobre la clave (22/10). Fecha límite en Notion: 2026-10-22.
- **P3 · Auditoría de landings y creatividades de paid** — corre en el chat "Landing Page". Pendiente:
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
