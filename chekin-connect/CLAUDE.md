# Chekin Connect · instrucciones para Claude Code

Sistema de tarjetas digitales + QR del equipo comercial de Chekin (Chekin Sales Team). Lee primero `docs/TRASPASO.md` (qué hay, dónde vive cada servicio, cuentas) y este archivo.

## Cómo trabajar con la persona responsable (importante)
- **Idioma: español.** Respuestas claras, sin jerga; la persona no escribe código y quiere ver capturas o comprobaciones visibles.
- **No ejecutes ni construyas nada sin su OK explícito** (ni HTML, ni apps, ni código) cuando la petición sea una pregunta o una propuesta. Primero explica y propón; actúa cuando diga "ok", "hazlo", etc.
- **No toques Notion** ni cuentas de empresa que no se hayan pedido.
- No publiques en producción sin que lo haya pedido o aprobado en esa misma conversación.
- Antes de decir que algo funciona, pruébalo (pruebas en `tools/sales-card/tests`, capturas con Playwright). Si no puedes abrir la web publicada, dilo.
- Nunca escribas contraseñas, claves de servicio ni tokens en el repositorio ni en mensajes.

## Estructura del repositorio
```
sales-card/                  ← lo que se publica (Vercel, raíz = sales-card)
  index.html                 ← GENERADO (no editar a mano)
  presentaciones/            ← presentaciones HTML (hoteles, alquiler vacacional, italiano de hoteles)
  vercel.json                ← reescribe /mi-perfil → /index.html
tools/sales-card/            ← fuentes para seguir editando
  app-template.html          ← LA APP (HTML+CSS+JS en un solo archivo, con marcadores __QRLIB__ __ICON__ __LOGO__ __LOGOW__)
  build.py                   ← compila el template → sales-card/index.html
  assets/                    ← librería de QR, icono, logos oficiales SVG
  decks/                     ← scripts para (re)generar/parchear presentaciones
  tests/                     ← pruebas Playwright con Supabase simulado (run.sh)
supabase/migrations/         ← esquema de la base (en orden de fecha; aplicado en producción hasta 20261023; 20261024_scan_leads PENDIENTE)
landing-evento/index.html    ← landing del evento de Madrid (archivo único, sin conectar a nada)
docs/TRASPASO.md            ← guía de traspaso y cuentas
```

## Flujo de trabajo
1. Edita `tools/sales-card/app-template.html`.
2. `python3 tools/sales-card/build.py` (regenera `sales-card/index.html`).
3. Comprueba la sintaxis: extrae el 2.º `<script>` de `index.html` y `node --check`.
4. `CHROMIUM=/ruta/chrome bash tools/sales-card/tests/run.sh` (todas) o `... run.sh web3 days2`. Hay 4 avisos conocidos en `sb.js` (esperaban el selector de presentaciones antiguo).
5. Commit + push. Despliegue: ver `docs/TRASPASO.md` (con Vercel conectado a Git se despliega solo al hacer push).

