// Shared helper: sends SMS + WhatsApp notifications via Twilio's REST API
// directly with fetch() — Cloudflare Pages Functions doesn't run `npm install`
// for the functions/ bundle, so the Twilio SDK can't be resolved at build
// time (same constraint already documented in functions/api/contact.js and
// functions/api/create-checkout-session.js for Resend and Stripe).
//
// This lives under functions/_lib/ (underscore prefix) so Cloudflare Pages
// does NOT treat it as a routable endpoint — it's imported by the actual
// API functions instead.
//
// Entirely optional and additive: it only sends once the relevant Twilio
// env vars are set in the Cloudflare Pages project, and any failure here is
// caught and logged, never thrown — it must never block or break the
// email-sending flow it's called alongside.
//
// Environment variables (set in Cloudflare Pages project settings, never in git):
//   TWILIO_ACCOUNT_SID    - Twilio Account SID
//   TWILIO_AUTH_TOKEN     - Twilio Auth Token
//   TWILIO_SMS_FROM       - Your Twilio SMS-capable number, e.g. +441512345678
//   TWILIO_SMS_TO         - Phone number(s) to text, comma-separated, e.g. +447490730237
//   TWILIO_WHATSAPP_FROM  - Twilio WhatsApp sender number, e.g. +14155238886 (sandbox) or your approved sender
//   TWILIO_WHATSAPP_TO    - Phone number(s) to WhatsApp, comma-separated, e.g. +447490730237
//
// SMS and WhatsApp are independent of each other — set only the pair you
// want active. Leaving all four unset disables this helper entirely; the
// functions calling it keep working exactly as before (email only).

async function sendTwilioMessage(env, { to, from, body }) {
  const url = `https://api.twilio.com/2010-04-01/Accounts/${env.TWILIO_ACCOUNT_SID}/Messages.json`;
  const auth = btoa(`${env.TWILIO_ACCOUNT_SID}:${env.TWILIO_AUTH_TOKEN}`);
  const params = new URLSearchParams({ To: to, From: from, Body: body });

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        Authorization: `Basic ${auth}`,
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: params.toString()
    });

    if (!res.ok) {
      const errText = await res.text();
      console.error(`Twilio send to ${to} failed: ${res.status} ${errText}`);
    }
  } catch (err) {
    console.error(`Twilio send to ${to} threw: ${err && err.message}`);
  }
}

// Fires SMS + WhatsApp notifications in parallel. Never throws.
export async function notifyTwilio(env, { subject, body }) {
  if (!env.TWILIO_ACCOUNT_SID || !env.TWILIO_AUTH_TOKEN) return;

  const fullBody = `${subject}\n\n${body}`;
  const jobs = [];

  if (env.TWILIO_SMS_FROM && env.TWILIO_SMS_TO) {
    for (const to of env.TWILIO_SMS_TO.split(',').map((s) => s.trim()).filter(Boolean)) {
      jobs.push(sendTwilioMessage(env, { to, from: env.TWILIO_SMS_FROM, body: fullBody }));
    }
  }

  if (env.TWILIO_WHATSAPP_FROM && env.TWILIO_WHATSAPP_TO) {
    const waFrom = env.TWILIO_WHATSAPP_FROM.startsWith('whatsapp:')
      ? env.TWILIO_WHATSAPP_FROM
      : `whatsapp:${env.TWILIO_WHATSAPP_FROM}`;
    for (const rawTo of env.TWILIO_WHATSAPP_TO.split(',').map((s) => s.trim()).filter(Boolean)) {
      const waTo = rawTo.startsWith('whatsapp:') ? rawTo : `whatsapp:${rawTo}`;
      jobs.push(sendTwilioMessage(env, { to: waTo, from: waFrom, body: fullBody }));
    }
  }

  if (jobs.length === 0) return;

  await Promise.allSettled(jobs);
}
