# Hallazgos (solo crece)

Cada descubrimiento con datos: **fecha · qué · fuente y periodo · qué implica · estado**. Lo más nuevo arriba.
Regla: toda cifra lleva su periodo (Carlos trabaja con 90 días). Si un dato no es fiable, se dice.

---

## 29-10-2026

### H-52 · Tramos por tamaño en HubSpot: SMB Micro, SMB, Mid-Market y Enterprise; con 3 viviendas, la mayoría está marcada como SMB, no como Micro
- **Qué:** `property_size` (contactos) tiene 4 valores: **SMB Micro** (`Micro SMB`), **SMB** (`Small Business`), **Mid-Market** y **Enterprise**. Alex los recuerda como **1-2, 3-10, 11-60 y más de 60**. Contactos creados desde el 1/08 con `number_of_units` = 3: **298 SMB frente a 104 SMB Micro**. Mid-Market con 11-60 unidades: 279. **Enterprise:** 312 con más de 60 unidades y 11 con 60 o menos; pero también hay **189 Mid-Market con más de 60**.
- **Fuente / periodo:** HubSpot, definición de la propiedad y búsquedas del 29/10/2026 (altas desde el 1/08/2026).
- **Implica:** el límite de Micro parece estar en **1-2**, no en 1-3 como se apuntó el 28/10 (p7-showme.md y borrador al CEO). Pero hay 104 de 3 viviendas marcados como Micro: o la regla ha cambiado o depende de otra cosa (país, habitaciones). Enterprise ≈ más de 60, aunque el límite Mid-Market/Enterprise tampoco es limpio (¿habitaciones de hotel frente a viviendas?). [POR COMPROBAR la regla exacta en el workflow que pone `property_size`.] Importa para ShowMe (quién entra) y para el onboarding nuevo (los botones de «¿cuántas propiedades?»).
- **Estado:** abierto.

### H-51 · PostHog no está en chekin.com; sin los clientes que buscan el login, en móvil conecta el PMS menos de 1 de cada 100; y casi todo lo que llega desde paid viene de las páginas de gracias
- **Qué:** 1) PostHog solo recibe páginas vistas de `dashboard.chekin.com` (y del entorno de pruebas): **ninguna de chekin.com**. El formulario web y el alta del dashboard no se pueden unir persona a persona. 2) Quitando las sesiones que pulsan «Iniciar sesión» (14 en móvil, 64 en ordenador): móvil 236 llegan → 103 escriben → 16 eligen PMS → **2 pulsan conectar (0,8%)**; ordenador 186 → 45 → 17 → **14 (7,5%)**. 3) De las ~46 sesiones de la muestra que pasan por landing.chekin.com, casi todas son de móvil y la mayoría llega desde **thank-you-page** (ES 18, PT 2, IT 1, DE 1): son leads que ya dejaron sus datos en el formulario de la landing y después rellenan otro formulario largo. Desde páginas de producto, pocas (PT check-in-online 9; SES 2+2).
- **Fuente / periodo:** PostHog (páginas vistas, últimos 30 días a 29/10/2026); Clarity, 500 grabaciones (móvil del 16 al 29/10, ordenador del 20 al 29/10).
- **Implica:** el lead de paid rellena **dos formularios**: el de la landing y el de alta. Con «dejar entrar al usuario», el de la página de gracias debería llevar directo al alta con Google o email, con los datos ya rellenos. Para unir web y producto en un funnel: instalar PostHog en chekin.com o pasar un identificador del formulario al dashboard [pendiente, decisión 29/10: los eventos por paso quedan para más adelante].
- **Estado:** abierto. Está en el dashboard del funnel (sección «Alta y onboarding»).

### H-53 · La PMax ES Vacational cayó de ~900 a ~65 clics al día desde el 20/10, con el mismo gasto
- **Qué:** campaña SB_ES_GOOGLE_PMAX_VACATIONAL_CHEKIN. Del 13 al 19/10: 610–969 clics/día, ~190–207 €/día, CPC ~0,2 €, 12–20 conversiones/día. Desde el 20/10 (21–28/10): 37–91 clics/día (media ~67), ~160–355 €/día, CPC ~3 €, 0–7 conversiones/día. Los clics a /es/check-in-online-ses-hospedajes siguen siendo casi todos de esta campaña (11.029 de 11.287 en 30 días).
- **Fuente / periodo:** Windsor.ai (Google Ads 103-962-2294), 29/09–28/10/2026.
- **Implica:** algo cambió en la campaña el 20/10 (puja, objetivo, inventario o exclusiones) [POR COMPROBAR con Carlos/Snowball]. Los clics baratos de antes podían ser de baja calidad, así que menos clics no es necesariamente peor; hay que mirarlo por leads y SQL. Para el A/B: ~65 clics/día → ~30 visitas por variante al día, así que el test tardará bastante más de lo que daban los números de antes del 20/10.
- **Estado:** abierto. Preguntar qué se cambió el 20/10.

### H-54 · Los formularios de las A de Italia y de ES hoteles piden solo el email; el de Portugal sale con prefijo de España
- **Qué:** en las A en vivo, /it/check-in-online-alloggiati-web y /it/ads/registrazione-ospiti-questura usan el formulario 5ef250b9 («Contattaci», 1 campo: e-mail) y /chekin-hoteles usa c7e8d490 («Contacta con nosotros», 1 campo: correo). No son los 5 campos del traspaso. Las dos A de Portugal (formulario 23a6aa7a) piden 5 campos, pero el teléfono sale por defecto con «Spain +34».
- **Fuente / periodo:** carga de las páginas en vivo en landing.chekin.com y de los formularios embebidos, 29/10/2026.
- **Implica:** las A se dejan como están y las B llevan las mejoras: formulario de 5 campos (ES e42c7acf, IT ca54cc24, PT 23a6aa7a) y prefijo del país por defecto. El A/B mide el paquete completo (diseño + formulario), no cada cambio por separado.
- **Estado:** aplicado en las 6 B (29/10). Decisión de Alex.

## 28-10-2026

### H-50 · Formulario web de registro, paso a paso (Clarity, 500 grabaciones): en móvil solo 1 de cada 100 llega a conectar el PMS; desde las landings de paid la intención es mucho mayor
- **Qué:** 250 grabaciones de móvil (16–29/10) y 250 de ordenador (20–29/10) de `chekin.com/…/onboarding/register-form/`, con el paso más lejano que alcanza cada sesión según lo que pulsa:
  | Paso | Móvil | Ordenador |
  |---|---|---|
  | Llegan | 250 | 250 |
  | Escriben algo | 44% | 24% |
  | Escriben y pulsan Continuar | 25% | 13% |
  | Responden sí/no | 26% | 12% |
  | Llegan al tipo de propiedad | 16% | 8% |
  | Eligen PMS | 7% | 7% |
  | **Pulsan conectar el PMS** | **1%** (3) | **6%** (15) |
  - No hacen nada: 39% en móvil, 35% en ordenador. Banner de cookies que hay que cerrar: 22% en móvil. Pulsan «Continuar» 3 veces o más: 6% en móvil (casi 0 en ordenador).
  - **26% de las sesiones de ordenador pulsan «Iniciar sesión»**: clientes que ya tienen cuenta y caen en el formulario de alta (52 de los 64 llegan en directo). Ensucian la cifra de abandono.
  - **Por origen** (500 sesiones): desde **landing.chekin.com** (paid) escriben el 75% y llegan al PMS el 25%; en directo, el 23% y el 2%; newsletter llega al PMS el 27% (n = 15); utm `test-a` el 11% (n = 37).
- **Fuente / periodo:** Microsoft Clarity (conector MCP), proyecto `rqlc6g9qhu`, 500 grabaciones del 16 al 29/10/2026. El paso se deduce de los textos pulsados: es una aproximación, no un evento.
- **Implica:** en **móvil**, el paso de elegir PMS → conectar casi no funciona (18 → 3), y encaja con lo visto en las grabaciones. Muchos «abandonos» son clientes que buscan el login. Hay que separarlos (enlace claro a «Ya tengo cuenta») antes de medir conversión. Para P3, la gente que llega desde las landings es la más decidida: no hay que perderla en el formulario.
- **Estado:** abierto. Para medirlo bien: eventos de Clarity (o PostHog) en cada paso del formulario web, a pedir a quien lleve la web.

### H-49 · ShowMe (Pedro, 29/10): «converted» cuenta a todo lead que pasa por la secuencia, haya hablado o no con el agente; quién entra lo deciden nuestros workflows
- **Qué:** respuestas de Pedro a las 3 preguntas: 1) **quién entra lo deciden los workflows de HubSpot de Chekin**: al principio solo micro no asignados a ventas, y después se han ido sumando otros tamaños (pide confirmarlo con Carlos, sobre todo por país); 2) **«converted» no depende de haber hablado con el agente**: en Pre-Trial es quien empieza la prueba; en Trial, quien pasa a `lifecyclestage = customer` (cuando entra el MRR). Las conversaciones van en columnas aparte; 3) no tienen vídeos por país. Si hacemos altas de prueba, avisar antes con los emails.
- **Fuente / periodo:** Slack #showme_chekin, respuesta de Pedro Bernar, 29/10/2026.
- **Implica:** las cifras de conversión de ShowMe **no miden el efecto del agente**, solo el resultado de los leads que pasan por la secuencia. Refuerza leer el impacto con grupo comparable y pagos reales (H-43). En el borrador al CEO hay que corregir «solo entran los leads de 1 a 3 viviendas»: el criterio ha cambiado con el tiempo y se decide en nuestros workflows (revisar en HubSpot el workflow que pone `showme_pretrial`, «UPDATED Lead As…»).
- **Estado:** abierto. Confirmar con Carlos (vuelve el 3/11) o revisando los workflows. Avisar a Pedro antes de las altas de prueba.

### H-48 · Último mes de onboarding: de cada 10 que entran en el alta, menos de 2 crean la cuenta; la siguiente caída es elegir el PMS
- **Qué:** 771 personas entran en `dashboard.chekin.com/register` → **126 crean cuenta (16%)** → 112 bienvenida → **64 eligen PMS** → 29 paso de conectar → 21 PMS conectado → 29 configuración completada. En la variante rebuilt: 331 → 97 (29%), y solo 84 escriben email y 56 pulsan Google. legacy (205) no envía eventos. Captcha: 42 personas fallan (1.364 veces); de las 13 que lo fallan en el alta, 12 no crean cuenta.
- **Fuente / periodo:** PostHog, 29/09–29/10/2026 (eventos desde el 13/10). Consultas puntuales; detalle en `trabajo-en-curso/p1-onboarding.md`.
- **Implica:** la mayor pérdida está en la propia página de alta, antes del producto. Apoya la propuesta de Alex (alta mínima con Google o email), con los riesgos anotados: el teléfono para ShowMe y la clasificación para ventas.
- **Estado:** abierto. Llevar a Daniel con la propuesta.

