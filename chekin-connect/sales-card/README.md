# Chekin Connect · Sales Team

Una sola página (`index.html`, sin dependencias externas salvo la fuente de Google) con tres pantallas según la URL:

| URL | Quién la abre | Qué ve |
|---|---|---|
| `index.html` | Administración (Marketing/Sales Ops) | Evento activo, equipo de ventas, leads y ajustes |
| `index.html?r=<slug>` | Cada comercial, en su móvil | Su **QR personal** (azul Chekin, con el cohete) |
| `index.html?c=<slug>` | El cliente, al escanear el QR | Tarjeta simple con 4 acciones: *Escríbeme* (WhatsApp o email), *Guardar contacto* (vCard con foto), *Ver presentación* (según su tipo de negocio) y *Agendar demo*. Sin formulario. |
| `index.html?team=1` | Público | Página del equipo: foto, nombre y cargo; filtro por evento; cada tarjeta lleva a su comercial |

El QR de cada comercial apunta a `?c=<su slug>`. Los QR son reales (librería `qrcode-generator`, MIT, incluida dentro del archivo).

## Qué se administra desde la página principal
- **Comerciales:** vienen **6 en blanco ya creados** (Comercial 1 a 6), cada uno con su enlace y su QR real, marcados *Por completar*. Al editarlos (nombre, cargo, foto…) su enlace y su QR **no cambian**, así que se pueden imprimir ya. Además, alta, edición y baja. Nombre, enlace (slug), cargo ES/EN, teléfono, email, LinkedIn, calendario propio, foto y activo/inactivo. Cada ficha muestra su QR, copia su enlace y descarga el QR en PNG para imprimir.
- **Eventos:** lista de eventos (nombre, fechas, lugar). Cada evento tiene su **equipo**: se asigna arrastrando un comercial sobre el evento (o con el botón *Asignar*) y se quita con la ×. Puede haber **varios eventos activos a la vez**, cada uno con su equipo. Los pasados se archivan y conservan sus leads. Los QR no cambian al cambiar de evento.
- **Reglas de evento:** el evento de un comercial es el primer evento *activo* al que está asignado. Si no tiene ninguno, su QR sigue funcionando para captación general y sus leads quedan como *Sin evento*. Si un comercial está en dos eventos activos, el panel avisa del conflicto.
- **Actividad:** (sustituye a los leads del formulario) aperturas, contactos guardados, mensajes por WhatsApp/email, presentaciones vistas por tipo de negocio, demos y compartidos; filtro por evento (incluye *Sin evento*), totales, comparativa por evento, por comercial, tabla completa y exportación a CSV. Cada lead guarda el evento activo en el momento de captarlo.
- **Ajustes:** dirección pública de la web (a donde apuntan los QR), enlaces de prueba gratuita, web, LinkedIn y calendario por defecto.

## Estado actual: DEMO
Los datos se guardan en `localStorage` del navegador, así que sirve para ver y probar todo el flujo en un mismo dispositivo. Un cliente que escanea desde otro móvil **no verá** los comerciales creados aquí hasta que haya backend.

## Para producción (pendiente, cuando haya cuentas de empresa)
1. **Notion de empresa** como base: tablas Comerciales, Eventos y Leads. La función `load()/persist()` de `index.html` es el único punto que se sustituye por llamadas a la API.
2. **Vercel de empresa:** funciones `api/` que leen comerciales y evento, y escriben los leads con la llave de Notion como variable de entorno (nunca en el HTML).
3. **Proteger la administración** (la página principal): contraseña/login de Vercel, o una ruta de admin separada. En la demo está abierta.
4. **Consentimiento RGPD** en el formulario, enlace real de la prueba gratuita y de calendario.
5. Poner la **dirección pública** en Ajustes para que los QR apunten al dominio final.

## Acceso del comercial en su móvil
Cada comercial recibe su enlace (`?r=<slug>`) con el botón **Enviar acceso** del panel (abre WhatsApp o email con el mensaje listo; si no hay teléfono ni email, lo copia). Al abrirlo ve su QR y un aviso para **añadirlo a la pantalla de inicio**; también puede **descargar el QR como imagen** (funciona sin cobertura) y **ver cómo lo ve el cliente**.

## Base de datos común (Supabase) · octubre 2026

Proyecto de Supabase en la organización **Chekin** (región eu-west-1). El esquema está en `supabase/migrations/`.

- **Perfiles** (`profiles`): un usuario por persona (email de Chekin + contraseña). Dos tipos: `admin` (Growth: ven todo) y `ae` (Account Executive: solo lo suyo).
  Un Account Executive solo puede cambiar su teléfono, email de contacto, enlace de Calendly y foto; no puede cambiar su nombre, cargo ni permisos.
- **Contactos** (`leads`): los que deja el cliente en la tarjeta (nombre, apellido, teléfono, email, nº de propiedades, consentimiento). El cliente solo puede **enviar** (función `submit_lead`); no puede leer nada. Cada Account Executive ve solo los suyos.
- **Fotos**: almacén `avatars`, cada persona escribe solo en su carpeta.
- **Primer acceso**: la contraseña provisional obliga a elegir una propia (`must_change_password`).

### Rutas
- `/?c=<slug>` tarjeta del cliente (pública). Lee el perfil actualizado del Account Executive; el QR no cambia aunque cambie su foto, teléfono o Calendly.
- `/?r=<slug>` pantalla de QR (pública).
- `/mi-perfil` (o `/?me=1`) entrada de cada persona: Account Executive → su perfil y sus contactos; administración → todos los contactos (filtro por Account Executive, CSV).
- `/` panel de eventos, QR y equipo (acceso con el email y la contraseña individuales de cada admin de Growth; los eventos y su asignación a los AE están en Supabase, tabla `events`).

### Presentaciones
HTML en `presentaciones/` (`hotels-en.html` es la versión corta para QR; `hotels-en-completa.html` la larga). El botón «Ver presentación» abre la del tipo de negocio en el idioma de la tarjeta; si no existe, en inglés; si tampoco, la página web. Faltan: vacation rental e italiano.

### Pendiente
- URL exacta de la política de privacidad (`PRIVACY_URL` en `index.html`) y texto legal revisado.
- Pasar a plan Pro de Supabase antes de depender de la herramienta en ferias (el gratuito pausa por inactividad).
- Eventos y Account Executives del panel siguen en el navegador de cada administrador; falta llevarlos a la base de datos.
- Conexión con HubSpot.
