"""GIF del logo de Chekin para la firma de Gmail: zoom suave y destello de luz de izquierda a derecha.
Uso: python3 make_gif.py <logo-hi.png> <salida.gif> <ancho_px>"""
import math, sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

src, out, W = sys.argv[1], sys.argv[2], int(sys.argv[3])
SS = 3                                   # supermuestreo: se dibuja a 3x y se reduce, para bordes suaves
logo = Image.open(src).convert("RGB")
LW = int(W * 0.90 * SS)                  # el logo ocupa el 90 % del ancho; el zoom crece hacia la derecha
logo = logo.resize((LW, round(logo.height * LW / logo.width)), Image.LANCZOS)
mask = ImageOps.invert(logo.convert("L")).point(lambda v: min(255, v * 2))   # dónde hay logo (para el destello)
CW, CH = W * SS, round(logo.height * 1.30)
H = CH // SS

def ease(t):  # entrada y salida suaves
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))

def frame(scale, shine):
    """scale: tamaño del logo (1 = normal). shine: posición del destello de 0 a 1, o None."""
    img = logo
    if shine is not None:
        band = Image.new("L", (img.width * 2, img.height), 0)
        d = ImageDraw.Draw(band)
        bw = img.width * 0.12
        cx = -bw * 1.5 + shine * (img.width + bw * 3)
        for i in range(int(bw * 2)):                          # banda con degradado (más intensa en el centro)
            x = cx - bw + i
            a = int(185 * math.exp(-((i - bw) / (bw * 0.42)) ** 2))
            d.line([(x + img.height * 0.35, 0), (x - img.height * 0.35, img.height)], fill=a)
        band = band.crop((0, 0, img.width, img.height)).filter(ImageFilter.GaussianBlur(SS * 2))
        m = ImageChops.multiply(band, mask)
        img = Image.composite(Image.new("RGB", img.size, (226, 232, 255)), img, m)   # luz plateada azulada, no blanca
    w, h = round(img.width * scale), round(img.height * scale)
    img = img.resize((w, h), Image.LANCZOS)
    canvas = Image.new("RGB", (CW, CH), (255, 255, 255))
    canvas.paste(img, (SS, (CH - h) // 2))   # pegado a la izquierda: alineado con el nombre de la firma
    return canvas.resize((W, H), Image.LANCZOS)

FPS_MS = 40                      # 25 fotogramas por segundo
frames, durs = [], []
def add(img, ms):
    frames.append(img); durs.append(ms)

add(frame(1.0, None), 1200)                                   # quieto
n = 22                                                        # zoom: sube a 1,08 y vuelve (0,9 s)
for i in range(1, n + 1):
    add(frame(1.0 + 0.08 * math.sin(math.pi * i / n), None), FPS_MS)
add(frame(1.0, None), 200)
n = 28                                                        # destello de luz (1,1 s)
for i in range(n + 1):
    add(frame(1.0, ease(i / n)), FPS_MS)
add(frame(1.0, None), 1800)                                   # quieto antes de repetir

pal = [f.quantize(colors=96, method=Image.Quantize.MEDIANCUT) for f in frames]
pal[0].save(out, save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(out, f"{W}x{H}", len(frames), "frames", sum(durs), "ms")