### H-47 · Formulario de registro (Clarity): la mitad se va en menos de 10 s y el selector de «tipo» da clics muertos en 3 idiomas
- **Qué:** `chekin.com/…/onboarding/register-form/`: **167 sesiones** del 27 al 29/10 (PC 114, móvil 52, tablet 1). En una muestra de las **100 grabaciones** más recientes (26/10 18:00 – 29/10 09:35 UTC): 51 ES, 25 IT, 16 EN, 6 PT, 2 DE; solo **38 de 100 escriben algo** en el formulario; **47 de 115** visitas a la página duran menos de 10 s (mediana 21 s). Hay **clics muertos en el desplegable «Selecciona el tipo / Seleziona il tipo / Select type»** en 5 sesiones distintas (ES, IT, EN). El banner de cookies aparece («Aceptar todo» pulsado 12 veces).
- **Fuente / periodo:** Microsoft Clarity (conector MCP), proyecto `rqlc6g9qhu`, 26–29/10/2026. Muestra de 100 sesiones, no el total.
- **Implica:** P1: hay pérdida **antes** del dashboard, en el propio formulario. El selector de tipo puede estar fallando (sobre todo en IT). Clarity no ve el paso al dashboard (otro dominio), así que el éxito del envío hay que cruzarlo con PostHog o HubSpot.
- **Ampliación 13–29/10 (Clarity, mismo proyecto):** **1.590 sesiones** en el formulario (PC 941, móvil 604, tablet 43, otro 2). Sesiones con clic muerto: ~19% en PC y en móvil (35% en tablet). Vuelta atrás rápida: 33% en PC, 23% en móvil. Scroll medio: 76–78%. Clics muertos más repetidos: **«Continuar» 356**, «Pasos para crear tu cuenta» 253, «No/no/yes» ~536, **«Selecciona el tipo» 132**, campos enmascarados ~600 y 2.732 sobre zonas sin texto. Smart events: solo 36 «SubmitForm» y 1 «SignUp» [POR COMPROBAR si Clarity detecta bien el envío en este formulario de varios pasos].
- **Implica (ampliación):** el botón **«Continuar» no responde** muchas veces. Lo más probable es una validación que no enseña el error, o el botón desactivado sin aviso [POR COMPROBAR viendo grabaciones]. Junto con el selector de tipo, es un arreglo rápido que no depende del onboarding nuevo.
- **Grabación vista por Alex (29/10, my2m9b/vw1cko, móvil):** el formulario sale **cortado** y para rellenarlo hay que **desplazarse mucho**. En palabras de Alex: «una locura, muy difícil de hacer». Una grabación, no una medida: hay que confirmarlo con más sesiones de móvil.
- **Segunda grabación vista por Alex (29/10, 5tmo9d/g2usdj, 13 min):** intenta **conectar el PMS** y **se queda trabado, no avanza**. El clic muerto cae en «Atrás · Conecta con tu…», o sea que el paso de conectar el PMS también aparece en este flujo [POR COMPROBAR si es el formulario web o el dashboard]. Encaja con la caída del PMS en PostHog (H-48: de 64 que eligen PMS, 21 lo conectan).
- **Tercera grabación vista por Alex (29/10, 3qs4c5/kxzwbv):** lo completa bien, pero **tarda unos 2 minutos solo en entrar**. Aunque todo funcione, el alta es larga.
- **Lectura de las 3 grabaciones:** en móvil se corta y cuesta rellenarlo; la conexión del PMS se traba; y cuando todo va bien, entrar lleva ~2 min. Respalda el alta mínima (Google o email → panel) y los arreglos rápidos del formulario actual.
- **Cuarta grabación vista por Alex (29/10, 1tmlugv/1nj6qv8, PT):** al pulsar «Seguir» sale un **error de «el teléfono (móvil) ya existe»** y no puede continuar. El formulario bloquea el alta si el número ya está registrado. Puede ser alguien que ya tenía cuenta o un número compartido (gestor con varias cuentas, mismo teléfono en dos altas) [POR COMPROBAR cuántas veces sale este error]. El aviso no le ofrece entrar ni recuperar la cuenta.
- **Segunda grabación (PMS):** el PMS era **Smoobu** («Conectar con Smoobu» → «Inicia sesión»). En otra sesión, una persona alemana lo intenta dos veces con Smoobu (1adyp6k). La conexión del PMS está en el propio formulario web (Select PMS → Connect with…).
- **Estado:** listo para llevar a Daniel. Falta saber qué PMS se trababa en la segunda grabación.

### H-46 · Clarity sí graba el formulario de registro: está en chekin.com/onboarding/, no en el dashboard
- **Qué:** Alex tiene acceso al proyecto de Clarity «Chekin», que cubre **chekin.com**. Export «Páginas principales» filtrado por *sitio de referencia* = `dashboard.chekin.com`: **375 sesiones** en `/onboarding/login/` (ES 215, EN 70, IT 62, DE 15, PT 13), **29** en `/onboarding/register-form/` (IT 13, ES 11, EN 5), **16** en las páginas del programa de referidos (EN, IT y ES, 5–6 cada una) y 12 en una landing italiana de check-in de visu.
- **Fuente / periodo:** Microsoft Clarity, proyecto «Chekin», 27/10–29/10/2026 (el 29 incompleto: export a las 10:18). Solo sesiones que vienen del dashboard, no el tráfico total de esas páginas.
- **Implica:** corrige lo dicho el 29/10 en el chat: **el formulario de registro (`chekin.com/…/onboarding/register-form/`) ya se graba en Clarity**, así que para P1 se pueden ver grabaciones del alta sin tocar el producto. Los pasos de `dashboard.chekin.com/setup` siguen sin grabarse. Que haya tanto login con el dashboard como origen apunta a clientes que vuelven al login desde el producto (cierre o caducidad de sesión) [POR COMPROBAR]. Para P6: unas 16 visitas en 3 días del dashboard a las páginas de referidos.
- **Estado:** siguiente paso: en Clarity, filtrar por URL que contenga `/onboarding/register-form/`, **sin** el filtro de referencia, para ver sesiones totales, abandono, clics de rabia y grabaciones. [POR COMPROBAR si chekin.com pide consentimiento antes de cargar Clarity]

### H-45 · Cello: 10 clientes referidos desde junio, y solo ~12k usuarios tienen Cello activado (se esperaban ~150k)
- **Qué:** según Cello, desde el lanzamiento en junio de 2026 han pagado 10 clientes referidos, y octubre ha sido el mejor mes. Solo hay **~12.000** usuarios con Cello activado frente a los **~150.000** esperados. Hay recompensas atascadas en «pending» porque Cello no se arranca al iniciar sesión y las comprobaciones de fraude no se resuelven solas.
- **Fuente / periodo:** resumen de Cello a Valery por Slack tras la reunión del 29/10/2026. Periodo: junio–octubre 2026. Cifras de Cello, no comprobadas en HubSpot ni en Leopard.
- **Implica:** el programa llega a menos del 10% de la base que se esperaba. Antes de optimizar mensajes, hay que arreglar la activación y el arranque de Cello al iniciar sesión (Tecnología). Detalle en `trabajo-en-curso/p6-cello.md`.
- **Estado:** abierto. [POR COMPROBAR el MRR de los 10 referidos en Leopard]

### H-44 · En Portugal, ningún lead del Pre-Trial recibe la marca de trial de ShowMe al empezar la prueba
- **Qué:** aviso de Pedro (ShowMe, 29/10) con 4 casos. Comprobado en HubSpot: de los **246** contactos con `showme_pretrial_portugal = true`, **0** tienen `showme_trial_started_portugal`. Los **9** que empezaron trial desde el 1/09 (del 7 al 27/10) tienen `trial_starts_we = Yes` y siguen sin la marca, así que reciben mensajes de Pre-Trial. La marca sí aparece en **90** contactos de Portugal fuera del recovery, todos sin Pre-Trial: entran directos al trial. En España, **15 de 15** leads del Pre-Trial con trial desde el 15/10 tienen `showme_trial_started`. Los 4 casos **no son del recovery**: altas del 22 al 27/10, sin `showme_pt_recovery`.
- **Fuente / periodo:** HubSpot, búsqueda del 29/10/2026 (Pre-Trial PT de cualquier fecha; trials desde el 1/09).
- **Implica:** el paso Pre-Trial → Trial no está montado o excluye a los de Pre-Trial en Portugal: leads en trial reciben mensajes que no tocan (uno ya pregunta por la URL de Booking). Además, «con ShowMe» en Portugal (H-27, H-43) no incluye a ningún lead que pasara por el Pre-Trial. No se puede ver el workflow con el conector: hay que abrirlo en HubSpot. [POR COMPROBAR quién es el dueño del workflow]
- **Causa (29/10, revisado en HubSpot con Alex):** la marca la ponen los workflows «ShowMe PreTrial -> Trial» (España, id 1841002847) y «ShowMe PreTrial -> Trial (Italy)», los dos publicados. **No existe uno para Portugal.** Disparador del de España: Pre-Trial = True y (`trial_starts_we` = Yes **o** `trial_start_date` conocida); acción: `showme_trial_started` = true; re-enroll off.
- **Arreglado el 29/10 (09:35, Alex en HubSpot):** workflow nuevo «ShowMe PreTrial -> Trial (Portugal)» (id 1912225094), clonado del de Italia. Disparador: (`trial_starts_we` = Yes **o** `trial_start_date` conocida) **y** `showme_pretrial_portugal` = Yes; acción: `showme_trial_started_portugal` = true; re-enroll off. Activado **solo para los nuevos**. En Portugal las propiedades son desplegables (Yes/No), no casillas como en España e Italia.
- **Error al inscribir a los 9 (29/10, 09:48):** la acción del clon seguía escribiendo en `showme_trial_started_italia` aunque el editor mostraba `showme_trial_started_portugal`. Los 9 quedaron con la marca de **Italia** y sin la de Portugal. [POR COMPROBAR con Pedro si llegó a dispararse la secuencia de trial de Italia]
- **Corregido (29/10, ~10:00):** acción borrada y creada de nuevo con «ShowMe Trial Started Portugal» = Yes (workflow apagado durante el cambio). A los 9 se les quitó `showme_trial_started_italia` y se les puso `showme_trial_started_portugal` = true con el conector de HubSpot (con OK de Alex). Comprobado contacto a contacto.
- **Estado:** cerrado en HubSpot. Falta confirmar con Pedro que ninguno entró en la secuencia de trial de Italia (estuvieron marcados ~14 min).

