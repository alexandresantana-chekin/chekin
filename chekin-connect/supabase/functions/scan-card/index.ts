// Chekin Connect · lectura de tarjetas de visita con Claude (visión).
// La app (AE con sesión iniciada) envía la foto en base64 y recibe los campos ya separados.
// Secreto necesario en Supabase (Edge Functions → Secrets): ANTHROPIC_API_KEY (cuenta de empresa).
// La clave nunca sale de aquí; la foto no se guarda.

import Anthropic from "npm:@anthropic-ai/sdk";

const client = new Anthropic();   // lee ANTHROPIC_API_KEY del entorno

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...CORS, "Content-Type": "application/json" } });

const FIELDS = ["first_name", "last_name", "company", "job_title", "phone", "email", "website", "country"] as const;
const SCHEMA = {
  type: "object",
  properties: Object.fromEntries(FIELDS.map((f) => [f, { type: "string" }])),
  required: [...FIELDS],
  additionalProperties: false,
};

const PROMPT = `Esta foto es una tarjeta de visita que un comercial de Chekin ha fotografiado en un evento.
Extrae los datos de la persona de la tarjeta:
- first_name y last_name: nombre y apellidos tal como aparecen, con tildes y en mayúsculas/minúsculas normales (no todo en mayúsculas). Los nombres compuestos (José Luis, Maria Grazia) van enteros en first_name.
- company: nombre de la empresa, sin lemas ni asteriscos.
- job_title: el cargo.
- phone: si hay móvil y fijo, el móvil. En formato internacional con prefijo (por ejemplo +34 600 123 456). Si no lleva prefijo, dedúcelo del país de la tarjeta.
- email y website tal cual.
- country: país de la persona o la empresa, en inglés (Spain, Italy, Portugal…), deducido de la dirección, el prefijo del teléfono o el dominio.
Si un dato no aparece, devuelve "". No inventes nada.`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);
  try {
    const { image, media_type } = await req.json();
    if (typeof image !== "string" || image.length < 100 || image.length > 7_000_000) return json({ error: "invalid_image" }, 400);
    const mt = ["image/jpeg", "image/png", "image/webp"].includes(media_type) ? media_type : "image/jpeg";

    const response = await client.beta.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 2000,
      betas: ["server-side-fallback-2026-07-01"],
      fallbacks: "default",
      output_config: { effort: "low", format: { type: "json_schema", schema: SCHEMA } },
      messages: [{
        role: "user",
        content: [
          { type: "image", source: { type: "base64", media_type: mt, data: image } },
          { type: "text", text: PROMPT },
        ],
      }],
    });

    if (response.stop_reason === "refusal") return json({ error: "refusal" }, 422);
    const text = response.content.find((b) => b.type === "text");
    if (!text || text.type !== "text") return json({ error: "no_output" }, 502);
    const data = JSON.parse(text.text);
    const out: Record<string, string> = {};
    for (const f of FIELDS) out[f] = typeof data[f] === "string" ? data[f].trim().slice(0, 200) : "";
    return json(out);
  } catch (e) {
    if (e instanceof Anthropic.RateLimitError) return json({ error: "rate_limited" }, 429);
    if (e instanceof Anthropic.AuthenticationError) return json({ error: "bad_api_key" }, 500);
    if (e instanceof Anthropic.APIError) return json({ error: "claude_error", status: e.status }, 502);
    return json({ error: "server_error" }, 500);
  }
});
