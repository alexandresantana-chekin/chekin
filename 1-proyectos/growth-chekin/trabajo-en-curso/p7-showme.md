# P7 · ShowMe (agente IA de ventas para leads Micro)

Proyecto de Alex (26/10): lo lleva él y lo trabaja con ShowMe. Recopilado el 26/10 de Slack (#showme_chekin, DM con Carlos) y de Notion.

## Qué es
- ShowMe (getshowme.ai) pone un **AE de IA llamado «Alex»** que habla con los leads **Micro (de 1 a 3 viviendas, confirmado por Alexandre el 28/10)** por teléfono, WhatsApp, email y chat web, en dos fases: **Pretrial** (convertido = empieza el trial) y **Trial** (convertido = paga).
- Mercados: España e Italia en marcha; **Portugal** arrancando (pretrial, trial y ahora *recovery*).
- Contacto en ShowMe: **Pedro Bernar** (pedro@getshowme.ai). Canal: Slack **#showme_chekin**.
- En Chekin: lo montó Gabriel Coachman (ver Notion «Handoff — Gabriel Coachman»); luego lo llevó Carlos; desde el 22/10 «Alexandre irá asumiendo la operativa de ShowMe».

## Datos (informes de Carlos, DM del 26/10)
- [Informe ShowMe Micro v4](https://claude.ai/artifact/E3nhU29SVYUaRg5C4ECSbA): conversaciones hasta el 19/10, **2.900 leads y 1.366 conversaciones**; embudo por mercado y fase, objeciones, errores del agente, base de conocimiento para AEs y **486 oportunidades para AEs** (173 de los últimos 45 días, con CSV).
- [MRR automático ShowMe · Leopard](https://claude.ai/artifact/Wu1JyQcVnLuxvLkGLmd4CJ): de **385 clientes que ShowMe declara convertidos, 331 pagan de verdad** en Leopard (España 300 de 327; Italia 31 de 58). Del 1/06 al 20/10 entraron **3.184 € de MRR**, de ellos **1.385 € sin AE**. Ticket medio de unos **9,7 €/mes**. Octubre sin cerrar en Leopard; Portugal todavía no viene en los exports.
- Fuente del MRR: **Leopard** (decisión de Alex, 26/10).

## Qué hay que mover (por impacto, según Carlos el 26/10)
1. **Handoff a una persona:** cuando el lead pide hablar con alguien, Alex da un email y un WhatsApp pero no crea un handoff real. Propuesta: tarea a AE o soporte con SLA de 2 h. (Ya existe la propiedad `Showme_Human_AE` para lanzar tareas a los AEs.)
2. **La secuencia escribe a clientes que ya pagan:** cortarla también por lifecycle = Customer, no solo por `payment_attached`. Del 13 al 18/10, 4 clientes más. En el export, 71 de 362 clientes (20%) nunca tienen `payment_attached` = Yes.
3. **Email personal de soporte:** Alex da un email personal de un empleado; hay que darle un buzón de soporte.
4. **IVA en Italia:** el arreglo del precio «+ IVA» funciona en España pero no en Italia.
5. Validar con Producto: el agente dijo que Chekin tiene facturación electrónica.
6. Por probar: bajas en Italia y la respuesta sobre menores (Legal).
7. Pasar las oportunidades para AEs (CSV, tier A = subieron la reserva y no pagaron) a secuencias.
- Ya funciona: no repite mensajes en bucle (0 de 88) y en Italia ya no mezcla español (0 de 54).

## Portugal (reunión del 22/10: Carlos, Alexandre y Pedro)
- **Recovery:** reactivar los leads de Portugal del 23/08 al 2/10 (llamada, WhatsApp, email). Caso de uso `Showme_PT_recovery` y disparador `showme_trial_started_portugal`. Se enrola por lotes, no todo de golpe (en la reunión se dijeron 100; Alex hace 50 al día desde el 26/10: tarea en Growth Daily › Alexandre; 50 acumulados el 26/10). Acumulado comprobado en HubSpot: 150 el 27/10 y **250 el 28/10**.
- **43% de los leads de Portugal son ruido** por textos confusos de los anuncios («préstamos», «empleo»): revisión de copies con Marta.
- Pendiente de ShowMe: plantillas de WhatsApp (aprobación de Meta), propiedad trial/stop de Portugal, cadencia de reintentos y avisos en Slack.
- Pendientes de Chekin (en Asana, de Carlos): número de soporte con Marta, **precio mínimo 495 € × 3 + IVA** con Alessandro [POR COMPROBAR qué es exactamente], copies de PT con Marta.
- Widget web: en España bastantes conversaciones, en Italia pocas, en Portugal no instalado. El chat no recuerda al usuario si sale y vuelve.

## Encargo del CEO: ¿ShowMe ayuda de verdad? (28/10)
Pedido por Slack a Alessandro y Carlos; lo lleva Alex. Fecha de entrega: [POR COMPROBAR].
1. **Vídeos del onboarding de ShowMe** por país (ES, IT, PT) y caso de uso: alta de prueba como Micro y como SMB (6 grabaciones). Ver si se enseña a todos o depende del tamaño. Contactos de prueba marcados como PRUEBA en HubSpot.
2. **Quién pasa por ShowMe y quién no**, y cómo convierte cada grupo (trial y pago, cruce con Leopard). Propiedades en HubSpot: `showme_pretrial`, `showme_pretrial_italia`, `showme_pretrial_portugal`, `showme_trial_started`, `showme_human_ae`, `showme_pt_recovery`. Falta saber si hay grupo de control comparable.
3. **Acción mínima para que ShowMe se apunte un lead**: regla de atribución de Pedro, contrastada con datos (informe v4: 2.900 leads, 1.366 conversaciones).
- Preparación de los 3 puntos (casos, plantilla, primer corte con datos, mensaje a Pedro) en `p7-showme-encargo-ceo.md`. Tarea en Asana gid 1219967710164778.

## Relación con otros proyectos
- **MRR automático:** el informe de MRR de ShowMe ya cruza con Leopard; es la base del MRR por canal.
- **P3:** los leads Micro que entran por paid acaban en ShowMe; el Qualified MQL excluye Micro.
- **P6 Cello:** con Valery, plan el 6/11 [por cruzar con ShowMe: ¿referidos desde clientes Micro?].
- Notion: «Agente Sales Conversation Intel (ShowMe)» (Growth › AI Agents) y «Form Recovery Reason Survey» (MRR automático).

## Seguridad (26/10)
- En un DM de Slack (21/10) está la contraseña de la cuenta de ShowMe en texto plano, y la cuenta es la de un usuario que ya no está en el equipo (Gabriel). Conviene cambiarla y pasar a una cuenta propia o de empresa.
- En Notion, la página «STRIPE» (Operations › OPS - FOLDERS) contiene una clave *live* de Stripe en texto plano. Avisar para que la roten y la saquen de Notion.
