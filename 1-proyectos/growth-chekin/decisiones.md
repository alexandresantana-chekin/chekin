# Decisiones (solo crece)

## 2026-10-23
- **P1 · Grabaciones:** no se activan sin Daniel y el DPO. Enmascarar no quita la necesidad de consentimiento; se le pide a Daniel el lunes (solo /register y /setup, todo enmascarado).
- **P1 · PostHog:** acción "Alta nueva en el dashboard (email o Google)" y funnel guardado (OK de Alex). La estimación del 16% se retira: no se sostenía (H-12).
- **P3 · Pack legal:** la guía SES y las 4 plantillas se unen en una sola landing con titular según el anuncio (`?recurso=`). Solo tiene sentido si se mantiene la expansión de URL (decisión del lunes con Carlos).
- **P3 · Guía v2:** formulario arriba con teléfono (decisión de Alex). España: versión nueva de todo lo que tiene más de 100 clics en 90 días.
- **P2 · Web de los AEs:** todo en la nueva, https://chekin-connect.vercel.app (cuenta de empresa). La antigua `qrsaleschekin` no se toca.
- **P2 · Lector con Claude:** se aparca por ahora (decisión de Alex). El escáner usa el lector del móvil.
- **P2 · HubSpot:** función desplegada con clave interna; la app privada la crea un superadmin (Carlos). Tokens solo en el terminal; los de hoy, revocados.
- **P5:** la versión **cuadrada** es para todo (firma, foto de perfil y Hasp). Se ve animada como foto de perfil de Google si se sube desde el móvil. No va en Vercel: se comparte como archivo. Foto de perfil de Carlos: foto → círculo azul desde el centro → check → vuelve la foto (definitiva).

## 2026-10-22
- **Growth Check:** el MRR automático pasa a Alex. Carlos de vacaciones 28/10–3/11: todo en Growth Daily con owner, fecha y "hecho" antes del 27/10; estado por comentario en la tarea.
- **P1 · Reunión con Daniel:** el lunes 26/10 se le enseña un funnel con datos limpios de PostHog, mes a mes, con variantes y huecos de medición señalados y propuesta para medir bien desde ahora.
- **P2 · Escáner:** lectura de tarjetas con Claude (`claude-opus-5-5`, esfuerzo bajo, salida JSON fija) en una función de Supabase; la clave solo vive en Supabase. Si falla, entra el lector del móvil.
- **P2 · HubSpot:** se conecta (decisión de Alex).
- **Cierre de tareas:** cada tarea terminada se comenta en Asana mencionando a Carlos.
- **P5:** GIF definitivo = versión 5 (cohete por la «e» que choca con el check + zoom al check). Enlace público en Vercel porque Gmail solo acepta imagen por URL o Drive.
- **P1:** propuesta de herramienta para medir el funnel = PostHog (parece estar ya en uso) [POR COMPROBAR con Daniel].

## 2026-10-21
- **Casa:** un solo proyecto `growth-chekin` con P1–P4 dentro, en vez de una carpeta por P. Motivo: proyectos pequeños, mismo responsable y misma métrica (MRR).
- **Regla de oro:** nada se toca, envía ni publica sin aprobación y revisión de Alexandre.
- **Orden de prioridad:** P2 (mejora del QR) y P3 en curso → P1 cuando arranque con producto → P4 el último.
- **Dedicación:** 4 h/día, lunes a viernes. Se registran las horas en `horas.md` para ver si se pasa.
- **Asana:** borradas las tareas de prueba "Tarea 1/2/3".
- **P1 · Onboarding en ciclos:** analizar funnel hasta activación → proponer → ejecutar → medir a las X semanas. Frecuencia con Daniel en la meet del 22/10.
- **P3 · Plazo:** España e Italia listas como mínimo el 27/10.
- **P2 · Código de Chekin Connect en la casa**, carpeta `chekin-connect/` (decisión de Alex frente a repo propio).
- **P2 · Escáner:** consentimiento = casilla "me ha dado su tarjeta" (interés legítimo); obligatorio nombre + email o teléfono; también disponible para admins.
- **P2 · Publicación:** primero versión de prueba en proyecto Vercel nuevo; la web real no se toca hasta probarlo en el móvil.
- **P3 · Solo se cambia la landing**, en la misma URL de la PMax. No se tocan anuncios, puja, presupuesto ni audiencias. Motivo: aislar el efecto y evitar revisión de anuncios y reaprendizaje de la PMax.
- **P3 · Método:** A/B de HubSpot 50/50; si el plan no lo permite, antes/después con periodos iguales. Éxito: conversión mayor con p < 0,05 y MQL→SQL igual o mejor.
- **P3 · Medir por página, no por UTM.** Motivo: las UTM mezclan campañas (589 contactos etiquetados como PMax Competitors ES; solo 6 entraron por chekin-hoteles).
- **P3 · Solo se cambian las landings de Google Ads.** Meta usa su propia plantilla de formulario, así que sus anuncios quedan fuera de los cambios de landing. Las mejoras salen de las campañas activas y se registran en el tracker "Tests de landing Chekin".
- **P3 · Despliegue:** España hoteles → España resto → Italia hoteles → Italia resto → siguientes países. Un test nuevo solo cuando termine el anterior del mismo país y segmento.

