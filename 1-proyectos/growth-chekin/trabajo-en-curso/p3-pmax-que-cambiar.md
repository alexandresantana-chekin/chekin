# P3 · PMax: qué recibe tráfico y qué cambiar (23/10)

Tarea de Asana: "Revisar la configuración de Performance Max (reparto de tráfico entre URLs)" (vence el 26/10).
Hecho = diagnóstico de qué URLs reciben tráfico y qué cambiar en la configuración. **Propuesta para revisar con Carlos el lunes 26. No se toca nada en Google Ads sin su OK.**
Datos: hallazgos H-02 a H-08 (`../hallazgos.md`) y `p3-auditoria-paid.md`.

## 1. Diagnóstico (90 días: 21 jul – 18 oct, salvo que se diga otra cosa)

**ES PMax Competitors** (URL configurada: /chekin-hoteles) · 3.791 clics · 10.384 € · 81 formularios · 13 SQL · 4 ganados
- Solo el **41%** de los clics llega a /chekin-hoteles (en los últimos 30 días, el **21%**, ~190 clics/mes). El resto se reparte entre 23 URLs.
- /chekin-hoteles: 1.559 clics, 6 formularios (**0,38%**). Plantillas y guía SES: 2,9–5,1%.
- El texto de anuncio que más gasta es **"Plantilla SES Hospedajes"** (título de la plantilla Word): 1.066 clics y 4.636 €. Nadie lo escribió: lo genera Google (textos automáticos + expansión de URL).
- Google optimiza a una sola conversión, "SB - (MQL)Registro Landing Hubspot", que cuenta **cualquier formulario**, plantillas incluidas. Manda el clic a la página que más formularios saca, y /chekin-hoteles convierte poco (carga en 3,9 s, `lang="en"`, formulario al 93% del scroll).
- Calidad: plantillas = 11 contactos en HubSpot, 2 SQL, 0 oportunidades (desde el 21/07).

**ES PMax Vacational** (URL: página SES) · 99% de los clics se queda en su landing (4,25% de conversión). No hay a dónde ir mejor. 500 formularios, 8 SQL, 0 ganados.

**Italia** · IT Vacational: 30% a su landing, **65% a /modello/contrattoaffittoturistico**. IT Competitors: 67% a su landing, 29% a la plantilla de contrato.

**Resto** (PT Competitors y Vacational, GB y DE Vacational): 100% a su landing. No hay problema de reparto.

**UTM:** 5 nombres de campaña distintos para la misma PMax, `{campaignname}` sin sustituir. MQL/SQL por campaña en HubSpot no son fiables (H-02).

## 2. Qué cambiar (por orden)

