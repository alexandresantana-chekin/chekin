# P1 · Onboarding con producto

Ciclos: analizar el funnel hasta la activación → proponer → ejecutar → medir. Responsable de producto: Daniel Clemares.

- Dashboard (privado, en vivo): [Funnel de activación Chekin](https://claude.ai/artifact/Mmx3qnEnaFtUbAmUihNsaP). Recorrido del cliente con filtros, onboarding por variante, control frente a variante y cruce con GA4.
- Herramienta: PostHog (proyecto "Default project", id 125487). El onboarding de anfitriones se registra en `dashboard.chekin.com`; `dashboard-ng.chekintest.xyz` es pruebas.
- Activación (Alex, 22/10): **primera vivienda registrada** y **primera reserva creada**. En PostHog no hay eventos de esos dos pasos. En la base sincronizada de Postgres sí (`postgres.housings.created_at`, `postgres.person_users.has_first_reservation_created`), pero la sincronización falla desde hace un mes: no sirve para octubre.

## Primer funnel (22-10-2026, datos del 13 al 22/10)
Los eventos del onboarding empiezan el 13–14/10: solo hay 9 días de datos. Ventana de conversión: 14 días.

| Paso | Evento | Personas | % del registro |
|---|---|---|---|
| Registro | `auth_registration_succeeded` | 32 | 100% |
| Bienvenida | `onboarding_welcome_continued` | 29 | 91% |
| Paso de configuración | `onboarding_setup_step_continued` | 22 | 69% |
| PMS conectado | `pms_connect_succeeded` | 11 | 34% |
| Configuración completada | `onboarding_setup_completed` | 10 | 31% |

- La mayor caída es la conexión del PMS: de 22 que llegan, 11 lo conectan.
- 12 de los 32 tuvieron algún fallo de conexión (`pms_connect_failed`); 4 fallaron y nunca lo lograron. 3 eligieron "otro PMS".
- `pms_connect_failed` no lleva el proveedor (`pms_provider` vacío): no se sabe qué PMS falla.
- `auth_started` y `signup_code_sent` son de la app de huéspedes (`guest.chekin.com`), no del alta de anfitriones.

## Funnel por variante (22-10-2026, del 13 al 22/10)
La entrada real es la página `/register`, no el registro. `onboarding_variant_assigned` salta sobre todo en `/login` (usuarios que ya existen), así que solo se cuenta cuando ocurre en `/register`.

| Variante | Entra en /register | Registro | Paso de configuración | PMS conectado | Configuración completada |
|---|---|---|---|---|---|
| legacy | 166 | 0 | 0 | 0 | 0 |
| rebuilt | 56 | 13 (23%) | 4 (7%) | 0 | 0 |
| beta | 22 | 17 (77%) | 16 (73%) | 11 (50%) | 10 (45%) |

- legacy: 0 registros seguramente porque ese flujo no envía los eventos nuevos, no porque nadie se registre [POR COMPROBAR con Daniel].
- rebuilt: se registra 1 de cada 4 y nadie conecta el PMS.
- beta: convierte mucho mejor, pero son 22 personas y pueden ser pruebas internas [POR COMPROBAR].

Preguntas añadidas para Daniel:
- ¿El flujo legacy envía `auth_registration_succeeded`? ¿Qué porcentaje de tráfico va a cada variante?
- ¿Se pueden enviar eventos de "vivienda creada" y "reserva creada" a PostHog, o arreglar la sincronización de Postgres?

## Cruce PostHog vs Google Analytics: entradas en /register (22-10-2026)
Personas únicas por día en `dashboard.chekin.com/register`. GA4 vía Windsor: hay dos propiedades que miden el dashboard.

| Día | PostHog | GA4 "CheKin web (.com)" | GA4 "Chekin.com" |
|---|---|---|---|
| 13/10 | 2 | 1 | 1 |
| 14/10 | 0 | 1 | 1 |
| 15/10 | 4 | 2 | 2 |
| 16/10 | 2 | 2 | 2 |
| 19/10 | 59 | 19 | 8 |
| 20/10 | 62 | 31 | 12 |
| 21/10 | 83 | 54 | 34 |
| 22/10 (parcial) | 28 | 9 | 8 |

- La forma coincide: mismos días con tráfico, el fin de semana a 0 y el salto desde el 19/10. Las cifras no: PostHog cuenta unas 2 veces más que la mejor de GA4.
- PostHog: 237 personas, 248 sesiones, 0 bots detectados, 36 países. No hay señales de duplicados ni de bots.
- Explicación probable: GA4 solo cuenta a quien acepta cookies (y los bloqueadores lo frenan); PostHog parece contar sin consentimiento [POR COMPROBAR la configuración de consentimiento de cada uno].
- Conclusión: las entradas de PostHog no parecen contaminadas, pero no se puede validar "cifra contra cifra" con GA4. Para P1 sirve PostHog; GA4 no.
- Hay dos propiedades de GA4 midiendo el mismo dashboard con cifras distintas [POR COMPROBAR cuál es la buena].
- Grabaciones de sesión: desactivadas en el proyecto de PostHog (`session_recording_opt_in: false`). Activarlas es un cambio de configuración: decisión de Daniel, con enmascarado de datos de huéspedes.

## Sincronización de Postgres en PostHog (22-10-2026)
- Última sincronización buena: `person_users` 04/09/2026, `housings` 04/09/2026. Estado: Failed.
- Error: PostHog no resuelve el servidor de la base de datos, o resuelve a una dirección privada. Lo más probable es que la base de datos cambiara de dirección o dejara de ser accesible desde fuera [POR COMPROBAR con ingeniería].
- Arreglarlo necesita la dirección nueva, credenciales y permitir el acceso de PostHog a la base. Es trabajo de ingeniería; nosotros no lo tocamos.

## Activación con datos de Postgres (altas del 07/06 al 03/09/2026, estado a 04/09)
Excluye usuarios de prueba y staff. Vivienda = la cuenta tiene una vivienda creada desde el 01/06. Los indicadores son el estado a 04/09: las altas de finales de agosto tuvieron menos tiempo.

| Segmento | Altas | Con vivienda | Con primera reserva | Con primer huésped |
|---|---|---|---|---|
| Alquiler vacacional (HOU) | 5.940 | 3.042 (51%) | 2.334 (39%) | 1.481 (25%) |
| Hoteles (HOT) | 1.058 | 662 (63%) | 459 (43%) | 329 (31%) |

Por origen (HOU + HOT):

| Origen | Altas | Con vivienda | Con primera reserva | `has_paid` |
|---|---|---|---|---|
| DASHBOARD (alta propia) | 2.532 | 1.369 (54%) | 1.041 (41%) | 831 (33%) |
| HOLIDU | 2.433 | 579 (24%) | 273 (11%) | 2.433 |
| LODGIFY | 541 | 526 (97%) | 478 (88%) | 541 |
| AMENITIZ | 350 | 346 (99%) | 310 (89%) | 341 |

- El onboarding que nos toca es el de origen DASHBOARD: casi la mitad de las altas propias no registra ninguna vivienda.
- Las altas por integración de PMS (Lodgify, Amenitiz…) traen la vivienda y las reservas solas. Holidu es la excepción: el 76% no tiene vivienda.
- `has_paid` en canales de partner sale siempre a true: no significa pago real del cliente [POR COMPROBAR].

### Funnel encadenado (cada paso exige el anterior; vivienda creada después del alta)
% total / % del paso anterior. Altas del 07/06 al 03/09/2026, estado a 04/09.

| Segmento | 1. Alta | 2. Vivienda | 3. Reserva | 4. Huésped |
|---|---|---|---|---|
| Alta propia · alquiler vacacional | 2.116 | 1.232 · 58,2% / 58,2% | 953 · 45,0% / 77,4% | 700 · 33,1% / 73,5% |
| Alta propia · hoteles | 416 | 137 · 32,9% / 32,9% | 88 · 21,2% / 64,2% | 65 · 15,6% / 73,9% |
| Integración · alquiler vacacional | 3.824 | 1.810 · 47,3% / 47,3% | 1.381 · 36,1% / 76,3% | 781 · 20,4% / 56,6% |
| Integración · hoteles | 642 | 525 · 81,8% / 81,8% | 371 · 57,8% / 70,7% | 264 · 41,1% / 71,2% |

- La reserva y el huésped son indicadores sin fecha: se exige que existan, no que vinieran después de la vivienda.
- Hallazgo: en hoteles con alta propia solo 1 de cada 3 registra una vivienda.

## Preguntas para Daniel
- ¿Qué cuenta como activación (primer check-in enviado, primera reserva sincronizada…)? ¿Se registra?
- ¿Se puede añadir el proveedor y el motivo del error a `pms_connect_failed`?
- ¿Qué es `onboarding_variant_assigned` (1.744 personas)? ¿Hay un test de variantes en marcha?
- ¿Se pueden activar las grabaciones de sesión solo en `/register` y el onboarding, con los datos enmascarados?
- ¿Quién puede arreglar la sincronización de Postgres en PostHog (parada desde el 04/09)?
