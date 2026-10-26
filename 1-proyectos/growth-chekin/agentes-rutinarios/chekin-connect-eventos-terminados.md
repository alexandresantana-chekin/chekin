# Rutina · Chekin Connect: eventos terminados → Asana

Creada el 26/10/2026 a petición de Alex. Sirve para controlar los leads captados en cada evento o webinar.

- **Cuándo:** de lunes a viernes a las 9:00 (tarea programada `chekin-connect-eventos-terminados`, en la app de Claude → Scheduled). Solo corre si la app está abierta; si no, al abrirla. Guardada en modo Auto.
- **Qué hace:**
  1. Lee de Supabase los eventos y webinars terminados en los últimos 30 días que aún no están en Asana, con sus leads en cifras: total, demos pedidas, tarjetas escaneadas, enviados a HubSpot y errores, por AE.
  2. Crea en Asana, en Growth Daily › Alexandre, una tarea por evento asignada a Alex («Evento X · Ciudad: N leads»), con una subtarea por AE («Seguimiento de N leads · AE», a 3 días laborables).
  3. Apunta el evento en `eventos-reportados.txt` para no repetirlo, y avisa a Alex con los enlaces.
- **Datos:** en Asana solo van cifras. El detalle de cada lead está en el panel (Actividad → Exportar contactos) y en HubSpot.
- **Script:** `chekin-connect/tools/supabase/eventos-terminados.sh`. Solo lee; con `--marcar ID` apunta un evento como hecho.
- **Clave:** token de acceso de Supabase en el Llavero de macOS (servicio `chekin-connect-rutina`). Se guarda con `bash chekin-connect/tools/supabase/guardar-clave-rutina.sh`. Nunca en el repositorio ni en el chat.
- **Primera ejecución:** pasará a Asana todos los eventos terminados en los últimos 30 días. Para saltarse alguno, márcalo antes con `--marcar`.