## 2026-10-22 (tarde)
- **P5 · Animación cuadrada:** solo el check (no el logo completo), porque es lo que se reconoce en el círculo pequeño de la foto de Google. Con acercamiento fuerte y destello de halo (elegido frente al anillo). El primer fotograma es el check entero, porque Outlook solo muestra ese.
- **P5 · Foto de perfil de Google:** imagen fija de 1024 px, porque Google no anima las fotos de perfil.
- **P1 · Dashboard de activación:** datos de 2026 con marzo fuera por defecto (volcado masivo de Holidu). LTV estimado con Stripe (ingreso medio × vida media por retención a 12 meses de 2024), editable a mano. El coste de oportunidad se calcula por la diferencia de tasa de pago entre los que siguen y los que se quedan en cada paso.

## 2026-10-23 (tarde)
- P3: Alex mantiene el 27/10 para las 4 landings (ES hoteles, ES resto, IT hoteles, IT resto). "Lista" = diseño terminado y revisado, listo para montar en HubSpot. Montaje, publicación y tests van aparte y dependen del OK de Carlos. **Por qué:** Alex se compromete a terminarlas; lo que no depende de él (lanzar y medir) se separa para que la fecha no dependa de terceros.
- Asana (Alex, 23/10): todo lo hecho pasa a Asana. En Growth Daily › Alexandre va una tarea índice con enlaces (no duplicados), porque el conector no deja añadir una tarea a otro proyecto. Se cierran 2 tareas sobrantes (repetida y sustituida).
- Nuevo proyecto P6 · Cello (referidos) con Valery, plan para el 6/11 (Alex, 23/10).

## 2026-10-26
- **P2 · HubSpot sin propiedades nuevas (Alex):** los contactos de Chekin Connect se marcan con las propiedades que ya existen, «MQL Type» y «Last MQL type» (Event, Webinar o la opción nueva **Digital QR** para lo que entra sin evento). Si el contacto ya existía, MQL Type no se toca, para no perder la atribución de paid, y Last MQL type pasa al valor de Chekin Connect. El evento concreto va en la nota del contacto. «SQL type» no existe en HubSpot y no se usa. **Por qué:** no duplicar propiedades y que Chekin Connect cuente en los informes de MQL que ya usa Growth.
- **P2 · Reenvío por la función, no por importación:** los contactos antiguos se envían uno a uno por `hubspot-sync`, sin el permiso `crm.import`. **Por qué:** no duplica (busca por email), no pisa propietario ni etapa y deja rastro de cada envío en la app.
- **P2 · Web de los AEs:** se queda https://chekin-connect.vercel.app/mi-perfil. Alex quería el nombre `qrsaleschekin.vercel.app`, pero sin acceso a la cuenta personal de Vercel no se puede mover. Si se recupera la cuenta, se pasa el nombre al proyecto de empresa.
- **P2 · Rutina de eventos terminados (Alex):** L–V 9:00, una tarea por evento en Growth Daily › Alexandre, con una subtarea por AE y solo cifras (sin datos personales en Asana). La clave va en el Llavero de macOS.
- **Contraseñas:** nunca en el chat. Se generan en el terminal de Alex con un script y la app obliga a cambiarlas al primer acceso.
- **P3 · Landings (Carlos, vía Alex, 26/10):** a Carlos le gustan los bocetos de las 4 landings (ES hoteles, ES resto, IT hoteles, IT resto). Siguiente paso: analizar las landings de la competencia para copiar lo que hagan mejor.
- **P3 · Competencia (Alex, 26/10):** se copia «sin tarjeta y sin compromiso» (la prueba es así, confirmado por Alex) y la opción «habla con un experto» en IT hoteles (boceto v1, versión 3 del artifact). El precio («desde X €/mes») no se pone: Alex cree que son ~17 € con IVA [POR COMPROBAR], así que no hay cifra oficial.
- **P3 · Ideas de la competencia (Alex, 26/10):**
  1. Sí a nombrar los portales: en IT, «Alloggiati Web, ISTAT e tassa di soggiorno» (aplicado en IT hoteles); en ES, SES v2 ya nombra Mossos y Ertzaintza.
  2. **No** se quita el teléfono ni ningún campo: los 5 son obligatorios para que cuente como lead.
  3. Lo decide Claude: se promete el plazo («nei tempi di legge», «en plazo»), no «sin multas» como garantía. La cifra de multas solo donde ya estaba (SES v2, Ley Orgánica 4/2015). **Por qué:** Chekin no puede garantizar que un cliente no reciba multas, y la cifra no está en la lista oficial del traspaso.
  4. Sí a una línea de prueba social bajo el botón, con cifras oficiales (IT hoteles: +10.000 hotel y +25M check-in; IT resto y SES v2: +200.000 propiedades y +25M check-in). En SES v2 sustituye la línea junto al titular, para no repetirla.
  5. Vídeos: de momento no.
