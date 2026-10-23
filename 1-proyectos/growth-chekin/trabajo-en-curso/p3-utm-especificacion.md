# P3 · Especificación para corregir las UTM de las PMax

Preparado el 23/10 para la tarea de Asana «Corregir las UTM de las PMax» (27/10). **Borrador: no se ha tocado nada en Google Ads.** Lo aplica Carlos o Snowball (se decide el 26/10).

## El problema (H-02)
- A /chekin-hoteles llegan 5 nombres de campaña distintos para la misma PMax. Uno de ellos es `{campaignname}`, sin sustituir.
- Consecuencia: en HubSpot, los MQL y SQL por campaña no son fiables. Cualquier test de landing se mediría mal.
- Las PMax Vacational ES, GB y DE casi no tienen contactos propios: es probable que sus contactos estén contados como Competitors (H-07).

## Las 8 PMax activas

| Campaña | ID | Clics | Gasto |
|---|---|---|---|
| SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN | 24067861438 | 861 | 2.613 € |
| SB_ES_GOOGLE_PMAX_VACATIONAL_CHEKIN | 24262948726 | 12.186 | 5.578 € |
| SB_IT_GOOGLE_PMAX_COMPETITORS_CHEKIN | 24171599742 | 1.089 | 1.868 € |
| SB_IT_GOOGLE_PMAX_VACATIONAL_CHEKIN | 24262948717 | 1.784 | 2.497 € |
| SB_PT_GOOGLE_PMAX_COMPETITORS_CHEKIN | 24171599232 | 13.052 | 4.720 € |
| SB_PT_GOOGLE_PMAX_VACATIONAL_CHEKIN | 24262948723 | 2.772 | 1.932 € |
| SB_DE_GOOGLE_PMAX_VACATIONAL_CHEKIN | 24262948720 | 257 | 358 € |
| SB_GB_GOOGLE_PMAX_VACATIONAL_CHEKIN | 24262948729 | 414 | 595 € |

Fuente: Google Ads vía Windsor.ai, últimos 30 días (hasta el 23/10/2026). Para comparar con Carlos, sacar también los 90 días.

## Qué poner
En **cada campaña**: Configuración → Opciones de URL de la campaña → **Sufijo de URL final**. Se escribe el nombre a mano, campaña por campaña, en lugar de usar `{campaignname}`:

```
utm_source=google&utm_medium=cpc&utm_campaign=SB_ES_GOOGLE_PMAX_COMPETITORS_CHEKIN&utm_id={campaignid}
```

- `utm_campaign` es el nombre exacto de la tabla, distinto en cada una de las 8. Así no depende de un parámetro que hoy no se sustituye.
- `utm_id={campaignid}` es un parámetro ValueTrack de Google: sirve de respaldo si alguien cambia el nombre de la campaña.
- `utm_source` y `utm_medium` son iguales en todas, para que HubSpot y GA4 las agrupen como «Paid search».

## Antes de cambiar, revisar (en Google Ads, con Carlos o Snowball)
1. **¿De dónde salen hoy las UTM?** Puede haber varios sitios a la vez, y el más concreto manda sobre el general:
   - la plantilla de seguimiento o el sufijo de la **cuenta**,
   - el de la **campaña**,
   - el que añade la integración de anuncios de **HubSpot** (seguimiento automático).

   Si dos sitios añaden UTM, aparecen nombres mezclados. [POR COMPROBAR cuál está activo.]
2. **El auto-etiquetado (gclid) se mantiene activado.** No choca con las UTM.
3. Dejar apuntado el sufijo actual antes de borrarlo, para poder volver atrás.

## Cómo comprobar que funciona
- **Al aplicarlo:** abrir la vista previa de un anuncio de cada campaña y comprobar que la URL final lleva su `utm_campaign`.
- **A las 48 h:** en HubSpot, contactos creados desde el cambio con `utm_campaign` que empiece por `SB_` y contenga `PMAX`. Solo deben salir los 8 nombres de la tabla, sin `{campaignname}`. Los datos personales se miran solo en agregado.
- **Hecho =** una semana de contactos nuevos de las PMax, cada uno con el nombre de su campaña y sin valores raros. El resultado se apunta en la tarea de Asana y en `hallazgos.md`.

## Ojo
- Se puede cambiar a la vez que el resto, porque no toca el aprendizaje de la PMax. Aun así conviene apuntar el día del cambio en el tracker: a partir de ese día, las cifras por campaña de HubSpot no son comparables con las de antes.
- Meta no se toca (usa su propia plantilla de formulario).
