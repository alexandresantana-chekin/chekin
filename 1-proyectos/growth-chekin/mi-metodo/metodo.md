# Método de trabajo de Growth

Cómo se trabaja cualquier proyecto de producto o web (onboarding, landings, web). Lo de cada proyecto vive en su carpeta; esto es común.

## Casa o proyecto
- **Casa:** todo lo que sirve a más de un proyecto o seguiría siendo útil aunque el proyecto terminara.
  - Roles: `.claude/agents/`.
  - Este método y las personas: `mi-metodo/`.
  - Marca y glosario: `2-herramientas/marca/`.
- **Proyecto:** lo que solo tiene sentido ahí.
  - Bitácora, KPIs, fichas de cambio, revisiones y dirección visual.
  - Ejemplo: `trabajo-en-curso/p1-onboarding/`.

## Roles
| Rol | Agente | Entra en |
|---|---|---|
| Dueño del producto (Alex) | — | 1 y 6: pide, prioriza y decide |
| Analista de datos | `analista-datos` | 1 y 7 |
| Investigador de usuarios | `investigador-usuarios` | 4 y 7 |
| Diseñador UX/UI | `disenador-ux` | 3 |
| Redactor | `redactor` | 3 |
| Legal y cumplimiento | `legal-cumplimiento` | 2 y 4 |
| Ventas y atención al cliente | `ventas-cs` | 2 y 4 |
| QA | `qa` | 5 |
| Auditor independiente | `auditor` | cada 3 o 4 versiones |

## El ciclo de cada cambio
1. **Entrada:** petición de Alex o Daniel, o un dato (el analista lo apunta en `hallazgos.md`).
2. **Ficha del cambio:** qué, por qué, KPI que mueve, hipótesis y pantallas. Legal y Ventas dicen qué falta y qué riesgos hay.
3. **Diseño y textos:** el diseñador y el redactor, en el generador, con la marca.
4. **Revisión:** las 3 personas, más legal y ventas. Si algo bloquea, vuelve al paso 3.
5. **QA:** todos los caminos en el navegador.
6. **OK de Alex:** se publica, se apunta en la bitácora y se sube a `main`. Nada se publica sin OK.
7. **Validación real:** cada pocas versiones, un test con 5 usuarios (al menos uno de cada persona) y el auditor. En producto, A/B y PostHog; las decisiones con Daniel van a `decisiones.md`.

## Reglas que no cambian
- Sin cifras inventadas: `[POR COMPROBAR]`. Toda cifra lleva fuente y periodo.
- Todo se justifica contra el MRR o un KPI que lo mueva.
- Nada en HubSpot, Notion, Asana, la web o campañas sin el OK de Alex.
