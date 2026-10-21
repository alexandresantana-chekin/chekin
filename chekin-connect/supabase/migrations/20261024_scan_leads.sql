-- Escáner de tarjetas: el Account Executive fotografía la tarjeta de visita de un contacto y lo guarda a su nombre.
-- Solo AÑADE campos y una función: el formulario del cliente (submit_lead) sigue funcionando igual.

alter table public.leads
  add column company text not null default '',
  add column country text not null default '',
  add column comments text not null default '',
  add column legal_basis text not null default 'consent' check (legal_basis in ('consent','card_given'));

-- en una tarjeta puede no saberse el nº de propiedades
alter table public.leads alter column properties drop not null;

-- consentimiento del cliente, o tarjeta entregada al Account Executive (interés legítimo)
alter table public.leads drop constraint if exists leads_consent_check;
alter table public.leads add constraint leads_consent_or_card check (consent or legal_basis = 'card_given');

alter table public.leads drop constraint if exists leads_channel_check;
alter table public.leads add constraint leads_channel_check check (channel in ('whatsapp','email','demo','card','scan'));

alter table public.leads add constraint leads_len_scan check (char_length(company) <= 200 and char_length(country) <= 80 and char_length(comments) <= 1000);

-- el Account Executive (con sesión) guarda un contacto escaneado a su nombre; nunca a nombre de otro
create or replace function public.add_scanned_lead(
  p_first text, p_last text, p_company text, p_phone text, p_email text,
  p_country text, p_properties integer, p_comments text, p_card_given boolean,
  p_event_name text default '', p_event_city text default '', p_lang text default 'es'
) returns uuid
language plpgsql security definer set search_path = public as $$
declare
  v_me public.profiles; v_id uuid;
  v_email text := lower(btrim(coalesce(p_email, '')));
  v_phone text := btrim(coalesce(p_phone, ''));
  v_first text := btrim(coalesce(p_first, ''));
  v_last text := btrim(coalesce(p_last, ''));
  v_digits int := char_length(regexp_replace(coalesce(p_phone, ''), '\D', '', 'g'));
begin
  select * into v_me from public.profiles where id = auth.uid() and active;
  if v_me.id is null then raise exception 'not_allowed' using errcode = '42501'; end if;
  if p_card_given is not true then raise exception 'card_required' using errcode = '22023'; end if;
  if char_length(v_first) < 1 then raise exception 'invalid_name' using errcode = '22023'; end if;
  if v_email <> '' and v_email !~ '^[^@[:space:]]+@[^@[:space:]]+\.[^@[:space:]]{2,}$' then raise exception 'invalid_email' using errcode = '22023'; end if;
  if v_phone <> '' and v_digits < 7 then raise exception 'invalid_phone' using errcode = '22023'; end if;
  if v_email = '' and v_phone = '' then raise exception 'contact_required' using errcode = '22023'; end if;
  if p_properties is not null and (p_properties < 0 or p_properties > 100000) then raise exception 'invalid_properties' using errcode = '22023'; end if;

  if (select count(*) from public.leads where ae_id = v_me.id and created_at > now() - interval '1 minute') >= 30 then
    raise exception 'rate_limited' using errcode = '22023';
  end if;

  select id into v_id from public.leads                                          -- doble toque: no duplica
   where ae_id = v_me.id and channel = 'scan' and created_at > now() - interval '1 minute'
     and ((v_email <> '' and lower(email) = v_email) or (v_email = '' and phone = v_phone))
   order by created_at desc limit 1;
  if v_id is not null then return v_id; end if;

  insert into public.leads (ae_id, ae_slug, event_name, event_city, first_name, last_name, phone, email, properties,
                            channel, consent, legal_basis, company, country, comments, lang)
  values (v_me.id, coalesce(v_me.slug, ''), left(coalesce(p_event_name, ''), 200), left(coalesce(p_event_city, ''), 120),
          left(v_first, 80), left(v_last, 120), left(v_phone, 40), left(v_email, 200), p_properties,
          'scan', false, 'card_given', left(btrim(coalesce(p_company, '')), 200), left(btrim(coalesce(p_country, '')), 80),
          left(btrim(coalesce(p_comments, '')), 1000), case when p_lang in ('es','en') then p_lang else 'es' end)
  returning id into v_id;
  return v_id;
end $$;
revoke all on function public.add_scanned_lead(text,text,text,text,text,text,integer,text,boolean,text,text,text) from public, anon;
grant execute on function public.add_scanned_lead(text,text,text,text,text,text,integer,text,boolean,text,text,text) to authenticated;
