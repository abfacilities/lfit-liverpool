// ONE-TIME setup endpoint: creates the Resend Audience for the L-FIT Liverpool
// newsletter and returns its ID so it can be saved as the RESEND_AUDIENCE_ID
// environment variable. Delete this file (or leave it - it requires the
// ADMIN_SETUP_SECRET header either way) once the audience has been created.
//
// Required environment variables:
//   NEWSLETTER_RESEND_API_KEY - Fully-permissioned Resend key (Audiences/Broadcasts)
//   ADMIN_SETUP_SECRET        - Shared secret required in the x-admin-setup-secret header

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.NEWSLETTER_RESEND_API_KEY || !env.ADMIN_SETUP_SECRET) {
// redeploy trigger 2026-09-29
    return new Response(JSON.stringify({ error: 'Not configured' }), { status: 500 });
  }

  const providedSecret = request.headers.get('x-admin-setup-secret');
  if (providedSecret !== env.ADMIN_SETUP_SECRET) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  try {
    const res = await fetch('https://api.resend.com/audiences', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.NEWSLETTER_RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name: 'L-FIT Liverpool Newsletter' })
    });

    const data = await res.json();
    if (!res.ok) {
      return new Response(JSON.stringify({ error: 'Could not create audience', detail: data }), { status: 500 });
    }

    return new Response(JSON.stringify({ ok: true, audience: data }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: 'Request failed', detail: String(err) }), { status: 500 });
  }
}

export async function onRequestGet() {
  return new Response('Method Not Allowed', { status: 405 });
}
