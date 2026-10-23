-- Demos pedidas: cuándo pidió demo cada contacto (botón «Agendar demo» de la tarjeta).
-- Antes solo se sabía si el contacto ENTRÓ por «Agendar demo» (channel = 'demo'); si ya había dejado
-- sus datos y después pulsaba «Agendar demo», la petición solo quedaba como un clic anónimo en activity.

alter table public.leads
  add column if not exists demo_first_at timestamptz,
  add column if not exists demo_last_at timestamptz,
  add column if not exists demo_clicks integer not null default 0;

-- Contactos que ya entraron por «Agendar demo»: su petición es la fecha de alta
update public.leads
   set demo_first_at = created_at, demo_last_at = created_at, demo_clicks = 1
 where channel = 'demo' and demo_first_at is null;

-- Los nuevos contactos que entren por «Agendar demo» llevan ya la fecha de la petición
create or replace function public.leads_demo_on_insert() returns trigger
language plpgsql set search_path = public as $$
begin
  if new.channel = 'demo' and new.demo_first_at is null then
    new.demo_first_at := new.created_at;
    new.demo_last_at := new.created_at;
    new.demo_clicks := 1;
  end if;
  return new;
end $$;
drop trigger if exists leads_demo_on_insert on public.leads;
create trigger leads_demo_on_insert before insert on public.leads
  for each row execute function public.leads_demo_on_insert();

-- El cliente (sin cuenta) que ya dejó sus datos y pulsa «Agendar demo»: se apunta en su contacto.
-- Solo toca las fechas de demo del contacto más reciente de ese email con ese Account Executive; no lee nada.
create or replace function public.mark_demo_request(p_slug text, p_email text)
returns void language plpgsql security definer set search_path = public as $$
declare
  v_id uuid;
  v_email text := lower(btrim(coalesce(p_email, '')));
begin
  if v_email = '' then return; end if;
  select l.id into v_id
    from public.leads l join public.profiles p on p.id = l.ae_id
   where p.slug = lower(btrim(coalesce(p_slug, ''))) and lower(l.email) = v_email
   order by l.created_at desc limit 1;
  if v_id is null then return; end if;
  update public.leads
     set demo_first_at = coalesce(demo_first_at, now()),
         demo_last_at = now(),
         demo_clicks = demo_clicks + 1
   where id = v_id
     and (demo_last_at is null or demo_last_at < now() - interval '10 seconds');   -- doble toque: no suma
end $$;
revoke all on function public.mark_demo_request(text, text) from public;
grant execute on function public.mark_demo_request(text, text) to anon, authenticated;
