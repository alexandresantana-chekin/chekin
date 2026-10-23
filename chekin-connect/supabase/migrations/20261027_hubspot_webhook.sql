-- Cada contacto nuevo se envía a HubSpot: el disparador llama a la función hubspot-sync (pg_net, asíncrono).
-- La clave compartida va en Vault (nombre 'hubspot_webhook_secret'), nunca en el repositorio; la misma clave es el secreto
-- WEBHOOK_SECRET de la función. Si falta la clave, el contacto se guarda igual y no se envía.
create extension if not exists pg_net;

create or replace function public.leads_to_hubspot() returns trigger
language plpgsql security definer set search_path = public as $$
declare v_secret text;
begin
  select decrypted_secret into v_secret from vault.decrypted_secrets where name = 'hubspot_webhook_secret' limit 1;
  if v_secret is null then return new; end if;
  perform net.http_post(
    url := 'https://lxjefebmndcbnoxlyykw.supabase.co/functions/v1/hubspot-sync',
    headers := jsonb_build_object('Content-Type', 'application/json', 'x-webhook-secret', v_secret),
    body := jsonb_build_object('type', 'INSERT', 'table', 'leads', 'record', to_jsonb(new))
  );
  return new;
exception when others then
  return new;   -- el envío a HubSpot nunca impide guardar el contacto
end $$;
revoke all on function public.leads_to_hubspot() from public, anon, authenticated;

drop trigger if exists leads_to_hubspot on public.leads;
create trigger leads_to_hubspot after insert on public.leads
  for each row execute function public.leads_to_hubspot();
