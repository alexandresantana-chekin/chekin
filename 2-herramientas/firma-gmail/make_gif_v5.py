"""GIF del logo de Chekin para la firma de Gmail · versión 5:
el cohete de luz cruza por la «e», sube y choca con el check, el check destella y la cámara se lanza hacia él.
Uso: python3 make_gif_v5.py <logo-hi.png> <salida.gif> <ancho_px>"""
import math, sys
import numpy as np
from PIL import Image

src, out, W = sys.argv[1], sys.argv[2], int(sys.argv[3])
SS, HI = 3, 4                                     # 3x para bordes suaves; el zoom sale de un lienzo 4x más grande
hi = Image.open(src).convert("RGB")

def compose(scale):
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
TICK = (SS + 0.800 * LW, TOP + 0.177 * LH)        # centro del check (medido en el logo oficial)
E_Y = TOP + 0.710 * LH                            # altura del centro de la «e»

WHITE = np.array([255, 255, 255], np.float32)
GLOW = np.array([185, 200, 255], np.float32)

def tick_mask(arr):
    b = arr[..., 2]; r = arr[..., 0]
    return np.clip((b - r - 60) / 80, 0, 1)       # 1 donde está el azul del check

def flashed(img_arr, k):
    """El check se ilumina hacia blanco azulado (k de 0 a 1)."""
    m = tick_mask(img_arr)[..., None] * k
    return img_arr * (1 - m * 0.75) + np.array([225, 232, 255], np.float32) * m * 0.75

BIG = np.asarray(big).astype(np.float32)
BIG_FLASH = Image.fromarray(np.clip(flashed(BIG, 1.0), 0, 255).astype(np.uint8))

def zoom(t, src_img, S=3.0):
    if t <= 0:
        return np.asarray(src_img.resize((CW, CH), Image.LANCZOS)).astype(np.float32) if src_img is not big else BASE
    s = 1 + (S - 1) * t
    px, py = TICK[0] + (CW / 2 - TICK[0]) * t, TICK[1] + (CH / 2 - TICK[1]) * t   # el check va al centro mientras crece
    ccx, ccy = TICK[0] - (px - CW / 2) / s, TICK[1] - (py - CH / 2) / s
    a = HI / s
    im = src_img.transform((CW, CH), Image.AFFINE, (a, 0, HI * ccx - a * CW / 2, 0, a, HI * ccy - a * CH / 2),
                           resample=Image.BICUBIC, fillcolor=(255, 255, 255))
    return np.asarray(im).astype(np.float32)

# ---------- recorrido del cohete: recto por la «e» y curva hacia arriba hasta el check ----------
def bez(p0, p1, p2, t):
    return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
A = (-0.06 * CW, E_Y); B = (0.58 * CW, E_Y); C = (TICK[0] + 0.02 * CW, E_Y); D = TICK
pts = [(A[0] + (B[0] - A[0]) * i / 200, E_Y) for i in range(200)] + [bez(B, C, D, i / 120) for i in range(121)]
P = np.array(pts, np.float32)
seg = np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
TOTAL = seg[-1]
def at(L):
    L = float(np.clip(L, 0, TOTAL)); i = int(np.searchsorted(seg, L))
    i = max(1, min(i, len(P) - 1)); f = (L - seg[i - 1]) / max(seg[i] - seg[i - 1], 1e-6)
    return P[i - 1] + (P[i] - P[i - 1]) * f

yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
def comet(img, head_L, fade):
    """Estela: manchas de luz a lo largo del recorrido, más finas y tenues cuanto más atrás."""
    tail = CW * 0.55
    a = np.zeros((CH, CW), np.float32)
    for j in range(110):
        k = j / 109                                   # 0 = cabeza, 1 = final de la estela
        L = head_L - k * tail
        if L < 0:
            break
        x, y = at(L)
        w = SS * (3.4 - 2.6 * k)
        g = np.exp(-(((xx - x) / (w * 1.6)) ** 2 + ((yy - y) / w) ** 2)) * (1 - k) ** 1.3
        a = np.maximum(a, g)
    a *= (1 - fade)
    dark = 1 - img.mean(axis=2, keepdims=True) / 255
    col = GLOW * (1 - dark) + WHITE * dark
    out = img * (1 - a[..., None]) + col * a[..., None]
    hx, hy = at(head_L)
    core = np.exp(-(((xx - hx) / (SS * 1.8)) ** 2 + ((yy - hy) / (SS * 1.3)) ** 2)) * (1 - fade)
    return out * (1 - core[..., None]) + WHITE * core[..., None]

def burst(img, k):
    """Destello al chocar: el check se ilumina y sale un halo que se abre y se apaga."""
    out = flashed(img, min(1.0, k * 1.6))
    r = np.hypot((xx - TICK[0]) / 1.4, yy - TICK[1])
    rad = SS * (6 + 26 * k)
    ring = np.exp(-((r - rad) / (SS * 3.0)) ** 2) * (1 - k) * 0.55
    return out * (1 - ring[..., None]) + GLOW * ring[..., None]

def frame(arr):
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)

ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))
frames, durs = [], []
add = lambda a, ms: (frames.append(frame(a)), durs.append(ms))

add(BASE, 900)                                                    # quieto
n = 36                                                            # el cohete recorre la «e» y sube al check (1,8 s)
for i in range(n + 1):
    add(comet(BASE, ease(i / n) * TOTAL, 0.0), 50)
for i in range(1, 6):                                             # choque: la estela se apaga y el check destella
    add(burst(comet(BASE, TOTAL, i / 5), i / 5), 50)
for i in range(1, 21):                                            # la cámara se lanza al check; el destello se va apagando
    t = ease(i / 20); k = max(0.0, 1 - i / 12)
    z = zoom(t, BIG_FLASH) * k + zoom(t, big) * (1 - k)
    add(z, 50)
add(zoom(1.0, big), 600)                                          # check en grande, entero
for i in range(1, 21):                                            # vuelve al logo
    add(zoom(ease(1 - i / 20), big), 50)
add(BASE, 1500)                                                   # quieto antes de repetir

pal = [f.quantize(colors=40, method=Image.Quantize.MEDIANCUT) for f in frames]
pal[0].save(out, save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(out, f"{W}x{H}", len(frames), "frames", sum(durs), "ms")
