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
