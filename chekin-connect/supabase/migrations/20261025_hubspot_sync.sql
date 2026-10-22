-- Envío de contactos a HubSpot: estado del envío en cada contacto (lo rellena la función hubspot-sync).
alter table public.leads
  add column hubspot_contact_id text not null default '',
  add column hubspot_synced_at timestamptz,
  add column hubspot_error text not null default '';