- **MRR automático (Alex, 26/10):** la fuente buena del MRR es **LEOPARD**, que en HubSpot se ve en la propiedad de contacto `mrr_leopard_eur` («MRR (LEOPARD)»: MRR del último mes cerrado, con reembolsos y descuentos ya restados; lo escribe la integración). El traspaso con Carlos sigue pendiente.
- **P3 · Mensaje a Snowball (Alex, 26/10):** se deja como está, sin cambios ni envío por ahora.
- **P3 · Autonomía con Snowball (Carlos, vía Alex, 26/10):** en P3, Alex trabaja de forma autónoma y habla directamente con Snowball, sin esperar a Carlos para cada cambio. A Carlos le parece bien. Las reglas de la casa siguen igual: nada se envía ni se publica sin el OK y la revisión de Alex.
- **P2 · AEs (Alex, 26/10):** enlace nuevo, contraseñas y perfiles de los AEs, resueltos.
- **P5 · GIF de la firma (Carlos, vía Alex, 26/10):** Carlos da el OK al GIF de la firma de Gmail. P5 queda entregado.
- **P7 · ShowMe (Alex, 26/10):** ShowMe pasa a ser un proyecto propio de Alex, que lo trabaja directamente con ShowMe. Cello (P6) se sigue tratando con Valery.
- **P3 · Fechas nuevas en Asana (Alex, 26/10):** el 2/11 es festivo. Quedan así:
  - SES v2: montaje en HubSpot el 30/10 y lanzamiento del test el **3/11**;
  - registro en el tracker y línea base de octubre: 3/11;
  - España hoteles: lista el 6/11 y lanzamiento el 10/11;
  - Italia hoteles: 4/11; Italia resto: 5/11 (Alex las adelanta porque ya están construidas; antes 13/11 y 20/11);
  - UTM: se mantiene el 27/10.
  Comentario con el motivo en cada tarea.