### H-43 · Con pagos reales (Leopard), los trials que pasan por ShowMe no pagan más que los que no pasan; la señal de Italia desaparece
- **Qué:** Micro con trial, altas 1/08–30/09, que pagan según Leopard (`mrr_leopard_eur` > 0; mes cerrado = septiembre 2026):
  | | Con ShowMe | Sin ShowMe |
  |---|---|---|
  | España | 62 / 418 · **14,8%** | 11 / 55 · **20,0%** |
  | Italia (total) | 14 / 136 · 10,3% | 18 / 119 · 15,1% |
  | Italia, solo agosto | 5 / 16 · 31% | 16 / 96 · 16,7% |
  | Italia, solo septiembre | 9 / 120 · 7,5% | 2 / 23 · 8,7% |
- **Fuente / periodo:** HubSpot (propiedad `mrr_leopard_eur` que escribe la integración de Leopard, mes de septiembre), altas 1/08–30/09/2026.
- **Implica:** con pago real no hay ventaja de ShowMe en España (sale 5 puntos por debajo, con un grupo «sin» de 55) ni en Italia mes a mes (agosto con 16 casos, septiembre igual). El +11 de Italia de H-30 venía del lifecycle Customer inflado. Ojo: solo cuenta quien pagó en septiembre; los trials de finales de septiembre que pagan en octubre aún no salen (afecta a los dos grupos).
- **Estado:** cifra para la respuesta al CEO (30/10).

### H-42 · Informe ShowMe Micro v5 (Carlos, 27/10): pagos reales, cadencia y atribución; corrige la lectura de Italia de H-27 a H-30
- **Qué:**
  - **Pagos reales (Leopard):** 3.040 leads Micro en ShowMe (ES, IT, PT) → ShowMe declara 630 «converted»; **360 pagan de verdad**; MRR actual 2.898 €/mes (ARPA 8,68 €). De los 360 cierres, **156 sin AE (43%)**, 118 con AE antes del cierre, 21 el mismo día y 65 después.
  - **Italia, HubSpot inflado:** de 78 «Customer» en HubSpot, 28 nunca han pagado y 36 pagan (Leopard). Trial IT: 60 customers en HubSpot, 34 cierres reales. En España, 37 de 384 nunca han pagado.
  - **Con y sin conversación con Alex** (todos enrolados en ShowMe): ES Trial 34,2% vs 19,7%; ES Pretrial **18,2% vs 25,5%** (peor con conversación); IT Trial 35,1% vs 16,7%; IT Pretrial 11,6% vs 9,2%; PT 3,3% vs 2,3%. En España, 1.234 de 2.388 leads (52%) nunca hablaron con Alex.
  - **Atribución:** el «converted» del export de ShowMe incluye a los leads sin ninguna conversación (en ES, 279 de 593). Es decir, ShowMe cuenta como suyo cualquier lead enrolado que convierte.
  - **Cadencia (transcripts, 1.540 hilos con conversación):** Pretrial: primer contacto por **llamada** (66%), 1 llamada por lead (70%) y WhatsApp de seguimiento cada **~48 h** durante hasta ~5 días. Trial: empieza por **WhatsApp** (72%) o chat web (20%); mediana de 6 WhatsApp en 12 días y contacto 4 días distintos; llamada solo al 25%, ~7 días después del inicio. Llamadas de 9:00 a 20:00.
  - **Canal:** Pretrial ES convierte por teléfono (31,7%) y casi nada por WhatsApp (3,8%); en Italia Pretrial solo convierte el teléfono (30,6%).
  - **Peticiones de persona:** 189 en ES (convierten 34,9%), 49 en IT, 4 en PT; no hay handoff real (falta el workflow de Chekin).
  - **Errores del agente (clasificador):** bucles, información incorrecta y no escalar son los tres primeros en ES e IT. Muchos corregidos y verificados desde el 06–07/10.
  - **Oportunidades para AEs:** 519 leads con señales de compra (74 tier A).
- **Fuente / periodo:** informe «ShowMe Micro v5» (artifact de Carlos, carga del 27/10; conversaciones hasta el 26/10; ES desde 18/06, IT desde 28/08, PT desde 06/10), con export de ShowMe, HubSpot y Leopard. Cadencia calculada por Claude sobre `transcripts.json` del mismo informe.
- **Implica:** responde a gran parte del encargo del CEO. Mi comparación de Italia (H-27 a H-30) usaba lifecycle Customer de HubSpot, que en Italia está muy inflado: la «señal positiva» de Italia hay que rehacerla con pagos de Leopard antes de darla por buena. La diferencia con/sin conversación no es causal (quien habla más está más interesado), pero en Pretrial España hablar con Alex no mejora.
- **Estado:** para el informe del 30/10. Preguntas a Pedro reducidas a las que el informe no responde.

### H-41 · Auditoría de /pt/check-in-online (PMax PT Competitors): página corta y clara, pero el formulario es de otra marca
- **Qué:** medido el 28/10 (1512×780 y 375×812). Alto 3.658 px en portátil y 4.518 en móvil (mucho mejor que SIBA, H-40). Fallos: botón de enviar **naranja** («Contacte-nos», rgb 255,122,89) distinto del resto de botones azules («Experimentar grátis →»); en portátil queda justo en el borde de la pantalla y en móvil por debajo; prefijo por defecto **Spain +34**; etiquetas en español («Tipo de propiedade», «propiedades/quartos»); dos tipografías (Plus Jakarta Sans y Figtree); título de la pestaña «Guestapp Chekin»; «50+ integrações PMS» (oficial +200); «SEF/AIMA» (el SEF ya no existe, pero se mantiene porque la gente lo sigue buscando así; decisión de Alex, 28/10). Carga en 1,1 s, 370 KB.
- **Fuente / periodo:** revisión en navegador (Playwright + Chrome), 28/10/2026. Tráfico en H-39 (26.521 clics en 90 días, 5,5% de conversión en Google).
- **Implica:** es la landing con más tráfico de todas (ES, IT y PT). La estructura ya es buena; lo que falla es el formulario. Variante B: mismo texto, formulario propio con PT +351, botón azul único y cifras oficiales.
- **Estado:** variante B hecha (28/10).

### H-40 · Auditoría de /pt/check-in-online-siba: el mensaje funciona, pero en móvil el titular sale cortado y el formulario está a 961 px
- **Qué:** medido en navegador el 28/10 (1512×780 y 375×812). Portátil: botón de enviar a 852 px (fuera de la primera pantalla de 780), página de 8.941 px. Móvil: **titular y entradilla cortados por la derecha** (el H1 llega a 411 px en una pantalla de 375), formulario a 961 px y botón a 1.586 px, página de 16.081 px. Prefijo del teléfono por defecto **España +34** en una página de Portugal; etiquetas mezcladas («Tipo de propiedade», «propiedades/quartos»); banner de cookies en español e inglés que tapa media pantalla. 11 pares de botones «Teste grátis» / «Falar com um especialista» y 5 textos de CTA distintos (más «Contacte-nos», «Comece grátis», «Calcule a sua receita»). Oferta del formulario «Sem cartão de crédito. Ativação imediata.» distinta de la del resto («un experto contacta»). Dos tipografías (Figtree y Proxima Nova). Cifras fuera de la lista oficial: «+45 países» (oficial +20), «Mais de 50 integrações» (oficial +200 PMS), «+35 €» de extra (oficial +55 €), «99% de precisão», «−90%», «+1.260 €/mês». 439 KB, carga en 1,2–1,4 s.
- **Fuente / periodo:** revisión en navegador (Playwright + Chrome), 28/10/2026. Tráfico y conversión en H-39.
- **Implica:** la página ya recibe el 96–100% del tráfico de la PMax PT Vacational y el mensaje (SIBA, AIMA, coimas) encaja. Los fallos son de forma y de fricción, sobre todo en móvil: es el caso típico de A/B con una variante B que mantenga el texto y arregle la estructura.
- **Estado:** auditoría entregada a Alex. Portugal fuera del orden de P3 por ahora.

### H-39 · Portugal: las dos PMax mandan casi el 100% de los clics a su landing principal, desde antes de parar la expansión
- **Qué:** PT PMax Competitors → `/pt/check-in-online`: 26.521 de 26.536 clics (100%) en 90 días; 98% del 22 al 26/10 y 99% el 27–28/10. PT PMax Vacational → `/pt/check-in-online-siba`: 3.592 de 3.609 (100%); 93% del 22 al 26/10 y 96% el 27–28/10. Lo poco que se escapa va a chekin.com (verificação de identidade, legalidade). Conversión que cuenta Google en la landing principal: Competitors 5,5% (1.460,6) en 90 días y 6,7–7,2% en la última semana; Vacational 9,0% (324,3) en 90 días, pero 2,3–2,5% en la última semana.
- **Fuente / periodo:** Windsor.ai (Google Ads 103-962-2294), clics y conversiones por URL expandida, 30/07–28/10/2026 (hoy incompleto).
- **Implica:** en Portugal la expansión no repartía tráfico, así que cada PMax ya testea una sola página: es el modelo al que van ES e IT desde el 27/10. Cualquier A/B en Portugal tendría volumen (sobre todo Competitors). Ojo: la conversión de Vacational PT cae de 9,0% a ~2,4% en la última semana [POR COMPROBAR si es la acción de conversión o la landing].
- **Estado:** para Alex. Portugal no está en el orden de P3 (ES e IT primero).

### H-38 · La expansión de URL se paró el 27/10 en España y en Italia; y qué busca la gente en cada PMax
- **Qué:** % de clics a la landing principal por día: 26/10 → ES Vacational 82%, IT Vacational 71%, IT Competitors 57%, ES Competitors 50%. **27/10 → 91%, 100%, 100%, 100%**. 28/10 → 92%, 92%, 100%, 100% (hoy incompleto). Términos de búsqueda (solo la parte con término visible, 30 días): IT Competitors, «alloggiati web» (7,9%) y mucha búsqueda de contratos de alquiler y «vikey»; IT Vacational, «vikey» (3,7%), «alloggiati web polizia di stato» y contratos de affitto breve; ES Vacational, «partee», «ses hospedajes registro viajeros», «avaibook», «hoomvip» y plantillas; ES Competitors, «ses hospedajes registro viajeros», «cheking», «partee».
- **Fuente / periodo:** Windsor.ai (Google Ads 103-962-2294), clics por URL expandida 26–28/10/2026 (forzado el refresco); términos de búsqueda 29/09–28/10.
- **Implica:** la orden de Carlos se aplicó en las 4 PMax desde el 27/10. Las búsquedas son sobre todo de alquiler vacacional, de competidores (Partee, Vikey, Avaibook) y de cumplimiento (SES, Alloggiati); casi nada específico de hoteles, también en las campañas «Competitors».
- **Estado:** para Alex.

