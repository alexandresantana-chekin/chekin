# P1 · Onboarding con producto

Ciclos: analizar el funnel hasta la activación → proponer → ejecutar → medir. Responsable de producto: Daniel Clemares.

- Dashboard (privado, en vivo): [Onboarding Chekin: del alta a la activación](https://claude.ai/artifact/Mmx3qnEnaFtUbAmUihNsaP). Recorrido del cliente con filtros, onboarding por variante, control frente a variante y cruce con GA4.
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

## Medición del funnel (23-10-2026, para el lunes 26 con Daniel)
Tres secciones nuevas en el dashboard, bajo "Medición del funnel":
- **Qué datos hay y de qué fechas:** línea de tiempo por fuente y paso. Base de la app: del 01/01 al 03/09 (altas) y al 04/09 (viviendas). PostHog: todo desde el 13/10, también las páginas vistas. Hueco sin datos del 04/09 al 12/10 (H-10).
- **Altas propias mes a mes, con las dos fuentes:** de enero a septiembre, alta → vivienda → reserva → huésped; octubre, registro → bienvenida → configuración → PMS → completada; fila roja para el hueco. Octubre cuenta alta con email + alta con Google (61 del 13 al 23/10); aparte, 96 personas pasan por el alta antigua sin evento (H-12, corrige el 16% de H-11).
- **Cómo medir bien a partir de ahora:** 9 pasos por orden (sincronización, registro en todos los flujos, eventos de vivienda/reserva/huésped, identify con id de cuenta, variante una sola vez, motivo del fallo del PMS, separar pruebas internas, grabaciones, funnel oficial en PostHog).

## En PostHog (creado el 23-10-2026, OK de Alex)
- Acción **"Alta nueva en el dashboard (email o Google)"** (id 172704): `auth_registration_succeeded` o `auth_social_succeeded` con `created = true`, en dashboard.chekin.com. https://eu.posthog.com/project/125487/data-management/actions/172704
- Insight **"Funnel de onboarding: alta nueva → configuración completada"** (TyO9mkZy), desde el 13/10, en orden, ventana de 14 días. https://eu.posthog.com/project/125487/insights/TyO9mkZy
- Validado contra el SQL del dashboard (13–23/10): mismas personas por paso (alta 61–62, bienvenida 46, configuración 33, PMS 13, completada 12).
- No incluye el alta antigua (`/register/accommodation-type`) ni vivienda/reserva/huésped: no hay eventos.

## Qué hace el cliente: no se ve (23-10-2026, H-13)
- En `/register*` y `/setup*` de dashboard.chekin.com **no hay ningún clic** (`$autocapture`), ni clics de rabia, clics muertos, salidas de página ni errores desde el 13/10. **No hay grabaciones** (`session_recording_opt_in: false`).
- Sabemos dónde se cae la gente, no por qué.
- Propuesta para Daniel (no activar sin su OK ni el del DPO): grabaciones solo en esas URL, todo enmascarado y solo con consentimiento de cookies; autocapture, clics de rabia y errores en esas páginas. Enmascarar no quita la necesidad de consentimiento (LSSI/AEPD) [POR COMPROBAR con el DPO]; PostHog parece medir sin pasar por el banner.

## Preguntas para Daniel
- ¿Qué cuenta como activación (primer check-in enviado, primera reserva sincronizada…)? ¿Se registra?
- ¿Se puede añadir el proveedor y el motivo del error a `pms_connect_failed`?
- ¿Qué es `onboarding_variant_assigned` (1.744 personas)? ¿Hay un test de variantes en marcha?
- ¿Se pueden activar las grabaciones de sesión solo en `/register` y el onboarding, con los datos enmascarados?
- (27/10, idea de Alex, a futuro) Mapas de calor y clics muertos o de rabia en el alta y el onboarding: ¿**Clarity** (ya está en las landings, H-14) o lo mismo en **PostHog** (tiene mapas de calor, clics muertos y de rabia, y lo une al funnel)? En los dos casos: banner de consentimiento en el dashboard, OK del DPO e instalación por producto.
- ¿Quién puede arreglar la sincronización de Postgres en PostHog (parada desde el 04/09)?

## Dashboard: arreglos y calculadora (27-10-2026)
- Cada fuente de PostHog fija primero el proyecto "Default project" (125487); el conector de claude.ai abría el proyecto vacío 143407 (H-25).
- La base de la app solo de enero a agosto de 2026 (decisión del 26/10). Stripe, hasta hoy.
- Nueva sección **"Calculadora de oportunidad por paso"**, adaptada de la calculadora de GMC: Alta » Vivienda » Reserva » Huésped » Pagan, con Todos / Alquiler vacacional / Hoteles por bloques. Ingresos = clientes de pago al final del camino × valor por cliente del dashboard (ARR a 12 meses, LTV o a mano; antes ARPA × 12, cambiado el 27/10 para descontar bajas); oportunidad = valor medio × personas del paso × % que no pasa. Sigue los filtros de origen y meses. Sin corregir los errores de fórmula de la plantilla original.
- Cambios visuales (27/10): dinero en €; "El camino del cliente" sin las caídas de pérdida (ahora en la calculadora), con un color y una línea discontinua por paso; la calculadora usa esos mismos colores y líneas y lleva debajo "Cómo leer la calculadora", con un ejemplo calculado con los datos; quitada la sección "Cómo medir bien a partir de ahora".
- Quitado también todo el bloque "Onboarding dentro del producto" (27/10, decisión de Alex: "no sirve"): onboarding por variante, control frente a variante, cómo mediremos un cambio y la fiabilidad del dato de entrada (PostHog frente a GA4). Borradas sus fuentes (onboarding, posthog_register, ga4_register). Las consultas siguen documentadas en este archivo y en H-12/H-13/H-24.

## Dónde se cae la gente · último mes (29-10-2026, H-47 y H-48)
PostHog, `dashboard.chekin.com`, del 29/09 al 29/10/2026. Los eventos del onboarding existen desde el 13/10, así que en la práctica son ~16 días. Consultas puntuales, no métricas guardadas.

| Paso | Personas | % de las que entran | % del paso anterior |
|---|---|---|---|
| Entran en `/register` | 771 | 100% | — |
| Crean la cuenta (email o Google) | 126 | 16% | 16% |
| Bienvenida | 112 | 15% | 89% |
| Eligen PMS | 64 | 8% | 57% |
| Paso de conectar | 29 | 4% | 45% |
| PMS conectado | 21 | 3% | 72% |
| Configuración completada | 29 | 4% | — (incluye «otro PMS» o saltar) |

Por variante (entran → cuenta creada): rebuilt 331 → 97 (29%; de ellos 27 ya eran clientes); legacy 205 → 0 (no envía eventos, H-12); sin variante 212 → 11 (109 pasan por el alta antigua); beta 23 → 18. En rebuilt, solo 84 escriben el email y 56 pulsan Google.
Fricción: 42 personas con `auth_captcha_failed` (1.364 veces); 13 entran en /register, y 12 de ellas no llegan a crear la cuenta. 6 con `auth_registration_failed`. 15 con fallo de PMS; 17 eligen «otro PMS»; 9 se saltan la configuración.
Antes del dashboard está el formulario web `chekin.com/…/onboarding/register-form/` (Clarity, 27–29/10): 167 sesiones; en 100, solo 38 escriben algo y casi la mitad se va en menos de 10 s; clics muertos en el selector de tipo (H-47).

**Las tres caídas grandes:** 1) la página de alta (de cada 10 que entran, menos de 2 crean cuenta; en rebuilt, 3); 2) tras la bienvenida, al elegir PMS (se va el 43%); 3) conectar el PMS (de 64 que eligen, 21 conectan).

