-- Reenvío a HubSpot de los contactos de Chekin Connect que todavía no están allí (sin hubspot_contact_id).
-- Uso puntual en Supabase → SQL Editor. Hace lo mismo que el disparador leads_to_hubspot: llama a la función
-- hubspot-sync con la clave de Vault, un contacto cada vez. La función no duplica (busca por email) y no cambia
-- propietario ni etapa de los contactos que ya existían en HubSpot.

-- PASO 1 · Vista previa (solo lee): qué se va a enviar.
select l.created_at::date as alta, l.ae_slug as ae, coalesce(nullif(l.event_name, ''), '(sin evento)') as evento,
       l.channel as canal, nullif(l.hubspot_error, '') as error_anterior
from public.leads l
where coalesce(l.hubspot_contact_id, '') = ''
order by l.created_at;

-- PASO 2 · Envío. Ejecutar solo tras revisar el paso 1. Selecciona desde «do $$» hasta «end $$;» y pulsa Run.
do $$
declare v_secret text; r record; n int := 0;
begin
  select decrypted_secret into v_secret from vault.decrypted_secrets where name = 'hubspot_webhook_secret' limit 1;
  if v_secret is null then raise exception 'Falta la clave hubspot_webhook_secret en Vault'; end if;
  for r in select * from public.leads where coalesce(hubspot_contact_id, '') = '' order by created_at loop
    perform net.http_post(
      url := 'https://lxjefebmndcbnoxlyykw.supabase.co/functions/v1/hubspot-sync',
      headers := jsonb_build_object('Content-Type', 'application/json', 'x-webhook-secret', v_secret),
      body := jsonb_build_object('type', 'INSERT', 'table', 'leads', 'record', to_jsonb(r))
    );
    n := n + 1;
  end loop;
  raise notice 'Enviados a la cola: %', n;
end $$;

-- PASO 3 · Comprobación (1–2 minutos después): enviados y errores.
select count(*) filter (where coalesce(hubspot_contact_id, '') <> '') as en_hubspot,
       count(*) filter (where coalesce(hubspot_contact_id, '') = '' and coalesce(hubspot_error, '') <> '') as con_error,
       count(*) filter (where coalesce(hubspot_contact_id, '') = '' and coalesce(hubspot_error, '') = '') as pendientes
from public.leads;
