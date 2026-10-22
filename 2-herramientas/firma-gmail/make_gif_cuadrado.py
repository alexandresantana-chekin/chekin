"""Logo de Chekin en cuadrado: fondo azul Chekin y logo en blanco, para la firma de Gmail y la foto de perfil de Google.
El check se dibuja de izquierda a derecha, suelta un destello en anillo y un brillo lo cruza en diagonal.
Uso: python3 make_gif_cuadrado.py <logo-hi.png> <carpeta_salida> [zoom]
(con "zoom": solo el check, con acercamiento y alejamiento y dos destellos, anillo y halo → chekin-cuadrado-zoom-<destello>-*)
Saca, para cada variante (check = solo el check, logo = palabra + check):
  chekin-cuadrado-<variante>-200.gif / -400.gif  (animados, para la firma)
  chekin-cuadrado-<variante>-1024.png             (estático, para la foto de perfil de Google)"""
import math, os, sys
import numpy as np
from PIL import Image

src, outdir = sys.argv[1], sys.argv[2]
BLUE = np.array([56, 91, 248], np.float32)        # azul del check en el logo oficial (#385BF8)
WHITE = np.array([255, 255, 255], np.float32)
R = 1200                                          # lado del lienzo de trabajo; luego se reduce

hi = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
tick_hi = np.clip((hi[..., 2] - hi[..., 0] - 60) / 80, 0, 1)          # 1 donde está el azul del check
text_hi = np.clip((1 - hi.mean(axis=2) / 255 - 0.15) / 0.6, 0, 1) * (1 - tick_hi)   # 1 donde está el texto oscuro


def crop(mask):
    ys, xs = np.where(mask > 0.05)
    return mask[ys.min():ys.max() + 1, xs.min():xs.max() + 1], (xs.min(), ys.min())


def place(mask, width_frac, cx=0.5, cy=0.5):
    """Escala una máscara a una fracción del lado y la centra en el lienzo R×R."""
    h, w = mask.shape
    nw = int(R * width_frac); nh = round(h * nw / w)
    m = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).resize((nw, nh), Image.LANCZOS)).astype(np.float32) / 255
    out = np.zeros((R, R), np.float32)
    x0, y0 = int(R * cx - nw / 2), int(R * cy - nh / 2)
    out[y0:y0 + nh, x0:x0 + nw] = m
    return out