### H-37 · Qué % de cada PMax llega a su landing principal: en la última semana baja (la expansión seguía activa hasta el 27/10)
- **Qué:** clics que van a la URL final de cada PMax:
  | Campaña | Landing principal | 90 d | Últimos 6 d | Conversión de la landing |
  |---|---|---|---|---|
  | ES PMax Vacational | /es/check-in-online-ses-hospedajes | 98% (12.946 de 13.214) | 69% (291 de 421) | Google 4,1% (534 conv.); HubSpot 3,7% (535 form. / 14.622 clics, todas las campañas, 21 jul–18 oct) |
  | IT PMax Vacational | /it/check-in-online-alloggiati-web | 35% (800 de 2.294) | 60% (248 de 414) | Google 0 (form. como secundaria); HubSpot 3,4% (17 / 501, 21 jul–18 oct) |
  | IT PMax Competitors | /it/ads/registrazione-ospiti-questura | 66% (3.370 de 5.082) | 66% (76 de 116) | Google 0; «todas las conv.» 101,3 / 3.288 ≈ 3,1% (21 jul–18 oct) |
  | ES PMax Competitors | /chekin-hoteles | 34% (1.119 de 3.338) | 46% (30 de 65) | Google 0,3% (3,6 conv.); HubSpot 0,38% (6 / 1.559, 21 jul–18 oct) |
  El resto va sobre todo a la plantilla de contrato (ES e IT), plantillas SES y guest app.
- **Fuente / periodo:** Windsor.ai (Google Ads 103-962-2294), clics por URL expandida: 90 d = 30/07–27/10/2026; últimos 6 d = 22/10–27/10. Conversión HubSpot: Biblioteca de anuncios (H-15, H-17, H-18, H-21), 21 jul–18 oct.
- **Implica:** hasta el 27/10 la expansión seguía repartiendo tráfico (ES Vacational bajó del 98% al 69%). Cuando Snowball la pare, estas 4 landings recibirán casi todo el clic y el A/B en HubSpot tendrá más volumen. En IT y en questura, Google no ve el formulario como conversión principal: hay que cambiarlo antes del test.
- **Estado:** para Alex. Volver a medir la semana del 2/11, con la expansión parada.

### H-36 · La landing principal de cada campaña de Google (ES e IT): la PMax Vacational IT no va al contrato, va a /it/check-in-online-alloggiati-web
- **Qué:** URL final (grupo de recursos en PMax, anuncio en Search) de las campañas activas de ES e IT:
  | Campaña | URL final (landing principal) | Clics 7 d | Gasto 7 d | Boceto nuestro |
  |---|---|---|---|---|
  | ES PMax Vacational | /es/check-in-online-ses-hospedajes | 482 | 1.527 € | SES v2 |
  | ES Search Intención | /ses-hospedajes | 302 | 616 € | — (página distinta de la anterior) |
  | ES PMax Competitors | /chekin-hoteles | 71 | 202 € | Hoteles v6 |
  | ES Brand | /es/ads/chekin | 16 | 26 € | — |
  | IT PMax Vacational | /it/check-in-online-alloggiati-web | 453 | 600 € | — |
  | IT PMax Competitors | /it/ads/registrazione-ospiti-questura | 130 | 133 € | Hotel Italia Questura v4 |
  | IT Brand | /it/ads/chekin | 32 | 61 € | — |
- **Fuente / periodo:** Windsor.ai (Google Ads 103-962-2294), campañas ENABLED, 22/10–28/10/2026 (hoy incompleto).
- **Implica:** con la expansión de URL parada, guía SES, guest app, pack legal y contratto IT (/modello/contrattoaffittoturistico) eran URL de expansión y dejan de recibir tráfico de paid. Para el A/B en HubSpot (variante B de la URL principal) valen SES v2 y las dos de hoteles; faltan bocetos para /ses-hospedajes (ES Search) y /it/check-in-online-alloggiati-web (IT rental, 2.º en prioridad).
- **Estado:** para Alex. Confirmar con Snowball que la expansión ya está parada.

### H-35 · Google Ads, últimos 7 días: 4.535 € en las campañas activas de ES, IT y PT y 73 contactos nuevos en HubSpot
- **Qué:** campañas activas (ENABLED) de ES, IT y PT, Google Ads (Windsor) frente a contactos nuevos en HubSpot con fuente Paid Search, agrupados por `utm_campaign` de la URL de entrada:
  | Campaña | Gasto | Clics | Conv. Google (todas) | Contactos HubSpot |
  |---|---|---|---|---|
  | ES PMax Vacational | 1.611 € | 519 | 23 (41) | 13 |
  | ES Search Intención | 715 € | 348 | 5 (18) | 7 |
  | ES PMax Competitors | 233 € | 88 | 4 (12) | 5 [utm sin país: «PMAXCOMPETITORS»] |
  | ES Brand | 30 € | 18 | 0 (2) | 0 |
  | IT PMax Vacational | 692 € | 529 | 10 (16) | 8 |
  | IT PMax Competitors | 155 € | 150 | 4 (8,5) | 5 |
  | IT Brand | 68 € | 36 | 0 (0) | 2 |
  | PT PMax Competitors | 504 € | 531 | 36 (41) | 26 |
  | PT PMax Vacational | 420 € | 221 | 5 (8) | 5 |
  | PT Search Intención | 38 € | 24 | 2 (2) | 1 |
  | PT Brand | 68 € | 35 | 1 (2) | 1 |
  | **Total** | **4.535 €** | **2.499** | **90** | **73** |
  Pausadas durante la semana (DE, CZ, GB): 202 € y 8 contactos más.
- **Fuente / periodo:** Windsor.ai (Google Ads 103-962-2294) y HubSpot, 21/10–28/10/2026 (hoy incompleto). HubSpot = solo contactos **nuevos** con fuente original Paid Search; las UTM mezclan campañas (H-02), así que el reparto por campaña es aproximado.
- **Implica:** ES PMax Vacational es lo que más gasta (1.611 €) y trae 13 contactos (~124 € por contacto nuevo); ES Search Intención, 715 € por 7 (~102 €). PT PMax Competitors es lo más barato: 504 € por 26 (~19 €). Google cuenta más conversiones que contactos nuevos en HubSpot (90 frente a 73): parte serán contactos que ya existían.
- **Estado:** para Alex. Medir por página para el detalle de landings.

### H-34 · Leads de formularios de Meta, últimos 7 días: cuadran con Meta; en alquiler vacacional ES casi la mitad ya estaban en HubSpot
- **Qué:** leads de formulario de Meta del 21/10 al 28/10, Meta (Windsor, «On-Facebook Leads») frente a HubSpot (contactos nuevos con primera conversión «Facebook Lead Ads: …» + contactos que ya existían y convirtieron en ese formulario):
  | Campaña activa | Gasto | Meta | HubSpot nuevos | HubSpot ya existían |
  |---|---|---|---|---|
  | SB_ESP_META_HOTELES_FORM_CK | 1.311 € | 20 | 21 | [no mirado] |
  | SB_ESP_META_VACATION_FORM_CK | 852 € | 19 | 9 | 8 |
  | SB_ITA_META_HOTELES_FORM_CK | 1.040 € | 22 | 21 | [no mirado] |
  | SB_PT_META_HOTELES_FORM_CK | 666 € | 9 | 9 | [no mirado] |
  | SB_PT_META_VACATION_FORM_CK | 204 € | 10 | 10 | [no mirado] |
  Italia alquiler vacacional: la campaña vieja y la V2, pausadas; «V2 - Copia», activa pero con 0,28 € y 0 leads.
- **Fuente / periodo:** Windsor.ai (Meta Ads, cuenta Chekin) y HubSpot, 21/10–28/10/2026 (hoy incompleto).
- **Implica:** los formularios de Meta entran en HubSpot casi 1 a 1 (diferencias de 1–2, por zona horaria o duplicados). En alquiler vacacional de España, 8 de 17 leads eran contactos que ya estaban en HubSpot (algunos desde 2022): Meta los cuenta como leads nuevos, pero no lo son. Italia no tiene ahora campaña de Meta de alquiler vacacional funcionando.
- **Estado:** compartir con Alex. Mirar los «ya existían» del resto de campañas.

### H-33 · Los formularios de Meta sí entran solos en HubSpot (corrige H-31)
- **Qué:** **236** contactos creados del 28/09 al 27/10 con primera conversión «Facebook Lead Ads: …», y **15** el 27–28/10 (el último, el 28/10 a las 17:31 UTC). 297 contactos de Paid Social en el mismo periodo. Los de formulario de Meta llegan con primera conversión «Facebook Lead Ads: <nombre del formulario>» (p. ej. `SB_ESP_FORM_HOTELES-GUIA_LOGICA_CK`, `SB_ESP_FORM_VACATIONRENTAL`, `SB_PORTUGAL_FORMULARIO-GUIA-HOTELES_CK`, entrados el 27/10) y campaña en `hs_analytics_source_data_2` (`sb_esp_meta_hoteles_form_ck`…). Las propiedades `facebook_lead_id`, `meta_ad_id` y `lead_ad_prop0` no se usan.
- **Fuente / periodo:** HubSpot, creados 28/09–28/10/2026.
- **Implica:** confirma lo que dice Valery: la sincronización de lead ads está activa a nivel de página y los formularios nuevos entran sin conectarlos uno a uno. H-31 estaba mal en ese punto.
- **Estado:** para responder en el hilo de Snowball (Mateo, Valery).

### H-32 · HubSpot sí envía automáticamente las fases del ciclo de vida como conversión a Google Ads y a Meta
- **Qué:** en HubSpot › Anuncios › Eventos hay eventos activos, disparados por fase del ciclo de vida, todos con último envío el 28/10/2026:
  - **Google Ads (Chekin):** Lead 40 · MQL 42 · SQL 7 · Opportunity 5 · Customer 108. Subscriber, apagado (último envío 5/02/2026).
  - **Meta (Chekin):** Lead 40 · MQL 461 · SQL 8 · Opportunity 5 · Customer 121 · Nurturing 153 (la lista sigue más abajo).
  Las cifras son la columna numérica de la tabla [POR COMPROBAR qué mide: probablemente eventos enviados en un periodo].
