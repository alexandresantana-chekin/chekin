-- Actividad anónima de las tarjetas, común a todo el equipo
create table public.activity (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  action text not null check (action in ('open','save','wa','mail','deck','demo','share')),
  ae_slug text not null,
  event_id text not null default '',
  extra text not null default ''
);
create index activity_created_idx on public.activity (created_at desc);
create index activity_slug_idx on public.activity (ae_slug);
alter table public.activity enable row level security;
create policy activity_select on public.activity for select to authenticated
  using (public.is_admin() or ae_slug = (select p.slug from public.profiles p where p.id = auth.uid()));
create policy activity_delete_admin on public.activity for delete to authenticated using (public.is_admin());
revoke all on public.activity from anon, authenticated;
grant select, delete on public.activity to authenticated;
create or replace function public.track_activity(p_slug text, p_action text, p_event_id text default '', p_extra text default '')
returns void language plpgsql security definer set search_path = public as $$
begin
  if p_action not in ('open','save','wa','mail','deck','demo','share') then return; end if;
  if not exists (select 1 from public.profiles where slug = p_slug and role = 'ae' and active) then return; end if;
  insert into public.activity (action, ae_slug, event_id, extra)
  values (p_action, p_slug, left(coalesce(p_event_id,''), 80), left(coalesce(p_extra,''), 40));
end $$;
revoke all on function public.track_activity(text,text,text,text) from public;
grant execute on function public.track_activity(text,text,text,text) to anon, authenticated;