- **27/10 · P1, dashboard del funnel: la base de la app solo de enero a agosto de 2026.** Se decidió el 26/10: en septiembre la sincronización se cortó el día 4 y el mes sale incompleto. Aplicado el 27/10 en activación, altas al mes, funnel mes a mes y cobertura. Stripe sigue hasta hoy (otra fuente). El hueco sin datos pasa a ir del 01/09 al 12/10.
- **27/10 · P1, dashboard: las cifras de dinero se muestran en euros (€).** Lo decide Alex. Hasta ahora la moneda de Stripe figuraba como [POR COMPROBAR]. Además, la calculadora de oportunidad usa el valor por cliente del dashboard (ARR a 12 meses, LTV o a mano) en lugar de ARPA × 12, para descontar las bajas.
- **27/10 · P3 y paid: prioridades de Carlos para las 2 próximas semanas** (mensaje del 27/10, acordado el 26/10 con Snowball). Se paran la expansión de URL y los recursos expandidos de todas las PMax (Snowball, hoy); se rebalancea el presupuesto 14 días hacia vacation rental de España e Italia y se paran las campañas de otros países sin ángulo ganador; se optimiza con las SQL de todos los canales. Alex lleva todo lo de landings (URLs, CVR, experimentos y CRO) y entrega el 30/10 la propuesta de mejoras CRO y el plan de experimentación. En espera hasta ver a qué landings llega el tráfico sin expansión: limpieza de URLs obsoletas y listado de URLs prioritarias. Durante las vacaciones de Carlos (28/10–3/11), la estrategia la lleva Ricardo Taveras.
- **27/10 · P3: nuevo orden, primero vacation rental.** Lo decide Alex siguiendo la prioridad de Carlos (rebalanceo hacia rental de ES e IT). Orden: ES resto → IT resto → IT hoteles → ES hoteles. Fechas en Asana sin cambiar por ahora; propuesta en el mapa: ES resto 3/11, IT resto 4/11, IT hoteles 5/11, ES hoteles 10/11.
- **27/10 · P6 Cello: nuevo plan (Alex).** El viernes 30/10 se revisa todo lo de Cello con Valery. La semana siguiente, presentar a Óscar (Cálido). Medir Cello en HubSpot queda fuera por ahora. A los 2 o 3 días, ver si se van cerrando acuerdos. Cómo funciona hacerse miembro y pasar contactos ya está explicado en la web. Tareas de Asana sin tocar.
- **28/10 · P3: formulario de 5 campos, como dice el traspaso.** Nombre, teléfono, email, tipo de alojamiento y nº exacto de habitaciones. Sin apellidos y sin empresa (se quita de la guía SES al montarla en HubSpot). Lo decide Alex. Los formularios actuales de HubSpot ya cumplen la regla, así que se reutilizan. [POR COMPROBAR al montar] propiedad del nº: `number_of_units` (formularios actuales) o `number_of_rooms` (traspaso).
- **28/10 · P3: el A/B de landings se hace en HubSpot, no en Google.** Lo confirma Snowball (seguimiento del 28/10). Consecuencia: cada landing nueva se monta como **variante B de la página actual** en HubSpot (misma URL, reparto 50/50), en vez de página nueva con otra URL; así no hay que cambiar la URL en Google Ads para el test. [POR COMPROBAR] que el plan de HubSpot de Chekin incluye A/B de landing pages.
- **28/10 · P3: el A/B se centra en las 4 PMax** (Vacational y Competitors de ES e IT), cada una con su landing principal (URL final, H-36). Search y Brand quedan fuera por ahora. Orden: ES Vacational (SES v2, lista) → IT Vacational (/it/check-in-online-alloggiati-web, falta boceto) → IT Competitors (Questura v4, lista) → ES Competitors (hoteles v6, lista). Lo decide Alex.
- **28/10 · P3 Portugal: se mantiene «SEF/AIMA» en /pt/check-in-online.** Aunque el SEF ya no existe (ahora AIMA), mucha gente lo sigue buscando con el nombre antiguo. Lo decide Alex.
- **28/10 · P3: las variantes B mantienen el bloque interactivo de producto (7 pestañas) de la A.** Aplicado en SES v2 (ES), SIBA PT v1 y Alloggiati IT v1, con el mismo texto que la A y el diseño de la B. Así el A/B mide la forma (formulario arriba, móvil, botón único, prefijo, cifras), no el contenido. Lo decide Alex. Cifras: documentos actualizados a «más de 2.500 de más de 150 países» (chekin.com); 15 países, 45 jurisdicciones y 20 cerraduras quitados hasta confirmarlos con Marketing (28/10); 99,8% se queda como dato de maqueta.
- **28/10 · P3: el plan de HubSpot permite A/B de landing pages** (comprobado por Alex en el editor de la A española: Test → A/B test, 50/50, ganador manual). El test se monta como variante de cada página A; no se crea hasta tener el conector con permisos y el OK de Alex.
- **28/10 · P3: subtítulo del formulario «Sin tarjeta de crédito. Activación inmediata.» en las 6 variantes B** (ES «Sin tarjeta…», IT «Senza carta di credito. Attivazione immediata.», PT «Sem cartão de crédito. Ativação imediata.»), igual que las A. Prefijo del teléfono por defecto según el país: ES +34, IT +39, PT +351. Lo decide Alex. Cambia la regla del traspaso («un experto contacta» como oferta del formulario); el texto legal y el enlace «¿Prefieres que te llame un experto?» se mantienen.
