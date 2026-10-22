# Estado · actualizado 2026-10-21

## Hecho
- P3: diagnóstico de la landing de PMax España Hoteles, deck de 14 diapositivas y tracker de tests creados.
- Casa `chekin` montada.
- Asana: tareas creadas en los 4 proyectos GTM (QR, Auditoría, Onboarding, Web). Faltan fechas de P1 tras la meet con Daniel.

## A medias
- **P2 · QR para eventos (AEs)** — fichas hechas; falta un retoque: el lector del escáner con IA de visión vía API (opción B, ver abajo). Bloqueado: se espera la decisión de Carlos sobre la clave (22/10). Fecha límite en Notion: 2026-10-22.
- **P3 · Auditoría de landings y creatividades de paid** — corre en el chat "Landing Page". Pendiente:
  - Aprobación del plan (Carlos).
  - Corregir las UTM de las PMax.
  - Confirmar si el plan de HubSpot permite A/B de landings.
  - Medir línea base: demo, guía y fuga.
  - Ticket medio de un hotel y su pipeline [€__].
  - Permiso para mostrar Iberostar, Meliá y Barceló; logos de PMS; fuente Proxima Nova.

## Pendiente
- **Lunes 26/10:** viaje a Tenerife (TNF) a trabajar con Carlos, 8:00–20:00 aprox. (en Google Calendar).
- **P5 · Animación del logo de Chekin para la firma de Gmail** (encargo de Carlos; proyecto Asana "GTM: Animación del logo para la firma de Gmail", entrega 27/10). Primera versión hecha en `2-herramientas/firma-gmail/`; falta enlace público y paso a paso. GIF ligero 150–200 px, fondo blanco o transparente, en bucle, estilo del reel de Instagram que indica la tarea; alojado en URL pública + paso a paso para ponerlo en Gmail. Se envía a Carlos, que lo pasa a Ventas y Partnerships. Fecha: en Asana pone 22/10, en la descripción "martes 27, antes de las vacaciones de Carlos" [POR COMPROBAR cuál vale].
- **P1 · Onboarding de producto** — Alexandre pregunta a producto el 2026-10-22 y empieza. Irá lento, a base de feedback. KPI de activación por definir con Daniel.
- **P4 · Web, CR y experimentos en WordPress** — el último en empezar.
- **Backlog:** MRR automático.
- P2 · Escáner de tarjetas (21/10):
  - Hecho: migración `20261024_scan_leads.sql` **aplicada en Supabase** (comprobada). Versión de prueba en Vercel, cuenta nueva: https://chekin-sales-card-navy.vercel.app (despliega solo desde `main` de este repo). Escáner también en la vista de admins.
  - Problema: el lector gratuito del móvil (Tesseract) **falla mucho con fotos reales**. Propuesta: opción B, IA de visión vía función en Vercel; necesita clave de API de empresa → decisión de Carlos.
  - Web real `qrsaleschekin` (cuenta Vercel antigua `alexsantanajimenez-afk`): **desconectada de Git**, sigue funcionando con la versión de antes. No se ha tocado.
  - Contactos de prueba guardados con "PRUEBA" en comentarios: borrarlos.
