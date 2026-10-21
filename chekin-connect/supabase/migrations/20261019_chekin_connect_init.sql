-- Chekin Connect · perfiles de Account Executives, contactos (leads) y fotos
-- Cada Account Executive ve y edita solo lo suyo; los administradores ven todo.

create extension if not exists pgcrypto with schema extensions;

-- ============ PERFILES ============
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  role text not null default 'ae' check (role in ('admin','ae')),
  slug text unique,
  name text not null,
  title text not null default 'Account Executive',
  phone text not null default '',
  contact_email text not null default '',
  calendly_url text not null default '',
  photo_path text not null default '',
  active boolean not null default true,
  must_change_password boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint profiles_email_lower check (email = lower(email)),
  constraint profiles_slug_fmt check (slug is null or slug ~ '^[a-z0-9-]{2,40}$'),
  constraint profiles_len check (char_length(name) <= 120 and char_length(title) <= 80 and char_length(phone) <= 40
    and char_length(contact_email) <= 200 and char_length(calendly_url) <= 300 and char_length(photo_path) <= 200)
);
create unique index profiles_email_key on public.profiles (email);
alter table public.profiles enable row level security;

create or replace function public.is_admin() returns boolean
language sql security definer stable set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin' and active);
$$;
revoke all on function public.is_admin() from public, anon;
grant execute on function public.is_admin() to authenticated;

-- permisos: anónimo solo ve los datos públicos de la tarjeta; el resto, nada
revoke all on public.profiles from anon, authenticated;
grant select (slug, name, title, phone, contact_email, calendly_url, photo_path, updated_at) on public.profiles to anon;
grant select, update on public.profiles to authenticated;

create policy profiles_public_card on public.profiles for select to anon
  using (role = 'ae' and active and slug is not null);
create policy profiles_select_own_or_admin on public.profiles for select to authenticated
  using (id = auth.uid() or public.is_admin());
create policy profiles_update_own_or_admin on public.profiles for update to authenticated
  using (id = auth.uid() or public.is_admin())
  with check (id = auth.uid() or public.is_admin());

-- un Account Executive solo puede cambiar teléfono, email de contacto, Calendly y foto
create or replace function public.profiles_guard() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  new.updated_at := now();
  if auth.uid() is not null and current_setting('app.bypass_guard', true) is distinct from '1' and not public.is_admin() then
    new.id := old.id; new.email := old.email; new.role := old.role; new.slug := old.slug;
    new.name := old.name; new.title := old.title; new.active := old.active;
    new.must_change_password := old.must_change_password; new.created_at := old.created_at;
    if new.photo_path <> old.photo_path and new.photo_path <> '' and new.photo_path not like auth.uid()::text || '/%' then
      raise exception 'invalid_photo_path' using errcode = '42501';
    end if;
  end if;
  return new;
end $$;
create trigger profiles_guard before update on public.profiles for each row execute function public.profiles_guard();

create or replace function public.mark_password_changed() returns void
language plpgsql security definer set search_path = public as $$
begin
  perform set_config('app.bypass_guard', '1', true);
  update public.profiles set must_change_password = false where id = auth.uid();
end $$;
revoke all on function public.mark_password_changed() from public, anon;
grant execute on function public.mark_password_changed() to authenticated;

-- ============ CONTACTOS (LEADS) ============
create table public.leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  ae_id uuid not null references public.profiles(id) on delete restrict,
  ae_slug text not null,
  event_name text not null default '',
  event_city text not null default '',
  first_name text not null,
  last_name text not null,
  phone text not null,
  email text not null,
  properties integer not null check (properties between 0 and 100000),
  channel text not null default 'card' check (channel in ('whatsapp','email','demo','card')),
  consent boolean not null check (consent),
  consent_version text not null default 'v1-2026-10',
  lang text not null default 'es',
  constraint leads_len check (char_length(first_name) <= 80 and char_length(last_name) <= 120 and char_length(phone) <= 40
    and char_length(email) <= 200 and char_length(event_name) <= 200 and char_length(event_city) <= 120)
);
create index leads_ae_created on public.leads (ae_id, created_at desc);
alter table public.leads enable row level security;

revoke all on public.leads from anon, authenticated;
grant select, delete on public.leads to authenticated;
create policy leads_select on public.leads for select to authenticated
  using (ae_id = auth.uid() or public.is_admin());