## Propuesta de Alex: alta mínima (29-10-2026)
Registro solo con Google o email. Con Google ya tenemos nombre, apellidos y email; con email se piden nombre y apellidos. Se entra directamente al panel, que se puede ver. Teléfono, tipo de propiedad y número de propiedades se piden al pulsar «Empezar la prueba gratis», y desde ahí se guía.
**Principio (Alex, 29/10): hay que dejar entrar al usuario.** Nada bloquea la entrada: si el teléfono ya existe, se avisa dentro o se ofrece iniciar sesión, nunca se corta el alta.
Encaja con la caída 1. Riesgos a resolver antes:
- **ShowMe necesita el teléfono y el tamaño en el Pre-Trial** (micro = 1–3 viviendas; la llamada convierte mucho más que WhatsApp, H-27 a H-30). Sin teléfono en el alta, el Pre-Trial se queda sin llamada.
- **HubSpot y ventas** clasifican el lead por tipo y número de propiedades (Micro/SMB/hotel, AE asignado).
- **Dos formularios hoy** (web en chekin.com y alta en el dashboard): el nuevo flujo debería ser uno solo.
- **Medir** con un A/B en PostHog (flag): KPI principal = cuenta creada / entra en el alta; después, vivienda creada, trial y MRR. Arreglar antes la medición de legacy.
Pendiente: ver con Daniel el flujo nuevo «en proceso».

## Recorrido del alta actual en móvil (29-10-2026, navegador a 375×812, sin enviar nada)
`chekin.com/onboarding/register-form/` (ES):
0. **Banner de cookies** que tapa media pantalla, con **Analítica y Marketing marcadas de serie** [POR COMPROBAR con el DPO: las casillas premarcadas no valen como consentimiento].
1. **Una sola pantalla con 8 datos**: nombre, email, contraseña, tipo de propiedad, número de propiedades, ciudad/región, teléfono (con prefijo) y «¿Quieres conectar tu PMS?» sí/no (si sí, nombre del PMS). En móvil son unas dos pantallas de scroll y el botón «Continuar» queda abajo. **No hay opción de Google.**
2. **Código de 6 dígitos por email**, con la pantalla **en inglés** («Two-step authentication») aunque la página está en español.
3. Según el PMS, **pantallas de Holidu o Amenitiz** que piden permiso para ceder los datos al partner.
4. «¡Bienvenido! Lo primero que tienes que hacer **is** crear tu cuenta» (errata en inglés) → «¡Empecemos!» → dashboard: bienvenida → elegir PMS → conectar.

## Propuesta de pasos del onboarding nuevo (29-10-2026, sobre la idea de Alex: «dejar entrar al usuario»)
1. **Entrar** (una pantalla, sin scroll): «Empieza tu prueba gratis de 14 días» → **Continuar con Google** o **email** (+ nombre y apellidos). Sin contraseña: el código de 6 dígitos que ya existe sirve como acceso (en el idioma de la página).
2. **Dentro del panel**, se ve el producto (demo o vacío con ejemplos) y una barra «Empieza tu prueba gratuita».
3. **Paso guiado 1, tu negocio**: tipo de propiedad y número (dos toques). De aquí sale micro/SMB/hotel para ventas y ShowMe.
4. **Paso guiado 2, teléfono**, con motivo: «Un experto en Chekin puede ayudarte con la configuración». Si ya existe, no bloquea: avisa y sigue.
5. **Paso guiado 3, conectar el PMS**: en ordenador, como ahora; **en móvil, ofrecer «Te mandamos el enlace para hacerlo en el ordenador» o «Que lo haga un experto»**, porque en móvil casi nadie lo consigue (H-51).
6. **Paso guiado 4, primera vivienda y primer check-in de prueba**: el momento de activación.
- Se quitan del alta: contraseña, ciudad/región (se deduce o se pide al crear la vivienda) y la pregunta del PMS.
- Las pantallas de Holidu y Amenitiz, solo dentro y solo si el PMS lo pide.
- Desde la página de gracias de las landings, el botón lleva al paso 1 con el email ya puesto (H-51).
- Medir cada paso con un evento de PostHog: así el funnel nuevo sale solo en el dashboard.

## Prototipo de Daniel (29-10-2026) · revisión con los datos
https://dclemares.github.io/chekin-prototypes/dashboard/auth.html#login (en inglés; 15 pantallas: entrar, crear cuenta, cuenta creada, 5 pasos guiados y la portada del dashboard).
**Recorrido:** entrar con Google o con email (una sola pantalla para login y alta) → crear cuenta (Google o email + contraseña + nombre completo + teléfono + tipo de propiedad) → «Cuenta lista, tres preguntas» (se puede saltar) → 1 dónde operas (países y su obligación legal) → 2/3 cómo gestionas las reservas (PMS, Airbnb/Booking o a mano; «saltar») → 4 qué te importa más → 5 tu plan (primera propiedad, marca, check-in de prueba: «en marcha en ~8 min») → dashboard con «este panel aún no está adaptado · terminar configuración».
**Lo que ya encaja con los datos y con «dejar entrar al usuario»:** Google arriba; login y alta en la misma pantalla (resuelve a los que caen en el alta buscando el login, H-50/H-51); todo se puede saltar y se entra al panel; el PMS es una opción entre tres, no una obligación; plan corto con la activación (primera propiedad y check-in de prueba).
**Propuestas para Daniel:**
1. **Crear cuenta sigue teniendo 5 datos con email**, y la contraseña con 4 reglas. Propuesta: email + nombre y nada más (código de 6 dígitos o enlace en vez de contraseña). Teléfono y tipo de propiedad, dentro, en los pasos guiados.
2. **Teléfono:** dentro y con motivo («te llamamos para dejarlo configurado»), porque ShowMe y ventas lo necesitan. Si ya existe, avisar y seguir: nunca bloquear (grabación PT, H-47).
3. **PMS en móvil:** en móvil casi nadie lo conecta (0,8% frente a 7,5% en ordenador, H-51). Si entra desde el móvil, ofrecer «te mando el enlace para hacerlo en el ordenador» o «que lo configure un experto».
4. **Número de propiedades:** no aparece. Hace falta para micro/SMB (ShowMe entra por tamaño): leerlo del PMS y, si no hay PMS, preguntarlo en «Your portfolio».
5. **Pasos 2 y 3 enseñan la misma pantalla** en el prototipo, y la bienvenida anuncia el orden «reservas → dónde operas» mientras los pasos van «dónde operas → reservas». Por revisar.
6. **Idiomas:** ES, IT y PT primero (ahí está el tráfico), y que el código de verificación salga en el idioma del usuario (hoy sale en inglés).
7. **Desde las páginas de gracias de las landings:** entrar con el email ya puesto (H-51).
8. **Medición desde el primer día:** un evento de PostHog por pantalla (vista, completada, saltada) y A/B contra el alta actual con una flag. KPI: cuenta creada / entra; después, primera propiedad, check-in de prueba, trial y MRR.

