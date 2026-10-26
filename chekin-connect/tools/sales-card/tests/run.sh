#!/usr/bin/env bash
# Pruebas de navegador (Playwright) con un servidor Supabase simulado: no tocan la base real.
# Uso, desde la raíz del repositorio:   bash tools/sales-card/tests/run.sh [prueba ...]
#   (sin argumentos las ejecuta todas)
# Requisitos: Node 18+, y un Chromium. Variables opcionales: CHROMIUM=/ruta/a/chrome  SHOTS=./capturas
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/../../.." && pwd)"
APP="$ROOT/sales-card"; SHOTS="${SHOTS:-$ROOT/tools/sales-card/tests/capturas}"; mkdir -p "$SHOTS"
if [ -z "$CHROMIUM" ]; then CHROMIUM="$(node -e "try{console.log(require('playwright-core').chromium.executablePath())}catch(e){}" 2>/dev/null || true)"; fi
[ -d "$HERE/node_modules" ] || (cd "$HERE" && npm install --silent)
TMP="$HERE/.run"; mkdir -p "$TMP"; cp "$HERE/package.json" "$TMP/" ; ln -sfn "$HERE/node_modules" "$TMP/node_modules"
LIST="${@:-sb ev3 team5 days2 web3 back1 center lang6 deck6 deck2 save1}"
for t in $LIST; do
  sed -e "s#__APP__#$APP#g" -e "s#__CHROMIUM__#$CHROMIUM#g" -e "s#__SHOTS__#$SHOTS#g" "$HERE/$t.js" > "$TMP/$t.js"
  printf "%-8s " "$t"; (cd "$TMP" && node "$t.js" 2>&1 | tail -1)
done