## Arquitectura de la app (un solo archivo)
- **Rutas por parámetro**: `?c=slug` tarjeta del cliente · `?r=slug` pantalla de QR · `?me=1` o `/mi-perfil` perfil personal (AE y admins) · sin parámetros = panel de administración (pide login; solo admins).
- **Datos**: Supabase (REST/RPC con `fetch`, sin SDK). La clave `anon` está en el código (es pública por diseño; la protección real es RLS). Nunca uses la `service_role` en el navegador.
- **Tablas**: `profiles` (AE y admins; `role`, `slug`, `active`, `must_change_password`…), `leads`, `events` (`kind` event|webinar, `auto`, `active`, `archived`, `reps` (slugs), `days_before`), `activity` (acciones anónimas). Funciones: `is_admin()`, `submit_lead()`, `mark_password_changed()`, `current_event(slug)`, `track_activity(...)`. Bucket `avatars` (fotos).
- **Quién ve qué**: admins (Growth) ven todo; cada AE ve solo su perfil, sus contactos y su QR (RLS). Los clientes (anónimos) solo leen el perfil público del AE, el evento actual (`current_event`) y envían datos con `submit_lead`.
- **Eventos**: un evento automático está activo desde las 00:00 (Europe/Madrid) de `fecha_inicio − days_before` hasta el final de su último día. Si un AE tiene varios activos, se usa el primero por fecha. Los webinars usan `days_before = 0`.
- **Contactos (leads)**: el cliente deja nombre, apellido, teléfono, email, nº de propiedades y consentimiento; se encola en `localStorage` (`chekin-lead-queue`) y se envía a `submit_lead`.
- **Escáner de tarjetas** (perfil del AE, `scanInit`): el AE fotografía la tarjeta de visita; Tesseract.js (CDN jsdelivr, se descarga al primer uso) lee el texto en el móvil y `parseCard` rellena nombre, empresa, teléfono, email y país. El AE añade Country, Number of properties or rooms (opcional) y Comments, marca "me ha dado su tarjeta" y se guarda con `add_scanned_lead` (`channel='scan'`, `legal_basis='card_given'`). Obligatorio: nombre + email o teléfono. Migración `20261024_scan_leads.sql`.
- **Idiomas**: es, en, it, pt (Portugal), fr, de (`LANGS` + `DICT`). Se detecta del móvil; el selector es un desplegable. Lo que falta en un idioma cae a inglés.
- **Presentaciones**: `PRES` en el template. Hoteles y Alquiler vacacional son un archivo multilingüe cada uno (`#es`, `#en`…); Hoteles en italiano es `hotels-it.html` (diseño anterior). Si la tarjeta abre una presentación, se pasa `?card=` para que «← Tarjeta» y «Reservar demo» vuelvan a la tarjeta (`?from=deck&go=demo`).
- **Claves de localStorage**: `chekin-cards-v1`, `chekin-cards-lang`, `chekin-sb-session`, `chekin-lead`, `chekin-lead-queue`, `chekin-act-queue`, `chekin-ev-<slug>`, `chekin-ev-imported`, `chekin-me-email`.

## Sistema de diseño (resumen; el sistema completo lo tiene el equipo de marketing)
Azul principal `#385BF8` (único acento) · textos `#19194B`/`#161643` (nunca negro puro) · grises `#6B6B95` `#9696B9` `#DEDEEB` · rojo `#FF2467` solo errores · degradado `#002CFA→#274BF0` solo en bandas/cabeceras · fondo plano (`#FDFDFF` panel, `#F4F6F9` tarjeta) · botones 12 px (no píldoras en producto), campos 8 px, campos vacíos `#F4F6F8` y con contenido blanco con borde `#161643` · aro de enfoque `0 0 0 3px rgba(56,91,248,.2)` · desactivado = opacidad .3 · hover con capa, sin mover ni cambiar sombra · sombras azuladas `rgba(26,148,255,.173)` · sin emojis en la interfaz · sin exclamaciones en la interfaz · tipografía Montserrat (sustituto de Proxima Nova, que es de pago).

## Pendiente / decisiones abiertas
- HubSpot: sincronizar contactos (token de app privada, propiedad personalizada nº de propiedades, propietario por email del AE, Lead vs SQL).
- Webinars: definir cómo entran los contactos (formulario propio o importación CSV). Fecha del webinar «avvapro ES (Verifactu)».
- Presentaciones que faltan: Campings y Otro; Alquiler vacacional en italiano.
- Traducciones de la tarjeta (it/pt/fr/de) sin revisar por nativos.
- Supabase Pro (el plan gratuito pausa por inactividad) antes de uso crítico.
- Mover GitHub y Vercel a cuentas de empresa (ver `docs/TRASPASO.md`).
- Landing del evento: sin publicar ni conectar a un destino de datos.
