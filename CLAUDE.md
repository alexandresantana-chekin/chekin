# Growth · Chekin

Cliente de Alex: Chekin (software de check-in y cumplimiento legal para alojamientos).
Prueba de 3 meses (oct 2026 – 15/01/2027), 4 h al día, lunes a viernes (20 h semanales). Leer `1-proyectos/growth-chekin/estado.md` antes de empezar.
Tono: directo y breve, en español. Claude propone y Alex decide.

## Reglas duras
- No ejecutar sin OK y revisión de Alex: nada de escribir en Notion, Asana o HubSpot, publicar en la web, tocar campañas ni enviar mensajes.
- No inventar cifras ni datos. Lo que falte: `[POR COMPROBAR]`.
- Toda mejora se justifica contra el MRR o un KPI que lo mueva (conversión, activación).
- Paid: solo se cambian las landings de Google Ads. Meta usa su propia plantilla de formulario: no se toca.
- La conversión se mide por página, no por UTM (las UTM mezclan campañas).
- Ninguna clave ni token en el chat ni en el repo. Van solo en el terminal o en el gestor del servicio. No subir `.env`.
- Archivar, no borrar (`3-archivo/`). Borradores para copiar y pegar: en el chat o en Notion.
- **Al terminar una tarea:** comentar en esa tarea de Asana mencionando a Carlos Cedrés (@Carlos, gid Asana `1216414955096276`) con qué se ha hecho y dónde está el entregable. Regla de Alex (22/10).

## Dónde vive cada dato
| Qué | Dónde |
|---|---|
| Tablero de proyectos | Notion · "Proyectos GTM & Growth" |
| Tareas y fechas | Asana · proyectos "GTM: …" de Alex |
| Landings, formularios, A/B, contactos | HubSpot |
| Datos de Google Ads | Windsor.ai |
| Registro de tests de landing | Artifact "Tests de landing Chekin" |
| Web | WordPress |
| Funnel del onboarding (P1) | **PostHog**: llegada a la web → registro → pasos del onboarding → activación. [POR COMPROBAR con Daniel: si cubre web, registro y webapp, y quién añade eventos] |
| Horas dedicadas | `1-proyectos/growth-chekin/horas.md` |
| Código de la app QR (Chekin Connect) | `chekin-connect/` (tiene su propio `CLAUDE.md`; leerlo antes de tocar código) |

## Personas
- Carlos Cedrés: responsable de Alex en todos los proyectos.
- Daniel Clemares: producto; P1 Onboarding.

## Proyectos
- **P2 · Ficha QR para AEs en eventos.** Entrega el 22/10. Falta el último retoque.
- **P3 · Landings de paid (Google).** España e Italia listas como mínimo para el 27/10. Orden: ES hoteles → ES resto → IT hoteles → IT resto. Se trabaja en el chat "Landing Page".
- **P1 · Onboarding con producto.** Hasta el 15/01. Ciclos: analizar el funnel hasta la activación → proponer → ejecutar → medir a las X semanas. Herramienta de medición: PostHog (funnels, grabaciones de sesión y A/B). Frecuencia de reuniones: se decide con Daniel.
- **P4 · Web y CRO en WordPress.** El último, después de P3.
- **P5 · Animación del logo para la firma de Gmail.** GIF para Ventas y Partnerships; entrega a Carlos el 27/10. Archivos en `2-herramientas/firma-gmail/`.
- **Backlog · MRR automático del onboarding.** Para después.

## Flujo semanal (4 h/día)
- Lunes: planificación, repaso de Asana y Notion y prioridades de la semana.
- Martes a jueves: trabajo de proyecto (ahora P3 y P1).
- Reunión con Daniel: [frecuencia por definir].
- Viernes: revisión de tests en el tracker, actualización de Notion y Asana, estado para Carlos y total de horas de la semana.

## Control de horas
- Al empezar el día, Claude apunta la hora de inicio que diga Alex. Al cerrar, la de fin y en qué proyecto se ha ido el tiempo.
- Se registra en `horas.md`. Si el día pasa de 4 h o la semana de 20 h, Claude lo avisa.

## Al cerrar sesión
Actualizar `estado.md`, `decisiones.md` (solo crece) y `horas.md`, y subir a `main`.

## Contradicciones abiertas
- En Notion, P3 figura como "Por empezar", pero en realidad está en curso.