create policy leads_delete_admin on public.leads for delete to authenticated
  using (public.is_admin());

-- el cliente (sin cuenta) solo puede ENVIAR un contacto, validado; no puede leer ninguno
create or replace function public.submit_lead(
  p_slug text, p_first text, p_last text, p_phone text, p_email text, p_properties integer,
  p_consent boolean, p_channel text default 'card', p_event_name text default '',
  p_event_city text default '', p_lang text default 'es', p_hp text default ''
) returns uuid
language plpgsql security definer set search_path = public as $$
declare
  v_ae uuid; v_id uuid;
  v_email text := lower(btrim(coalesce(p_email, '')));
  v_phone text := btrim(coalesce(p_phone, ''));
  v_first text := btrim(coalesce(p_first, ''));
  v_last text := btrim(coalesce(p_last, ''));
begin
  if coalesce(p_hp, '') <> '' then return gen_random_uuid(); end if;            -- bots: se ignora sin avisar
  if p_consent is not true then raise exception 'consent_required' using errcode = '22023'; end if;
  if v_email !~ '^[^@[:space:]]+@[^@[:space:]]+\.[^@[:space:]]{2,}$' then raise exception 'invalid_email' using errcode = '22023'; end if;
  if char_length(v_first) < 2 or char_length(v_last) < 2 then raise exception 'invalid_name' using errcode = '22023'; end if;
  if char_length(regexp_replace(v_phone, '\D', '', 'g')) < 7 then raise exception 'invalid_phone' using errcode = '22023'; end if;
  if p_properties is null or p_properties < 0 or p_properties > 100000 then raise exception 'invalid_properties' using errcode = '22023'; end if;
  if p_channel not in ('whatsapp','email','demo','card') then p_channel := 'card'; end if;

  select id into v_ae from public.profiles where slug = lower(btrim(coalesce(p_slug, ''))) and role = 'ae' and active;
  if v_ae is null then raise exception 'unknown_ae' using errcode = '22023'; end if;

  if (select count(*) from public.leads where ae_id = v_ae and created_at > now() - interval '1 minute') >= 30 then
    raise exception 'rate_limited' using errcode = '22023';
  end if;

  select id into v_id from public.leads
   where ae_id = v_ae and lower(email) = v_email and created_at > now() - interval '1 minute'
   order by created_at desc limit 1;
  if v_id is not null then return v_id; end if;                                  -- doble toque: no duplica

  insert into public.leads (ae_id, ae_slug, event_name, event_city, first_name, last_name, phone, email, properties, channel, consent, lang)
  values (v_ae, lower(btrim(p_slug)), left(coalesce(p_event_name, ''), 200), left(coalesce(p_event_city, ''), 120),
          left(v_first, 80), left(v_last, 120), left(v_phone, 40), left(v_email, 200), p_properties, p_channel, true,
          case when p_lang in ('es','en') then p_lang else 'es' end)
  returning id into v_id;
  return v_id;
end $$;
revoke all on function public.submit_lead(text,text,text,text,text,integer,boolean,text,text,text,text,text) from public;
grant execute on function public.submit_lead(text,text,text,text,text,integer,boolean,text,text,text,text,text) to anon, authenticated;

-- ============ FOTOS ============
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('avatars', 'avatars', true, 1048576, array['image/jpeg','image/png','image/webp'])
on conflict (id) do update set public = true, file_size_limit = 1048576, allowed_mime_types = excluded.allowed_mime_types;

create policy avatars_insert_own on storage.objects for insert to authenticated
  with check (bucket_id = 'avatars' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()));
create policy avatars_update_own on storage.objects for update to authenticated
  using (bucket_id = 'avatars' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()))
  with check (bucket_id = 'avatars' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()));
create policy avatars_delete_own on storage.objects for delete to authenticated
  using (bucket_id = 'avatars' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()));

-- (añadido después) permiso de lectura de su propia carpeta de fotos, necesario para reemplazar/borrar la foto anterior
create policy avatars_select_own on storage.objects for select to authenticated
  using (bucket_id = 'avatars' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()));
-- (añadido después) la función interna del control de cambios no debe poder llamarse desde fuera
revoke all on function public.profiles_guard() from public, anon, authenticated;