- **Fuente / periodo:** captura de HubSpot de Alex, 28/10/2026, 14:20.
- **Implica:** la respuesta a Snowball es «sí»: cada cambio de fase se manda solo a las dos plataformas. A Google le llegan muchos menos MQL que a Meta (42 frente a 461), seguramente porque Google solo puede atribuir contactos con clic de Google (gclid). Para «optimizar con SQL» (decisión del 27/10), el evento de SQL ya existe en Google, pero con muy poco volumen (7) para que una PMax optimice con él.
- **Estado:** para responder a Snowball. Ver qué mide la columna numérica y el resto de la lista de Meta.

### H-31 · HubSpot guarda el clic de Google (gclid) pero no recibe leads de formularios de Meta por integración
- **Qué:** contactos creados en los últimos 30 días con: `hs_google_click_id` (gclid) **1.314**; `hs_facebook_click_id` (fbclid) 85; `facebook_lead_id`, `meta_ad_id` y propiedades de lead ads (`lead_ad_prop0`) **0**.
- **Fuente / periodo:** HubSpot, búsqueda por propiedades, creados 28/09–28/10/2026.
- **Implica:** la conexión HubSpot ↔ Google Ads está activa al menos para guardar el clic (necesario para enviar conversiones offline). Los leads de los formularios de Meta no entran por la integración nativa de lead ads (o entran por otra vía sin esas propiedades). Por la API no se ve si HubSpot **envía** conversiones o audiencias a Meta y Google: hay que mirarlo en HubSpot › Marketing › Anuncios › Configuración (eventos de conversión y audiencias).
- **Estado:** ⚠️ **Corregido por H-33 (28/10):** los leads de Meta sí entran por la integración nativa; esas propiedades simplemente no se rellenan.

### H-30 · Con referencia 1/08 (agosto y septiembre completos), España sale peor con ShowMe; Italia, +11 puntos
- **Qué:** referencia pedida el 28/10: ShowMe desde el 1/08. Micro con trial, altas 1/08–30/09 (cohortes cerradas). % = clientes (lifecycle) / trials.
  | País | Con ShowMe | Sin ShowMe | Pasan por ShowMe | Mar–may (sin ShowMe) |
  |---|---|---|---|---|
  | España | 99 / 418 · **23,7%** | 15 / 55 · **27,3%** | 88% | 301 / 862 · 34,9% |
  | Italia | 37 / 136 · **27,2%** | 19 / 119 · **16,0%** | 53% | 80 / 354 · 22,6% |
- **Fuente / periodo:** HubSpot, suma de los cortes mensuales de H-27 (agosto + septiembre 2026). Cliente = lifecycle Customer (no Leopard). Portugal fuera (la marca incluye el recovery).
- **Implica:** el resultado no cambia de sentido: en España no hay mejora (−3,6 puntos, con solo 55 trials sin ShowMe: ruido); en Italia, +11 puntos en el mismo periodo. España con ShowMe queda 11 puntos por debajo de su primavera.
- **Estado:** cifra para el CEO (30/10) con la referencia del 1/08. Falta Leopard y el coste de ShowMe.

### H-29 · Con cohortes ya cerradas (altas 1/07–30/09), ShowMe no mejora en España; en Italia sí; Portugal no se puede leer
- **Qué:** solo altas hasta el 30/09, para que todos hayan terminado el trial de 14 días y tenido margen de negociación (idea de Alex). Micro con trial; % = clientes (lifecycle) / trials.
  | País | Con ShowMe | Sin ShowMe | Total jul–sep | Mar–may (sin ShowMe) |
  |---|---|---|---|---|
  | España | 754 · **27,5%** | 122 · **26,2%** | 876 · 27,3% | 862 · 34,9% |
  | Italia | 138 · **26,8%** | 254 · **16,5%** | 392 · 20,2% | 354 · 22,6% |
  | Portugal | 52 · 1,9% | 61 · 21,3% | 113 · 12,4% | 37 · 24,3% |
- **Fuente / periodo:** HubSpot, búsqueda por propiedades; altas 1/07–30/09/2026 (ES e IT sumadas de los cortes mensuales de H-27) y 1/03–31/05/2026. Cliente = lifecycle Customer.
- **Implica:** España: +1,3 puntos con ShowMe, dentro del ruido, y por debajo de la primavera. Italia: +10 puntos dentro del mismo periodo (señal clara, n = 138), aunque el total de Italia no sube frente a la primavera. **Portugal no vale:** la marca `showme_trial_started_portugal` la llevan también los leads del recovery (enrolados a mano desde el 26/10, solo leads de 23/08–2/10 que no convirtieron), así que el grupo «con» está sesgado a no convertidos.
- **Estado:** cifra base para el CEO (30/10). Falta Leopard y la regla de entrada de ShowMe.

### H-28 · Antes y después de ShowMe: la conversión trial → cliente de Micro no sube; en España baja
- **Qué:** Micro con trial, por fecha de alta. % = clientes (lifecycle) / trials.
  | País | Mar–may (sin ShowMe) | Jul–sep (con ShowMe) | Jul–28/10 · con ShowMe | Jul–28/10 · sin ShowMe |
  |---|---|---|---|---|
  | España | 862 · **34,9%** | 876 · **27,3%** | 936 · 24,1% | 135 · 23,7% |
  | Italia | 354 · **22,6%** | 392 · **20,2%** | 214 · 24,8% | 258 · 16,7% |
  | Portugal | 37 · 24,3% | — | 84 · 2,4% | 80 · 16,3% |
  En mar–may solo 18 trials de España tienen la marca de ShowMe (piloto o pruebas). En España, ShowMe coge el 87% de los trials del 1/07 al 28/10.
- **Fuente / periodo:** HubSpot, búsqueda por propiedades; altas 1/03–31/05 y 1/07–28/10/2026. Cliente = lifecycle Customer (no Leopard). La importación de Holidu de marzo (H-23) no aparece en estos números (862 trials en ES, no decenas de miles).
- **Implica:** con ShowMe cubriendo casi todo, la conversión no mejora frente a la primavera sin ShowMe: en España baja 7,6 puntos (34,9% → 27,3%) y en Italia 2,4. Del 1/07 a hoy, en España los dos grupos convierten igual (24,1% vs 23,7%). Factores que pueden tapar un efecto de ShowMe: estacionalidad (primavera = antes de temporada), cambios en el mix de campañas, y que jul–oct tiene menos tiempo para convertir (octubre, casi nada). Aun así, **no hay señal de que ShowMe suba la conversión en España**; en Italia, la única señal positiva es la comparación dentro del mismo periodo (24,8% vs 16,7%).
- **Estado:** para el CEO (30/10). Pendiente: cruce con Leopard, regla de entrada de ShowMe (Pedro) y propuesta de grupo de control aleatorio.

### H-27 · Por país, la ventaja de ShowMe desaparece en España; en Italia hay señal positiva con muestras pequeñas
- **Qué:** mismo grupo que H-26 (Micro con trial, creados 1/06–19/10), separado por país (`country_dropdown`; España incluye Canarias) y con la marca de trial de cada mercado (`showme_trial_started`, `_italia`, `_portugal`). % = clientes (lifecycle) / trials.
  | País | Con ShowMe | Sin ShowMe |
  |---|---|---|
  | España | 1.070 trials · 281 clientes · **26,3%** | 312 · 93 · **29,8%** |
  | Italia | 202 · 51 · **25,2%** | 385 · 72 · **18,7%** |
  | Portugal | 80 · 2 · 2,5% | 91 · 19 · 20,9% |
  | Otros países | — | ~1.190 trials sin ShowMe |
  Por mes de alta:
  | Mes | ES con | ES sin | IT con | IT sin |
  |---|---|---|---|---|
  | Jun | 158 · 35,4% | 178 · 34,3% | — | 265 (jun–jul) · 19,6% |
  | Jul | 336 · 32,1% | 67 · 25,4% | 2 · 0% | (en jun–jul) |
  | Ago | 213 · 29,1% | 32 · 28,1% | 16 · 31,3% | 96 · 15,6% |
  | Sep | 205 · 18,0% | 23 · 26,1% | 120 · 26,7% | 23 · 17,4% |
  | Oct (1–19) | 158 · 11,4% | 12 · 0% | 64 · 21,9% | 3 · 33% |
- **Fuente / periodo:** HubSpot, búsqueda por propiedades, creados 1/06–19/10/2026. Cliente = lifecycle Customer (no Leopard). Sep y oct están verdes (trial de 14 días + pago).
- **Implica:** el 27,7% vs 15,9% de H-26 es sobre todo **mezcla de países**: ShowMe está en España, donde se convierte más, y el grupo «sin» está lleno de otros países. **En España no hay mejora**: en junio, el único mes con dos grupos parecidos (158 vs 178), 35,4% frente a 34,3%; desde julio ShowMe coge al 85–93% y apenas queda grupo de control. **En Italia sí hay señal** (ago–sep: 27–31% con ShowMe frente a 16–20% sin o antes), pero con grupos pequeños. Portugal: arranque reciente, sin conclusión.
- **Estado:** para el CEO (encargo del 30/10). Falta: regla de entrada de ShowMe (Pedro), cruce con Leopard y, si se quiere medir de verdad, un grupo de control aleatorio (p. ej. 20% de Micro ES sin ShowMe durante 4 semanas).

### H-26 · 2 de cada 3 trials Micro no pasan por la fase trial de ShowMe; los que pasan convierten a cliente casi el doble (sin control de sesgo)
- **Qué:** contactos Micro (`property_size` = SMB Micro) creados del 1/06 al 19/10, con fecha de inicio de trial:
  | Grupo | Trials | Clientes (lifecycle) | % a cliente |
  |---|---|---|---|
  | Con `showme_trial_started` | 1.103 | 306 | 27,7% |
  | Sin ShowMe en trial | 2.230 | 355 | 15,9% |
  | Total Micro con trial | 3.333 | 661 | 19,8% |
  Pretrial: 1.492 Micro con alguna marca `showme_pretrial*` (ES, IT o PT) de 8.250 creados (18%); 89 son clientes (6,0%).
