#!/bin/bash
# Guarda en el Llavero de macOS el token de acceso de Supabase que usa la rutina de eventos terminados.
# El token se pega sin mostrarse y no pasa por archivos, historial ni chat. Se puede repetir para cambiarlo.
set -euo pipefail
printf 'Pega el token de Supabase (Cmd+V) y pulsa Enter: '; read -rs T; echo
T=$(printf '%s' "$T" | tr -d '[:space:]')
case "$T" in sbp_*) ;; *) echo "Eso no es un token de Supabase (empieza por sbp_). No se ha guardado."; exit 1 ;; esac
security delete-generic-password -s chekin-connect-rutina -a supabase >/dev/null 2>&1 || true
security add-generic-password -s chekin-connect-rutina -a supabase -l "Chekin Connect · rutina de eventos" -w "$T"
unset T
echo "Guardado en el Llavero (Chekin Connect · rutina de eventos)."
