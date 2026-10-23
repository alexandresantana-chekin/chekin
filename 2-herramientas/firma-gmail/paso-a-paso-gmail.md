# Logo animado de Chekin en la firma de Gmail

Enlace del GIF (público): https://chekin-sales-card-navy.vercel.app/firma/chekin-firma.gif

1. Gmail → rueda ⚙️ → **Ver todos los ajustes** → pestaña **General** → apartado **Firma**.
2. **Crear nueva** → nombre: `Chekin`.
3. Escribe tu nombre (en negrita) y debajo tu cargo.
4. En la línea siguiente, pulsa el icono **Insertar imagen** → pestaña **Dirección web (URL)** → pega el enlace del GIF → **Seleccionar**.
5. Si sale muy grande, haz clic en la imagen y elige **Original**.
6. Debajo, tu email y chekin.com.
7. En **Valores predeterminados de firma**, elige `Chekin` para correos nuevos y para respuestas.
8. Baja del todo y pulsa **Guardar cambios**.

En Outlook de escritorio el GIF no se mueve: se ve el primer fotograma, que es el logo completo.

Archivo definitivo: `chekin-firma-DEFINITIVA.gif` (= versión 5, 200 px). Script: `make_gif_v5.py`.


## Foto de perfil de Google animada (comprobado por Alex el 23/10)
Carlos quiere la **versión cuadrada** para todo. Google no admite oficialmente GIF animados como foto de perfil, pero con este GIF (cuadrado, 200×200, 183 KB) **funciona**: se ve animado en el círculo de Gmail.
1. Pásate al móvil el archivo `chekin-firma-cuadrada-DEFINITIVA.gif`.
2. Desde el **móvil**: myaccount.google.com → Información personal → Foto → Cambiar → elige el GIF → Guardar. (Desde el ordenador puede quedarse fija.)
3. Si en algún sitio sale fija, la alternativa es `chekin-foto-perfil-google.png` (mismo diseño, 1024 px).
La versión cuadrada **no está en Vercel** (decisión de Alex): se comparte como archivo.


## Foto de perfil con la foto de la persona (23/10)
Definitiva de Carlos: `chekin-perfil-carlos-DEFINITIVA.gif` (200×200, 166 KB, ~10 s en bucle). Foto quieta 2,2 s → el azul sale del centro y la cubre (1,4 s) → animación del check → el logo se encoge hacia el centro y vuelve la foto (1,4 s).
Para otra persona (foto cuadrada o de cara en `fotos/`):
`python3 make_gif_persona.py fotos/<nombre>.png chekin-perfil-<nombre>-DEFINITIVA.gif 200 255 2 10 nada circulo 12 1400`
Tiene que quedar por debajo de ~200 KB para que Google la anime. Subir desde el móvil. Las fotos y sus GIF no se suben al repositorio (.gitignore).