- **Fuente / periodo:** HubSpot, búsqueda por propiedades, creados 1/06–19/10/2026. Cliente = lifecycle Customer (no Leopard).
- **Implica:** sí hay una división clara medible (punto 2 del encargo del CEO), y 2.230 trials Micro no pasan por ShowMe. Pero **no prueba que ShowMe cause la mejora**: hay que saber por qué unos entran y otros no (país, fecha de arranque por mercado, criterio de ShowMe, si marcan a quien ya está avanzado). Hasta entonces, no comparable como test.
- **Estado:** pendiente de cruzar por país y mes, de la regla de entrada de ShowMe (Pedro) y del cruce con Leopard para el pago real.

## 27-10-2026

### H-25 · El dashboard del funnel salía vacío: la conexión de PostHog apuntaba a otro proyecto
- **Qué:** 9 de las 10 fuentes del dashboard "Funnel de activación Chekin" fallaban. La conexión de PostHog tenía como proyecto activo "Chekin - Dashboard" (id 143407, sin ningún evento) en lugar de "Default project" (125487). Las consultas no fijan proyecto, así que usan el que esté activo. Al volver a 125487 (OK de Alex), cargan las tres de prueba: eventos, base de la app y Stripe. Además, la sincronización de Stripe en PostHog está **pausada**: la última buena es de hace 15 días (≈12/10).
- **Fuente / periodo:** registro de ejecuciones del dashboard (27/10, 09:36 UTC) y PostHog (proyecto activo modificado el 26/10 a las 17:26 UTC).
- **Implica:** el dashboard se vacía para cualquiera que tenga otro proyecto activo. Las cifras de Stripe (suscripciones de octubre, MRR, LTV) llevan unos 15 días de retraso [POR COMPROBAR quién la pausó y si es a propósito].
- **Estado:** resuelto en el dashboard (27/10, 10:18 UTC). Reconectar el conector de claude.ai no bastó: seguía abriendo el 143407. Ahora cada fuente de PostHog fija el proyecto 125487 antes de consultar, y cargan las 10. Pendiente: lo de Stripe.

## 26-10-2026

### H-24 · GA4 no sirve para unir visitas a la web con registros: ve menos gente entrando al registro de la que se da de alta
- **Qué:** según GA4 ("CheKin web (.com)"), a las páginas de registro del dashboard entran unas 170–210 personas al mes (ene–sep), pero en la app se dan de alta por su cuenta entre 574 y 1.027 al mes. GA4 ve, como mucho, 1 de cada 3–5 altas. Además, las dos propiedades de GA4 dan cifras muy distintas de la web: entre 21.000 y 35.000 frente a entre 58.000 y 72.000 usuarios al mes, y "Chekin.com GA4" casi no mide el dashboard en enero y abril.
- **Fuente / periodo:** GA4 vía Windsor y base de la app en PostHog, 01/01 – 25/10/2026.
- **Implica:** "visitas a la web (GA4) → registro" quedaría mal medido: el paso de entrada al registro está infracontado (cookies, bloqueadores) y no se pueden mezclar fuentes. Sirve para tendencias de la web, no para tasas de conversión.
- **Estado:** para medir web → registro bien, PostHog en chekin.com (con OK del DPO) o eventos de registro en GA4 con consentimiento. [POR COMPROBAR cuál de las dos propiedades de GA4 es la oficial].

### H-23 · El pico de marzo son tres cargas masivas de cuentas de Holidu con prueba de 14 días, no clientes nuevos
- **Qué:** 3 días concentran 64.909 altas: 9/03 (15.034), 17/03 (42.592) y 10/04 (7.283), casi todas de Holidu (99,6%). Ese mismo día Stripe crea el mismo número de suscripciones (15.052, 42.618 y 7.294), y el 99,8% termina en menos de un mes (mediana: 14 días, la duración de una prueba). Siguen activas 44.
- **Fuente / periodo:** base de la app (person_users) y Stripe (suscripciones) en PostHog, 01/03 – 30/04/2026.
- **Implica:** es una importación de anfitriones de Holidu con prueba gratuita automática que caducó, no captación. Hay que excluirla de cualquier métrica de altas, conversión o churn de 2026 (también infla las bajas de marzo y abril en Stripe).
- **Estado:** el dashboard ya quita marzo por defecto; abril (10/04) se quita con el origen "Todos sin la importación de Holidu". [POR COMPROBAR con Carlos o Daniel: acuerdo con Holidu detrás de la carga].

### H-22 · PostHog mide sobre todo a los huéspedes; el dashboard de anfitriones, solo desde octubre
- **Qué:** en 2026, la app de huéspedes envía eventos a PostHog desde marzo (entre 1,7 y 8,6 millones de eventos al mes) y también lo hacen los portales de huéspedes, las webs de clientes y PMS y el servidor. El **dashboard de anfitriones** (dashboard.chekin.com, donde está el registro y el onboarding) **solo envía eventos desde octubre** (58.624 eventos de 9.253 personas, del 1 al 26/10). La web chekin.com no está en PostHog.
- **Fuente / periodo:** PostHog, eventos por web y mes, 01/01 – 26/10/2026.
- **Implica:** el hueco "desde septiembre sin datos" es solo del lado del anfitrión: hasta el 04/09 venía de la copia de la base de la app (rota) y los eventos del dashboard no existían. Antes de octubre, PostHog no ha medido nunca el onboarding de anfitriones.
- **Estado:** para Daniel: arreglar la copia de la base y añadir eventos de vivienda y reserva.

### H-21 · PMax Vacational IT: la landing alloggiati sí saca formularios (17), y el 98% de los clics por título va a títulos de «contrato»
- **Qué:** en la Biblioteca de anuncios, la PMax Vacational IT tiene 1.676 clics, 52 formularios (3,1%) y 2.284 €. Por página: plantilla de contrato, 1.084 clics y **34 formularios (3,1%)**; `/it/check-in-online-alloggiati-web`, 501 clics y **17 formularios (3,4%)**. Google Ads cuenta 0 conversiones en alloggiati, pero sí convierte, incluso un poco mejor que la plantilla. Es la confirmación de H-18 (formulario como conversión secundaria). Los títulos «Modello Contratto Affitti Brevi» (1.814 clics, 2.777 €) y «Contratto Affitto Turistico» (472 clics) se llevan casi todos los clics de títulos de la campaña (2.286 de 2.330) y mandan todos a la plantilla. En HubSpot: 52 MQL (36 de alquiler vacacional, 5 de hoteles) → 4 SQL → 1 deal → 1 cliente; 5 trials.
- **Fuente / periodo:** artifact «Biblioteca de anuncios» (data.json, extraído el 19/10): Google Ads y GA4, 21 jul – 18 oct 2026 (90 días); formularios por página y embudo de HubSpot por MQL en el mismo periodo. Las cargas de GA4 (762 de 1.676 clics, 45%) no son comparables entre campañas: van del 3% al 96%, así que no se usan para sacar conclusiones.
- **Implica:** el boceto «IT resto» (affitti brevi) tiene que recoger a quien busca el contrato, porque es lo que trae el tráfico. Si alloggiati pasa a conversión principal, la PMax dejaría de esquivarla. Calidad baja: 4 SQL de 52 MQL (7,7%), frente a los 105 Qualified MQL de Italia del plan de noviembre (H-19).
- **Estado:** para revisar con el boceto IT resto (26/10). Copiado en la ficha P3 de Notion (26/10, con OK de Alex).

### H-20 · Chekin Connect: 3 de los 5 eventos terminados no tienen ningún lead, y parte de los leads son pruebas internas
- **Qué:** de los 5 eventos terminados entre el 21 y el 25/10, **3 tienen 0 leads** (Tu Alquiler Asturias, Cloudbeds PT, Avvapro Sevilla). Los otros 2 suman 5 leads: The TOPO Connect, 4 (Marta); Scale Fest, 1 (Pablo). Entre los contactos de The TOPO Connect están el email de la propia Marta y el de Carlos, así que es probable que algunos sean pruebas. Ninguno de los 5 estaba en HubSpot hasta el reenvío del 26/10 (ahora 5 de 5, sin errores).
- **Fuente / periodo:** Supabase de Chekin Connect (tablas `events` y `leads`), eventos terminados del 21 al 25/10/2026. HubSpot, comprobado el 26/10.
- **Implica:** con estos datos no se puede medir lo que aportan los eventos. O los AEs no usan el QR, o no están asignados al evento en el panel [POR COMPROBAR con los AEs]. Hay que separar las pruebas de los leads reales antes de sacar conclusiones.
- **Estado:** tareas por evento creadas en Asana (Growth Daily › Alexandre). Confirmado por Alex (26/10): 2 de los 4 de The TOPO Connect eran pruebas; leads reales: 2 + 1 (Scale Fest). Falta preguntar a los AEs por los 3 eventos con 0 leads.

### H-19 · Plan de noviembre de Snowball frente a las landings de Italia: Google es ~30% del presupuesto IT, no hay campaña de hoteles en Google y Search Intención IT no está en el plan
- **Qué:** el plan de noviembre de Snowball, preparado por Carlos, fija para Italia (paid) un mínimo de **105 Qualified MQL y 50 SQL**. Hoy llega a Qualified el **10,9%** de los MQL de Italia (jul–sep), así que harían falta **960 formularios** con la calidad actual. Google IT recibe **4.350 €** en noviembre: PMax Vacational 3.000 € (100 €/día), PMax Competitors 1.200 € (40 €/día) y Brand 150 €. El presupuesto de Italia es de ~14.250 € (Rental IT 9.750 € + Hoteles IT 4.500 €); el resto es Meta, fuera de P3. Snowball espera **0,7 Qualified** de PMax Vacational, con un coste histórico de 2.645 €/Qualified y 529 €/SQL, y **1,5** de PMax Competitors (756 €/Qualified, 302 €/SQL). **Las dos PMax IT se clasifican como *Rental IT*. No hay campaña de hoteles de Google en Italia:** los hoteles IT solo van por Meta (`SB_ITA_META_HOTELES_FORM_CK`). **`SB_IT_GOOGLE_SEARCH_INTENCION_CHEKIN` no aparece en el plan**, aunque fue la que mandó el 97,9% de su tráfico a questura y la única donde esa landing contó conversiones (H-17). El plan pide subir los Qualified MQL y SQL de HubSpot a Google y Meta como conversiones offline. Los €/día de partida no cuadran con el gasto real: el plan dice 94 €/día para Vacational, pero en 90 días gastó ~25 €/día (2.280 €).
- **Fuente / periodo:** «Snowball · Plan noviembre 2026.xlsx» (hojas 1–3; % Qualified jul–sep, costes históricos jun–oct según el propio plan). Comparado con Google Ads vía Windsor.ai, 21 jul – 18 oct (90 días), de H-18.
- **Implica:**
  1. El boceto «IT hoteles» va a recibir tráfico de alquiler vacacional. O se reorienta, o se pide a Snowball una campaña de hoteles en Google. Choca con la regla de P3 (público: hoteles y cadenas).
  2. La landing tiene que filtrar por tipo y tamaño de alojamiento (Micro no cuenta como Qualified), no solo captar más formularios.
  3. Para las conversiones offline, el formulario debe guardar el `gclid` en HubSpot [POR COMPROBAR]. Además, el formulario tiene que pasar a conversión principal (H-18).
  4. Preguntar a Snowball por Search Intención IT.
  5. Comprobar los €/día de partida con los últimos 30 días [POR COMPROBAR].
