---
name: onboarding
description: Rutina diaria del onboarding de Chekin (P1). Úsala cuando Alex diga «arrancamos onboarding», escriba /onboarding, pegue «Ajustes del laboratorio (onboarding)» o pida un cambio en el onboarding o su prototipo.
---

# Trabajar en el onboarding (P1)

Método común: `1-proyectos/growth-chekin/mi-metodo/metodo.md`. Carpeta del proyecto: `1-proyectos/growth-chekin/trabajo-en-curso/p1-onboarding/`. Claude propone y Alex decide; nada se publica sin su OK.

## 1 · Arranque del día
1. Leer `p1-onboarding/README.md`, las 3 últimas entradas de `bitacora.md`, `kpis.md`, `direccion-visual.md` y lo marcado `[POR COMPROBAR]`.
2. Contar a Alex en pocas líneas dónde lo dejamos, qué está pendiente y una propuesta para hoy (máximo 3 cambios, cada uno con su KPI).
3. Esperar a que Alex elija.

## 2 · Cada cambio (ciclo del método)
1. **Ficha** en `cambios/AAAA-MM-DD-nombre.md` con la plantilla. Lanzar en paralelo `legal-cumplimiento` y `ventas-cs` si el cambio toca datos, legal o ayuda.
2. **Diseño y textos**, con los criterios de `disenador-ux` y `redactor`. Se edita solo el código fuente, nunca el HTML compilado:
   - pantallas: `2-herramientas/onboarding-prototipo/generador.py`;
   - comportamiento y laboratorio: `plantillas/tpl_movil.html`, `plantillas/tpl_portatil.html` y `plantillas/lab.part`;
   - explicaciones de cada pantalla: lista `TIPS` de `plantillas/explicaciones.py`.
3. **Compilar** desde `2-herramientas/onboarding-prototipo/`:
   ```
   python3 plantillas/explicaciones.py
   python3 generador.py
   python3 plantillas/build.py fuentes . logos/chekin-logo.svg logos/chekin-logo-white.svg
   ```
   Comprobar el JavaScript de `onboarding-movil.html`, `onboarding-portatil.html` y `onboarding.html` con `node --check`.
4. **Revisión:** lanzar en paralelo `investigador-usuarios` (Lucía, Javier y Carmen), `legal-cumplimiento` y `ventas-cs`. Guardar lo que digan en `revisiones/vNN-AAAA-MM-DD.md`. Si algo bloquea, volver al paso 2.
5. **QA:** lanzar `qa`, o recorrerlo tú en el navegador, sirviendo la carpeta (`python3 -m http.server 8777`, en segundo plano) y abriendo `http://127.0.0.1:8777/onboarding.html`.
6. **OK de Alex.** Con su OK, publicar en el enlace único:
   - Artifact `publish` con `file_path` `…/onboarding-prototipo/onboarding.html` y `url` https://claude.ai/artifact/DfLw9HeJKddbpxHYRC6mLP;
   - `files`: `movil.html` y `portatil.html`, con rutas absolutas.
7. **Apuntar:**
   - entrada en `bitacora.md` (fecha, versión, qué cambia y por decisión de quién);
   - la ficha cerrada;
   - si hay datos nuevos, `hallazgos.md`;
   - commit y push a `main`.

## Ajustes del laboratorio
Cuando Alex pegue «Ajustes del laboratorio (onboarding): {…}»:
1. Apuntarlos en `direccion-visual.md`, sección «Ajustes elegidos», con la fecha.
2. Pasarlos al generador y a las plantillas como valores de verdad (letra, color, fondo, columna, esquinas, sombras, movimiento, mensajes). Cuando sean definitivos, también a `2-herramientas/marca/README.md`.
3. Seguir el ciclo desde el paso 3.

## Cada 3 o 4 versiones
- `auditor`: revisión independiente, comparada con la auditoría anterior.
- Proponer a Alex un test con 5 usuarios reales (guion del `investigador-usuarios`).

## Cierre del día
Hora de fin y proyecto en `horas.md`. `estado.md` y `decisiones.md` al día. Subir a `main`.
