# Traspaso de Chekin Connect

Guía para pasar el proyecto a un portátil nuevo y a cuentas de empresa. **No contiene contraseñas.**

## 1. Qué hay y dónde vive

| Pieza | Dónde está hoy | Notas |
|---|---|---|
| Base de datos (usuarios, contactos, eventos, webinars, actividad, fotos) | Supabase · proyecto `lxjefebmndcbnoxlyykw` (UE-oeste-1), cuenta `alexandre.santana@chekin.com` | Ya es de empresa. Añade a otro responsable como propietario (Organization → Team). |
| Web publicada | Vercel · proyecto `qrsaleschekin` (raíz del proyecto = `sales-card`), dominios `qrsaleschekin.vercel.app` y `chekin-sales-card.vercel.app` | Hoy en una cuenta personal. Mover a la cuenta de empresa. |
| Código | GitHub · `alexsantanajimenez-afk/Alexsantanagrowth`, rama `ccr-a117993b-4zv2fe` (es la que se despliega) | Hoy personal. Mover a una organización de empresa. |
| Fuentes para seguir editando | `tools/sales-card/` en este mismo repositorio | Plantilla, compilación, logos, pruebas. |
| Contraseñas iniciales de las cuentas | **Fuera del repositorio** (se entregaron por mensaje privado) | Guardarlas en el gestor de contraseñas de empresa. Cada persona debe cambiarla al entrar. |

## 2. Cuentas de la app (emails)
- **Administradores (Growth):** alexandre.santana@, carlos.cedres@, valery@, irene.decastro@ (todos @chekin.com). Ven y gestionan todo.
- **Account Executives:** marta.cunha@, giulia@, pablo.rodriguez@, manuel.sanchez@, joan.herrera@, rocco@ (@chekin.com). Slugs: marta, giulia, pablo, manuel, joan, rocco. Cada uno ve solo su ficha y sus contactos.
- Entrada: `https://qrsaleschekin.vercel.app/` (panel, solo admins) y `/mi-perfil` (perfil de cada persona). Al primer acceso se obliga a cambiar la contraseña.

### Dar de alta a otra persona (AE o admin)
Las cuentas se crean por SQL (el panel no puede crear usuarios). Genera una contraseña y su hash bcrypt en tu equipo:
```python
import secrets, bcrypt
al = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
pw = "-".join("".join(secrets.choice(al) for _ in range(5)) for _ in range(4))
print(pw); print(bcrypt.hashpw(pw.encode(), bcrypt.gensalt(10, prefix=b"2b")).decode())
```
Y ejecuta en el editor SQL de Supabase (cambia los valores entre `<>`):
```sql
do $$ declare v_id uuid := gen_random_uuid(); begin
  insert into auth.users (instance_id,id,aud,role,email,encrypted_password,email_confirmed_at,raw_app_meta_data,raw_user_meta_data,created_at,updated_at,confirmation_token,recovery_token,email_change_token_new,email_change)
  values ('00000000-0000-0000-0000-000000000000',v_id,'authenticated','authenticated','<email>','<hash bcrypt>',now(),'{"provider":"email","providers":["email"]}','{}',now(),now(),'','','','');
  insert into auth.identities (id,user_id,provider_id,identity_data,provider,last_sign_in_at,created_at,updated_at)
  values (gen_random_uuid(),v_id,v_id::text,jsonb_build_object('sub',v_id::text,'email','<email>','email_verified',true),'email',now(),now(),now());
  insert into public.profiles (id,email,role,slug,name,title,phone,contact_email,must_change_password)
  values (v_id,'<email>','<ae|admin>','<slug o null si es admin>','<Nombre>','Account Executive','','<email>',<true para ae | false para admin>);
end $$;
```
Darlo de baja: `update public.profiles set active=false where email='<email>';` (la tarjeta deja de mostrarse). Para borrar del todo, antes hay que borrar o reasignar sus contactos.

## 3. Pasos para el portátil nuevo y cuentas de empresa
1. **Cuentas de empresa:** crea (o usa) una cuenta de **GitHub** y otra de **Vercel** con el email de Chekin, idealmente una organización/equipo de empresa.
2. **Claude:** instala Claude Code (o usa claude.ai/code) e inicia sesión con el email de Chekin. En claude.ai → Personalizar → Conectores, conecta GitHub, Vercel y Supabase con las cuentas de empresa.
3. **Código a GitHub de empresa:** crea un repositorio vacío en la organización y empuja este (`git remote add empresa <url>` y `git push empresa --all`), o transfiere el actual (Settings → Transfer).
4. **Vercel de empresa:** Add New → Project → importa el repositorio de empresa. Ajustes: *Root Directory* = `sales-card`, sin *build command* (sitio estático). Elige la rama de producción (`ccr-a117993b-4zv2fe`, o renómbrala a `main` y cámbialo en Vercel). Desde entonces cada push despliega solo.
5. **Dominio:** el nuevo proyecto tendrá su propia dirección `*.vercel.app`; añade el dominio definitivo (por ejemplo uno de chekin.com) en *Settings → Domains*. Los QR ya impresos apuntan a `qrsaleschekin.vercel.app`: mientras esa dirección siga activa funcionan; si se retira, hay que regenerar los QR (el panel los genera con la dirección desde la que se abre).
6. **Supabase:** no cambia. Comprueba en *Authentication → URL configuration* que la dirección nueva esté permitida si algún día se usan enlaces de correo.
7. **Portátil:** `git clone <repositorio de empresa>`, abre Claude Code dentro de la carpeta (leerá `CLAUDE.md`) y pide: «lee docs/TRASPASO.md y dime el estado del proyecto».
8. **Seguridad tras el traspaso:** guarda las contraseñas en el gestor de empresa, cambia las que se compartieron por chat y retira del equipo anterior los accesos personales a GitHub y Vercel.

## 4. Operación del día a día
- **Eventos y webinars:** panel → pestañas *Eventos* / *Webinars* → «+ Añadir», «Asignar» (o arrastra un AE sobre el evento). Automáticos: se activan solos (1 día antes por defecto; webinars el mismo día) y se apagan al terminar.
- **Contactos:** cada AE los ve en su perfil; los admins en `/mi-perfil` (todos, con exportación CSV y tabla de leads por evento/webinar).
- **Presentaciones:** pestaña *Presentaciones* del panel (tabla tipo × idioma, con «Ver» y copiar enlace).
- **Cambiar la app:** edita `tools/sales-card/app-template.html` y sigue el flujo de `CLAUDE.md`.

## 5. Riesgos conocidos
- Supabase gratuito se **pausa por inactividad** y tiene límites: pasar a Pro antes de ferias importantes.
- Las contraseñas de AE/admin solo existen cifradas en la base: si alguien la olvida, hay que generar una nueva (apartado 2).
- Los contactos son datos personales (RGPD): consentimiento en el formulario enlazado a https://chekin.com/privacidad/ (comprobar que esa política es la vigente).
