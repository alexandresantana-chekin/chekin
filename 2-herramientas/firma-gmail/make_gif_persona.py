"""Foto de perfil animada: la foto de la persona (acercamiento lento) → un círculo azul Chekin la tapa →
la animación cuadrada del check (chekin-firma-cuadrada-DEFINITIVA.gif) → la foto vuelve a abrirse en círculo.
Uso: python3 make_gif_persona.py fotos/carlos.png salida.gif [lado=200] [colores_foto=96]
Pensado para la foto de perfil de Google: cuadrado y por debajo de ~200 KB (si pesa más, puede quedarse fija)."""
import math, os, sys
from PIL import Image, ImageDraw

foto, out = sys.argv[1], sys.argv[2]
S = int(sys.argv[3]) if len(sys.argv) > 3 else 200
COL = int(sys.argv[4]) if len(sys.argv) > 4 else 96
STEP = int(sys.argv[5]) if len(sys.argv) > 5 else 1      # 2 = usa uno de cada dos fotogramas del logo (pesa menos)
NZ = int(sys.argv[6]) if len(sys.argv) > 6 else 8        # fotogramas del acercamiento a la foto
BLUE = (56, 91, 248)
here = os.path.dirname(os.path.abspath(__file__))
ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))

src = Image.open(foto).convert("RGB")
w, h = src.size; k = min(w, h)
src = src.crop(((w - k) // 2, (h - k) // 2, (w - k) // 2 + k, (h - k) // 2 + k))
BIG = 4 * S
src = src.resize((BIG, BIG), Image.LANCZOS)

def photo(z, cx=0.52, cy=0.40):
    """Acercamiento z (1 = foto entera) centrado hacia la cara."""
    side = BIG / z
    x0 = min(max(cx * BIG - side / 2, 0), BIG - side); y0 = min(max(cy * BIG - side / 2, 0), BIG - side)
    return src.crop((int(x0), int(y0), int(x0 + side), int(y0 + side))).resize((S, S), Image.LANCZOS)

def circle_mask(r):
    m = Image.new("L", (S * 4, S * 4), 0)
    c = S * 2; R = r * S * 4 * 0.75
    ImageDraw.Draw(m).ellipse((c - R, c - R, c + R, c + R), fill=255)
    return m.resize((S, S), Image.LANCZOS)

# Fotogramas del logo (animación cuadrada definitiva), sin su primer fotograma quieto
logo = Image.open(os.path.join(here, "chekin-firma-cuadrada-DEFINITIVA.gif"))
lf, ld = [], []
for i in range(logo.n_frames):
    logo.seek(i); lf.append(logo.convert("RGB").resize((S, S), Image.LANCZOS)); ld.append(logo.info.get("duration", 50))
blue = Image.new("RGB", (S, S), BLUE)

frames, durs, kinds = [], [], []
add = lambda im, ms, kind: (frames.append(im), durs.append(ms), kinds.append(kind))
MODE = sys.argv[7] if len(sys.argv) > 7 else "anillo"
base = photo(1.0)
if MODE == "zoom":
    Z = 1.10
    add(base, 700, "foto")                                    # primer fotograma: la foto (lo que se ve si no se anima)
    for i in range(1, NZ + 1):                                # acercamiento lento a la cara
        add(photo(1 + (Z - 1) * ease(i / NZ)), round(1440 / NZ), "foto")
    last = photo(Z)
elif MODE == "nada":
    add(base, 2200, "foto")                                   # foto quieta
    last = base
else:
    def ring(p):                                              # anillo azul que se dibuja en el borde del círculo de perfil
        im = base.copy().resize((S * 4, S * 4), Image.LANCZOS); d = ImageDraw.Draw(im)
        m = S * 4 * 0.035; w = int(S * 4 * 0.045)
        if p > 0: d.arc((m, m, S * 4 - m, S * 4 - m), -90, -90 + 360 * p, fill=BLUE, width=w)
        return im.resize((S, S), Image.LANCZOS)
    add(base, 900, "foto")                                    # primer fotograma: la foto quieta
    for i in range(1, NZ + 1):
        add(ring(ease(i / NZ)), 70, "foto")
    add(ring(1), 600, "foto")
    last = ring(1)
TRANS = sys.argv[8] if len(sys.argv) > 8 else "circulo"
NF = int(sys.argv[9]) if len(sys.argv) > 9 else 8             # pasos de la transición
TMS = int(sys.argv[10]) if len(sys.argv) > 10 else 400         # duración de cada transición, en ms
first_logo = lf[1]
for i in range(1, NF + 1):                                    # transición foto → logo (fondo azul)
    if TRANS == "fundido": add(Image.blend(last, first_logo, ease(i / NF)), TMS // NF, "mix")
    else: add(Image.composite(blue, last, circle_mask(ease(i / NF))), TMS // NF, "mix")
body_f, body_d = lf[1:], ld[1:]
for j in range(0, len(body_f), STEP):                         # la animación del check (con STEP>1, menos fotogramas y más largos)
    add(body_f[j], sum(body_d[j:j + STEP]), "logo")
end = lf[-1]
for i in range(1, NF + 1):                                    # transición logo → foto
    if TRANS == "fundido": add(Image.blend(end, base, ease(i / NF)), TMS // NF, "mix")
    else: add(Image.composite(end, base, circle_mask(ease(1 - i / NF))), TMS // NF, "mix")   # el círculo del logo se encoge hacia el centro (lo contrario de la entrada)

ref = Image.new("RGB", (S, S * 2)); ref.paste(base, (0, 0)); ref.paste(blue, (0, S))
try: fpal = ref.quantize(colors=COL, method=Image.Quantize.LIBIMAGEQUANT)   # mejor color en la piel, si está disponible
except Exception: fpal = ref.quantize(colors=COL, method=Image.Quantize.MAXCOVERAGE)
pal = []
for im, kind in zip(frames, kinds):
    pal.append(im.quantize(palette=fpal, dither=Image.Dither.NONE) if kind != "logo" else im.quantize(colors=48, method=Image.Quantize.MEDIANCUT))
pal[0].save(out, save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=True, disposal=1)
print("fotogramas del logo:", len(body_f))
print(out, f"{S}x{S}", len(pal), "fotogramas", round(sum(durs) / 1000, 1), "s", os.path.getsize(out) // 1024, "KB")
