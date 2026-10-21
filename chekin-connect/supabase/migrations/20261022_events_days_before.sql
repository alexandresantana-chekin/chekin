-- Activación automática de eventos: desde las 00:00 de «days_before» días antes (por defecto 1) hasta el final de su último día
alter table public.events add column days_before smallint not null default 1 check (days_before between 0 and 7);
create or replace function public.current_event(p_slug text)
returns table(id text, name text, city text, loc text)
language sql stable security definer set search_path = public as $$
  select e.id, e.name, e.city, e.loc from public.events e
  where not e.archived and p_slug = any(e.reps)
    and (case when e.auto
              then e.date_from is not null
                   and (now() at time zone 'Europe/Madrid')::date between (e.date_from - e.days_before) and coalesce(e.date_to, e.date_from)
              else e.active end)
  order by e.date_from nulls last, e.created_at limit 1
$$;
revoke all on function public.current_event(text) from public;
grant execute on function public.current_event(text) to anon, authenticated;
