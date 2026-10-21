-- Eventos presenciales y webinars en la misma tabla, separados por «kind» para medir la calidad del lead por separado
alter table public.events add column kind text not null default 'event' check (kind in ('event','webinar'));
create index events_kind_idx on public.events (kind);