## Guía de Alex («Onboarding de anfitriones con 2-3 viviendas», PDF) frente al prototipo de Daniel (29-10-2026)
La guía se hizo sin datos de la empresa (recorrido como anfitrión de prueba, ICE estimado). North Star de la guía: **viviendas activadas** = datos de la vivienda + check-in online activado + una reserva.
**Ya recogido en el prototipo de Daniel:** preguntas que salen del registro y pasan dentro; «¿Cómo recibes tus reservas?» con tres vías (guía #6); pasos con tiempos y un plan («en marcha en ~8 min», guía #4); Inicio con dos estados, cuenta nueva y en marcha (guía #2); login y alta en una sola pantalla.
**De la guía que todavía no está:**
- Usar lo declarado: número de viviendas y «vamos a activarlas, una a una» (guía #1). El prototipo no pregunta cuántas viviendas.
- Los 3 pasos de activación de la guía (datos, check-in online, reserva). El plan del prototipo es: propiedad, marca, check-in de prueba. Propuesta: la reserva antes que la marca.
- Envío automático del check-in encendido desde el alta (ICE 8,0, el primero de la guía).
- NIF/CIF/DNI con validación (ICE 7,7) y ubicación con sugerencias.
- Asistente que sabe en qué paso estás; segunda vivienda con los datos del propietario ya puestos.
**Lo que cambian los datos que la guía no tenía (H-47 a H-51):**
- La mayor pérdida está **antes del producto**: 16% de los que entran crean cuenta. El registro corto de la guía (C3) pasa a ser lo primero que hay que probar, y con menos campos todavía (Google o email + nombre).
- **Móvil:** 38% de las sesiones del formulario. El PMS en móvil casi nunca se conecta. En móvil, la vía recomendada no debería ser el PMS («FASTEST» en el prototipo), sino calendario, a mano o «hazlo en el ordenador».
- Clientes que buscan el login dentro del alta: lo resuelve la pantalla única de Daniel.
- Teléfono duplicado que bloquea, y leads de paid que rellenan dos formularios.
- El ICE de la guía se puede recalcular con datos: sube la confianza del registro corto y del PMS en móvil.

## Alta con Google: lo que falta pedir (Alex, 29-10-2026)
Con Google ya llegan nombre, apellidos y email. Una sola pantalla después, «Cuéntanos tu negocio» (~15 s):
- **Tipo de propiedad**, con botones (alquiler vacacional, hotel o aparthotel, camping, otro).
- **Número de propiedades**, con botones que coinciden con los tramos de HubSpot (Alex, 29/10): **1-3 (SMB Micro) · 4-10 (SMB) · 11-60 (Mid-Market) · más de 60 (Enterprise)**. Así el tramo queda puesto en el alta [POR COMPROBAR la regla exacta, H-52].
- **Teléfono**, con el prefijo **puesto según el país desde el que entra** (España +34, Italia +39, Portugal +351…: por el idioma o la página de entrada y, si no, por la ubicación de la conexión), que se puede cambiar; y el motivo («Un experto en Chekin puede ayudarte con la configuración»). Si ya existe, no bloquea.
- Botón «Entrar en Chekin». Después, el panel y los pasos guiados (reservas, primera vivienda, check-in).
Con email: email + nombre y apellidos → código de 6 dígitos → la misma pantalla.

## Onboarding propuesto: mezcla de la guía de Alex (PDF), el prototipo de Daniel y los datos (29-10-2026, borrador para Daniel)
| # | Paso | Qué pasa | De dónde sale |
|---|---|---|---|
| 0 | Llegada | Desde la página de gracias de una landing: email ya puesto. Prefijo e idioma según el país de entrada | Datos H-51 · Alex |
| 1 | Entrar | **Continuar con Google** arriba; o email + nombre y apellidos + código de 6 dígitos (sin contraseña). Login y alta en la misma pantalla | Alex · Daniel · datos H-48/H-50 |
| 2 | Cuéntanos tu negocio (~15 s) | Tipo de propiedad; cuántas (1-3 SMB Micro · 4-10 SMB · 11-60 Mid-Market · +60 Enterprise; en hoteles, habitaciones); teléfono con motivo, que nunca bloquea | Alex · H-52 · H-47 |
| 3 | Panel + «Primeros pasos» | Se entra y se ve el producto. Tarjeta fija: «Indicaste 3 viviendas: vamos a activarlas una a una», progreso y vídeo de 1 min. Sin «Ver planes» durante el onboarding | PDF #1-#3 · Daniel (inicio «aún no adaptado») |
| 4a | ¿Cómo recibes tus reservas? | Tres vías con una recomendada. **En móvil no se recomienda el PMS**: «te mando el enlace al ordenador» o «que lo haga un experto» | PDF #6 · Daniel paso 2 · datos H-51 |
| 4b | Datos de la vivienda | País y obligación legal (de Daniel), NIF/CIF/DNI con validación, dirección con sugerencias | Daniel paso 1 · PDF #4 |
| 4c | Check-in online | Envío automático **encendido** desde el alta, con aviso de qué se envía y cuándo | PDF #7 (ICE 8,0) |
| 4d | Primera reserva y check-in de prueba | Si no llegó por PMS o calendario, una a mano; enviarse el enlace de prueba | PDF · Daniel plan |
| 5 | ¡Vivienda activada! | Lo que ya funciona y «Siguiente: vivienda 2» con los datos del propietario ya puestos | PDF #5 |
| 6 | Después, opcional | Cumplimiento legal (credenciales SES), marca, upselling («3 ofertas en 1 minuto»), bandeja; «qué te importa más» aquí, no antes | PDF #11 · Daniel pasos 4-5 |
Asistente: sabe en qué paso estás y lleva al siguiente (PDF #3). Al plan de Daniel se le cambia el orden: la reserva antes que la marca.
**North Star:** viviendas activadas (datos + check-in online + reserva) ÷ declaradas, a 7 días (PDF). **KPI del alta:** cuenta creada / entra en el alta (H-48).
**Primer A/B:** pasos 1-2 (alta corta) frente al alta actual. Es donde se pierde más gente; después, la tarjeta «Primeros pasos» y el envío automático.
- **Documento para Daniel (29/10):** https://claude.ai/artifact/2WEQKEeA2NfBKpybzB45gX · **Pantallas en móvil, clicables:** https://claude.ai/artifact/U8YpmnbK8qQrjdd3vssSUc (6 pantallas: entrar, negocio, panel, reservas, vivienda y activada). Los dos privados hasta que Alex los comparta.
- **Prototipos navegables (29/10), uno por dispositivo:** portátil https://claude.ai/artifact/DfLw9HeJKddbpxHYRC6mLP · móvil https://claude.ai/artifact/CjcH5gMdon5qBKatXSLopN. Frases de las landings («Prueba Chekin gratis 14 días», «Sin tarjeta de crédito. Activación inmediata.», «sin permanencia», «+200.000 propiedades y +25M de check-ins», «El parte de viajeros, enviado solo y en plazo»). Alta con el patrón del prototipo de Daniel (email → Continuar → nombre y apellidos si la cuenta es nueva → código).
- **Versión 30/10 de los prototipos** (mismos enlaces): login sin contraseña que entra solo, dirección con autocompletado, vivienda 2 con datos reutilizados, «¡Todo listo!», plan de 14 días en el Inicio, upselling destacado, textos en positivo y explicaciones emergentes («Explicaciones: sí/no») para presentar. El lienzo de diseño se queda en la versión del 29/10: la referencia son los prototipos.
- **Versión 30/10 tarde** (mismos enlaces). Ahora hay los mismos 12 pasos en móvil y en portátil: entrar → tu negocio → Inicio → 1 reservas (→ guía del PMS) → 2 vivienda → 3 check-in → ¡activada! → Inicio 1 de 2 → vivienda 2 → ¡todo listo! → Inicio final.
  - **Vivienda (la mayor caída: 58,2 % de alquiler vacacional y 32,9 % de hoteles llegan a crear vivienda, altas solas 07/06–03/09/2026):** solo nombre y dirección. El NIF pasa a opcional (se pide al conectar SES). Si viene del PMS, la vivienda llega rellena.
  - **Paso 3, check-in online como valor por adelantado:** se ve lo que verá el huésped, con extras de pago. El envío automático viene activado y el cliente se manda un enlace de prueba.
  - **Pantalla de logro igual en los dos dispositivos:** qué ya funciona y qué falta (SES ≈ 3 min). Después, «Continuar con la vivienda 2» o «Hacerlo después».
  - **Guía por PMS:** 3 pasos, la API key explicada en una frase, un vídeo de 2 min por PMS y un experto como salida. Los vídeos están [POR GRABAR]; la lista de PMS, [POR COMPROBAR] con la página de integraciones.
  - **Mid-Market y Enterprise (11-60, +60):** sale un aviso «¿Quieres que un experto en Chekin te ayude a configurar tus viviendas?» (o habitaciones, en hoteles). No bloquea. Micro y SMB siguen la guía solos.
- **Versión 30/10 noche, flujo único** (mismos enlaces; el de portátil ya está compartido con la organización). Revisado antes el prototipo de Daniel y el alta real de chekin.com (registro y login en páginas separadas, con contraseña y sin Google).
  - **Entrar:** una sola puerta que reconoce el email. Cuenta nueva → nombre y apellidos → código → tu negocio. Ya tiene cuenta → «¡Hola de nuevo!» → código → su Inicio, donde lo dejó. En la demo, dos botones: «Cliente nuevo» y «Ya tiene cuenta».
  - **Tu negocio:** el número exacto de viviendas (vacío, con + y −, o escrito a mano) en vez de los tramos. Con más de 10, sale el aviso de experto.
  - **Pasos:**
    - 1: ¿usas PMS? Sí → guía del PMS; no → calendario o a mano.
    - 2: ¿dónde está la vivienda? España → comunidad: Cataluña (Mossos), País Vasco (Ertzaintza), resto (SES.Hospedajes). Italia: Alloggiati. Portugal: SIBA. Después, conectar el parte de viajeros («paso clave»; no bloquea).
    - 3: vivienda (nombre y dirección).
    - 4: check-in y enlace de prueba.
    - El nombre de la autoridad elegida se arrastra al resto de pantallas.
  - **Ajustes de Alex (30/10, 15:30):**
    - Contador de viviendas estrecho, con − y + a los lados y sin las flechas del navegador.
    - El aviso de experto sale al pulsar «Ir a mi panel», no mientras escribe el número.
    - El paso 1 ofrece **tres formas al mismo nivel**: PMS, calendario de Airbnb o Booking, o a mano. En portátil se destaca el PMS; en móvil, el calendario.
  - **Países (30/10, de chekin.com/legalidad):**
    - Con parte a las autoridades: España (comunidad: SES, Mossos o Ertzaintza), Italia, Portugal, Alemania, Austria, Croacia, Suiza, República Checa, Bulgaria, EAU, Brasil y Colombia.
    - Solo formulario de entrada, sin parte a la policía: Francia, Reino Unido, Grecia, Países Bajos, Bélgica y Rumanía. Estos van directos a la vivienda.
    - Quien conecta el PMS no pasa por «¿Dónde está tu vivienda?»: va directo al parte de viajeros.
    - [POR COMPROBAR el nombre de la autoridad en Suiza, Chequia, EAU, Brasil y Colombia.]
  - **Con PMS, «Tus viviendas» (paso de Daniel «Reading your portfolio», 30/10):**
    - Al conectar el PMS, una lectura rápida con animación: contamos las viviendas, las situamos y vemos a quién va el parte de cada una.
    - Después, las viviendas agrupadas por zona, cada grupo con su autoridad: Madrid → SES, Barcelona → Mossos, Lisboa → SIBA. Cada autoridad se conecta una sola vez.
    - Debajo, «¿No es correcto? Ajústalo a mano», que lleva a elegir el país.
    - Daniel además lee el precio medio y la tasa turística por zona; lo dejamos fuera [POR COMPROBAR qué devuelve cada PMS].
  - **Banderas:** las comunidades llevan su bandera (senyera, ikurriña) en vez de emojis.
  - **PENDIENTE (idea de Alex, 30/10, sin ejecutar): pantalla de «creando tu cuenta».**
    - Cuándo: después del código, solo para cuenta nueva. Crear la cuenta tarda unos segundos y la página no debe quedarse en blanco (Daniel tiene esta pantalla en su prototipo: `auth.html#r-creating`).
    - Mientras carga: el logo de Chekin encuadrado y centrado, latiendo despacio como un corazón. Debajo, textos que van cambiando con lo que se está haciendo («Creando tu cuenta…»).
    - Al terminar: la animación del GIF de la firma (P5): el check crece y se ilumina. Después entra en «Cuéntanos tu negocio».
    - Referencia: `2-herramientas/firma-gmail/chekin-firma-cuadrada-DEFINITIVA.gif` y `cuadrado/chekin-cuadrado-check-400.gif` (scripts `make_gif_cuadrado.py`).
    - **Y justo después, una bienvenida con lo que viene y sus tiempos (le gusta a Alex, de Daniel: `auth.html#r-welcome`).**
      - «¡Hola, Katia! Bienvenida a Chekin»: tu cuenta está lista.
      - Tarjeta «Lo que viene · ≈ 8 min» con nuestros pasos y su tiempo: 1 Reservas (PMS, calendario o a mano) · 2 Parte de viajeros · 3 Vivienda · 4 Check-in y enlace de prueba.
      - Botones: «Empezar» y «Saltar por ahora».
      - En portátil, la columna izquierda marca el progreso de los pasos, como en Daniel.
      - Al pulsar «Empezar», salta al paso siguiente.
    - **Decidido por Alex (30/10):**
      - **Países:** se coge el de Daniel: selección múltiple, buscador y tarjetas con bandera, etiqueta y autoridad. España sigue preguntando la comunidad.
      - **Reservas** (PMS, calendario o a mano): se queda el nuestro.
      - **«Protege tus viviendas»** (protección de daños o fianza): entra como paso.
      - Pendiente de decidir: la columna de progreso con chips y la barra fina.
      - **Upselling y protección, prioridad (Alex, 30/10):** «el upselling es primordial: ellos ganan dinero y nosotros también; con asegurar su casa, igual». Deben ser **pasos del onboarding**, no solo una tarjeta en el Inicio.
      - **Referencia, el Inicio de Daniel** (`dashboard/index.html`):
        - Cabecera «Tu panel está listo» con un plan de 7 pasos, unos 18 min y un anillo de % de configuración («0 de 7 hechos»). Los pasos: primera vivienda, protección de daños, fianza, parte de viajeros, tasa turística, branding y enlace de prueba.
        - Debajo, «De un vistazo» (viviendas, reservas importadas, check-ins listos, partes enviados), «La agenda de hoy» y «Salud del cumplimiento» por autoridad (SES, Mossos, tasa turística).
        - Al final, recursos: guía, tour de 2 min y centro de ayuda.
      - **Lo que hace Daniel al elegir PMS (capturas de Alex, 30/10), para comparar con lo nuestro:**
        1. **Elegir PMS:** rejilla de logos (Guesty, Hostaway, Lodgify, Smoobu, Avantio, Cloudbeds, Octorate, Otro) y buscador «81 integraciones». La web oficial dice «+200 PMS» [POR COMPROBAR cuál vale].
        2. **«Conecta Cloudbeds»:** sin copiar nada. Autorizas en la web del PMS (OAuth, «nunca vemos tu contraseña»), con vídeo y «Qué hace esta integración» (qué trae del PMS y qué le devuelve). Botón «Lo conecto luego».
           - **Mejor que nuestra API key** cuando el PMS lo permite. Donde no, se queda nuestra guía de API key con vídeo [POR COMPROBAR qué PMS permiten OAuth].
        3. **Ventana «Autorizar Chekin»** con los permisos → «Cloudbeds conectado».
        4. **«Esto nos ha dicho Cloudbeds»:**
           - 14 viviendas, 3 grupos y precio medio por noche;
           - cada grupo con su % de la cartera y su precio;
           - «Fue una lectura, no una importación»;
           - «¿No es correcto? Ajústalo a mano».
           - Nuestro «Tus viviendas» es la versión corta de esto.
        5. **«Cumplimiento legal, grupo a grupo»:** cada grupo en tres columnas, ya activado como lo dejaríamos:
           - parte a la policía (obligatorio, con su autoridad y «Configurar luego»);
           - verificación de identidad (documento + selfie, recomendada);
           - tasa turística (importe por huésped y noche, exentos y máximo de noches).
           - Las cifras de las tasas son de Daniel [POR COMPROBAR].
        - **Propuesta:** coger 1, 2, 4 y 5 dentro de nuestro paso de reservas y de parte de viajeros. Nuestras reservas siguen siendo las de 3 formas.
    - **Más cosas del prototipo de Daniel vistas el 30/10 (capturas de Alex), por decidir:**
      - **Columna izquierda en portátil:** los pasos con su estado (✓, actual y pendientes). Debajo, «Tu configuración hasta ahora» con chips de lo que ha contestado (p. ej. «Hotel / aparthotel», «11-30 habitaciones», «España · cumplimiento») y «¿Dudas? Habla con nosotros: respondemos en unos 3 min».
      - **Países con selección múltiple:** buscador y tarjetas con bandera, etiqueta («Policía + tasa turística» o «Tasa turística») y autoridad. Sirve a quien tiene viviendas en varios países.
      - **Paso «Protege tus viviendas»:** protección de daños (hasta 2.500 €, la paga el huésped) o fianza (se cobra y se devuelve a los 7 días), con vídeo y «Obligatorio / Opcional / Apagado». Es valor por adelantado y venta extra. Las cifras son las del prototipo de Daniel [POR COMPROBAR con Producto].
      - Una barra de progreso fina arriba.
  - **Fuera, de Daniel:** «¿Qué te importa más?» y «Tu plan» (branding y lo demás). El upselling sigue en el Inicio.
  - **Por comprobar con Producto:**
    - qué datos pide cada autoridad;
    - si van por titular o por vivienda;
    - si Cataluña y País Vasco envían también a SES.

## Versión 30/10 tarde-noche: onboarding completo de una vez (nuestro + Daniel)
Mismos enlaces (móvil y portátil). Principio de Alex: entrar y terminarlo todo de una vez, sin salir ni volver a meter viviendas. Después solo quedan las reservas, con el envío del check-in elegido.
- **Entrada:** Entrar (puerta única: cuenta nueva o ya tiene cuenta → su Inicio) → Tu negocio (número exacto; aviso de experto con más de 10) → **Creando tu cuenta** (el logo late; al terminar, el check crece y se ilumina, y pasa solo) → **Bienvenida** con los 7 pasos y su tiempo (≈ 10 min).
- **7 pasos** (en portátil, columna izquierda con el progreso y «Lo que nos has contado»; en móvil, barra de progreso):
  1. **Reservas:** PMS, calendario de Airbnb o Booking, o a mano (el nuestro).
     - Con PMS: elegir el PMS por su logo y buscador → **conectar sin copiar** (se autoriza en la web del PMS; alternativa: guía de la API key con vídeo).
  2. **Dónde están:**
     - Con PMS, «Esto nos ha dicho tu PMS»: viviendas agrupadas por zona.
     - Sin PMS, países con **selección múltiple** (Daniel). España abre la comunidad (Mossos, Ertzaintza o SES).
  3. **Cumplimiento legal, grupo a grupo** (Daniel): en cada zona, el parte a la policía (se conecta una vez; «te lo recordamos»), la verificación de identidad y la tasa turística. Sin importes inventados.
  4. **Tus viviendas:** todas de una vez (filas y «+ Añadir otra»). Con PMS este paso se salta.
  5. **Protege tus viviendas:** protección de daños o fianza (Daniel). Cifras [POR COMPROBAR].
  6. **Ventas extra:** 4 ofertas con precio editable.
  7. **Check-in y envío:** envío automático sí o no, y con cuánta antelación (al confirmar, 72 h, 48 h o 24 h), vista del huésped y enlace de prueba.
- **Final:** «¡Todo listo!» con lo que ya funciona → **Inicio** al 100 %, con las próximas reservas (cada una con su interruptor de envío), las ventas extra y el cumplimiento.
- **Fuera:** «¿Qué te importa más?» y «Tu marca» de Daniel.
- **Por comprobar con Producto:**
  - qué PMS permiten autorizar sin copiar;
  - 81 integraciones o +200 PMS;
  - las cifras de protección;
  - los importes de las tasas;
  - las autoridades sin nombre;
  - el envío por defecto (48 h).
- **Fallos vistos por Alex en esta versión (30/10, sin arreglar todavía):**
  - **Viviendas:** todas a la vez en una rejilla abruma, justo en el paso con más caída. Propuesta: una a una dentro del mismo paso («Vivienda 2 de 4»), con las hechas a la vista y «Guardar y siguiente».
  - **Se ha perdido la dirección con autocompletado de Google.** Hay que recuperarla: al escribir salen sugerencias y, al elegir una, se rellenan ciudad, código postal y provincia, más «Piso, puerta o bloque».
  - **Falta el NIF/CIF del titular** (con validación). Se pide una vez, con «El mismo titular para todas mis viviendas», y se reutiliza en el parte.
  - **Revisar qué otros pasos se han caído** frente a versiones anteriores y al producto real [POR COMPROBAR con Producto: número de registro o licencia de la vivienda, código de establecimiento de SES].
  - **Credenciales de SES.Hospedajes mal planteadas.** El prototipo pide «Usuario de SES.Hospedajes» y contraseña, como si fuera el login del portal. Según fuentes externas (Amplistay, 04/10/2026; grupo de ayuda de SES en Facebook), para conectar un software hacen falta:
    - el **código de arrendador**;
    - el **código de establecimiento** (uno por vivienda);
    - el **usuario y la contraseña del servicio web (WS)**, distintos del email de acceso al portal. Se generan en SES.Hospedajes y llegan en el correo de confirmación.
    - Hay que cambiar los campos y explicar dónde se encuentra cada dato, con vídeo.
    - [POR COMPROBAR con Producto o con la guía de Chekin (landing.chekin.com, «ES_Guide_SES»): qué pide exactamente Chekin, y qué piden Mossos y Ertzaintza.]

### Investigación: qué pide cada autoridad (30/10, fuentes externas; falta confirmarlo con Producto)
- **SES.Hospedajes (España, menos Cataluña):** son dos altas distintas que la gente confunde (Kinapi, «Alta en SES Hospedajes paso a paso», 05/09/2026; Apartop, 11/10/2026; Amplistay, 04/10/2026):
  1. **Alta del titular («sujeto obligado») y sus establecimientos**, en la Sede Electrónica con **certificado digital o Cl@ve**. Piden el NIF/CIF, el nombre o razón social y el domicilio del titular, y por cada vivienda la **dirección completa** y, cuando corresponde, el **número de registro turístico autonómico**. A cambio dan el **código de arrendador** (uno por titular) y un **código de establecimiento por vivienda**.
  2. **Alta del usuario del servicio web**, aparte. Da el **usuario WS y su contraseña**, que **no son los de la Sede**. Esto es lo que necesita un software como Chekin, junto con los dos códigos.
  - El titular es el dueño de la actividad, no quien la gestiona. **Un gestor con pisos de varios propietarios tiene varios titulares**, así que «el mismo titular para todas» no siempre vale.
- **Mossos d'Esquadra (Cataluña):** el parte va a su portal, no a SES (Checkin Vacacional, 03/05/2026). Qué credenciales pide para un software: [POR COMPROBAR].
- **Ertzaintza (País Vasco):** [POR COMPROBAR].
- **Alloggiati Web (Italia):** acceso con un usuario que identifica la estructura y una contraseña (Questura di Rovigo). Para conectar un software suele hacer falta además una clave del servicio web [POR COMPROBAR].
- **SIBA/AIMA (Portugal):** [POR COMPROBAR].
- **Implica:** los campos «Usuario y contraseña de SES» del prototipo están mal. Además, mucha gente aún no tiene el usuario WS, porque requiere certificado o Cl@ve. Hace falta:
  - una salida buena: «No lo tengo: te guiamos para pedirlo» con vídeo, «Lo hacemos contigo» con un experto, y un recordatorio;
  - que el paso nunca bloquee el resto del onboarding.

### Revisión UX a fondo del prototipo (Alex: «la experiencia debe ser brutal»), pendiente de aplicar
1. **Los botones de abajo se pierden** al final de las pantallas largas. Hace falta una barra inferior fija con Atrás y Continuar, siempre visible en portátil y en móvil.
2. **Errores de texto:** «✓Smoobuconectado» sin espacios (el diseño en caja flexible se come los espacios entre trozos). Revisarlo en todos los botones con nombre dinámico.
3. **Orden de los pasos, propuesta:** Reservas → Dónde están → **Titular y viviendas, una a una** → **Conectar el parte** con los datos correctos, una vez por titular, más verificación de identidad y tasa turística → Protección → Ventas extra → Envío del check-in.
   - Los datos de cada vivienda (dirección con autocompletado de Google, piso o puerta, número de registro turístico, código de establecimiento de SES) van con la vivienda.
   - Las credenciales van una vez por titular.
4. **Viviendas una a una** («Vivienda 2 de 4»), con las hechas a la vista. **NIF/CIF del titular** con validación y «El mismo titular para todas», que se puede cambiar por vivienda (para gestores).
5. **Protección:** quitar «Obligatorio / Opcional / Apagado». Los dos interruptores salen activados y se pueden apagar.
6. **Etiquetas de cumplimiento** («OBLIGATORIO POR LEY», «TE LO RECOMENDAMOS»): decidir con Alex si se quitan igual que en Protección. El parte sí es obligatorio por ley.
7. **Países en móvil:** la lista es muy larga. Primero el buscador y los 3 principales; el resto, tras «Ver más países».
8. **Guardado automático visible** («Guardado · puedes seguir luego») y retomar donde se quedó.
9. **Validación al momento** (NIF, códigos) con mensajes en positivo, nunca solo en rojo.
10. **Accesibilidad:** foco visible, etiquetas en todos los campos y botones de al menos 44 px.
11. **Diseño general (Alex, 30/10):** las pantallas se ven «muy amplias, con poca UI y UX», por ejemplo la bienvenida en portátil: una lista larga y estirada, con mucho vacío y los botones lejos. Hay que trabajar todo el prototipo:
    - contenido más estrecho y centrado (una columna de unos 640 px);
    - jerarquía clara y algo visual en cada paso (ilustración, vista previa o ejemplo);
    - tarjetas compactas;
    - el botón principal cerca del contenido.
12. **«Creando tu cuenta»:**
    - Un solo color: el cuadrado del check **azul marino oscuro** (#19194B) de principio a fin. Ahora pasa de marino a azul (#385BF8) al terminar.
    - Que haga la animación del GIF (el check crece y se ilumina), en marino.
    - Al terminar, mensaje en positivo bien visible: «¡Cuenta creada!» y algo como «Ya puedes empezar a recibir huéspedes».
    - **Que se quede 2-3 segundos** para que se lea. Ahora pasa a la bienvenida demasiado rápido: el mensaje final dura 1,4 s.
    - Referencia: el GIF que mandó Alex (cuadrado redondeado con el check blanco).
13. **Principio de diseño: «como abrir un producto de Apple» (Alex, 30/10).** El ritmo engancha: pausas buscadas, que algo se descubra poco a poco y momentos de recompensa. No se trata de ir lo más rápido posible. Dónde aplicarlo:
    - **Creando tu cuenta:** latido mientras carga, un instante de pausa, el check crece y se ilumina y «¡Cuenta creada!» se queda 2-3 s antes de pasar.
    - **Entre pasos:** transición suave, con la columna de progreso marcando el ✓ del paso que acaba.
    - **Leyendo tu PMS:** las líneas aparecen una a una y los números (viviendas, grupos) suben contando.
    - **¡Todo listo!:** la lista de lo que ya funciona se marca ✓ por ✓, cada uno con un pequeño retraso, y al final el botón «Ir a mi panel».
    - **Inicio:** el anillo se llena hasta el 100 %.
    - **Límites:** nada de esperas sin sentido (cada pausa enseña algo) y respetar «movimiento reducido» en accesibilidad.

### Aplicado el 30/10 por la tarde (mismos enlaces): las 13 mejoras
- **Diseño:**
  - Columna centrada de 640 px (860 en las pantallas anchas).
  - Tarjetas compactas, un icono por paso y textos en positivo.
  - **Barra de botones fija abajo.** En portátil, cada pantalla mide 900 px y el contenido se desplaza por dentro; en móvil, la barra va pegada abajo.
  - «✓ Guardado» en la cabecera.
- **Ritmo, «como un producto de Apple»:**
  - Creando tu cuenta: todo en marino. El logo late; a los 1,5 s, «Preparando tu panel…»; a los 3 s, el check crece y se ilumina con «¡Cuenta creada!», que se queda 3 s.
  - Cada paso entra con un leve desplazamiento y el ✓ del paso anterior aparece con un pequeño rebote.
  - «Leído del PMS»: líneas una a una y números que suben contando.
  - ¡Todo listo!: lista ✓ a ✓ y, al final, el botón.
  - Inicio: anillo grande que se llena hasta el 100 %, con degradado de oscuro a claro y «100 % · CONFIGURADO» dentro.
  - Todo se desactiva si el usuario tiene «reducir movimiento».
- **Orden nuevo:** 1 Reservas → 2 Dónde están → 3 Titular y viviendas → 4 Parte de viajeros → 5 Protección → 6 Ventas extra → 7 Check-in y envío.
- **Titular:** NIF, NIE o CIF comprobado al escribirlo, y «El mismo titular para todas», que se puede desmarcar para gestores.
- **Viviendas una a una** («Vivienda 2 de 4»): dirección con autocompletado («✓ Dirección encontrada»), piso, registro turístico y código de establecimiento de SES (opcional). A la derecha se van marcando las hechas. Con PMS este paso se salta.
- **Parte de viajeros:**
  - SES con código de arrendador, usuario y contraseña del servicio web, más el aviso «no son los del portal».
  - Mossos y SIBA con usuario y contraseña [POR COMPROBAR].
  - Salidas si no tiene los datos: vídeo, un experto o un recordatorio.
  - Sin etiquetas de «obligatorio»; la verificación de identidad y la tasa turística salen activadas.
- **Protección:** sin «Obligatorio / Opcional / Apagado»; dos interruptores activados que se pueden apagar.
- **Países:** buscador y los 3 principales a la vista; el resto, en «+ Ver más países (15)».
- **Arreglos:** espacios en «✓ Smoobu conectado» (sin cajas flexibles en textos con nombre dinámico), campos de dos en dos apilados en móvil, foco visible y botones de 44 px o más.
- **Confirmado (30/10, 17:20) con más fuentes:** Check-in Easy (08/08/2026), Kinapi (05/09/2026), Amplistay (04/10/2026), Apartop (11/10/2026) y el vídeo de MisterPlan coinciden. Para enviar el parte de SES automáticamente hacen falta **cuatro datos**:
  - **usuario del servicio web** (suele terminar en «WS»);
  - **contraseña del servicio web**, distinta de Cl@ve y del certificado;
  - **código de arrendador**, el «código de entidad», que **no es el NIF**;
  - **código de establecimiento**, uno por vivienda.
  - Cl@ve y el certificado solo sirven para entrar al portal y darse de alta.
  - El prototipo pide los tres primeros en el parte y el código de establecimiento en cada vivienda: cuadra.
  - Falta confirmar con Producto que Chekin pide exactamente esto. Chekin tiene su propia guía en PDF en landing.chekin.com, «ES_Guide_SES».
  - **Mossos y SIBA:** los campos «usuario y contraseña» del prototipo son una suposición [POR COMPROBAR].

### 30/10, 17:30 (mismos enlaces)
- **Protección como la de Daniel, con nuestro diseño:**
  - ventajas (respaldo económico, cobro inmediato) y vídeo;
  - «Todas tus viviendas», con «Separar por grupos»;
  - protección de daños (hasta 2.500 €, 27,20 € por estancia que paga el huésped) y fianza (200 €, se devuelve a los 7 días), cada una con «?» y Ajustes;
  - y lo que elige el huésped.
  - Sin «obligatorio/opcional»: vienen activadas y se pueden apagar. Cifras de Daniel [POR COMPROBAR].
- **Viviendas:** al guardar cada una sale «¡Bien hecho, Katia! Ya tenemos tu primera vivienda registrada. ¿Seguimos con el resto? Te quedan 3». Botones «Sí, seguir con la vivienda 2» o «Termino aquí y sigo con el resto del alta»; las demás se añaden luego desde Viviendas.
- **Botones:** «← Atrás» con borde, al lado de «Continuar», los dos juntos a la derecha. La barra inferior, blanca y con sombra para que se vea más.
- **Final:** «Entrar en mi panel →» grande y centrado, debajo de la lista; sin barra vacía.
- **¿Es obligatorio? (30/10).**
  - **Por ley**, comunicar los huéspedes a la policía sí lo es (RD 933/2021: SES, o Mossos en Cataluña y Ertzaintza en el País Vasco).
  - **Darle los datos a Chekin no lo es:** sirve para que el parte salga solo; sin ellos, el cliente lo envía a mano. Por eso el paso nunca bloquea.
  - **Verificación de identidad:** función de Chekin, recomendada, no exigida por ley.
  - **Tasa turística:** solo donde la cobra el municipio o la comunidad.
  - **Mossos:** se pide usuario y contraseña **por establecimiento**, más su número (ReceptionGo, 22/10/2026). El portal oficial es registreviatgers.mossos.gencat.cat. Ertzaintza, Alloggiati y SIBA: [POR COMPROBAR].
- **Ertzaintza y Navarra (30/10):**
  - **Ertzaintza:** primero se da de alta el establecimiento y luego el usuario, con certificado digital o con un formulario sin certificado. Al aprobar el alta, la Ertzaintza da **usuario y contraseña**, que son los que se usan para enviar (Lodgify, 17/03/2026). Admite el envío automático desde un software.
  - **Navarra / Policía Foral:** no encontramos un sistema propio. Las fuentes (softwareparahoteles.app, oct. 2026, y otras) dicen que solo **Cataluña (Mossos) y el País Vasco (Ertzaintza)** van aparte; el resto, Navarra incluida, va a SES [POR COMPROBAR con Producto].
  - **Dato de mercado** (softwareparahoteles.app, oct. 2026): Chekin es el socio que envía los partes para Cloudbeds (a Mossos y Ertzaintza), Amenitiz, Smoobu y Avantio. Vía Amenitiz, Chekin envía a SES, Mossos o Ertzaintza **cada noche a las 23:00**, con reenvío manual.
- **Aplicado al prototipo (mismos enlaces):**
  - Cada autoridad pide sus propios datos, con una ayuda debajo.
  - Nueva tarjeta **«¿Qué te pedimos según dónde esté tu vivienda?»**:
    - SES (Navarra incluida): código de arrendador, usuario y contraseña del servicio web, y el código de establecimiento en cada vivienda;
    - Mossos y Ertzaintza: usuario y contraseña del establecimiento;
    - Alloggiati y SIBA: usuario y contraseña.
  - Cl@ve y el certificado solo hacen falta para el alta; a Chekin no se le dan.

### 02/11: un solo marco y un solo diseño en todos los pasos (mismos enlaces)
- Alex vio pantallas con marcos, tonos y animaciones distintos («Entrar» y «Tu negocio» seguían con el diseño antiguo; «Creando tu cuenta» y el Inicio iban por libre).
- **Ahora las 18 pantallas comparten marco**, comprobado una a una en el navegador:
  - **Portátil:** columna izquierda de 300 px con el mismo degradado marino, fondo #F7F7FC, títulos de 28 px en negrita y contenido en columna centrada. En el Inicio, la misma columna con el menú de la app.
  - **Móvil:** la misma cabecera fija, el mismo fondo y títulos de 24 px.
  - En todas: los mismos botones (azul y con borde), las mismas tarjetas y la misma animación de entrada.
- «Entrar» y «Tu negocio» rehechos con ese diseño y con todo lo que hacían: Google o email, cuenta nueva o ya tiene cuenta, el código que entra solo, el contador, el teléfono y el aviso del experto con más de 10.
- **Inicio con «Ventas extra» detallado (02/11, mismos enlaces):** sección propia justo bajo las cifras, con:
  - ingresos del mes, ventas, % de huéspedes que compran y ticket medio;
  - ingresos por semana, en barras que crecen al entrar;
  - cada oferta con su precio, ventas, ingresos e interruptor;
  - protección y fianza activas, con estancias protegidas y fianzas cobradas;
  - «Vende más · 1 clic», con ofertas recomendadas.
  - Datos de ejemplo coherentes (165 € = 80 + 40 + 30 + 15; 10 ventas de 64 huéspedes) y marcados como tales. Además, sirve de lista de lo que Producto debería medir (H-61).
- **Inicio reordenado (02/11, Alex: «primero lo importante, por lo que contratan Chekin»):**
  1. **Estado de la operación:** «Todo en orden, Katia» (4 viviendas listas, partes al día, 1 cosa que revisar) y «Crear reserva». Llegadas de hoy, próximos 7 días (6 llegadas, 14 huéspedes), check-in online hecho (5 de 6) y partes enviados (31, ninguno pendiente).
  2. **Próximas reservas,** con su estado y el interruptor de envío. Al lado, **lo que falta** (un huésped sin documento: sin él no sale su parte; «Reenviar enlace») y el **parte de viajeros** por autoridad, todas conectadas, con el recordatorio de que es obligatorio y necesario para enviar el check-in.
  3. **Tus viviendas,** cada una con su ciudad, autoridad y «✓ Lista».
  4. **Ventas extra, abajo:** «**Este mes, Chekin te sale gratis**: tus extras han generado 165 €, cubren 4,2 meses de tu suscripción y te sobran 126 €». Debajo, las cifras, los ingresos por semana, la protección y la fianza, y «Vende más». La lista de ofertas queda detrás de «Ver tus 4 ofertas».
  - El precio de suscripción (39 €/mes) es de ejemplo [POR COMPROBAR con los precios reales]. Datos de ejemplo.

### 03/11: auditoría UX/UI del onboarding (estilo Big 4)
- Informe: https://claude.ai/artifact/WtCPS5BDJgfZMFLec1pnFV (doc privado hasta que Alex lo comparta). Revisión independiente de un agente que no participó en el diseño, contrastada en el prototipo.
- **Nota media: 2,5 sobre 5.** Motivación 4; claridad y feedback 3; esfuerzo, coherencia, prevención de errores, accesibilidad y confianza 2.
- **Fricciones críticas y altas:**
  - el parte de viajeros pide las credenciales de tres autoridades en una sola pantalla;
  - teléfono y tres preguntas antes de entrar;
  - el aviso del experto, mal calibrado para hoteles;
  - el PMS «el más rápido» frente a «a mano», también en móvil;
  - el calendario no tiene pantalla para pegar el enlace;
  - la vivienda dice «solo nombre y dirección» y pide 5 campos.
- **Errores de coherencia:**
  - «165 € cubren 4,2 meses y te sobran 126 €»;
  - «Madrid y Valencia» frente a las viviendas del Inicio;
  - «¡Todo listo!» dice «desde tu PMS» aunque no se eligiera;
  - mensajes como «¡Viviendas listas!» que son falsos según el camino.
- **Plan en 3 oleadas:**
  1. arreglos rápidos del prototipo (1 semana);
  2. cambios de flujo con Daniel (2–3 semanas);
  3. confianza y cumplimiento con Producto y el DPO.
- **Oleada 1 aplicada (03/11, mismos enlaces):**
  - **Cifras y textos coherentes:**
    - «Este mes, tus extras pagan Chekin: 165 € pagan 4 meses (39 €/mes, de ejemplo)»;
    - «Madrid» en lugar de «Madrid y Valencia»;
    - los pasos suman 10 min;
    - mensajes de paso neutros («Vas genial…»);
    - «Ahora no» como único nombre para saltar.
  - **Vivienda:** solo nombre y dirección. El código de establecimiento de SES pasa al parte de viajeros, opcional y por vivienda.
  - **Tu negocio:** teléfono opcional, con selector de prefijo y para qué se usa. El aviso del experto salta con más de 10 viviendas o más de 60 habitaciones o parcelas, y en las dos salidas.
  - **Entrar:** antes del código no se ven los 7 pasos, sino el valor y «¿Ya eres cliente? Entrar».
  - **Una sola confirmación:** «¡Cuenta creada!» a los 1,6 s, con botón «Continuar», y pasa sola a los 4,6 s. «Tu negocio» ya no dice «Ya estás dentro» y la bienvenida dice «Empezamos».
  - **«¡Todo listo!» fiel al camino:** reservas desde el PMS, el calendario o a mano; viviendas hechas o pendientes; parte conectado o «pendiente: te lo recordamos» (en ámbar).
  - **AA:** gris secundario #55557F, textos de 11–12 px subidos a 12–13 px, interruptores de 52×30 y foco visible.
- **Copia de seguridad del código** en `2-herramientas/onboarding-prototipo/`: la carpeta temporal perdió los logos el fin de semana; se recuperaron de la última versión compilada.
- **Oleada 2 aplicada (03/11, mismos enlaces; ahora 20 pantallas):**
  - **Parte de viajeros, una autoridad cada vez y sin bloquear.** Cada autoridad va plegada con dos opciones:
    - «No los tengo: ayúdame»: vídeo, un experto o «recuérdamelo»; en móvil, también «mándamelo al ordenador»;
    - «Tengo los datos»: el formulario.
    - Al conectar, «✓ Conectado». Lo pendiente pasa a ser una tarea en el Inicio.
    - Verificación de identidad y tasa turística, una vez para todas; la tasa, apagada por defecto.
  - **Calendario de Airbnb o Booking:** pantalla nueva para pegar el enlace de cada anuncio, con dónde encontrarlo, «✓ 3 reservas encontradas» y «+ Añadir otro anuncio».
  - **Reservas ordenadas por dispositivo:** en móvil, el calendario primero y el PMS al final. «A mano» ya no compite en rapidez («para probar sin conectar nada»).
  - **Estados de error, con un botón de demo:** código incorrecto, permiso del PMS rechazado, API key no válida, dirección no encontrada y datos de la autoridad incorrectos.
  - **Inicio honesto para la cuenta nueva:** «Lo que te queda», según lo hecho en el alta; «Aún no tienes reservas»; ventas extra listas. Debajo, el enlace «Así se verá tu Inicio con reservas». A él llegan «¡Todo listo!» y «Ahora no» de la bienvenida; quien ya tenía cuenta va al Inicio con reservas.
  - Las rutas de menú de Airbnb y Booking para el enlace del calendario están [POR COMPROBAR].

- **Oleada 3 aplicada (03/11, mismos enlaces; versión 21): confianza y cumplimiento.**
  - **Alta:** «Al continuar, con Google o con tu email, aceptas las Condiciones y la Política de privacidad». El boletín es opcional y va sin marcar.
  - **Teléfono:** dice para qué se usa («sin publicidad y sin cedérselo a nadie») y enlaza a Privacidad. El aviso del experto dice cómo se le contactará.
  - **Claves:** en el parte y en la API key se dice cómo se guardan («cifradas, solo para enviar tus partes, puedes borrarlas»).
  - **Selfie:** el huésped da su consentimiento antes de la selfie.
  - **Protección y ventas extra:**
    - vienen apagadas; se activan en un clic («Activar las dos» / «Activar las 4»), pero lo elige el cliente;
    - se dice quién cobra (Chekin, al huésped, en el check-in) y que el importe llega menos la comisión;
    - enlaces a «Comisiones» y a «Cómo se reclama un daño».
  - **¡Todo listo!:** identidad, tasa, protección y extras salen como activados o «no activadas», según lo elegido. Añade cuándo acaba la prueba (sin tarjeta y sin permanencia, aviso antes).
  - **Inicio de cuenta nueva:**
    - tarjeta «Tu prueba gratis»: días que quedan y plan después (39 €/mes, marcado como ejemplo);
    - ventas extra con su estado real y la comisión.
  - [POR COMPROBAR] con Producto y el DPO:
    - textos legales;
    - si la puerta única puede revelar que un email ya es cliente;
    - la base legal del teléfono;
    - el cifrado real de las claves;
    - el texto del consentimiento de la selfie;
    - la comisión de extras y protección;
    - el proceso de reclamación de daños;
    - qué pasa el día 15 y el precio real.
- **Ventas extra rehecho (03/11, versión 22), a petición de Alex.** Antes había 4 ofertas fijas y no se veía nada más.
  - **«Empecemos por lo básico»:** cuatro preguntas de sí o no:
    - ¿Dejas entrar antes de la hora?
    - ¿Y salir más tarde?
    - ¿Aceptas mascotas? Con precio por noche y mascota, o por estancia y mascota.
    - ¿Tienes aparcamiento? Con precio por noche o por reserva.
  - Con «Sí» aparecen el precio y cómo se cobra. Nada viene activado.
  - **«¿Quieres ganar más? Mira todos los extras»:** despliega el catálogo:
    - desayuno, cesta de bienvenida, traslado al aeropuerto, bicis, limpieza extra, cuna o trona, cambio de sábanas, excursiones;
    - y «Crea tu propia oferta».
  - **Vista previa en vivo:** «Así lo ve tu huésped» se rellena con lo activado. En portátil va fija a la derecha; en móvil, al final.
  - «¡Todo listo!» y el Inicio cuentan las ofertas activadas de verdad.
  - [POR COMPROBAR con Producto]: qué extras tiene hoy el catálogo de Chekin y cómo cobra cada uno; precios de ejemplo.
- **Explicaciones al día (03/11, versión 23).** Las 20 pantallas del panel «Por qué lo hacemos así» siguen ahora un mismo formato:
  - qué hace la pantalla y por qué;
  - «Dato:», con su fuente y periodo;
  - «Por comprobar:»;
  - «Pruébalo:», con el botón de demo.

  Se han corregido cuatro textos que contradecían el prototipo:
  - Protección: vienen apagadas.
  - Creando cuenta: botón a los 1,6 s y avance solo a los 4,6 s.
  - Inicio con reservas: «tus extras pagan Chekin».
  - Inicio de cuenta nueva: estado real de los extras.

- **Palabra según el negocio y tiempos (03/11, versión 24).**
  - Si elige hotel o camping en «Tu negocio», todo el alta y el Inicio dicen «propiedad/es» en vez de «vivienda/s». Es femenino, como vivienda, así que las frases no cambian de género.
  - Si vuelve a alquiler vacacional, vuelve a decir «viviendas».
  - Ventas extra pasa a 2 min, y el total, a unos 11 min.
- **Alta con NIF y móvil (03/11, versión 25), por decisión de Alex.** Antes de crear la cuenta se piden nombre, apellidos, NIF/NIE/CIF (con validación) y móvil (con prefijo y para qué se usa).
  - Con Google pasa por la misma ficha, con nombre y apellidos ya rellenos, y va directo a «Tu negocio» (sin código).
  - Nada se pide dos veces:
    - «Tu negocio» se queda en dos preguntas, sin teléfono;
    - el titular viene relleno con el nombre y el NIF del alta («Lo traemos de tu alta»).
  - Riesgo: hoy el 16 % de quien llega al alta crea la cuenta (126 de 772, 30 días) y dos campos más antes del valor pueden bajarlo. Medirlo en el A/B.
- **Contraseña, policías y titular (03/11, versión 26), por decisión de Alex.**
  - **Alta con email:** contraseña en vez de código (mínimo 8 caracteres, con letra y número, «Mostrar»). Quien ya es cliente entra con su contraseña, con «¿Has olvidado tu contraseña?» y error de demo. Con Google no hay contraseña.
  - **Dónde están:** primero solo países. Al marcar España sale «¿A qué policía envías el parte?»: SES.Hospedajes, Policía Nacional (nueva), Mossos d'Esquadra y Ertzaintza, con ayuda por comunidad. El parte de viajeros enseña solo las autoridades elegidas (también Ertzaintza y Alloggiati).
  - **Titular:**
    - arriba, el interruptor «El mismo titular para todas mis viviendas»;
    - debajo, el nombre y el NIF/CIF del alta ya rellenos.
  - [POR COMPROBAR con Producto]:
    - si el parte va hoy a la Policía Nacional directamente o por SES.Hospedajes;
    - si falta la Guardia Civil;
    - qué datos pide cada autoridad;
    - la regla de contraseña.
