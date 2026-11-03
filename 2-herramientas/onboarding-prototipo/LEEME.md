# Prototipo del onboarding (P1)

Código fuente del prototipo. Se compila y se publica desde aquí: no hace falta ninguna carpeta temporal.

- `generador.py`: crea las pantallas en `fuentes/` (base de la columna del menú en `fuentes/_base/`).
- `plantillas/`:
  - `tpl_movil.html` y `tpl_portatil.html`: marco, navegación y comportamiento;
  - `lab.part`: el laboratorio de estilo;
  - `explicaciones.py`: los textos de «Por qué lo hacemos así»;
  - `build.py`: lo compila todo.
- Compilar:
  ```
  python3 plantillas/explicaciones.py
  python3 generador.py
  python3 plantillas/build.py fuentes . logos/chekin-logo.svg logos/chekin-logo-white.svg
  ```
- Salida:
  - `onboarding-movil.html` y `onboarding-portatil.html` (cada prototipo suelto);
  - `movil.html` y `portatil.html` (las mismas, como documento completo);
  - `onboarding.html` (la página única con pestañas que las carga).
- Enlace único: https://claude.ai/artifact/DfLw9HeJKddbpxHYRC6mLP (pestañas «Móvil y portátil», «Móvil» y «Portátil»). El enlace antiguo del móvil (CjcH5gMdon5qBKatXSLopN) queda en la versión 31 y ya no se actualiza.
- Rutina diaria: comando `/onboarding` (`.claude/skills/onboarding/SKILL.md`).