| # | Cambio | Dónde | Por qué | Riesgo |
|---|---|---|---|---|
| 1 | **Corregir la plantilla de seguimiento / sufijo de URL final** de todas las PMax | Google Ads (Snowball) | Sin UTM fiables no se puede medir nada de lo que sigue | Ninguno en la entrega |
| 2 | **Desactivar los recursos de texto automáticos** en la ES Competitors | Google Ads | Los textos sobre plantillas atraen búsquedas de plantillas gratis, no hoteles | Algo menos de volumen |
| 3 | **Acotar la expansión de URL final**: excluir /plantillas/*, /plantillas-seshospedajes, /es/guia/*, /en/*, /check-in-guestapp y /es/check-in-online-ses-hospedajes (o desactivarla) | Google Ads | Que el tráfico de hoteles llegue a la landing de hoteles | Bajan los formularios: en 90 días, las URL a excluir dieron 71 de los 81 (plantillas y guía SES: 51; guestapp: 10; página SES: 8; /en/: 2). Las plantillas son de baja calidad; el resto, sin medir |
| 4 | **Objetivo de conversión**: que la principal sea el formulario de prueba o demo de la landing; las descargas de plantillas, secundarias (solo observación) | Google Ads + HubSpot | Hoy vale lo mismo bajarse una plantilla que pedir una prueba | Reaprendizaje de la PMax [POR COMPROBAR cuánto tarda] |
| 5 | **Arreglar /chekin-hoteles** (velocidad, idioma, formulario arriba) o pasar a la landing nueva | HubSpot (Alex) | Si la landing sigue convirtiendo al 0,38%, Google seguirá buscando otra página | — |
| 6 | **Italia**: decidir si la landing es para quien busca una plantilla de contrato o excluir esa URL | Google Ads + landing | El 65% del tráfico de IT Vacational va a la plantilla | Volumen |

- Los cambios 2 y 3 juntos son "una sola variable" (la configuración de reparto). Se miden 2–3 semanas, **antes** del test de landing. Nunca a la vez que un test de landing.
- **Antes de excluir las plantillas, comprobar de qué URL vinieron los 13 SQL y los 4 ganados de Competitors** [POR COMPROBAR]. Si salen de plantillas, hay que replantear el cambio 3.
- Pendiente: términos de búsqueda de la PMax (Windsor) para ver cuánto es "plantilla gratis" y cuánto es búsqueda de software para hoteles.

## Grabaciones de las landings
Las landings ya cargan Microsoft Clarity por GTM (proyectos `rrl7tp5b6k` y `rqlc6g9qhu`, H-14). Puede que ya haya grabaciones y mapas de calor de /chekin-hoteles. **23/10: Alex no tiene acceso a ninguno de los dos.** Pedirlo a Carlos o a Snowball.

## Borrador para Snowball (canal general de Slack; lo envía Alex tras hablar con Carlos)
> Hola, equipo 👋 Soy Alexandre, del equipo de growth de Chekin. Estoy revisando con Carlos las landings de las Performance Max y queremos confirmar con vosotros un par de cosas:
>
> 1. **Reparto de URLs en la PMax ES Competitors.** Según el informe de URLs de Google Ads (21 jul – 18 oct), solo el 41% de los clics llega a /chekin-hoteles; el resto va a otras 23 URLs, sobre todo plantillas SES y de contrato, guestapp y la guía SES. ¿Nos confirmáis si tiene activada la expansión de URL final y los recursos de texto automáticos, y si hay alguna URL excluida?
> 2. **Objetivo de conversión.** Vemos que la campaña optimiza a "SB - (MQL)Registro Landing Hubspot", que cuenta cualquier formulario, también la descarga de plantillas. ¿Es así?
> 3. **Clarity.** En las landings se cargan dos proyectos de Microsoft Clarity por Tag Manager (`rrl7tp5b6k` y `rqlc6g9qhu`). ¿Son vuestros? Si es así, ¿me podéis dar acceso (alexandre.santana@chekin.com)? Queremos ver grabaciones y mapas de calor de /chekin-hoteles.
> 4. **Datos que nos ayudarían:** el informe de términos de búsqueda y el de recursos de los últimos 90 días de las PMax ES e IT.
> 5. **UTM:** a /chekin-hoteles llegan cinco nombres de campaña distintos, uno de ellos `{campaignname}` sin sustituir. ¿Podéis revisar la plantilla de seguimiento o el sufijo de URL final de las PMax?
>
> Con esto queremos proponeros algunos cambios de configuración antes de lanzar el test de landing. ¡Gracias!

## 3. Decisiones para Carlos (lunes 26)
0. ¿De quién son los dos proyectos de Clarity de las landings? Acceso para Alex.
1. ¿Acotamos la expansión de URL (cambios 2 y 3), o pasamos directamente a una landing por anuncio?
2. ¿Cambiamos el objetivo de conversión (cambio 4) ya, o después de medir el reparto?
3. ¿Quién ejecuta en Google Ads: Snowball o él?
4. Italia: ¿excluimos la plantilla de contrato o hacemos landing para ese tráfico?
