#!/bin/bash
# Despliega el envío de contactos a HubSpot en Supabase (proyecto lxjefebmndcbnoxlyykw):
#   1) función hubspot-sync (sin verificación de JWT: la protege la clave interna)
#   2) clave interna nueva → secreto WEBHOOK_SECRET de la función
#   3) la misma clave en Vault ('hubspot_webhook_secret') + migración 20261027 (disparador leads_to_hubspot)
#   4) comprobación
# Requisito: SUPABASE_ACCESS_TOKEN en el entorno (pegado con read -s; nunca en archivos ni en el chat).
# El token de HubSpot lo pide también sin mostrarlo (Enter para dejar el que ya hay).
set -euo pipefail
REF=lxjefebmndcbnoxlyykw
cd "$(dirname "$0")/../.."
export PATH="$HOME/.local/node/bin:$PATH"
for i in 1 2 3; do   # pide el token sin mostrarlo, quita espacios y comprueba el formato
  if [ -z "${SUPABASE_ACCESS_TOKEN:-}" ]; then printf 'Pega el token de Supabase (Cmd+V) y pulsa Enter: '; read -rs SUPABASE_ACCESS_TOKEN; echo; fi
  SUPABASE_ACCESS_TOKEN=$(printf '%s' "$SUPABASE_ACCESS_TOKEN" | tr -d '[:space:]')
  case "$SUPABASE_ACCESS_TOKEN" in
    sbp_*) [ ${#SUPABASE_ACCESS_TOKEN} -ge 40 ] && break ;;
  esac
  echo "Eso no es un token de Supabase (debe empezar por sbp_ y tener unos 44 caracteres). Copia el token otra vez en Safari y repite."
  SUPABASE_ACCESS_TOKEN=""
done
[ -n "$SUPABASE_ACCESS_TOKEN" ] || exit 1
export SUPABASE_ACCESS_TOKEN

q() {   # ejecuta SQL (por la entrada estándar) con la API de gestión de Supabase
  node -e 'process.stdout.write(JSON.stringify({query:require("fs").readFileSync(0,"utf8")}))' |
    curl -sS -f -X POST "https://api.supabase.com/v1/projects/$REF/database/query" \
      -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" -H "Content-Type: application/json" --data-binary @-
}

echo "1/4 Desplegando la función hubspot-sync..."
npx --yes supabase@latest functions deploy hubspot-sync --project-ref "$REF" --no-verify-jwt --use-api

echo "2/4 Creando la clave interna (no se muestra)..."
WS=$(openssl rand -hex 32)
npx --yes supabase@latest secrets set "WEBHOOK_SECRET=$WS" --project-ref "$REF" >/dev/null

echo "3/4 Guardando la clave en Vault y creando el disparador..."
printf "select vault.create_secret('%s', 'hubspot_webhook_secret', 'Clave del disparador leads_to_hubspot') where not exists (select 1 from vault.secrets where name = 'hubspot_webhook_secret');\nselect vault.update_secret(id, '%s') from vault.secrets where name = 'hubspot_webhook_secret';\n" "$WS" "$WS" | q >/dev/null
unset WS
q < supabase/migrations/20261027_hubspot_webhook.sql >/dev/null

echo "Token de HubSpot (app privada «Chekin Connect» → Auth). Pulsa solo Enter para dejar el que ya hay."
printf 'Pega el token de HubSpot (Cmd+V) y pulsa Enter: '; read -rs HS; echo
HS=$(printf '%s' "$HS" | tr -d '[:space:]')
if [ -n "$HS" ]; then
  case "$HS" in pat-*) ;; *) echo "Eso no parece un token de HubSpot (empieza por pat-). No se ha guardado."; HS="" ;; esac
fi
if [ -n "$HS" ]; then   # por archivo temporal privado, para que el token no salga en la lista de procesos
  TMP=$(mktemp); chmod 600 "$TMP"; printf 'HUBSPOT_TOKEN=%s\n' "$HS" > "$TMP"
  npx --yes supabase@latest secrets set --env-file "$TMP" --project-ref "$REF" >/dev/null
  rm -f "$TMP"; echo "HUBSPOT_TOKEN guardado."
fi
unset HS

echo "4/4 Comprobación:"
echo "select (select count(*) from pg_trigger where tgname = 'leads_to_hubspot') as disparador, (select count(*) from vault.secrets where name = 'hubspot_webhook_secret') as clave_en_vault;" | q
echo
npx --yes supabase@latest secrets list --project-ref "$REF" 2>/dev/null | grep -E "NAME|WEBHOOK_SECRET|HUBSPOT_TOKEN" || true
echo "Listo. Si arriba sale HUBSPOT_TOKEN, ya se puede probar con un contacto PRUEBA."