def layouts():
    # Variante "check": solo el check, grande y dentro del círculo de la foto de perfil (cabe en el 62 % central).
    tick_only, _ = crop(tick_hi)
    yield "check", place(tick_only, 0.56, 0.5, 0.52), None
    # Variante "logo": palabra y check en blanco, al 78 % del ancho (el recorte en círculo no toca las esquinas).
    both = np.maximum(text_hi, tick_hi)
    _, (bx, by) = crop(both)
    ys, xs = np.where(both > 0.05)
    t = tick_hi[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    x = text_hi[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    yield "logo", place(t, 0.78), place(x, 0.78)


yy, xx = np.mgrid[0:R, 0:R].astype(np.float32)
ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def render(tick, text, draw, text_in, ring, shine):
    """draw: 0→1 cuánto del check está dibujado; ring: 0→1 destello; shine: 0→1 brillo diagonal."""
    ys, xs = np.where(tick > 0.05)
    x0, x1 = xs.min(), xs.max()
    edge = (x1 - x0) * 0.08
    reveal = np.clip((x0 + (x1 - x0 + edge) * draw - xx) / edge, 0, 1)
    a = tick * reveal
    if text is not None:
        a = np.maximum(a, text * text_in)
    img = BLUE[None, None] * (1 - a[..., None]) + WHITE * a[..., None]
    if ring > 0:
        cx, cy = xs.mean(), ys.mean()
        r = np.hypot(xx - cx, yy - cy)
        rad = (x1 - x0) * (0.35 + 0.9 * ring)
        g = np.exp(-((r - rad) / (R * 0.018)) ** 2) * (1 - ring) * 0.55
        img = img * (1 - g[..., None]) + WHITE * g[..., None]
    if 0 < shine < 1:
        band = (xx + yy) / (2 * R)                     # paralelo al trazo largo del check (45°), avanza de izquierda a derecha
        pos = -0.15 + 1.3 * shine
        s = np.exp(-((band - pos) / 0.035) ** 2) * 0.40
        lit = a * s                                    # el brillo solo se ve sobre el logo blanco…
        glow = s * 0.22                                # …y sobre el fondo azul, que es donde se ve pasar
        img = img + (WHITE - img) * np.maximum(lit, glow)[..., None]
    return img


def frames_for(tick, text):
    fr, du = [], []
    add = lambda arr, ms: (fr.append(arr), du.append(ms))
    has_text = text is not None
    if has_text:
        add(render(tick, text, 0, 0, 0, 0), 300)
        for i in range(1, 9):                          # la palabra aparece
            add(render(tick, text, 0, ease(i / 8), 0, 0), 50)
    else:
        add(render(tick, text, 0, 0, 0, 0), 400)
    for i in range(1, 15):                             # el check se dibuja
        add(render(tick, text, ease(i / 14), 1, 0, 0), 45)
    for i in range(1, 11):                             # destello en anillo
        add(render(tick, text, 1, 1, i / 10, 0), 45)
    add(render(tick, text, 1, 1, 0, 0), 500)
    for i in range(1, 13):                             # brillo diagonal
        add(render(tick, text, 1, 1, 0, i / 13), 45)
    add(render(tick, text, 1, 1, 0, 0), 1800)          # quieto antes de repetir
    return fr, du


def to_img(arr, size):
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).resize((size, size), Image.LANCZOS)


def zoom_variant(flash="anillo"):
    """Solo el check: se dibuja, la cámara se acerca mucho al check, se queda un instante y vuelve con un destello."""
    HI = 3
    tick_only, _ = crop(tick_hi)
    h, w = tick_only.shape
    nw = int(R * HI * 0.62); nh = round(h * nw / w)
    m = Image.fromarray((tick_only * 255).astype(np.uint8)).resize((nw, nh), Image.LANCZOS)
    big = Image.new("L", (R * HI, R * HI), 0)
    big.paste(m, (int(R * HI * 0.5 - nw / 2), int(R * HI * 0.52 - nh / 2)))
    base = np.asarray(big.resize((R, R), Image.LANCZOS)).astype(np.float32) / 255
    ys, xs = np.where(base > 0.05)
    cx, cy = xs.mean(), ys.mean()

    def zoomed(s, t):
        px, py = cx + (R / 2 - cx) * t, cy + (R / 2 - cy) * t          # el check va al centro mientras crece
        a = HI / s
        im = big.transform((R, R), Image.AFFINE, (a, 0, HI * (cx - px / s), 0, a, HI * (cy - py / s)), resample=Image.BICUBIC, fillcolor=0)
        k = np.asarray(im).astype(np.float32)[..., None] / 255
        return BLUE[None, None] * (1 - k) + WHITE * k

    S = 4.0
    fr, du = [], []
    add = lambda arr, ms: (fr.append(arr), du.append(ms))
    add(render(base, None, 1, 1, 0, 0), 1700)          # quieto: el primer fotograma es el check entero (lo que ve Outlook)
    add(render(base, None, 0, 0, 0, 0), 300)
    for i in range(1, 15):                             # el check se dibuja
        add(render(base, None, ease(i / 14), 1, 0, 0), 45)
    add(render(base, None, 1, 1, 0, 0), 350)
    for i in range(1, 19):                             # se acerca mucho
        t = ease(i / 18)
        add(zoomed(1 + (S - 1) * t, t), 45)
    add(zoomed(S, 1), 450)                             # muy de cerca
    for i in range(1, 19):                             # se aleja
        t = ease(1 - i / 18)
        add(zoomed(1 + (S - 1) * t, t), 45)
    if flash == "anillo":
        for i in range(1, 21):                         # destello en anillo, lento
            add(render(base, None, 1, 1, ease(i / 20), 0), 60)
    else:
        from PIL import ImageFilter
        glow = np.asarray(Image.fromarray((base * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(R * 0.025))).astype(np.float32) / 255
        glow = glow * (1 - base)                       # la luz queda fuera del check: el borde sigue nítido
        rest = render(base, None, 1, 1, 0, 0)
        for i in range(1, 19):                         # halo: el check se enciende y la luz se abre a su alrededor
            k = math.sin(math.pi * i / 18)
            img = rest + (WHITE - rest) * np.clip(glow * 1.1 * k, 0, 0.55)[..., None]
            add(img, 60)
        for i in range(1, 15):                         # y un brillo lo cruza en diagonal
            add(render(base, None, 1, 1, 0, i / 15), 55)
    return fr, du


os.makedirs(outdir, exist_ok=True)
if len(sys.argv) > 3 and sys.argv[3] == "zoom":
    for flash in ("anillo", "halo"):
        fr, du = zoom_variant(flash)
        to_img(fr[0], 1024).save(os.path.join(outdir, "chekin-cuadrado-zoom-1024.png"))
        for size in (200, 400):
            imgs = [to_img(f, size).quantize(colors=48, method=Image.Quantize.MEDIANCUT) for f in fr]
            path = os.path.join(outdir, f"chekin-cuadrado-zoom-{flash}-{size}.gif")
            imgs[0].save(path, save_all=True, append_images=imgs[1:], duration=du, loop=0, optimize=True, disposal=1)
            print(path, f"{size}x{size}", len(imgs), "frames", sum(du), "ms", os.path.getsize(path) // 1024, "KB")
    sys.exit(0)
for name, tick, text in layouts():
    fr, du = frames_for(tick, text)
    to_img(fr[-1], 1024).save(os.path.join(outdir, f"chekin-cuadrado-{name}-1024.png"))
    for size in (200, 400):
        imgs = [to_img(f, size).quantize(colors=48, method=Image.Quantize.MEDIANCUT) for f in fr]
        path = os.path.join(outdir, f"chekin-cuadrado-{name}-{size}.gif")
        imgs[0].save(path, save_all=True, append_images=imgs[1:], duration=du, loop=0, optimize=True, disposal=1)
        print(path, f"{size}x{size}", len(imgs), "frames", sum(du), "ms", os.path.getsize(path) // 1024, "KB")
