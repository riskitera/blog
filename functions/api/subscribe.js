/**
 * CF Pages Function: Newsletter subscription via Brevo API.
 * POST /api/subscribe { email: "user@example.com" }
 */
export async function onRequestPost(context) {
  const BREVO_API_KEY = context.env.BREVO_API_KEY;
  const BREVO_LIST_ID = 3; // "Blog Riskitera Newsletter"

  if (!BREVO_API_KEY) {
    return new Response(JSON.stringify({ error: "Newsletter not configured" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }

  let body;
  try {
    body = await context.request.json();
  } catch {
    return new Response(JSON.stringify({ error: "Invalid request" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }

  const email = (body.email || "").trim().toLowerCase();
  if (!email || !email.includes("@")) {
    return new Response(JSON.stringify({ error: "Email invalido" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }

  try {
    const resp = await fetch("https://api.brevo.com/v3/contacts", {
      method: "POST",
      headers: {
        "api-key": BREVO_API_KEY,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email,
        listIds: [BREVO_LIST_ID],
        updateEnabled: true,
      }),
    });

    if (resp.ok || resp.status === 204) {
      return new Response(JSON.stringify({ ok: true, message: "Suscrito correctamente" }), {
        headers: { "Content-Type": "application/json" },
      });
    }

    const data = await resp.json().catch(() => ({}));

    // Already subscribed (duplicate)
    if (data.code === "duplicate_parameter") {
      return new Response(JSON.stringify({ ok: true, message: "Ya estas suscrito" }), {
        headers: { "Content-Type": "application/json" },
      });
    }

    return new Response(JSON.stringify({ error: data.message || "Error de suscripcion" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: "Error del servidor" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}
