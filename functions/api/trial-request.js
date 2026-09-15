// Sends L-FIT's "Claim My Free Trial Week" signup (from /join/) to L-FIT's
// inbox via the Resend REST API, and optionally notifies Adam by SMS/WhatsApp
// via Twilio (see functions/_lib/notify.js).
//
// Cloudflare Pages Function. Calls Resend directly via fetch (no npm SDK),
// for the same reason as functions/api/contact.js and
// functions/api/create-checkout-session.js: Pages Functions doesn't run
// `npm install` for the functions/ bundle.
//
// Required environment variable (set in Cloudflare Pages project settings, never in git):
//   RESEND_API_KEY     - API key from resend.com
//
// Optional environment variables:
//   TRIAL_TO_EMAIL      - Where trial signups land. Defaults to contact@lfitlpl.com
//   TRIAL_FROM_EMAIL    - Verified sending address, e.g. "L-FIT Website <contact@lfitlpl.com>".
//                          Defaults to Resend's shared sandbox sender.
//   (see functions/_lib/notify.js for the Twilio SMS/WhatsApp env vars)

import { notifyTwilio } from '../_lib/notify.js';

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.RESEND_API_KEY) {
    return new Response(
      JSON.stringify({ error: 'The trial signup form is not fully set up yet. Please call or message us on Instagram instead.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }

  let name, email, phone, classPref, botField;
  try {
    const contentType = request.headers.get('content-type') || '';
    if (contentType.includes('application/json')) {
      ({ name, email, phone, 'class-pref': classPref, 'bot-field': botField } = await request.json());
    } else {
      const form = await request.formData();
      name = form.get('name');
      email = form.get('email');
      phone = form.get('phone');
      classPref = form.get('class-pref');
      botField = form.get('bot-field');
    }
  } catch (e) {
    return new Response(JSON.stringify({ error: 'Invalid request' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Honeypot: bots fill hidden fields, real users leave it blank.
  if (botField) {
    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  if (!name || !email || !phone) {
    return new Response(JSON.stringify({ error: 'Please fill in your name, email and phone number.' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const toEmail = env.TRIAL_TO_EMAIL || 'contact@lfitlpl.com';
  const fromEmail = env.TRIAL_FROM_EMAIL || 'L-FIT Website <onboarding@resend.dev>';
  const classPrefText = classPref || 'Not specified';

  try {
    const resendRes = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [toEmail],
        reply_to: email,
        subject: `New free trial request from ${name}`,
        text: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nClass interested in: ${classPrefText}\n\nThey were told we'll text or email to confirm their first class — no payment needed for the trial week.`
      })
    });

    if (!resendRes.ok) {
      const errText = await resendRes.text();
      return new Response(
        JSON.stringify({ error: 'Could not send your request. Please try again or contact us directly.', detail: errText }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
    }

    context.waitUntil(
      notifyTwilio(env, {
        subject: `New L-FIT free trial signup: ${name}`,
        body: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nClass interested in: ${classPrefText}`
      }).catch(() => {})
    );

    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err) {
    return new Response(
      JSON.stringify({ error: 'Could not send your request. Please try again or contact us directly.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}

export async function onRequestGet() {
  return new Response('Method Not Allowed', { status: 405 });
}