- **Estado:** para decidir con Carlos (26/10). Copiado en la ficha P3 de Notion (26/10, con OK de Alex).

### H-18 · Italia: el tráfico de las 4 campañas cae en 3 páginas, y la landing de hoteles sí convierte pero como conversión secundaria
- **Qué:** las 4 campañas IT apuntan a 17 URL distintas, pero 3 páginas se llevan el **94% de los 8.946 clics**: `/it/ads/registrazione-ospiti-questura` (5.383 clics), `/modello/contrattoaffittoturistico` (2.514) y `/it/check-in-online-alloggiati-web` (548). En cada campaña, una URL concentra entre el 65% y el 98% del tráfico (Search Intención 97,9%, Brand 98,1%). El resto son colas de 1–57 clics. **Nuevo frente a H-17:** en la PMax Competitors, la landing de questura tiene 0 conversiones pero **101,3 en «todas las conversiones»**. Lo mismo pasa con alloggiati en Vacational: 0 frente a 10. El formulario sí se registra, pero como acción secundaria, y la PMax no puja por ella. **Cruce con otros países:** Vacational IT manda 12 clics a páginas en inglés o de España (`/en/online-check-in`, `/ads/online-check-in-uk`, `/template/tenancycontractformat`, `/template/seshospedajesword`). Es el 0,7%, poco volumen. 6 de las 7 landings en italiano revisadas declaran `lang="en"` (solo alloggiati dice `it`). La de questura tiene el `<title>` de otra página: «Self Check-in de visu legale».
- **Fuente / periodo:** Google Ads vía Windsor.ai, 21 jul – 18 oct (90 días), por URL expandida, sin parámetros. Revisión con curl el 26/10.
- **Implica:** hay que rediseñar 3 páginas, no 21. Arreglar la acción de conversión (pasar el formulario a principal) es el cambio con más palanca y no toca el diseño. Cada +1 pp de conversión en los 3.288 clics de la PMax Competitors en questura serían ~33 formularios más en 90 días. El valor en MRR es [POR COMPROBAR: tasa lead→cliente y ticket en IT].
- **Estado:** resumen para Alex (26/10). Bocetos IT hoteles y resto ya cubren 2 de las 3 páginas. Decidir con Carlos la acción de conversión.

## 23-10-2026

### H-17 · Italia: Google Ads cuenta 0 conversiones en la landing de la PMax IT Competitors, pero en HubSpot entran contactos
- **Qué:** la PMax IT Competitors apunta a `landing.chekin.com/it/ads/registrazione-ospiti-questura`. En 90 días le llegaron **3.288 clics y 1.560 €, y Google Ads registra 0 conversiones**. En el mismo periodo, la plantilla de contrato `/modello/contrattoaffittoturistico` recibe 1.431 clics y 2.526 € de esa campaña y **sí cuenta 45 conversiones**. En HubSpot, **154 contactos** tienen esta landing como primera página desde el 21/07. La página sí tiene formulario en la primera pantalla («Contattaci», HubSpot, form `5ef250b9…`), declara `lang="en"` y usa cifras no oficiales: «50+ PMS», «4.8/5 Trustpilot», «87%», «100% conformità garantita», y testimonios de clientes de España.
- **Fuente / periodo:** Google Ads vía Windsor.ai, 21 jul – 18 oct (90 días), por URL expandida. HubSpot: contactos creados del 21/07 al 23/10, propiedad `hs_analytics_first_url` (primera página, no necesariamente la del formulario). Revisión en navegador el 23/10.
- **Matiz (mismo día):** en Italia hubo 4 campañas en esos 90 días, no 2. La de búsqueda `SB_IT_GOOGLE_SEARCH_INTENCION_CHEKIN` mandó 2.095 clics (3.928 €) a esta misma landing del 21/07 al 06/08, y ahí Google sí contó 6,7 conversiones. Después se paró: desde el 06/08 solo tiene clics sueltos. La cuarta, `SB_IT_GOOGLE_SEARCH_BRAND_CHEKIN`, sigue activa con poco volumen: 205 clics en 90 días, a `/it/ads/chekin`. Así que la conversión existe en la cuenta; lo que falla es que la PMax IT Competitors no la cuenta.
- **Implica:** lo más probable es que la PMax IT Competitors optimice hacia otro objetivo de conversión que no incluye este formulario [POR COMPROBAR en Ads: objetivos de conversión de la campaña]. La PMax no ve que la landing convierte y desvía el tráfico a la plantilla, que sí cuenta. Es el mismo mecanismo que H-08 en España. Arreglar la medición puede valer más que cambiar el diseño. Además, muchos contactos parecen alquiler vacacional, no hoteles [POR COMPROBAR el tipo de alojamiento en agregado].
- **Estado:** boceto de landing IT hoteles en curso (23/10). Para el lunes con Carlos: revisar las conversiones de la PMax IT en Google Ads.

