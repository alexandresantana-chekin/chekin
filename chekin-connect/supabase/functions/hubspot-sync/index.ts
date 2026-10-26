// Chekin Connect → HubSpot: cada contacto nuevo de la app se envía a HubSpot marcado con su evento o webinar.
// Lo dispara el disparador leads_to_hubspot (INSERT en public.leads, migración 20261027) con la cabecera x-webhook-secret.
// Se despliega sin verificación de JWT (--no-verify-jwt): la protección es esa clave (secreto WEBHOOK_SECRET).
// Secreto necesario en Supabase (Edge Functions → Secrets): HUBSPOT_TOKEN (token de la app privada de HubSpot).
// Reglas: si el contacto ya existe en HubSpot no se cambian propietario ni etapa; solo se rellenan campos vacíos, «Last MQL type» pasa a Event, Webinar o Digital QR («MQL Type» solo si estaba vacío) y se añade una nota con el evento.

const HS = "https://api.hubapi.com";
const SB_URL = Deno.env.get("SUPABASE_URL")!;
const SB_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const HS_TOKEN = Deno.env.get("HUBSPOT_TOKEN") ?? "";

type Lead = {
  id: string; ae_id: string; ae_slug: string; event_name: string; event_city: string;
  first_name: string; last_name: string; phone: string; email: string; properties: number | null;
  channel: string; company?: string; country?: string; comments?: string; created_at: string;
};

async function hs(path: string, init: RequestInit = {}) {
  const r = await fetch(HS + path, { ...init, headers: { Authorization: `Bearer ${HS_TOKEN}`, "Content-Type": "application/json", ...(init.headers ?? {}) } });
  const txt = await r.text();
  const data = txt ? JSON.parse(txt) : null;
  if (!r.ok) throw new Error(`HubSpot ${r.status}: ${data?.message ?? txt}`.slice(0, 500));
  return data;
}
async function sb(path: string, init: RequestInit = {}) {
  const r = await fetch(SB_URL + path, { ...init, headers: { apikey: SB_KEY, Authorization: `Bearer ${SB_KEY}`, "Content-Type": "application/json", ...(init.headers ?? {}) } });
  const txt = await r.text();
  return txt ? JSON.parse(txt) : null;
}

async function originOf(l: Lead) {
  if (!l.event_name) return "Chekin Connect · Sin evento";
  const ev = await sb(`/rest/v1/events?name=eq.${encodeURIComponent(l.event_name)}&select=kind&limit=1`);
  return ev?.[0]?.kind === "webinar" ? "Chekin Connect · Webinar" : "Chekin Connect · Evento";
}

// Valor de «MQL Type» (form_type) y «Last MQL type» (last_form_type) en HubSpot. «Digital QR» es la opción
// de esas dos propiedades para quien deja sus datos sin evento ni webinar (creada en HubSpot el 26/10).
function mqlTypeOf(origin: string) {
  if (origin.endsWith("Webinar")) return "Webinar";
  if (origin.endsWith("Evento")) return "Event";
  return "Digital QR";
}

async function ownerFor(aeId: string) {
  const p = await sb(`/rest/v1/profiles?id=eq.${aeId}&select=email,name`);
  const email = p?.[0]?.email;
  if (!email) return { ownerId: null, aeName: "" };
  const o = await hs(`/crm/v3/owners/?email=${encodeURIComponent(email)}&limit=1`);
  return { ownerId: o?.results?.[0]?.id ?? null, aeName: p[0].name ?? email };
}

async function sync(l: Lead) {
  const origin = await originOf(l);
  const mqlType = mqlTypeOf(origin);
  const evento = l.event_name ? l.event_name + (l.event_city ? ` · ${l.event_city}` : "") : "";
  const { ownerId, aeName } = await ownerFor(l.ae_id);
  const data: Record<string, string> = {
    firstname: l.first_name, lastname: l.last_name ?? "", phone: l.phone ?? "", company: l.company ?? "",
    country: l.country ?? "", number_of_units: l.properties == null ? "" : String(l.properties),
  };
  const fill = Object.keys(data);

  let id: string | null = null, existing: Record<string, string> = {};
  if (l.email) {
    const s = await hs("/crm/v3/objects/contacts/search", { method: "POST", body: JSON.stringify({
      filterGroups: [{ filters: [{ propertyName: "email", operator: "EQ", value: l.email }] }], properties: [...fill, "form_type"], limit: 1 }) });
    if (s?.results?.[0]) { id = s.results[0].id; existing = s.results[0].properties ?? {}; }
  }

  if (id) {   // ya existía: solo campos vacíos + «Last MQL type»; «MQL Type» solo si estaba vacío
    const props: Record<string, string> = { last_form_type: mqlType };
    if (!existing.form_type) props.form_type = mqlType;
    for (const k of fill) if (data[k] && !existing[k]) props[k] = data[k];
    await hs(`/crm/v3/objects/contacts/${id}`, { method: "PATCH", body: JSON.stringify({ properties: props }) });
  } else {
    const props: Record<string, string> = { email: l.email ?? "", form_type: mqlType, last_form_type: mqlType, lifecyclestage: "lead", hs_lead_status: "NEW" };
    for (const k of fill) if (data[k]) props[k] = data[k];
    if (ownerId) props.hubspot_owner_id = String(ownerId);
    if (!props.email) delete props.email;
    const c = await hs("/crm/v3/objects/contacts", { method: "POST", body: JSON.stringify({ properties: props }) });
    id = c.id;
  }

  const lines = [`${origin}${evento ? " · " + evento : ""}`, `Captado por: ${aeName}`, l.channel === "scan" ? "Tarjeta de visita escaneada por el AE" : `Canal: ${l.channel}`];
  if (l.comments) lines.push(`Comentarios: ${l.comments}`);
  await hs("/crm/v3/objects/notes", { method: "POST", body: JSON.stringify({
    properties: { hs_timestamp: new Date(l.created_at).toISOString(), hs_note_body: lines.join("<br>") },
    associations: [{ to: { id }, types: [{ associationCategory: "HUBSPOT_DEFINED", associationTypeId: 202 }] }] }) });
  return id;
}

Deno.serve(async (req) => {
  // Solo la base de datos puede llamar a la función: el disparador de public.leads manda esta clave (guardada en Vault).
  const secret = Deno.env.get("WEBHOOK_SECRET") ?? "";
  if (!secret || req.headers.get("x-webhook-secret") !== secret) return new Response("forbidden", { status: 401 });
  let lead: Lead | null = null;
  try {
    const body = await req.json();
    if (body?.type !== "INSERT" || body?.table !== "leads") return new Response("ignored", { status: 200 });
    lead = body.record as Lead;
    if (!HS_TOKEN) throw new Error("Falta el secreto HUBSPOT_TOKEN");
    const id = await sync(lead);
    await sb(`/rest/v1/leads?id=eq.${lead.id}`, { method: "PATCH", body: JSON.stringify({ hubspot_contact_id: String(id), hubspot_synced_at: new Date().toISOString(), hubspot_error: "" }) });
    return new Response(JSON.stringify({ ok: true, id }), { status: 200, headers: { "Content-Type": "application/json" } });
  } catch (e) {
    const msg = String((e as Error)?.message ?? e).slice(0, 500);
    if (lead?.id) await sb(`/rest/v1/leads?id=eq.${lead.id}`, { method: "PATCH", body: JSON.stringify({ hubspot_error: msg }) }).catch(() => {});
    console.error(msg);
    return new Response(JSON.stringify({ ok: false, error: msg }), { status: 200, headers: { "Content-Type": "application/json" } });
  }
});
