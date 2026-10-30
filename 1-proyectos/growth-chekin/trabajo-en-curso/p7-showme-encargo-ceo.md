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


## Respuesta de Pedro (29/10) · cambios para el borrador al CEO (H-49)
- Corregir «Solo entran los leads de 1 a 3 viviendas»: el criterio lo ponen nuestros workflows de HubSpot (al principio, micro no asignados a ventas; después, más tamaños). Confirmar el criterio actual y por país (Carlos o el workflow «UPDATED Lead As…»).
- Añadir: el «converted» de ShowMe cuenta a todo lead de la secuencia, haya hablado o no con el agente. Por eso nuestra lectura usa grupo comparable y pagos reales (H-43).
- Vídeos: ShowMe no los tiene. Hay que grabarlos nosotros con altas de prueba, avisando antes a Pedro con los emails.

---

## Respuesta al CEO · versión 30/10 (sin enviar · la revisa y la envía Alexandre)
Corrige el borrador del 28/10 con H-49 (Pedro), H-43 (pagos de Leopard) y H-56 (recovery de Portugal).

> **ShowMe: ¿ayuda de verdad? Resumen con datos**
>
> **1. Cómo trabaja ShowMe**
> - **Quién entra no lo decide ShowMe, lo deciden nuestros workflows de HubSpot.** Al principio solo entraban los Micro (1–3 viviendas) no asignados a ventas y después se han ido sumando otros tamaños (confirmado por Pedro el 29/10). El criterio actual por país lo confirmo con Carlos a su vuelta (3/11).
> - Dos fases: **Pretrial** (registrado sin prueba; éxito = empieza la prueba) y **Trial** (éxito = paga).
> - **Pretrial:** primer contacto por llamada (66%) y luego WhatsApp cada ~48 h durante unos 5 días. **Trial:** empieza por WhatsApp (72%) o chat web (20%), unos 6 WhatsApp en 12 días, y solo llama al 25%, hacia el día 7.
> - **Lo que funciona:** la llamada en Pretrial (España: 31,7% de conversión por teléfono frente al 3,8% por WhatsApp; Italia: 30,6% por teléfono).
> - **Lo que falla:** cuando el lead pide hablar con una persona (189 veces en España, y esos leads convierten un 34,9%), no se le pasa a nadie. Falta un handoff nuestro en HubSpot.
> - **Vídeos:** ShowMe no tiene grabaciones por país. Los grabamos nosotros con altas de prueba en ES, IT y PT (Micro y SMB), avisando antes a Pedro. [POR HACER: fecha]
>
> **2. Con y sin ShowMe, con pago real (Leopard)**
> Trials Micro por mes de alta que pagan según Leopard (último mes cerrado: septiembre). Fuente: HubSpot, consulta del 30/10.
> | Mes de alta | España con | España sin | Italia con | Italia sin |
> |---|---|---|---|---|
> | Julio | 90/331 · **27,2%** | 14/66 · **21,2%** | — (ShowMe arranca en IT el 28/08) | 19/135 · 14,1% |
> | Agosto | 51/213 · **23,9%** | 7/32 · **21,9%** | 5/16 · 31% | 16/97 · 16,5% |
> | Septiembre (sin cerrar) | 11/204 · 5,4% | 4/22 · 18,2% | 9/120 · 7,5% | 2/23 · 8,7% |
> | **Julio + agosto** | **141/544 · 25,9%** | **21/98 · 21,4%** | | |
> - **En España, con los meses ya cerrados, ShowMe sale +4,5 puntos** (25,9% frente a 21,4%). Es una ventaja pequeña y el grupo sin ShowMe es corto (98 trials, porque ShowMe trabaja ~85% de los trials), así que no es concluyente.
> - **Septiembre todavía no se puede leer:** la prueba dura 14 días y muchos de septiembre pagan en octubre, que Leopard aún no ha cerrado. Lo rehacemos a primeros de noviembre.
> - **Italia:** sin conclusión. Agosto da +15 puntos, pero con 16 casos. La ventaja que salía en HubSpot estaba inflada: 28 de 78 «Customer» de Italia nunca han pagado.
> - Hablar con el agente tampoco marca la diferencia en Pretrial España (18,2% con conversación frente a 25,5% sin). En Trial sí convierten más los que hablan (34,2% frente a 19,7%), pero eso no es causal: quien contesta ya está más interesado.
> - **Para saberlo de verdad hace falta un grupo de control aleatorio:** por ejemplo, el 20% de los Micro de España sin ShowMe durante 4 semanas, midiendo el pago en Leopard.
>
> **3. Qué necesita ShowMe para apuntarse un lead**
> - **Nada: basta con que entre en la secuencia.** Pedro lo confirma (29/10): en Pretrial cuenta como convertido a quien empieza la prueba y en Trial a quien pasa a Customer, haya hablado con el agente o no. En España, el 52% de sus leads nunca tuvo conversación.
> - Cifras del informe v5 (export de ShowMe + HubSpot + Leopard; ES desde el 18/06, IT desde el 28/08, PT desde el 6/10, hasta el 26/10): de **3.040 leads**, ShowMe declara **630 convertidos**, pagan **360** (2.898 €/mes de MRR) y **156 de esos 360 cerraron sin AE**. Lo atribuible a ShowMe está más cerca de 156 que de 630, y ni eso es seguro sin grupo de control.
>
> **4. Portugal: recovery (26–30/10)**
> - **468 leads** antiguos (altas 23/08–2/10 que no convirtieron) enrolados en ShowMe.
> - En Portugal se están probando ahora los tres canales: **llamada, WhatsApp y email**.
> - ShowMe da **6 reactivados (1,3%)**. En HubSpot solo **2** han vuelto a hacer algo: rellenan el alta y empiezan la prueba (27/10 y 29/10). Una de esas dos pruebas no está en la lista de ShowMe.
> - Ninguno de los que empiezan la prueba recibe la marca de trial de ShowMe en Portugal, así que pueden seguir recibiendo mensajes de recovery. Se arregla con un cambio en el workflow de Portugal (pendiente de OK).
>
> **Próximos pasos que propongo**
> 1. Grupo de control aleatorio en España (4 semanas).
> 2. Handoff a persona cuando el lead lo pide (tarea al AE con SLA de 2 h).
> 3. Grabar los vídeos con altas de prueba.
> 4. Confirmar con Carlos el criterio de entrada actual por país.
