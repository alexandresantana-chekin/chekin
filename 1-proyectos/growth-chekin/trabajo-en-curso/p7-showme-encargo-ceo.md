# P7 · Encargo del CEO: ¿ShowMe ayuda de verdad? (28/10)

Tarea en Asana: «ShowMe: ¿ayuda de verdad? Vídeos del onboarding, con/sin ShowMe y atribución (encargo del CEO)», proyecto MRR automático + ShowMe · Alexandre (gid 1219967710164778). Fecha: **30/10**.

---

## Punto 1 · Vídeos del onboarding de ShowMe

**Quién entra (Alexandre, 28/10):** Alex, el agente IA de ShowMe, solo trabaja leads de **1 a 3 viviendas** (Micro). Los SMB no pasan por ShowMe: sus vídeos sirven de comparación (qué recibe un lead que no entra).

Canales de ShowMe: **llamada, WhatsApp y email** (confirmado por Alexandre, 28/10). Cadencia medida en el informe v5 de Carlos (H-42): Pretrial empieza con llamada y sigue con WhatsApp cada ~48 h hasta ~5 días; Trial empieza por WhatsApp o chat web, ~6 WhatsApp en 12 días y llamada al 25% hacia el día 7. Frecuencia según Alexandre: [POR COMPROBAR].

### Casos (6 grabaciones)
| # | País | Perfil | Qué declarar en el alta | Qué esperamos ver |
|---|---|---|---|---|
| 1 | ES | Micro | 1–2 viviendas de alquiler vacacional | Flujo completo de ShowMe (pretrial → trial) |
| 2 | ES | SMB | 8–15 viviendas o un hotel pequeño | ¿ShowMe o AE? ¿Depende del tamaño? |
| 3 | IT | Micro | 1–2 appartamenti | Flujo IT (idioma, IVA, contrato) |
| 4 | IT | SMB | 8–15 unidades | Igual que el 2 |
| 5 | PT | Micro | 1–2 alojamientos locales | PT: pretrial/trial; sin widget web |
| 6 | PT | SMB | 8–15 unidades | Igual que el 2 |

Si un caso no recibe nada de ShowMe, también es resultado: se graba y se apunta.

### Antes de empezar (preparación)
1. **Preguntar a Pedro** (mensaje abajo) el criterio de entrada y avisar de las altas de prueba.
2. **Emails de prueba:** alias del correo de empresa, uno por caso (p. ej. `tu-usuario+sm-es-micro@chekin.com`). [POR COMPROBAR que el registro acepta el «+»]
3. **Teléfono:** ShowMe llama y escribe por WhatsApp. Con un solo número puede que deduplique y solo trate el primer caso. Opciones: 2–3 números de compañeros (uno por país) o preguntar a Pedro si deduplica por teléfono. [POR COMPROBAR]
4. **Dónde darse de alta:** la misma entrada que un lead real de cada país (web del país → registro). [POR COMPROBAR URL de registro por país]
5. **Marcar como prueba:** en HubSpot, nombre o empresa con «PRUEBA» y sacarlos de informes y listas; pedir a ShowMe que no los cuente.

### Qué grabar y anotar en cada caso
- Grabación de pantalla del alta (web/app) y del móvil (WhatsApp, llamadas, emails).
- Plantilla de observación:
  | Campo | Caso 1 | … |
  |---|---|---|
  | Hora del alta | | |
  | Primer contacto de ShowMe (canal y minutos tras el alta) | | |
  | Mensajes en las primeras 48 h (canal, nº) | | |
  | ¿Explica el producto / ofrece demo / empuja al trial? | | |
  | ¿Idioma correcto? ¿Precio e IVA correctos? | | |
  | ¿Ofrece hablar con una persona? ¿Se crea handoff real? | | |
  | Errores o respuestas falsas | | |
  | ¿Cambia algo en HubSpot (propiedades `showme_*`)? | | |
- Seguir cada caso al menos 3 días (o hasta el final de la secuencia de pretrial).

---

## Punto 2 · Quién pasa por ShowMe y quién no (primer corte, H-26)

Micro creados del 1/06 al 19/10/2026, con fecha de inicio de trial (HubSpot):

| Grupo | Trials | Clientes | % a cliente |
|---|---|---|---|
| Con ShowMe en trial (`showme_trial_started`) | 1.103 | 306 | 27,7% |
| Sin ShowMe en trial | 2.230 | 355 | 15,9% |
| Total | 3.333 | 661 | 19,8% |

- **2 de cada 3 trials Micro no pasan por ShowMe en trial.** Hay división clara y medible.
- **No es todavía una comparación justa:** falta saber por qué unos entran y otros no. Siguientes cortes:
  1. Por país (ES, IT, PT y resto) y por mes de alta, para quitar el efecto de cuándo arrancó ShowMe en cada mercado.
  2. Con la regla de entrada de ShowMe (Pedro): si solo coge a ciertos leads, comparar dentro de ese mismo criterio.
  3. Pago real en Leopard en lugar de lifecycle Customer.
