# P3 · Propuesta de fechas nuevas (para el lunes 26/10 con Carlos)

Preparada el 23/10. **Es una propuesta, no se ha cambiado nada en Asana.** Se cambia en Asana cuando Carlos dé el OK.

## Por qué hay que mover el 27/10
- El compromiso era "España e Italia listas como mínimo para el 27/10". Hoy ninguna de las 4 landings puede estar lista en esa fecha con datos que la respalden.
- **ES Hoteles:** el test de /chekin-hoteles está pausado. La PMax Competitors reparte el tráfico por la expansión de URL: llega el 41% de los clics en 90 días (21 jul – 18 oct) y el 21% en los últimos 30 (~190 clics/mes). Con ese volumen, el A/B de 1.560–2.900 visitas por versión no termina en plazo (H-03, H-04 y H-08).
- **Italia:** la PMax IT Vacational manda el 65% de los clics a /modello/contrattoaffittoturistico, y la IT Competitors el 29% (90 días, H-05). Antes de diseñar hay que decidir si la landing es para quien busca una plantilla de contrato o para hoteles.
- **UTM:** mientras sigan rotas, MQL y SQL por campaña no son fiables (H-02). Hay que arreglarlas antes de lanzar cualquier test.
- **KPI de P3:** +30% de conversión en noviembre frente a la línea base de octubre (fecha: 30/11). Para que noviembre mida algo, al menos una landing tiene que estar en marcha el **lunes 2/11**.

## Propuesta
| Tarea de Asana | Fecha actual | Fecha propuesta | Owner | Hecho = | Depende de |
|---|---|---|---|---|---|
| Corregir las UTM de las PMax | 27/10 | **27/10** (se mantiene) | Carlos o Snowball (en Ads); Alex da la especificación | Los contactos nuevos de cada PMax llegan con su nombre de campaña, sin `{campaignname}` | Acceso a Google Ads |
| España · Resto: página SES en la PMax Vacational (v2) | 27/10 | **30/10** montada en HubSpot sin publicar · **lanzamiento 2/11** | Alex | v2 en HubSpot, test 50/50 en marcha y registrado en el tracker | OK de Carlos el 26 al boceto v2 y al test; A/B en el plan de HubSpot; texto legal del DPO; excluir las otras URLs de la PMax mientras dure el test |
| España · Hoteles: landing nueva | 27/10 | **6/11** lista · lanzamiento **9/11** | Alex | Landing lista en la URL que se decida y test registrado | Decisión del 26 sobre Competitors: acotar la expansión, testear donde va el tráfico o una landing por anuncio; revisión con Carlos el 4/11 |
| Registrar cada test en el tracker | 27/10 | **El mismo día de cada lanzamiento** (el primero, el 2/11) | Alex | Cada test con fecha de inicio, URL, variante y métrica | Lanzamientos |
| Italia · Hoteles: landing | 27/10 | **20/11** | Alex | Landing lista y revisada | Decidir el enfoque de la plantilla de contrato; revisión del italiano [POR COMPROBAR: quién la hace] |
| Italia · Resto: landing | 27/10 | **27/11** | Alex | Landing lista y revisada | Ídem |
| Línea base de conversión de octubre por landing | 31/10 (sábado) | **2/11** | Alex | Tabla en la ficha P3 de Notion | Octubre cerrado |

Se mantienen: configuración de la PMax, mensaje a Snowball y alternativas de landing (26/10); auditoría (30/10); lista priorizada (4/11); integrar mejoras con Valery (6/11); cierre de noviembre (30/11).

## Lo que necesito que Carlos decida el lunes
1. **Competitors ES:** ¿acotamos la expansión de URL, testeamos donde va el tráfico o pasamos a una landing por anuncio (fase 2)?
2. **Test SES en Vacational:** ¿OK al boceto v2 para lanzarlo el 2/11?
3. **OK durante sus vacaciones (28/10–3/11):** ¿puedo publicar la v2 en HubSpot el 2/11 con mi OK, o esperamos a su vuelta el 4/11? Si esperamos, el lanzamiento se va al 4/11 y noviembre se mide incompleto.
4. **UTM:** ¿quién las corrige el 27/10, él o Snowball?
5. **Italia:** ¿el 20/11 y el 27/11 le valen, o prefiere solo hoteles en noviembre?

## Pendientes de otros que frenan las fechas
- Plan de HubSpot: ¿tiene A/B de landings? Si no lo tiene, se compara antes y después con periodos iguales.
- DPO: texto legal bajo el formulario.
- Ventas: qué recibe el hotel al enviar el formulario y cuándo le contacta el experto.
- Tamaño de muestra del test SES con conversión base del 4,25% [POR COMPROBAR: el cálculo de 1.560–2.900 visitas era para /chekin-hoteles].
