// Creates a Stripe Checkout Session for an L-FIT membership (recurring) or
// a single drop-in class / free-trial hold (one-off, or zero-value).
//
// Cloudflare Pages Function. Calls the Stripe REST API directly via fetch
// rather than the Stripe Node SDK, since Cloudflare Pages Functions does not
// run `npm install` for the functions/ bundle, so npm packages like "stripe"
// cannot be resolved at build time.
//
// Required environment variables (set in Cloudflare Pages project settings, never in git):
//   STRIPE_SECRET_KEY        - Stripe secret key (sk_live_... or sk_test_...)
//   STRIPE_PRICE_4CLASS      - Price ID for the "4 classes / month" membership (£35/mo)
//   STRIPE_PRICE_8CLASS      - Price ID for the "8 classes / month" membership (£65/mo)
//   STRIPE_PRICE_UNLIMITED   - Price ID for the "Unlimited" membership (£75/mo)
//
// The Price objects themselves (amount, currency, recurring interval) are configured
// in the Stripe Dashboard, not in this code, so pricing changes never need a redeploy.

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.STRIPE_SECRET_KEY) {
    return new Response(
      JSON.stringify({ error: 'Payments are not configured yet. Please contact L-FIT directly to join.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }

  let plan;
  try {
    ({ plan } = await request.json());
  } catch (e) {
    return new Response(JSON.stringify({ error: 'Invalid request' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const PRICE_MAP = {
    '4class': env.STRIPE_PRICE_4CLASS,
    '8class': env.STRIPE_PRICE_8CLASS,
    unlimited: env.STRIPE_PRICE_UNLIMITED
  };

  const priceId = PRICE_MAP[plan];
  if (!priceId) {
    return new Response(JSON.stringify({ error: 'Unknown membership plan' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const siteUrl = new URL(request.url).origin;

  const body = new URLSearchParams();
  body.set('mode', 'subscription');
  body.set('line_items[0][price]', priceId);
  body.set('line_items[0][quantity]', '1');
  body.set('success_url', `${siteUrl}/join/success/?session_id={CHECKOUT_SESSION_ID}`);
  body.set('cancel_url', `${siteUrl}/join/cancelled/`);
  body.set('allow_promotion_codes', 'true');
  body.set('billing_address_collection', 'auto');

  try {
    const stripeRes = await fetch('https://api.stripe.com/v1/checkout/sessions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: body.toString()
    });

    const session = await stripeRes.json();

    if (!stripeRes.ok) {
      return new Response(
        JSON.stringify({ error: 'Could not start checkout. Please try again or contact L-FIT directly.' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
    }

    return new Response(JSON.stringify({ url: session.url }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err) {
    return new Response(
      JSON.stringify({ error: 'Could not start checkout. Please try again or contact L-FIT directly.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}

export async function onRequestGet() {
  return new Response('Method Not Allowed', { status: 405 });
}
