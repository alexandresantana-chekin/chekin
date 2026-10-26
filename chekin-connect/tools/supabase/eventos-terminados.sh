#!/bin/bash
# Eventos y webinars de Chekin Connect que ya han terminado y aún no se han pasado a Asana, con sus leads en cifras.
# Lo usa la rutina «chekin-connect-eventos-terminados» (L–V 9:00). Solo lee: no cambia nada en Supabase.
#   bash eventos-terminados.sh               → JSON con los eventos pendientes de pasar a Asana
#   bash eventos-terminados.sh --marcar ID   → apunta ese evento como ya pasado a Asana
# Clave: token de acceso de Supabase en el Llavero de macOS (servicio chekin-connect-rutina, cuenta supabase).
# Se guarda una vez con guardar-clave-rutina.sh. Nunca en archivos ni en el chat.
set -euo pipefail
REF=lxjefebmndcbnoxlyykw
ESTADO="$(cd "$(dirname "$0")/../../.." && pwd)/1-proyectos/growth-chekin/agentes-rutinarios/eventos-reportados.txt"
touch "$ESTADO"

if [ "${1:-}" = "--marcar" ]; then
  [ -n "${2:-}" ] || { echo "Falta el id del evento" >&2; exit 1; }
  grep -qxF "$2" "$ESTADO" || echo "$2" >> "$ESTADO"
  echo "Marcado: $2"; exit 0
fi

TOKEN=$(security find-generic-password -s chekin-connect-rutina -a supabase -w 2>/dev/null) ||
  { echo '{"error":"No hay clave en el Llavero. Ejecuta tools/supabase/guardar-clave-rutina.sh"}'; exit 2; }

# Eventos terminados en los últimos 30 días (hora de Madrid) y, por cada AE, sus leads en cifras.
SQL=$(cat <<'EOF'
with hoy as (select (now() at time zone 'Europe/Madrid')::date as d),
ev as (
  select e.id, e.name, e.kind, e.city, e.date_from, e.date_to
  from public.events e, hoy
  where e.date_to is not null and e.date_to < hoy.d and e.date_to >= hoy.d - 30
)
select coalesce(json_agg(json_build_object(
  'id', ev.id, 'nombre', ev.name, 'tipo', ev.kind, 'ciudad', ev.city,
  'desde', ev.date_from, 'hasta', ev.date_to,
  'leads', (select count(*) from public.leads l where l.event_name = ev.name),
  'por_ae', (select coalesce(json_agg(a order by a.leads desc), '[]'::json) from (
      select p.name as ae, l.ae_slug as slug, count(*) as leads,
             count(*) filter (where l.demo_first_at is not null) as demos,
             count(*) filter (where l.channel = 'scan') as escaneadas,
             count(*) filter (where coalesce(l.hubspot_contact_id, '') <> '') as en_hubspot,
             count(*) filter (where coalesce(l.hubspot_error, '') <> '') as error_hubspot
      from public.leads l left join public.profiles p on p.id = l.ae_id
      where l.event_name = ev.name group by p.name, l.ae_slug) a)
) order by ev.date_to), '[]'::json) as eventos
from ev;
EOF
)

RES=$(python3 -I -c 'import json,sys;print(json.dumps({"query":sys.stdin.read()}))' <<<"$SQL" |
  curl -sS -f -X POST "https://api.supabase.com/v1/projects/$REF/database/query" \
    -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" --data-binary @-)
unset TOKEN

# Quita los eventos ya pasados a Asana.
python3 -I - "$ESTADO" "$RES" <<'EOF'
import json, sys
hechos = {l.strip() for l in open(sys.argv[1]) if l.strip()}
filas = json.loads(sys.argv[2])
eventos = (filas[0]["eventos"] if filas else []) or []
print(json.dumps([e for e in eventos if e["id"] not in hechos], ensure_ascii=False, indent=1))
EOF
