"""GIF del logo de Chekin para la firma de Gmail · versión 2: zoom ojo de pez + cohete de luz con estela.
Uso: python3 make_gif_v2.py <logo-hi.png> <salida.gif> <ancho_px>"""
import math, sys
import numpy as np
from PIL import Image

src, out, W = sys.argv[1], sys.argv[2], int(sys.argv[3])
SS = 3                                            # se dibuja a 3x y se reduce: bordes suaves
logo = Image.open(src).convert("RGB")
LW = int(W * 0.94 * SS)
logo = logo.resize((LW, round(logo.height * LW / logo.width)), Image.LANCZOS)
CW = W * SS
CH = round(logo.height * 1.30)
H = CH // SS
base = Image.new("RGB", (CW, CH), (255, 255, 255))
base.paste(logo, (SS, (CH - logo.height) // 2))   # pegado a la izquierda: alineado con el texto de la firma
BASE = np.asarray(base).astype(np.float32)

yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
cx, cy = CW / 2, CH / 2
RX, RY = CW * 0.62, CH * 1.25                    # tamaño de la "lente" (elipse, el logo es ancho)
nx, ny = (xx - cx) / RX, (yy - cy) / RY
r = np.sqrt(nx * nx + ny * ny)

def fisheye(k):
    """k = fuerza del ojo de pez (0 = nada). El centro se acerca más que los bordes; fuera de la lente no cambia."""
    if k <= 0:
        return BASE
    f = np.where(r < 1, 1 - k * (1 - r) ** 2, 1.0)   # lente: el centro se amplía 1/(1−k) y el borde de la lente queda igual
    sx = np.clip(cx + nx * f * RX, 0, CW - 1)
    sy = np.clip(cy + ny * f * RY, 0, CH - 1)
    x0, y0 = np.floor(sx).astype(int), np.floor(sy).astype(int)
    x1, y1 = np.minimum(x0 + 1, CW - 1), np.minimum(y0 + 1, CH - 1)
    ax, ay = (sx - x0)[..., None], (sy - y0)[..., None]
    return (BASE[y0, x0] * (1 - ax) * (1 - ay) + BASE[y0, x1] * ax * (1 - ay)
            + BASE[y1, x0] * (1 - ax) * ay + BASE[y1, x1] * ax * ay)

BLUE = np.array([56, 91, 248], np.float32)        # azul Chekin
GLOW = np.array([170, 190, 255], np.float32)      # azul claro: estela y cabeza sobre las letras
def comet(img, head_x, fade):
    """Cohete por el medio: cabeza brillante en head_x y estela detrás que se apaga (fade 0..1 = cuánto se ha desvanecido)."""
    tail = CW * 0.55
    d = head_x - xx                                   # distancia por detrás de la cabeza
    along = np.where((d >= 0) & (d <= tail), 1 - d / tail, 0.0) ** 1.6
    thick = SS * (0.5 + 1.3 * along)                  # la estela se afina hacia atrás
    across = np.exp(-((yy - cy) / np.maximum(thick, 0.5)) ** 2)
    a = 0.85 * along * across * (1 - fade)
    dark = (1 - img.mean(axis=2, keepdims=True) / 255)            # 0 sobre blanco, 1 sobre las letras
    col = BLUE * (1 - dark) + GLOW * dark                         # azul sobre blanco, azul claro sobre las letras
    out = img * (1 - a[..., None]) + col * a[..., None]
    head = np.exp(-(((xx - head_x) / (SS * 3.6)) ** 2 + ((yy - cy) / (SS * 2.4)) ** 2)) * (1 - fade)
    core = np.exp(-(((xx - head_x) / (SS * 1.4)) ** 2 + ((yy - cy) / (SS * 1.0)) ** 2)) * (1 - fade)
    out = out * (1 - head[..., None] * 0.85) + col * head[..., None] * 0.85
    out = out * (1 - core[..., None]) + np.array([235, 240, 255], np.float32) * core[..., None]   # núcleo casi blanco
    return out

def to_frame(arr):
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    return im.resize((W, H), Image.LANCZOS)

ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))
MS = 40
frames, durs = [], []
add = lambda a, ms: (frames.append(to_frame(a)), durs.append(ms))

add(BASE, 1000)                                               # quieto
n = 18                                                        # ojo de pez: sube y vuelve (0,7 s)
for i in range(1, n + 1):
    add(fisheye(0.16 * math.sin(math.pi * i / n)), MS)
add(BASE, 240)
n = 30                                                        # cohete cruzando (1,2 s)
for i in range(n + 1):
    hx = -CW * 0.05 + ease(i / n) * CW * 1.15
    add(comet(BASE, hx, 0.0), MS)
n = 14                                                        # la estela se desvanece (0,56 s)
for i in range(1, n + 1):
    add(comet(BASE, CW * 1.10, i / n), MS)
add(BASE, 1600)                                               # quieto antes de repetir

pal = [f.quantize(colors=64, method=Image.Quantize.MEDIANCUT) for f in frames]
pal[0].save(out, save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(out, f"{W}x{H}", len(frames), "frames", sum(durs), "ms")
