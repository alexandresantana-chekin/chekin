-- Eventos compartidos por todo el equipo (antes vivían en el navegador de quien los creaba)
create table public.events (
  id text primary key,
  name text not null check (char_length(name) between 1 and 200),
  date_from date, date_to date,
  time_txt text not null default '',
  loc text not null default '', city text not null default '',
  auto boolean not null default false,
  active boolean not null default false,
  archived boolean not null default false,
  reps text[] not null default '{}',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
alter table public.events enable row level security;
create policy events_admin_all on public.events for all to authenticated using (public.is_admin()) with check (public.is_admin());
revoke all on public.events from anon;
grant select, insert, update, delete on public.events to authenticated;
create or replace function public.events_touch() returns trigger language plpgsql as $$ begin new.updated_at := now(); return new; end $$;
create trigger events_touch before update on public.events for each row execute function public.events_touch();
-- Evento actual de un Account Executive (lo ve el cliente al escanear): solo id, nombre, ciudad y lugar
create or replace function public.current_event(p_slug text)
returns table(id text, name text, city text, loc text)
language sql stable security definer set search_path = public as $$
  select e.id, e.name, e.city, e.loc from public.events e
  where not e.archived and p_slug = any(e.reps)
    and (case when e.auto
              then e.date_from is not null and (now() at time zone 'Europe/Madrid')::date between e.date_from and coalesce(e.date_to, e.date_from)
              else e.active end)
  order by e.date_from nulls last, e.created_at limit 1
$$;
revoke all on function public.current_event(text) from public;
grant execute on function public.current_event(text) to anon, authenticated;