- Pretrial: 1.492 Micro con marca `showme_pretrial*` de 8.250 creados (18%).

### Por país y por mes (H-27): la ventaja global es mezcla de países
Con la marca de trial de cada mercado (`showme_trial_started`, `_italia`, `_portugal`). % = clientes / trials.

| País | Con ShowMe | Sin ShowMe |
|---|---|---|
| España | 1.070 · **26,3%** | 312 · **29,8%** |
| Italia | 202 · **25,2%** | 385 · **18,7%** |
| Portugal | 80 · 2,5% | 91 · 20,9% |

| Mes de alta | ES con | ES sin | IT con | IT sin |
|---|---|---|---|---|
| Jun | 158 · 35,4% | 178 · 34,3% | — | 265 (jun–jul) · 19,6% |
| Jul | 336 · 32,1% | 67 · 25,4% | 2 · 0% | (en jun–jul) |
| Ago | 213 · 29,1% | 32 · 28,1% | 16 · 31,3% | 96 · 15,6% |
| Sep | 205 · 18,0% | 23 · 26,1% | 120 · 26,7% | 23 · 17,4% |
| Oct (1–19) | 158 · 11,4% | 12 · 0% | 64 · 21,9% | 3 · 33% |

Lectura para el CEO:
- **España: sin mejora visible.** En junio, el único mes con dos grupos parecidos, 35,4% con ShowMe frente a 34,3% sin. Desde julio ShowMe coge al 85–93% de los trials y casi no queda con qué comparar.
- **Italia: señal positiva** (ago–sep: 27–31% con ShowMe frente a 16–20% sin o antes de ShowMe), con grupos pequeños.
- **Portugal:** arranque reciente; sin conclusión.
- Septiembre y octubre están verdes (trial de 14 días + pago): bajan los dos grupos.

### Antes y después (H-28): mar–may sin ShowMe frente a jul–hoy con ShowMe
| País | Mar–may (sin ShowMe) | Jul–sep (con ShowMe) | Jul–28/10 · con | Jul–28/10 · sin |
|---|---|---|---|---|
| España | 862 · **34,9%** | 876 · **27,3%** | 936 · 24,1% | 135 · 23,7% |
| Italia | 354 · **22,6%** | 392 · **20,2%** | 214 · 24,8% | 258 · 16,7% |
| Portugal | 37 · 24,3% | — | 84 · 2,4% | 80 · 16,3% |

- España: con ShowMe en el 87% de los trials, la conversión **baja** frente a la primavera (34,9% → 27,3%), y del 1/07 a hoy con y sin ShowMe convierten igual.
- Italia: baja un poco antes/después (22,6% → 20,2%), pero dentro del mismo periodo con ShowMe convierte más (24,8% vs 16,7%).
- Ojo: estacionalidad, mix de campañas y menos tiempo para convertir en jul–oct.

### Cifra para el CEO con referencia 1/08 (H-30): agosto y septiembre completos
| País | Con ShowMe | Sin ShowMe | Pasan por ShowMe | Mar–may (sin ShowMe) |
|---|---|---|---|---|
| España | 99 / 418 · **23,7%** | 15 / 55 · **27,3%** | 88% | 301 / 862 · 34,9% |
| Italia | 37 / 136 · **27,2%** | 19 / 119 · **16,0%** | 53% | 80 / 354 · 22,6% |

- No cambia el sentido: España sin mejora (grupo «sin» de solo 55 trials); Italia +11 puntos.

> ⚠️ **28/10, H-42 y H-43:** en Italia el lifecycle Customer de HubSpot está inflado (28 de 78 nunca han pagado según Leopard). La señal de Italia de estas tablas hay que rehacerla con pagos de Leopard.

### Corte anterior (H-29): altas 1/07–30/09
| País | Con ShowMe | Sin ShowMe | Mar–may (sin ShowMe) |
|---|---|---|---|
| España | 754 · **27,5%** | 122 · **26,2%** | 862 · 34,9% |
| Italia | 138 · **26,8%** | 254 · **16,5%** | 354 · 22,6% |
| Portugal | 52 · 1,9% | 61 · 21,3% | 37 · 24,3% |

- España: sin efecto (+1,3 puntos). Italia: +10 puntos en el mismo periodo. Portugal: no se puede leer, porque la marca de ShowMe incluye el recovery (leads que ya no convirtieron).

- **Para medirlo de verdad:** grupo de control aleatorio (p. ej. 20% de los Micro de España sin ShowMe durante 4 semanas) y pago real en Leopard.

---

## Punto 3 · Acción mínima para que ShowMe se apunte un lead

