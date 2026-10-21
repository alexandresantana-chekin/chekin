#!/usr/bin/env python3
"""Compila sales-card/index.html a partir de app-template.html.
Uso (desde la raíz del repositorio):  python3 tools/sales-card/build.py
Sustituye los marcadores __QRLIB__, __ICON__, __LOGO__ y __LOGOW__ por la librería de QR, el icono y los logos oficiales."""
import base64, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
A = HERE / "assets"
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
h = (HERE / "app-template.html").read_text(encoding="utf-8")
h = (h.replace("__QRLIB__", (A / "qrcode-lib.js").read_text(encoding="utf-8"))
      .replace("__ICON__", "data:image/png;base64," + b64(A / "icon-mark.png"))
      .replace("__LOGO__", "data:image/svg+xml;base64," + b64(A / "logo-tight.svg"))
      .replace("__LOGOW__", "data:image/svg+xml;base64," + b64(A / "logo-white.svg")))
out = ROOT / "sales-card" / "index.html"
out.write_text(h, encoding="utf-8")
print("OK", out, len(h), "bytes")