### H-16 · /check-in-guestapp: la página donde más gasta Competitors ES sale en blanco en móvil
- **Qué:** 377 clics, 2.009 € y 10 formularios (2,7%) en 90 días: más gasto que /chekin-hoteles (1.916 €). En móvil (375×812), **el titular sigue con opacidad 0 a los 6 s** de cargar: solo se ve el botón fijo "Probar Chekin gratis". En portátil aparece tras 1–2 s, pero el botón "Enviar" queda cortado en el borde (iframe 279–807 px con pantalla de 780). Cifras no oficiales ("50+ integraciones", "★ 4.8", "hasta 1 hora por reserva", "cero riesgo de multas"), oferta "activación inmediata", `lang="en"`, 7.116 px (portátil) y 11.076 px (móvil). El tráfico llega por el anuncio automático "Guestapp Chekin" (408 clics, H-08).
- **Fuente / periodo:** Biblioteca de anuncios, 21 jul – 18 oct (90 días); revisión en navegador el 23/10 [POR COMPROBAR la pantalla en blanco en un móvil real: puede ser cosa del emulador].
- **Implica:** si se confirma, quien llega desde el móvil no ve nada: explicaría parte de la conversión baja con el gasto más alto.
- **Estado:** boceto v2 hecho (https://claude.ai/artifact/6H23uPLZEJyBSbnVNWhTPP) y en el brief para Carlos.

### H-15 · La guía y las 4 plantillas se llevan el 45% del gasto de la PMax Competitors ES, y ya tienen el formulario arriba
- **Qué:** guía SES, contrato de alquiler vacacional, plantilla SES Word, plantillas SES y modelo de factura suman **1.357 clics, 51 formularios (3,8%) y 4.704 €** de los 10.384 € de la campaña (45%). Las plantillas ya ponen el formulario al lado del titular (por eso convierten al 2,9–5,0% frente al 0,38% de /chekin-hoteles), pero el botón queda por debajo de la primera pantalla (contrato: 939 px en 1512×780), la página declara `lang="en"` y tiene 6 enlaces de salida. Las landings de plantillas **sí muestran banner de cookies** con opciones (esenciales, analíticas, marketing): matiza H-14.
- **Fuente / periodo:** Biblioteca de anuncios, 21 jul – 18 oct (90 días); revisión en navegador el 23/10.
- **Implica:** si se mantiene la expansión de URL, unificar estas cinco páginas en un pack es la mejora de más volumen. Calidad baja (plantillas: 2 SQL, 0 oportunidades desde el 21/07).
- **Estado:** boceto del pack legal hecho (https://claude.ai/artifact/P8tf8sdAtaTqAXr8f7iZAj) y en el brief para Carlos. Depende de la decisión del lunes sobre la expansión.

### H-14 · Las landings ya tienen Microsoft Clarity (dos proyectos), y el alta del dashboard no tiene banner de cookies
- **Qué:** en `landing.chekin.com/chekin-hoteles` se cargan dos etiquetas de Clarity por Google Tag Manager (`GTM-PK7Q9R9`), con los proyectos `rrl7tp5b6k` y `rqlc6g9qhu`. Es decir, **puede que ya haya grabaciones y mapas de calor de las landings de paid**. Además cargan GA4, dos cuentas de Google Ads, Meta, Reddit, Amplitude y HubSpot. La página tiene un script de banner de cookies de HubSpot, pero en el navegador del panel no se mostró [POR COMPROBAR en una ventana privada]. En `dashboard.chekin.com/register` no aparece ningún banner de cookies.
- **Fuente / periodo:** revisión en navegador, 23/10/2026.
- **Implica:** para P3 no hace falta instalar nada: hay que pedir acceso a esos proyectos de Clarity (¿de Snowball o de Chekin?). Para grabar en el producto, primero hace falta un banner de consentimiento en el dashboard.
- **Estado:** preguntar a Carlos y a Snowball de quién son y pedir acceso. Consentimiento: DPO.
- **Actualización 27/10 (Slack):** en jun-2024 ya había una etiqueta de Clarity en GTM (Sergio Aguado lo pregunta en #mktg-team y Julia Pedrol responde que hay cuenta). El 05/06/2025 Gabriel Coachman avisa en #mktg-team de que ha invitado al equipo a Clarity y que lo sigue con Karina. Probablemente son los dos proyectos [POR COMPROBAR en el historial de versiones de GTM-PK7Q9R9].

### H-13 · En el alta y la configuración no se ve nada de lo que hace el cliente
- **Qué:** en `dashboard.chekin.com` (`/register*` y `/setup*`) no hay clics (`$autocapture`), clics de rabia, clics muertos, salidas de página ni errores desde el 13/10, y las grabaciones están desactivadas (`session_recording_opt_in: false`). Solo hay páginas vistas y los eventos a medida del onboarding.
- **Fuente / periodo:** PostHog, eventos del 13 al 23/10/2026.
- **Implica:** sabemos en qué paso se cae la gente (sobre todo al conectar el PMS), pero no por qué. Para P1 hacen falta grabaciones y clics en esas páginas.
- **Estado:** propuesta para Daniel: grabaciones solo en esas URL, campos enmascarados, más autocapture, clics de rabia y errores. Antes, OK del DPO y revisar el consentimiento de cookies.

### H-12 · Corrige H-11: PostHog no cuenta ni las altas con Google antes del 21/10 ni el alta antigua
- **Qué:** del 13 al 23/10 PostHog registra **61 altas nuevas**: 38 con email (`auth_registration_succeeded`) y 23 con Google (`auth_social_succeeded` con `created = true`, evento que solo existe desde el 21/10). Además, **96 personas** llegan a `/register/accommodation-type` (pantalla del alta antigua) sin ningún evento de alta ni variante.
- **Comprobado:** el otro proyecto de PostHog ("Chekin - Dashboard") no tiene eventos; ningún otro dominio tiene eventos de alta del dashboard antes del 13/10 (solo `dashboard-ng.chekintest.xyz`, pruebas); Google Analytics ve tráfico en `/register` y en `/register/accommodation-type` en las mismas fechas.
- **Fuente / periodo:** PostHog, eventos del 13 al 23/10/2026; GA4 vía Windsor, 13–22/10 y agosto de 2026.
- **Implica:** el 16% de H-11 no vale (contaba solo email y comparaba con agosto). Lo que sí se sostiene: PostHog cuenta solo una parte de las altas, y la parte que falta es sobre todo el alta antigua. [POR COMPROBAR con producto: si en `/register/accommodation-type` la cuenta ya está creada.]
- **Estado:** dashboard corregido (fila de octubre con email + Google y aviso del alta antigua). Estimación del 16% retirada.

### H-11 · PostHog solo ve una de cada seis altas propias (estimación)
- **Qué:** PostHog registra 38 personas con `auth_registration_succeeded` del 13 al 23/10 (≈3,5 al día). La base de la app tenía 686 altas propias (origen DASHBOARD) en agosto (≈22 al día). Si el ritmo de altas no ha caído, PostHog capta en torno al **16%** de las altas.
- **Fuente / periodo:** PostHog, eventos del 13 al 23/10/2026; base de la app sincronizada, altas de agosto de 2026. No hay ningún periodo en que las dos fuentes midan a la vez: es una estimación [POR COMPROBAR con la sincronización arreglada].
- **Implica:** el funnel de PostHog de octubre no es el de todas las altas, sino el de quien pasa por los flujos que envían eventos (rebuilt y beta). Legacy no envía el registro. Cualquier tasa de PostHog vale para comparar variantes, no para dar el total.
- **Estado:** ❌ corregido por H-12 (no contaba las altas con Google y la comparación con agosto no se sostiene). Retirado del dashboard.

### H-10 · PostHog no tiene nada del dashboard antes del 13/10: hay un hueco del 04/09 al 13/10 sin ninguna fuente
- **Qué:** en `dashboard.chekin.com` el primer evento de PostHog, incluida la página vista, es del **13/10/2026**: no hay histórico del alta en PostHog. Por eventos: `$pageview` y `auth_registration_succeeded` desde el 13/10, `pms_connect_succeeded` desde el 14/10, `onboarding_variant_assigned` desde el 14/10 y `onboarding_setup_completed` desde el 15/10. La base de la app sincronizada (Postgres) se para el 04/09.
- **Fuente / periodo:** PostHog, eventos de 2025-01-01 a 2026-10-23, host `dashboard.chekin.com`.
- **Implica:** el funnel mes a mes solo se puede montar con dos fuentes que no se tocan. De enero al 3 de septiembre: base de la app (alta → vivienda → reserva → huésped). Desde el 13/10: eventos de PostHog (registro → onboarding → PMS). **Del 04/09 al 12/10 no hay datos en ninguna**, y los pasos de una fuente no son los de la otra.
- **Estado:** para la reunión del lunes 26 con Daniel. Arreglo: sincronización de Postgres (ingeniería) y eventos de vivienda y reserva creadas en PostHog.

### H-09 · Coste de oportunidad del onboarding en ARR a 12 meses (alta propia 2026)
- **Qué:** valor de un cliente a 12 meses = 39,76 al mes × 12 × 78,5% de retención a un año = **374** (LTV de vida completa: 2.219). Con ese valor, las altas propias de 2026 sin marzo (5.694, de ene a 3 sep) dejan de aportar unos **580.000 de ARR a 12 meses**: 388.000 en el paso alta → vivienda (≈1.037 clientes), 94.000 en vivienda → reserva (≈252) y 98.000 en reserva → huésped (≈261).
- **Fuente / periodo:** Stripe (MRR y clientes a 12/10, retención de las suscripciones de 2024 que duraron más de 31 días) y base de la app en PostHog (altas del 01/01 al 03/09/2026 sin marzo, estado a 04/09). Moneda de Stripe [POR COMPROBAR].
- **Implica:** el paso que más ARR deja escapar es registrar la primera vivienda: 2 de cada 3 euros del coste. Es una cota alta: supone que quien se queda pagaría como quien sigue, y el campo de pago (`has_paid`) tiene rarezas (agosto) [POR COMPROBAR con Daniel].
- **Estado:** en el dashboard "Funnel de activación Chekin" con selector de horizonte (12 meses o vida completa).

## 22-10-2026

### H-08 · Por qué la PMax Vacational ES se queda en su landing y la Competitors no
- **Qué:** las dos PMax tienen textos de anuncio generados con los títulos de otras páginas (expansión de URL + textos automáticos). Google manda el clic a la página que más formularios saca. Vacational: su landing (página SES) convierte al 4,25% → no hay a dónde ir mejor (99,1% del tráfico se queda). Competitors: /chekin-hoteles convierte al 0,38% (carga 3,9 s, `lang="en"`, formulario al 93%) → Google desvía a plantillas (4–5%).
- **Dato fuerte:** el texto que más gasta en Competitors, "Plantilla SES Hospedajes" (título de la plantilla Word), = 1.066 clics y 4.636 €. Nadie lo escribió.
- **Fuente / periodo:** Biblioteca de anuncios (tabla por texto), 21 jul – 18 oct (90 días).
- **Implica:** el problema de Competitors es de configuración + landing débil, no solo de medición.
- **Estado:** [POR COMPROBAR en Google Ads] expansión y exclusiones, textos automáticos, objetivo de conversión, términos de búsqueda. Lunes 26 con Carlos.

### H-07 · La página SES es la landing de la PMax Vacational, no de Competitors
- **Qué:** /es/check-in-online-ses-hospedajes recibe 11.600 de los 11.707 clics de la PMax Vacational ES (99%). En la vista por landing suma 14.622 clics, 535 formularios (3,7%) de 4 campañas.
- **Fuente / periodo:** Biblioteca de anuncios, 90 días.
- **Implica:** los ~508 contactos "de Competitors" que entraban por la página SES en HubSpot eran casi seguro tráfico de Vacational mal etiquetado (UTM rotas).
- **Estado:** confirmado con la biblioteca (atribuye por ID de campaña de la URL).

### H-06 · Volumen frente a calidad: Vacational trae leads baratos, Competitors trae las ventas
| 90 días | Vacational ES | Competitors ES |
|---|---|---|
| Gasto | ~5.400 € | ~10.400 € |
| Formularios | 500 (~11 €/form) | 81 (~128 €/form) |
| SQL | 8 (1,6%) | 13 |
| Ganados | 0 | 4 |
- **Fuente / periodo:** Biblioteca de anuncios (funnel por campaña), 21 jul – 18 oct.
- **Implica:** mejorar la página SES sube volumen; para ventas, lo que importa es el tráfico de hoteles.

### H-05 · Reparto de clics por URL en todas las PMax (90 días)
| PMax | % a su landing configurada |
|---|---|
| PT Competitors, PT Vacational, GB Vacational, DE Vacational | 100% |
| ES Vacational | 99% |
| IT Competitors | 67% (29% a /modello/contrattoaffittoturistico) |
| ES Competitors | 41% (23 URLs) |
| IT Vacational | 30% (65% a /modello/contrattoaffittoturistico) |
- **Implica:** Italia atrae a gente que busca una plantilla de contrato; tenerlo en cuenta antes de las landings de IT.

### H-04 · 41% frente a 21%: no es un error, son periodos distintos
- **Qué:** % de clics de la PMax ES Competitors que llegan a /chekin-hoteles = 41% en 90 días (21 jul – 18 oct, export de Google Ads) y 21% en los últimos 30 (~190 clics, Windsor).
- **Implica:** el último mes llega menos tráfico a la landing de hoteles que la media → la expansión se lo está llevando cada vez más.

### H-03 · El test de /chekin-hoteles no sale en plazo
- **Qué:** con ~190 clics/mes a la landing (30 días), el A/B de 1.560–2.900 visitas por versión no sale.
- **Estado:** test **pausado** en el tracker con el motivo. Decidir con Carlos: acotar expansión / testear donde va el tráfico / landing por anuncio.

### H-02 · Las UTM de las PMax mezclan campañas
- **Qué:** 589 contactos con `utm_campaign = SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN`; /chekin-hoteles recibe 5 nombres de campaña distintos (incluido `{campaignname}`); las PMax Vacational ES/GB/DE casi no tienen contactos propios.
- **Fuente / periodo:** HubSpot, desde el 21 jul.
- **Implica:** MQL, SQL y coste por SQL por campaña en HubSpot **no son fiables**. Usar la biblioteca (ID de campaña) o medir por página.
- **Estado:** prioritario corregir la plantilla de seguimiento / sufijo de URL final de las PMax.

### H-01 · Fallos de las landings SES actuales
- **Página SES** (/es/check-in-online-ses-hospedajes): en móvil el título y el párrafo salen cortados; formulario fuera de la primera pantalla (móvil) y botón bajo el pliegue (portátil 14"); etiqueta sobre el título que no hace nada; dos CTA iguales al mismo sitio; 11 botones; 13.963 px en móvil; inputs a 15 px; "+50 integraciones" (oficial: +200 PMS).
- **Guía SES** (/es/guia/seshospedajes): formulario al final y de 7 campos; errata "en un proceso"; texto de 2024; enlaces de salida con UTM de otra campaña.
- **Fuente:** revisión en navegador a 1512×780 y 375×812.
- **Estado:** boceto v2 de la página SES hecho (`trabajo-en-curso/p3-landings/landing-ses-hospedajes-v2.html`); guía en espera. Detalle en `p3-landings/auditoria-ses/`.
