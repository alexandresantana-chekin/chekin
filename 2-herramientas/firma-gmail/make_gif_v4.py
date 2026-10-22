"""GIF del logo de Chekin para la firma de Gmail · versión 4: zoom fuerte hacia el check + cohete de luz blanca por la «e».
Uso: python3 make_gif_v4.py <logo-hi.png> <salida.gif> <ancho_px>"""
import math, sys
import numpy as np
from PIL import Image

src, out, W = sys.argv[1], sys.argv[2], int(sys.argv[3])
SS = 3                                            # se dibuja a 3x y se reduce: bordes suaves
HI = 4                                            # el zoom se toma de una versión 4x más grande para que el check no salga borroso
hi = Image.open(src).convert("RGB")

def compose(scale):
    """Lienzo blanco con el logo pegado a la izquierda (alineado con el texto de la firma), a `scale` veces el tamaño de trabajo."""
    lw = int(W * 0.94 * SS * scale)
    lg = hi.resize((lw, round(hi.height * lw / hi.width)), Image.LANCZOS)
    cw, ch = W * SS * scale, round(lg.height * 1.30)
    c = Image.new("RGB", (cw, ch), (255, 255, 255))
    top = (ch - lg.height) // 2
    c.paste(lg, (SS * scale, top))
    return c, lw, lg.height, top

base, LW, LH, TOP = compose(1)
big, _, _, _ = compose(HI)
CW, CH = base.size
H = CH // SS
BASE = np.asarray(base).astype(np.float32)

# puntos clave medidos en el logo oficial
TICK = (SS + 0.800 * LW, TOP + 0.177 * LH)        # centro del check
E_Y = TOP + 0.710 * LH                            # altura del centro de la «e» (por aquí pasa el cohete)

def zoom(t, S=3.0):   # 3x: el check entero cabe en el alto del GIF
    """Cámara que se lanza hacia el check: t=0 logo normal, t=1 el check ampliado S veces y centrado."""
    if t <= 0:
        return base
    s = 1 + (S - 1) * t
    # el check va de su sitio al centro de la pantalla mientras crece: así nunca se sale por arriba
    px, py = TICK[0] + (CW / 2 - TICK[0]) * t, TICK[1] + (CH / 2 - TICK[1]) * t
    ccx = TICK[0] - (px - CW / 2) / s
    ccy = TICK[1] - (py - CH / 2) / s
    # píxel de salida (x, y) ← punto del lienzo grande: (cc + (x − centro)/s) · HI
    a = HI / s
    return big.transform((CW, CH), Image.AFFINE,
                         (a, 0, HI * ccx - a * CW / 2, 0, a, HI * ccy - a * CH / 2),
                         resample=Image.BICUBIC, fillcolor=(255, 255, 255))

yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
GLOW = np.array([185, 200, 255], np.float32)      # halo azul claro sobre el fondo blanco
WHITE = np.array([255, 255, 255], np.float32)     # luz blanca sobre las letras
def comet(img, head_x, fade):
    """Cohete a la altura de la «e»: cabeza brillante y estela que se afina y se apaga."""
    tail = CW * 0.60
    d = head_x - xx
    along = np.where((d >= 0) & (d <= tail), 1 - d / tail, 0.0) ** 1.4
    thick = SS * (1.0 + 2.4 * along)
    across = np.exp(-((yy - E_Y) / np.maximum(thick, 0.5)) ** 2)
    a = np.minimum(1.0, 1.0 * along * across) * (1 - fade)
    dark = 1 - img.mean(axis=2, keepdims=True) / 255
    col = GLOW * (1 - dark) + WHITE * dark
    out = img * (1 - a[..., None]) + col * a[..., None]
    head = np.exp(-(((xx - head_x) / (SS * 4.5)) ** 2 + ((yy - E_Y) / (SS * 3.0)) ** 2)) * (1 - fade)
    core = np.exp(-(((xx - head_x) / (SS * 1.8)) ** 2 + ((yy - E_Y) / (SS * 1.3)) ** 2)) * (1 - fade)
    out = out * (1 - head[..., None]) + col * head[..., None]
    out = out * (1 - core[..., None]) + WHITE * core[..., None]
    return out

def frame(img):
    if isinstance(img, np.ndarray):
        img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    return img.resize((W, H), Image.LANCZOS)

ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))
MS = 40
frames, durs = [], []
add = lambda im, ms: (frames.append(frame(im)), durs.append(ms))

add(base, 1000)                                               # quieto
for i in range(1, 21): add(zoom(ease(i / 20)), 50)            # se acerca al check (1 s)
add(zoom(1.0), 600)                                           # check en grande, entero
for i in range(1, 21): add(zoom(ease(1 - i / 20)), 50)        # vuelve al logo (1 s)
add(base, 300)
n = 32                                                        # cohete cruzando, más lento (1,6 s)
for i in range(n + 1):
    add(comet(BASE, -CW * 0.05 + ease(i / n) * CW * 1.15, 0.0), 50)
for i in range(1, 11):                                        # la estela se apaga (0,5 s)
    add(comet(BASE, CW * 1.10, i / 10), 50)
add(base, 1400)                                               # quieto antes de repetir

pal = [f.quantize(colors=40, method=Image.Quantize.MEDIANCUT) for f in frames]
pal[0].save(out, save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(out, f"{W}x{H}", len(frames), "frames", sum(durs), "ms")
