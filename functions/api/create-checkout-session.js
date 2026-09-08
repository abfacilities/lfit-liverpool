// Creates a Stripe Checkout Session for an L-FIT membership (recurring) or
// a single drop-in class / free-trial hold (one-off, or zero-value).
//
// Cloudflare Pages Function (replaces the old Netlify Function of the same purpose).
// Required environment variables (set in Cloudflare Pages project settings, never in git):
//   STRIPE_SECRET_KEY        - Stripe secret key (sk_live_... or sk_test_...)
//   STRIPE_PRICE_4CLASS      - Price ID for the "4 classes / month" membership (£35/mo)
//   STRIPE_PRICE_8CLASS      - Price ID for the "8 classes / month" membership (£65/mo)
//   STRIPE_PRICE_UNLIMITED   - Price ID for the "Unlimited" membership (£75/mo)
//
// The Price objects themselves (amount, currency, recurring interval) are configured
// in the Stripe Dashboard, not in this code, so pricing changes never need a redeploy.

import Stripe from 'stripe';

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

  // Cloudflare Workers runtime: use Stripe's fetch-based HTTP client rather than
  // the default Node http client, per Stripe's edge-runtime guidance.
  const stripe = new Stripe(env.STRIPE_SECRET_KEY, {
    httpClient: Stripe.createFetchHttpClient()
  });
  const siteUrl = new URL(request.url).origin;

  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'subscription',
      line_items: [{ price: priceId, quantity: 1 }],
      success_url: `${siteUrl}/join/success/?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${siteUrl}/join/cancelled/`,
      allow_promotion_codes: true,
      billing_address_collection: 'auto'
    });

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
