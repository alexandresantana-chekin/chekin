# Auditoría · landing.chekin.com/es/check-in-online-ses-hospedajes (22-10-2026)

Landing de la **PMax Vacational ES** (99% de sus clics). En la vista por landing de la biblioteca (90 días, 21 jul – 18 oct): 14.622 clics, 535 formularios, 3,7%. Calidad: Vacational ES 500 MQL → 8 SQL (1,6%), 0 ganados.
Revisada en el navegador a 1512×780 (portátil 14") y 375×812 (móvil). Capturas en esta carpeta.

## Fallos (por prioridad)
1. **Móvil: el texto del hero sale cortado por la derecha.** El H1 ("…evit[a] multas: automatiza e[l]…") y el párrafo se salen de la pantalla y quedan recortados. Es lo primero que ve el usuario de móvil.
2. **Móvil: el formulario empieza a 961 px** (más abajo de la primera pantalla de 812) y el botón de enviar termina a 1.559 px. Quien no baja no ve dónde dejar los datos.
3. **Portátil: el botón de enviar queda cortado.** El formulario empieza a 244 px y mide 580 px; el botón "Prueba Gratis 14 Días" termina a ~824 px, por debajo del pliegue de 780.
4. **Formulario muy grande** (580–598 px de alto): nombre, email, prefijo + teléfono, tipo de negocio, nº de propiedades/habitaciones + texto legal. Mucho bloque para una primera pantalla.
5. **Etiqueta encima del título que parece no hacer nada:** "Check-in online y cumplimiento legal →" es un enlace (cursor de mano y flecha) a `#form`; en portátil el formulario ya está a la vista, así que al pulsar no pasa nada visible.
6. **Dos CTA iguales que van al mismo sitio:** "Prueba gratuita" y "Hablar con un experto" tienen la misma altura (52 px), "experto" es incluso más ancho (236 vs 181 px) y **los dos llevan a `#form`**. No hay jerarquía y el segundo promete algo (hablar con un experto) que el formulario no distingue. Se repite 4 veces en la página.
7. **Demasiados CTA y página larguísima:** 11 botones, todos a `#form`; 7.669 px en portátil y 13.963 px en móvil.
8. **Inputs a 15 px en móvil:** por debajo de 16 px, iOS hace zoom al tocar el campo.
9. **Cifra no oficial:** "Más de 50 integraciones con PMS y cerraduras". La cifra oficial es +200 PMS.
10. **Texto del CTA distinto en cada sitio:** "Prueba gratuita", "Prueba Gratis 14 Días", "Hablar con un experto", "Calcula tus ingresos con un experto".

## Lo que está bien
- Sin enlaces de salida (0): todo lleva al formulario.
- Idioma declarado `es`.
- Ya pide tipo de negocio y nº de propiedades/habitaciones (sirve para separar hoteles de alquiler vacacional).

## Mejoras propuestas (sin publicar; con OK de Alex y en HubSpot)
- Arreglar el corte del texto en móvil (prioridad 1, es un bug).
- Formulario compacto en la primera pantalla (portátil y móvil): botón visible sin bajar; en móvil, formulario justo después del H1 o botón fijo abajo.
- Un solo CTA principal ("Empieza tu prueba gratis") y, si se mantiene "Hablar con un experto", como enlace secundario más pequeño, que lleve a algo distinto (calendario o el mismo formulario con el motivo marcado).
- Quitar el enlace de la etiqueta de arriba (o que no parezca botón).
- Inputs a 16 px.
- Cambiar "+50 integraciones" por la cifra oficial.
- Acortar la página.
- Medir antes y después por página (formularios ÷ visitas), con el periodo indicado.

## Boceto v2 (22-10-2026) · `../landing-ses-hospedajes-v2.html`
Archivo único, se abre con doble clic. **No conectado a HubSpot** (el formulario muestra "Boceto"). Campo oculto `landing = ses-hospedajes-es-v2-boceto`.
| | Actual | v2 |
|---|---|---|
| Botón de enviar en portátil 1512×780 | por debajo del pliegue (~824 px) | a 474 px |
| Formulario en móvil 375×812 | empieza a 961 px, botón a 1.559 | empieza a 316 px, botón a 731 (sin bajar) |
| Texto del hero en móvil | cortado por la derecha | entero, sin scroll horizontal |
| Alto de página (portátil / móvil) | 7.669 / 13.963 px | 2.520 / 4.085 px |
| Botones | 11, dos iguales al mismo sitio | 1 principal ("Empieza tu prueba gratis", 3 veces) + enlace secundario "¿Prefieres que te llame un experto?" que marca `request_type = expert` |
| Etiqueta sobre el título | enlace a #form que no hace nada | texto, no clicable |
| Letra de los campos en móvil | 15 px | 16 px |
| Cifras | "+50 integraciones", "+45 países" | solo oficiales: +200.000 propiedades, +25M check-ins, +200 PMS |
Se quitó: el bloque de upselling y la calculadora (+1.260 €/mes), cerraduras, verificación de identidad, Veri*Factu y el resumen de integraciones (para acortar y centrar la página en SES). Se mantiene el texto legal actual bajo el botón [validar con DPO].
[POR COMPROBAR] "+45 países" (página actual) frente a "+20 países" (cifra oficial del traspaso); no se usa ninguna de las dos.
