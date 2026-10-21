# P2 · Ficha con QR para los AEs en eventos

- Estado: hecho, falta una mejora.
- Código: `chekin-connect/` en esta casa (copiado del zip el 21/10). Antes vivía en `alexsantanajimenez-afk/Alexsantanagrowth`, rama `ccr-a117993b-4zv2fe`.
- Publicada en Vercel (`qrsaleschekin`), que **todavía despliega desde el GitHub antiguo**. Pendiente reconectar Vercel a este repo con Root Directory = `chekin-connect/sales-card`.
- Datos: Supabase `lxjefebmndcbnoxlyykw`.

## Decisiones del escáner (21/10)
- Consentimiento: casilla del AE "La persona me ha dado su tarjeta" → interés legítimo.
- Obligatorio: nombre + (email o teléfono).
- Lectura de la tarjeta en el propio móvil (opción A, gratis); pasar a IA de visión si falla mucho.

## Mejora pendiente (21/10): captar leads al revés
Nuevo apartado para los AEs:
1. El AE hace una foto a la tarjeta de visita del contacto.
2. La app detecta **nombre, empresa, teléfono y email**.
3. El AE rellena a mano:
   - **Country**
   - **Number of properties or rooms**
   - **Comentarios libres**
   (Etiquetas de los campos en inglés, tal cual.)
- [POR COMPROBAR] Dónde se guardan los leads (HubSpot, hoja, email…) y cómo se revisan los datos detectados antes de guardar.
- Fecha límite (Notion): 2026-10-22.
- KPI: fichas listas para el próximo evento.