### Qué hay que saber
- Su regla exacta: ¿cuenta como suyo con un mensaje enviado, con respuesta, con conversación o con llamada?
- ¿Desde cuándo cuenta (primer contacto) y hasta cuándo (ventana de atribución)?
- ¿Cuenta un trial que empezó **antes** de su primer contacto?

### Cómo contrastarlo con datos
- Del informe v4 (hasta el 19/10): 2.900 leads y 1.366 conversaciones → más de la mitad de los leads no tiene conversación.
- Pedir a ShowMe el export de los 385 «convertidos» con: fecha de primer contacto, canal, nº de mensajes del lead (respuestas) y fecha de conversión.
- Cruzar con HubSpot (fecha de inicio de trial y lifecycle) y Leopard:
  - % de convertidos sin ninguna respuesta del lead;
  - % que empezó el trial antes del primer contacto de ShowMe;
  - lo que queda es lo atribuible con criterio estricto.

---

## Mensaje para Pedro (Slack #showme_chekin) · borrador, lo envía Alex

> Hola Pedro! Estamos revisando a fondo cómo funciona ShowMe y necesito que me confirmes unas cosas:
> 1. **Quién entra en la secuencia:** entendemos que entran los leads de 1 a 3 viviendas. ¿Entran todos los de ese tamaño en cada país o hay algún filtro más (fuente, fase, tamaño sin declarar)?
> 2. **Atribución:** en vuestro export, «converted» incluye leads con los que Alex nunca llegó a hablar. ¿Es así como lo contáis en los resultados que nos presentáis? ¿Contáis trials que empezaron antes de vuestro primer contacto?
> 3. Vamos a hacer altas de prueba en ES, IT y PT (Micro y SMB) para ver el flujo completo. ¿Deduplicáis por teléfono? ¿Cómo hacemos para que no os cuenten en los resultados?
>
> Gracias!

---

## Borrador de respuesta al CEO (28/10, sin enviar · lo revisa y envía Alexandre)

> Te adelanto lo que ya tenemos con datos; los vídeos los grabamos esta semana.
>
> **1. Cómo funciona el onboarding de ShowMe**
> - Solo entran los leads **de 1 a 3 viviendas** (micro) de España, Italia y Portugal. Los SMB no pasan por ShowMe.
> - Dos fases: **Pretrial** (registrado sin trial; éxito = empieza el trial) y **Trial** (éxito = paga).
> - Pretrial: primero **una llamada** y luego WhatsApp cada ~48 h durante unos 5 días. Trial: **WhatsApp** o chat web, ~6 mensajes en 12 días, y llamada solo a 1 de cada 4, hacia el día 7.
> - Lo que convierte: el **teléfono en Pretrial** (31,7% en España frente al 3,8% de WhatsApp) y resolver la duda legal concreta (SES, Mossos, Alloggiati).
> - Lo que falla: cuando el lead pide una persona (189 en España, que convierten un 35%), Alex no la pasa a nadie. Falta un workflow nuestro en HubSpot.
> - Vídeos: 3 altas micro (ES, IT, PT) para ver el flujo y 1 SMB como comparación. [POR HACER]
>
> **2. Quién pasa por ShowMe y quién no, y cómo convierte cada uno**
> - División clara: en España, ShowMe trabaja el 86–88% de los trials micro desde julio; en Italia, la mitad.
> - Con **pago real** (Leopard), trials micro de agosto y septiembre: España **14,8% con ShowMe frente a 20,0% sin**; Italia, mes a mes, igual (septiembre 7,5% frente a 8,7%). **No vemos que ShowMe suba la conversión a pago.**
> - Antes de ShowMe (marzo–mayo) España convertía más que ahora, aunque ahí influyen la temporada y las campañas.
> - Para medirlo de verdad: un **grupo de control aleatorio** (por ejemplo, el 20% de los micro de España sin ShowMe durante 4 semanas).
>
> **3. Qué hace ShowMe sobre un lead y qué necesita para apuntárselo**
> - ShowMe se apunta como «convertido» **cualquier lead que entra en su secuencia y convierte, haya hablado con Alex o no**: en España, el 52% de sus leads nunca tuvo conversación y cuentan igual.
> - De 3.040 leads, ShowMe declara **630 convertidos**; **pagan 360** (2.898 €/mes de MRR) y de esos **156 cerraron sin AE**. Lo atribuible a ShowMe con criterio estricto está más cerca de los 156 que de los 630, y ni siquiera eso es seguro sin grupo de control.
> - Se lo estamos confirmando a ShowMe por escrito.
>
> Fuentes: informe ShowMe Micro v5 (Carlos, 27/10; export de ShowMe + HubSpot + Leopard) y HubSpot (altas 1/08–30/09/2026, pago = MRR de Leopard de septiembre).
