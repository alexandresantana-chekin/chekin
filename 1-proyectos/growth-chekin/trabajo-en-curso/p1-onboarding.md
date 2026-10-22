# P1 · Onboarding con producto

Ciclos: analizar el funnel hasta la activación → proponer → ejecutar → medir. Responsable de producto: Daniel Clemares.

- Herramienta: PostHog (proyecto "Default project", id 125487). El onboarding de anfitriones se registra en `dashboard.chekin.com`; `dashboard-ng.chekintest.xyz` es pruebas.
- Activación: [POR COMPROBAR con Daniel]. No hay evento de "primer check-in" del anfitrión en PostHog; el último paso medido es `onboarding_setup_completed`.

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

## Preguntas para Daniel
- ¿Qué cuenta como activación (primer check-in enviado, primera reserva sincronizada…)? ¿Se registra?
- ¿Se puede añadir el proveedor y el motivo del error a `pms_connect_failed`?
- ¿Qué es `onboarding_variant_assigned` (1.744 personas)? ¿Hay un test de variantes en marcha?
