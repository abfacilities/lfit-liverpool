// Creates a Stripe Checkout Session for an L-FIT membership (recurring) or
// a single drop-in class / free-trial hold (one-off, or zero-value).
//
// Required environment variables (set in Netlify site settings, never in git):
//   STRIPE_SECRET_KEY        - Stripe secret key (sk_live_... or sk_test_...)
//   STRIPE_PRICE_4CLASS      - Price ID for the "4 classes / month" membership (£35/mo)
//   STRIPE_PRICE_8CLASS      - Price ID for the "8 classes / month" membership (£65/mo)
//   STRIPE_PRICE_UNLIMITED   - Price ID for the "Unlimited" membership (£75/mo)
//   URL                      - Netlify sets this automatically to the site's live URL
//
// The Price objects themselves (amount, currency, recurring interval) are configured
// in the Stripe Dashboard, not in this code, so pricing changes never need a redeploy.

const Stripe = require('stripe');

const PRICE_MAP = {
  '4class': process.env.STRIPE_PRICE_4CLASS,
  '8class': process.env.STRIPE_PRICE_8CLASS,
  'unlimited': process.env.STRIPE_PRICE_UNLIMITED
};

exports.handler = async function (event) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  if (!process.env.STRIPE_SECRET_KEY) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Payments are not configured yet. Please contact L-FIT directly to join.' })
    };
  }

  let plan;
  try {
    ({ plan } = JSON.parse(event.body || '{}'));
  } catch (e) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Invalid request' }) };
  }

  const priceId = PRICE_MAP[plan];
  if (!priceId) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Unknown membership plan' }) };
  }

  const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
  const siteUrl = process.env.URL || 'https://www.lfitlpl.com';

  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'subscription',
      line_items: [{ price: priceId, quantity: 1 }],
      success_url: `${siteUrl}/join/success/?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${siteUrl}/join/cancelled/`,
      allow_promotion_codes: true,
      billing_address_collection: 'auto'
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ url: session.url })
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Could not start checkout. Please try again or contact L-FIT directly.' })
    };
  }
};
