/**
 * CF Pages Function: Newsletter subscription via Brevo API.
 * POST /api/subscribe { email: "user@example.com" }
 * 
 * 1. Adds contact to list
 * 2. Sends welcome email immediately (Template 1)
 * 3. Schedules follow-up emails via Brevo scheduled sends
 */
export async function onRequestPost(context) {
  const BREVO_API_KEY = context.env.BREVO_API_KEY;
  const BREVO_LIST_ID = 3;

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

  const headers = {
    "api-key": BREVO_API_KEY,
    "Content-Type": "application/json",
  };

  try {
    // Step 1: Add contact to list
    const addResp = await fetch("https://api.brevo.com/v3/contacts", {
      method: "POST",
      headers,
      body: JSON.stringify({
        email,
        listIds: [BREVO_LIST_ID],
        updateEnabled: true,
      }),
    });

    const addData = await addResp.json().catch(() => ({}));
    const isDuplicate = addData.code === "duplicate_parameter";

    if (!addResp.ok && !isDuplicate && addResp.status !== 204) {
      return new Response(JSON.stringify({ error: addData.message || "Error de suscripcion" }), {
        status: 400,
        headers: { "Content-Type": "application/json" },
      });
    }

    // Step 2: Send welcome email immediately (only for new subscribers)
    if (!isDuplicate) {
      await sendTemplate(headers, 1, email); // Welcome (now)
      
      // Step 3: Schedule follow-up emails
      const now = Date.now();
      const DAY = 86400000;
      await scheduleTemplate(headers, 2, email, new Date(now + 2 * DAY)); // Product (day 2)
      await scheduleTemplate(headers, 3, email, new Date(now + 5 * DAY)); // Case study (day 5)
      await scheduleTemplate(headers, 4, email, new Date(now + 8 * DAY)); // Resource (day 8)
      await scheduleTemplate(headers, 5, email, new Date(now + 12 * DAY)); // Demo CTA (day 12)
    }

    return new Response(JSON.stringify({
      ok: true,
      message: isDuplicate ? "Ya estas suscrito" : "Suscrito correctamente. Revisa tu email.",
    }), {
      headers: { "Content-Type": "application/json" },
    });

  } catch (err) {
    return new Response(JSON.stringify({ error: "Error del servidor" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}

async function sendTemplate(headers, templateId, email) {
  try {
    await fetch("https://api.brevo.com/v3/smtp/email", {
      method: "POST",
      headers,
      body: JSON.stringify({
        templateId,
        to: [{ email }],
      }),
    });
  } catch {}
}

async function scheduleTemplate(headers, templateId, email, sendAt) {
  try {
    await fetch("https://api.brevo.com/v3/smtp/email", {
      method: "POST",
      headers,
      body: JSON.stringify({
        templateId,
        to: [{ email }],
        scheduledAt: sendAt.toISOString(),
      }),
    });
  } catch {}
}
