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

## Demos pedidas y resumen (23/10, OK de Alex a los pasos 2 y 3)
- Descuadre explicado: Actividad → "Demos" eran **clics** anónimos en «Agendar demo»; la tabla de Leads → "Demos" eran contactos que **entraron** por «Agendar demo»; las reservas reales en Calendly no se registran. La tabla de Leads además descartaba los contactos sin evento.
- Hecho en el código (sin desplegar): migración `supabase/migrations/20261026_demo_requests.sql` (fechas de demo en el contacto + `mark_demo_request`), la tarjeta apunta la demo de quien ya dejó datos, tabla "Demos pedidas" (persona, email, teléfono, AE, evento, alta, pidió demo, veces) en Actividad y en Contactos del equipo, CSV con "Pidió demo" y "Veces demo", fila "Sin evento" en Leads y textos claros ("Clics en «Agendar demo»" / "Demos pedidas"). Probado con datos de ejemplo en el navegador (captura `p2-demos-pedidas-prueba.jpg`); sin Node no se han pasado las pruebas de Playwright.
- Pendiente: aplicar las migraciones 20261025 y 20261026 en Supabase, subir a `main` (despliega la versión de prueba de Vercel) y saber si reservó en Calendly (depende del plan de Calendly [POR COMPROBAR]).

## HubSpot (paso 1): qué falta
- En HubSpot `number_of_units` ya existe. Faltan las propiedades de contacto `chekin_connect_evento` (texto) y `chekin_connect_origen` (texto o desplegable).
- App privada "Chekin Connect" con permisos de contactos (lectura y escritura) y de propietarios (lectura); el token va solo a Supabase → Edge Functions → Secrets → `HUBSPOT_TOKEN`.
- Desplegar la función `hubspot-sync` y crear el Database Webhook (INSERT en `public.leads` → `hubspot-sync`).
