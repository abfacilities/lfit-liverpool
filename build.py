import os

ROOT = "/tmp/lfit"

NAV_ITEMS = [
    ("/", "Home"),
    ("/gym/", "The Gym"),
    ("/kids/", "L-FIT Kids"),
    ("/join/", "Join"),
    ("/community/", "Community"),
    ("/about/", "About"),
    ("/contact/", "Contact"),
]

DONATE_URL = "https://buy.stripe.com/9B628q55g91Y2Wi7qc9Zm00"

SITE_NAME = "L-FIT Liverpool"
PHONE = "07490 730237"
PHONE_TEL = "+447490730237"
IG_ADULT = "https://www.instagram.com/lfit_liverpool/"
IG_KIDS = "https://www.instagram.com/lfit_kids/"
CLASSFORKIDS_URL = "https://l-fit-kids.classforkids.io/"
WHATSAPP_URL = "https://wa.me/447490730237"

GA4_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-M9T8NWNPMD"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-M9T8NWNPMD');
</script>
"""

LOCAL_BUSINESS_JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ExerciseGym",
  "name": "L-FIT Liverpool",
  "image": "https://www.lfitlpl.com/assets/lfit-liverpool-logo.jpg",
  "url": "https://www.lfitlpl.com/",
  "telephone": "+447490730237",
  "priceRange": "\u00a335-\u00a375",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "15 Irlam Rd",
    "addressLocality": "Bootle",
    "addressRegion": "Merseyside",
    "postalCode": "L20 4AE",
    "addressCountry": "GB"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 53.4489184,
    "longitude": -2.9986456
  },
  "sameAs": [
    "https://www.instagram.com/lfit_liverpool/",
    "https://www.instagram.com/lfit_kids/"
  ],
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Wednesday"], "opens": "06:00", "closes": "07:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Friday"], "opens": "16:45", "closes": "18:15"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Wednesday"], "opens": "18:15", "closes": "19:15"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday"], "opens": "17:00", "closes": "19:30"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Thursday"], "opens": "18:30", "closes": "19:30"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday"], "opens": "06:00", "closes": "07:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday"], "opens": "09:00", "closes": "10:00"}
  ]
}
</script>
"""

def head(title, desc, canonical_path, ogimage="lfit-liverpool-logo.jpg"):
    canonical = f"https://www.lfitlpl.com{canonical_path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA4_SNIPPET}<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta property="og:image" content="https://www.lfitlpl.com/assets/{ogimage}">
<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/favicon.png">
<link rel="stylesheet" href="/assets/style.css">
<link rel="canonical" href="{canonical}">
{LOCAL_BUSINESS_JSONLD}</head>
<body>
"""

def logo_html(logo_img="lfit-liverpool-logo.jpg", logo_alt="L-FIT Liverpool"):
    return f"""<a href="/" class="logo">
      <img src="/assets/{logo_img}" alt="{logo_alt}" class="logo-img">
    </a>"""

def header(active, logo_img="lfit-liverpool-logo.jpg", logo_alt="L-FIT Liverpool"):
    links = []
    for href, label in NAV_ITEMS:
        cls = " active" if href == active else ""
        links.append(f'<a href="{href}" class="{cls.strip()}">{label}</a>')
    nav_links = "".join(links)
    return f"""<header class="site">
  <div class="container nav-row">
    {logo_html(logo_img, logo_alt)}
    <nav class="main" id="site-nav">{nav_links}</nav>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
    <div class="nav-cta">
      <a class="phone" href="tel:{PHONE_TEL}">{PHONE}</a>
      <a class="btn" href="/join/">Join Now</a>
    </div>
  </div>
</header>
"""

def footer():
    return f"""<footer class="site">
  <div class="container grid">
    <div>
      <img src="/assets/lfit-liverpool-logo.jpg" alt="L-FIT Liverpool" class="footer-logo-img">
      <p style="margin-top:14px">Adult strength &amp; conditioning classes and a dedicated kids programme, under one roof in Bootle, Liverpool.</p>
      <div class="social-row">
        <a href="{IG_ADULT}" aria-label="L-FIT Liverpool on Instagram" target="_blank" rel="noopener">IG</a>
        <a href="{IG_KIDS}" aria-label="L-FIT Kids on Instagram" target="_blank" rel="noopener">KID</a>
      </div>
    </div>
    <div>
      <h4>Train</h4>
      <a href="/gym/">The Gym</a>
      <a href="/kids/">L-FIT Kids</a>
      <a href="/join/">Membership &amp; Pricing</a>
    </div>
    <div>
      <h4>Company</h4>
      <a href="/community/">Community</a>
      <a href="/about/">About</a>
      <a href="/contact/">Contact</a>
    </div>
    <div>
      <h4>Get In Touch</h4>
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="{IG_ADULT}" target="_blank" rel="noopener">@lfit_liverpool</a>
      <a href="{IG_KIDS}" target="_blank" rel="noopener">@lfit_kids</a>
      <a href="{CLASSFORKIDS_URL}" target="_blank" rel="noopener">Book L-FIT Kids</a>
    </div>
  </div>
  <div class="container bottom">
    &copy; 2026 L-FIT Liverpool &middot; Bootle, Liverpool L20 &middot;
    <a href="/privacy/" style="display:inline;color:#8496ab">Privacy Policy</a> &middot;
    <a href="/terms/" style="display:inline;color:#8496ab">Terms &amp; Conditions</a>
  </div>
</footer>

<script src="/assets/nav.js" defer></script>
</body>
</html>
"""

WHATSAPP_FLOAT_HTML = f"""<a href="{WHATSAPP_URL}" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Message L-FIT Liverpool on WhatsApp">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="#fff"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.87 9.87 0 0 0 4.74 1.21h.01c5.46 0 9.9-4.45 9.9-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2zm5.8 14.14c-.24.68-1.4 1.3-1.93 1.38-.5.08-1.12.11-1.8-.11-.42-.13-.96-.31-1.65-.6-2.9-1.25-4.8-4.17-4.94-4.36-.14-.19-1.18-1.57-1.18-3s.75-2.13 1.02-2.42c.27-.29.58-.36.78-.36l.56.01c.18.01.42-.07.65.5.24.58.82 2 .89 2.14.07.14.12.31.02.5-.1.19-.15.31-.29.48-.15.17-.31.38-.44.51-.14.14-.29.29-.13.58.17.29.75 1.24 1.61 2 1.11.99 2.04 1.3 2.33 1.44.29.15.46.13.63-.08.17-.2.72-.84.91-1.13.19-.29.38-.24.63-.14.26.1 1.65.78 1.93.92.29.14.48.22.55.34.07.13.07.72-.17 1.4z"/></svg>
</a>
"""

def page(title, desc, path, active, body, ogimage="lfit-liverpool-logo.jpg", logo_img=None, logo_alt="L-FIT Liverpool"):
    header_logo = logo_img if logo_img else ogimage
    return head(title, desc, path, ogimage) + header(active, header_logo, logo_alt) + body + WHATSAPP_FLOAT_HTML + footer()

def write(relpath, content):
    full = os.path.join(ROOT, relpath.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", full)


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
home_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">&#128205; Bootle, Liverpool L20</div>
    <h1>Train Together.<br><span class="text-gradient">Grow Together.</span></h1>
    <p class="hero-lede">Adult strength &amp; conditioning classes and a dedicated kids programme, under one roof in Bootle. Confidence starts here &mdash; for the whole family.</p>
    <div class="hero-actions">
      <a href="/join/" class="btn">Get Your Free Trial Week</a>
      <a href="/kids/" class="btn outline">Explore L-FIT Kids</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="brand-split">
      <div class="brand-card">
        <span class="tag">Adults</span>
        <h2>L-FIT Liverpool</h2>
        <p style="color:var(--muted)">Kettlebell, partner and circuit classes built around real strength and conditioning &mdash; six sessions a week, coached in a small-group setting.</p>
        <ul>
          <li>Full Body Circuit, Kettlebell, Partner Chipper &amp; Hyrox Circuit</li>
          <li>6 classes a week, early morning &amp; evening slots</li>
          <li>Members WhatsApp community</li>
          <li>Membership from &pound;35/month</li>
        </ul>
        <a href="/gym/" class="btn outline">Explore The Gym &rarr;</a>
      </div>
      <div class="brand-card">
        <span class="tag">Ages 5&ndash;16</span>
        <h2>L-FIT Kids</h2>
        <p style="color:var(--muted)">&ldquo;Confidence Starts Here.&rdquo; Boxing, fitness and Hyrox-style training for kids and teens, powered by L-FIT Liverpool.</p>
        <ul>
          <li>Mini Movers, Future Athletes, Kids Hyrox &amp; Teen Athletes</li>
          <li>Age-based pathway from 5 up to 16</li>
          <li>Book &amp; pay online via ClassForKids</li>
          <li>Run from the same Bootle gym</li>
        </ul>
        <a href="/kids/" class="btn outline">Explore L-FIT Kids &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Why L-FIT</div>
      <h2>One gym. <span class="text-gradient">Every age.</span></h2>
      <p>Whatever brought you through the door, it's the same coaching standard and the same community on both sides.</p>
    </div>
    <div class="grid">
      <div class="card">
        <div class="icon">&#128170;</div>
        <h3>Small-Group Coaching</h3>
        <p>Real coaching, not just a playlist &mdash; classes are built and led by coaches who know your name.</p>
      </div>
      <div class="card">
        <div class="icon">&#129309;</div>
        <h3>One Community</h3>
        <p>A members WhatsApp group, community events like our run club with Anna's Coffee Shop, and a gym that knows its own. <a href="/community/">Read about L-FIT In The Community &rarr;</a></p>
      </div>
      <div class="card">
        <div class="icon">&#128200;</div>
        <h3>Built To Progress</h3>
        <p>From a child's first Mini Movers session to an adult's first Hyrox circuit, every class is part of a pathway, not a one-off.</p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Follow Along</div>
      <h2>From the <span class="text-gradient">gym floor.</span></h2>
      <p>See what's happening in class this week &mdash; follow us on Instagram for timetable updates, community events and behind-the-scenes clips.</p>
    </div>
    <div class="ig-grid">
      <a href="https://www.instagram.com/lfit_liverpool/" target="_blank" rel="noopener" class="ig-card">
        <div class="ig-card-icon">&#128170;</div>
        <h3>@lfit_liverpool</h3>
        <p>Adult classes, coaching clips &amp; member shoutouts</p>
      </a>
      <a href="https://www.instagram.com/lfit_kids/" target="_blank" rel="noopener" class="ig-card">
        <div class="ig-card-icon">&#129497;</div>
        <h3>@lfit_kids</h3>
        <p>Kids sessions, camps &amp; the L-FIT Kids pathway</p>
      </a>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>First week's <span class="text-gradient">on us.</span></h2>
    <p>New to L-FIT? Grab a free trial week on the adult classes, or get your child booked onto their first session.</p>
    <div class="hero-actions" style="justify-content:center">
      <a href="/join/#trial" class="btn">Claim Your Free Trial Week</a>
      <a href="https://l-fit-kids.classforkids.io/" class="btn outline" target="_blank" rel="noopener">Book L-FIT Kids</a>
    </div>
  </div>
</section>
"""
write("index.html", page(
    "L-FIT Liverpool &amp; L-FIT Kids | Gym &amp; Kids Fitness in Bootle",
    "Adult strength & conditioning classes and a dedicated kids fitness programme in Bootle, Liverpool. Kettlebell, circuit, Hyrox and kids boxing & fitness classes.",
    "/", "/", home_body
))

# ---------------------------------------------------------------------------
# GYM (adults)
# ---------------------------------------------------------------------------
gym_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">L-FIT Adults</div>
    <h1>Kettlebell. Partner.<br>Circuit. <span class="text-gradient">Hyrox.</span></h1>
    <p class="hero-lede">Six classes a week in Bootle &mdash; early mornings and evenings, built for people who want real strength and conditioning without a 24-hour gym membership they never use.</p>
    <div class="hero-actions">
      <a href="/join/#trial" class="btn">Get Your Free Trial Week</a>
      <a href="/join/#membership" class="btn outline">See Membership Pricing</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Timetable</div>
      <h2>This week at <span class="text-gradient">L-FIT</span></h2>
      <p>Classes run from our Bootle gym. Spaces are limited to keep coaching quality high &mdash; grab your spot through the members WhatsApp group or your membership.</p>
    </div>
    <div class="table-wrap">
      <table class="timetable">
        <thead>
          <tr><th>Day</th><th>Time</th><th>Class</th></tr>
        </thead>
        <tbody>
          <tr><td class="day">Monday</td><td class="time">6:00am</td><td>Full Body Circuit</td></tr>
          <tr><td class="day">Monday</td><td class="time">6:15pm</td><td>Full Body Circuit</td></tr>
          <tr><td class="day">Tuesday</td><td class="time">6:30pm</td><td>Kettlebell</td></tr>
          <tr><td class="day">Wednesday</td><td class="time">6:00am</td><td>Partner Chipper</td></tr>
          <tr><td class="day">Wednesday</td><td class="time">6:15pm</td><td>Partner Chipper</td></tr>
          <tr><td class="day">Friday</td><td class="time">6:00am</td><td>Hyrox Circuit</td></tr>
          <tr><td class="day">Saturday</td><td class="time">9:00am</td><td>Full Body Circuit</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">The Classes</div>
      <h2>What to <span class="text-gradient">expect</span></h2>
    </div>
    <div class="grid">
      <div class="card">
        <div class="icon">&#128170;</div>
        <h3>Full Body Circuit</h3>
        <p>A full-body strength and conditioning circuit hitting every major muscle group in one session &mdash; our most popular class on the timetable.</p>
      </div>
      <div class="card">
        <div class="icon">&#127940;</div>
        <h3>Kettlebell</h3>
        <p>Kettlebell-focused strength and conditioning &mdash; swings, cleans and carries built into a coached, structured session.</p>
      </div>
      <div class="card">
        <div class="icon">&#129309;</div>
        <h3>Partner Chipper</h3>
        <p>Work through the class as a pair, splitting the reps between you &mdash; a great way to push harder with someone alongside you.</p>
      </div>
      <div class="card">
        <div class="icon">&#9889;</div>
        <h3>Hyrox Circuit</h3>
        <p>Hyrox-style functional fitness &mdash; running paired with functional stations, for anyone training for an event or just wanting the toughest session of the week.</p>
      </div>
    </div>
  </div>
</section>

<section id="membership" class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Membership</div>
      <h2>Simple, <span class="text-gradient">monthly pricing</span></h2>
      <p>No 24-hour gym contract to untangle &mdash; pick the class allowance that fits your week.</p>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <div class="label">4 Classes</div>
        <div class="amount">&pound;35<span>/mo</span></div>
        <p style="color:var(--muted);font-size:.9rem">Perfect if you're easing in or training around a busy week.</p>
        <a href="/join/#membership" class="btn outline block">Choose 4 Classes</a>
      </div>
      <div class="price-card featured">
        <span class="badge">Most Popular</span>
        <div class="label">8 Classes</div>
        <div class="amount">&pound;65<span>/mo</span></div>
        <p style="color:var(--muted);font-size:.9rem">Two sessions a week, every week &mdash; our most popular tier.</p>
        <a href="/join/#membership" class="btn block">Choose 8 Classes</a>
      </div>
      <div class="price-card">
        <div class="label">Unlimited</div>
        <div class="amount">&pound;75<span>/mo</span></div>
        <p style="color:var(--muted);font-size:.9rem">Train as often as the timetable allows, every week.</p>
        <a href="/join/#membership" class="btn outline block">Choose Unlimited</a>
      </div>
    </div>
    <p class="form-note" style="margin-top:20px">Not sure yet? <a href="/join/#trial">Grab a free trial week</a> before you commit &mdash; no card required.</p>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Ready to <span class="text-gradient">get started?</span></h2>
    <p>Join the members WhatsApp group, get your timetable and turn up to your first class.</p>
    <a href="/join/" class="btn">Join L-FIT</a>
  </div>
</section>
"""
write("gym/index.html", page(
    "The Gym | L-FIT Liverpool &mdash; Kettlebell, Circuit &amp; Hyrox Classes",
    "L-FIT Liverpool adult classes in Bootle: Full Body Circuit, Kettlebell, Partner Chipper and Hyrox Circuit. Membership from £35/month, free trial week available.",
    "/gym/", "/gym/", gym_body
))

# ---------------------------------------------------------------------------
# KIDS
# ---------------------------------------------------------------------------
kids_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">L-FIT Kids &middot; Ages 5&ndash;16</div>
    <h1>Confidence<br><span class="text-gradient">Starts Here.</span></h1>
    <p class="hero-lede">Boxing, fitness and Hyrox-style training for kids and teens, powered by L-FIT Liverpool. A safe place to build confidence through movement and community.</p>
    <div class="hero-actions">
      <a href="https://l-fit-kids.classforkids.io/" class="btn" target="_blank" rel="noopener">Book A Class &rarr;</a>
      <a href="#pathway" class="btn outline">See The Pathway</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container two-col">
    <div>
      <div class="eyebrow">Our Mission</div>
      <h2>To build confident, healthy young people <span class="text-gradient">through movement and community.</span></h2>
      <p style="color:var(--muted)">A safe place where children build confidence through movement. We help them develop a love of being active, build lasting friendships and progress through every stage of their journey, creating healthy habits that stay with them for life.</p>
    </div>
    <div class="quote">
      <p>&ldquo;Confidence Starts Here&rdquo;</p>
      <div class="who">L-FIT Kids</div>
    </div>
  </div>
</section>

<section id="pathway" class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Our Pathway</div>
      <h2>Every child has a <span class="text-gradient">pathway.</span></h2>
      <p>Our age-based pathway helps every child grow in confidence, ability and independence at their own pace.</p>
    </div>
    <div class="grid">
      <div class="card">
        <span class="badge-pill">Ages 5&ndash;8</span>
        <h3 style="margin-top:14px">Mini Movers</h3>
        <p>Build confidence, build movement skills, make friends.</p>
      </div>
      <div class="card">
        <span class="badge-pill">Ages 9&ndash;12</span>
        <h3 style="margin-top:14px">Future Athletes</h3>
        <p>Develop fitness, build resilience, grow independence.</p>
      </div>
      <div class="card">
        <span class="badge-pill">Ages 9&ndash;12 &middot; Advanced</span>
        <h3 style="margin-top:14px">Kids Hyrox</h3>
        <p>A Hyrox-style class for kids who want an extra challenge alongside Future Athletes.</p>
      </div>
      <div class="card">
        <span class="badge-pill">Ages 13&ndash;16</span>
        <h3 style="margin-top:14px">Teen Athletes</h3>
        <p>Build strength, lead by example, prepare for the future.</p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Timetable</div>
      <h2>This week's <span class="text-gradient">classes</span></h2>
    </div>
    <div class="table-wrap">
      <table class="timetable">
        <thead>
          <tr><th>Day</th><th>Time</th><th>Class</th><th>Age</th></tr>
        </thead>
        <tbody>
          <tr><td class="day">Monday</td><td class="time">4:45pm</td><td>Mini Movers</td><td>5&ndash;8</td></tr>
          <tr><td class="day">Monday</td><td class="time">5:30pm</td><td>Future Athletes</td><td>9&ndash;12</td></tr>
          <tr><td class="day">Tuesday</td><td class="time">5:00pm</td><td>Kids Hyrox</td><td>9&ndash;12</td></tr>
          <tr><td class="day">Thursday</td><td class="time">6:30pm</td><td>Teen Athletes</td><td>13&ndash;16</td></tr>
          <tr><td class="day">Friday</td><td class="time">4:45pm</td><td>Mini Movers</td><td>5&ndash;8</td></tr>
          <tr><td class="day">Friday</td><td class="time">5:30pm</td><td>Future Athletes</td><td>9&ndash;12</td></tr>
        </tbody>
      </table>
    </div>
    <p class="form-note">Terms and exact class times are kept up to date on our booking system &mdash; always check ClassForKids for the current term dates before you turn up.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="card" style="max-width:720px">
      <span class="badge-pill">Seasonal</span>
      <h3 style="margin-top:14px">L-FIT Kids Summer Camp</h3>
      <p>A full day of fitness games, sports games, mindful arts &amp; crafts and team challenges &mdash; sign-in through to a reflection circle at the end of the day. Runs during school holidays &mdash; follow @lfit_kids on Instagram for dates.</p>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Book your child's <span class="text-gradient">first class</span></h2>
    <p>Booking and payment is handled through our ClassForKids schedule &mdash; see live availability and book in a couple of minutes.</p>
    <a href="https://l-fit-kids.classforkids.io/" class="btn" target="_blank" rel="noopener">Book Online via ClassForKids &rarr;</a>
  </div>
</section>
"""
write("kids/index.html", page(
    "L-FIT Kids | Kids Boxing, Fitness &amp; Hyrox Classes in Bootle",
    "L-FIT Kids: boxing, fitness and Hyrox-style classes for ages 5-16 in Bootle, Liverpool. Confidence Starts Here. Book online via ClassForKids.",
    "/kids/", "/kids/", kids_body, ogimage="lfit-kids-logo.jpg", logo_alt="L-FIT Kids"
))

# ---------------------------------------------------------------------------
# COMMUNITY
# ---------------------------------------------------------------------------
community_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">L-FIT In The Community</div>
    <h1>More than fitness.<br><span class="text-gradient">We're a community hub.</span></h1>
    <p class="hero-lede">Low-cost training for people across Bootle and North Liverpool who are struggling &mdash; physically or mentally &mdash; and need an affordable, judgement-free way back into movement.</p>
    <div class="hero-actions">
      <a href="{donate_url}" class="btn" target="_blank" rel="noopener">Donate Now &rarr;</a>
      <a href="/contact/" class="btn outline">Get In Touch</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container two-col">
    <div>
      <div class="eyebrow">Our Mission</div>
      <h2>Fitness shouldn't be <span class="text-gradient">out of reach.</span></h2>
      <p style="color:var(--muted)">Cost and confidence stop a lot of people from ever walking through the door &mdash; especially anyone managing their mental health, recovering from illness, or just getting back into movement after a hard stretch.</p>
      <p style="color:var(--muted)">L-FIT In The Community is our commitment to keeping training genuinely affordable for children and adults across Bootle and the wider North Liverpool community, whatever your starting point. We're not just a gym &mdash; we're a community hub, and we'd rather find a way to include you than turn you away.</p>
      <p style="color:var(--muted)">If cost is a barrier for you or your child, message us directly &mdash; we'll always try to find a way to get you involved.</p>
    </div>
    <div>
      <img src="/assets/lfit-community-logo.jpg" alt="L-FIT In The Community" style="border-radius:var(--radius);border:1px solid var(--border)">
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Support The Work</div>
      <h2>Help us keep training <span class="text-gradient">affordable.</span></h2>
      <p>Every donation goes directly towards low-cost and subsidised places for people in our community who couldn't otherwise afford to train.</p>
    </div>
    <div class="card" style="max-width:720px">
      <div class="icon">&#10084;</div>
      <h3>Make A Donation</h3>
      <p>Choose your own amount &mdash; every contribution, big or small, helps us keep the doors open to people who need us most.</p>
      <a href="{donate_url}" class="btn" target="_blank" rel="noopener">Donate Now &rarr;</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Out In The Community</div>
      <h2>More than just <span class="text-gradient">classes.</span></h2>
    </div>
    <div class="grid">
      <div class="card">
        <div class="icon">&#9749;</div>
        <h3>Run Club with Anna's Coffee Shop</h3>
        <p>We've teamed up with Anna's Coffee Shop for a community run club &mdash; a 5K followed by coffee and croissants. Run. Coffee. Community.</p>
      </div>
      <div class="card">
        <div class="icon">&#127942;</div>
        <h3>L-FIT Kids Summer Camp</h3>
        <p>School holiday camps packed with fitness games, sports games, mindful arts &amp; crafts and team challenges.</p>
      </div>
      <div class="card">
        <div class="icon">&#128172;</div>
        <h3>Members WhatsApp Group</h3>
        <p>Every adult member gets added to our WhatsApp community &mdash; class updates, timetable changes and a bit of banter.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Struggling to get started? <span class="text-gradient">Talk to us.</span></h2>
    <p>Whether it's cost, confidence, or just not knowing where to begin &mdash; get in touch and we'll help you find a way in.</p>
    <a href="/contact/" class="btn" target="_blank" rel="noopener">Get In Touch &rarr;</a>
  </div>
</section>
""".format(donate_url=DONATE_URL)
write("community/index.html", page(
    "L-FIT In The Community | Low-Cost Training &amp; Donations in Bootle",
    "L-FIT In The Community: low-cost training for people across Bootle and North Liverpool struggling physically or mentally. We're more than fitness, we're a community hub. Support us with a donation.",
    "/community/", "/community/", community_body, ogimage="lfit-community-logo.jpg", logo_alt="L-FIT In The Community"
))

# ---------------------------------------------------------------------------
# JOIN
# ---------------------------------------------------------------------------
join_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">Join L-FIT</div>
    <h1>Let's get you <span class="text-gradient">started.</span></h1>
    <p class="hero-lede">Adult membership signs up securely online below. Booking your child onto L-FIT Kids happens through our ClassForKids schedule.</p>
  </div>
</section>

<section id="trial" class="tight">
  <div class="container two-col">
    <div>
      <div class="eyebrow">Adults &middot; Free Trial</div>
      <h2>Try your first week <span class="text-gradient">free.</span></h2>
      <p style="color:var(--muted)">No card required. Tell us a bit about you and we'll message you to get your first class booked in.</p>
      <div class="info-row" style="margin-top:32px">
        <div class="ic">&#128241;</div>
        <div><h4>Prefer to just message us?</h4><p>DM <a href="https://www.instagram.com/lfit_liverpool/" target="_blank" rel="noopener">@lfit_liverpool</a> on Instagram or call <a href="tel:+447490730237">07490 730237</a>.</p></div>
      </div>
    </div>
    <div class="form-card">
      <form name="trial-request" method="POST" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="trial-request">
        <p style="display:none"><label>Don't fill this out: <input name="bot-field"></label></p>
        <div class="field">
          <label for="name">Full name</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="field">
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" required>
        </div>
        <div class="field">
          <label for="class-pref">Which class interests you?</label>
          <select id="class-pref" name="class-pref">
            <option>Full Body Circuit</option>
            <option>Kettlebell</option>
            <option>Partner Chipper</option>
            <option>Hyrox Circuit</option>
            <option>Not sure yet</option>
          </select>
        </div>
        <button type="submit" class="btn block">Claim My Free Trial Week</button>
        <p class="form-note">We'll text or email you to confirm your first class &mdash; no payment needed for your trial week.</p>
      </form>
    </div>
  </div>
</section>

<section id="membership" class="tight">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Adults &middot; Membership</div>
      <h2>Choose your <span class="text-gradient">plan.</span></h2>
      <p>Secure online sign-up, powered by Stripe. Cancel any time from your confirmation email.</p>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <div class="label">4 Classes</div>
        <div class="amount">&pound;35<span>/mo</span></div>
        <p style="color:var(--muted);font-size:.9rem">One class a week, every week.</p>
        <button class="btn outline block join-btn" data-plan="4class">Join &mdash; &pound;35/mo</button>
      </div>
      <div class="price-card featured">
        <span class="badge">Most Popular</span>
        <div class="label">8 Classes</div>
        <div class="amount">&pound;65<span>/mo</span></div>
        <p style="color:var(--muted);font-size:.9rem">Two classes a week, every week.</p>
        <button class="btn block join-btn" data-plan="8class">Join &mdash; &pound;65/mo</button>
      </div>
      <div class="price-card">
        <div class="label">Unlimited</div>
        <div class="amount">&pound;75<span>/mo</span></div>
        <p style="color:var(--muted);font-size:.9rem">Every class on the timetable.</p>
        <button class="btn outline block join-btn" data-plan="unlimited">Join &mdash; &pound;75/mo</button>
      </div>
    </div>
    <p id="join-error" class="form-note" style="display:none;color:#f59e0b"></p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="card" style="max-width:720px">
      <span class="badge-pill">Kids</span>
      <h3 style="margin-top:14px">Booking L-FIT Kids</h3>
      <p>Kids classes are booked and paid for through our ClassForKids schedule, where you can see live availability, book a trial and manage payments term by term.</p>
      <a href="https://l-fit-kids.classforkids.io/" class="btn outline" target="_blank" rel="noopener">Go To ClassForKids &rarr;</a>
    </div>
  </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var buttons = document.querySelectorAll('.join-btn');
  var errorEl = document.getElementById('join-error');
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var plan = btn.getAttribute('data-plan');
      buttons.forEach(function (b) { b.disabled = true; });
      btn.textContent = 'Redirecting to secure checkout...';
      errorEl.style.display = 'none';
      fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plan: plan })
      })
        .then(function (res) { return res.json(); })
        .then(function (data) {
          if (data.url) {
            window.location = data.url;
          } else {
            throw new Error(data.error || 'Something went wrong');
          }
        })
        .catch(function (err) {
          errorEl.textContent = err.message || 'Could not start checkout. Please call 07490 730237 to join instead.';
          errorEl.style.display = 'block';
          buttons.forEach(function (b) { b.disabled = false; });
          btn.textContent = btn.getAttribute('data-plan') === '4class' ? 'Join — £35/mo' : (btn.getAttribute('data-plan') === '8class' ? 'Join — £65/mo' : 'Join — £75/mo');
        });
    });
  });
});
</script>
"""
write("join/index.html", page(
    "Join L-FIT | Membership &amp; Free Trial in Bootle, Liverpool",
    "Join L-FIT Liverpool: secure online membership sign-up from £35/month, or claim a free trial week. Kids classes book via ClassForKids.",
    "/join/", "/join/", join_body
))

success_body = """
<section class="hero" style="text-align:center">
  <div class="container">
    <div class="eyebrow">Payment Confirmed</div>
    <h1>Welcome to <span class="text-gradient">L-FIT.</span></h1>
    <p class="hero-lede" style="margin-left:auto;margin-right:auto">Your membership is active. Keep an eye on your email for a receipt, and join the members WhatsApp group to get your timetable and class booking link.</p>
    <div class="hero-actions" style="justify-content:center">
      <a href="/gym/" class="btn">View The Timetable</a>
      <a href="/" class="btn outline">Back To Home</a>
    </div>
  </div>
</section>
"""
write("join/success/index.html", page(
    "You're In | L-FIT Liverpool",
    "Your L-FIT Liverpool membership is confirmed.",
    "/join/success/", "/join/", success_body
))

cancelled_body = """
<section class="hero" style="text-align:center">
  <div class="container">
    <div class="eyebrow">Checkout Cancelled</div>
    <h1>No <span class="text-gradient">problem.</span></h1>
    <p class="hero-lede" style="margin-left:auto;margin-right:auto">Your card hasn't been charged. If you hit a snag or just want to ask a question first, message us on Instagram or give us a call.</p>
    <div class="hero-actions" style="justify-content:center">
      <a href="/join/#membership" class="btn">Try Again</a>
      <a href="tel:+447490730237" class="btn outline">Call 07490 730237</a>
    </div>
  </div>
</section>
"""
write("join/cancelled/index.html", page(
    "Checkout Cancelled | L-FIT Liverpool",
    "Your L-FIT Liverpool checkout was cancelled — no charge was made.",
    "/join/cancelled/", "/join/", cancelled_body
))

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">About Us</div>
    <h1>One gym.<br><span class="text-gradient">A whole community.</span></h1>
    <p class="hero-lede">L-FIT Liverpool is a strength &amp; conditioning gym in Bootle, running adult classes six days a week and powering L-FIT Kids &mdash; our dedicated fitness programme for ages 5 to 16.</p>
  </div>
</section>

<section class="tight">
  <div class="container two-col">
    <div>
      <div class="eyebrow">L-FIT Kids Mission</div>
      <h2>To build confident, healthy young people <span class="text-gradient">through movement and community.</span></h2>
      <p style="color:var(--muted)">A safe place where children build confidence through movement. We help them develop a love of being active, build lasting friendships and progress through every stage of their journey, creating healthy habits that stay with them for life.</p>
    </div>
    <div class="card">
      <div class="icon">&#127968;</div>
      <h3>Bootle, Liverpool L20</h3>
      <p>Both L-FIT and L-FIT Kids run from the same gym in Bootle &mdash; one space, one coaching team, one community for the whole family.</p>
    </div>
  </div>
</section>

<section id="community" class="tight">
  <div class="container two-col">
    <div>
      <div class="eyebrow">L-FIT In The Community</div>
      <h2>Fitness shouldn't be <span class="text-gradient">out of reach.</span></h2>
      <p style="color:var(--muted)">We're more than a gym &mdash; L-FIT is a community hub, running low-cost training for people across Bootle and North Liverpool who are struggling physically or mentally, and who need an affordable, judgement-free way back into movement.</p>
      <a href="/community/" class="btn outline">Read About L-FIT In The Community &rarr;</a>
    </div>
    <div>
      <img src="/assets/lfit-community-logo.jpg" alt="L-FIT In The Community" style="border-radius:var(--radius);border:1px solid var(--border)">
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Come and see it <span class="text-gradient">for yourself.</span></h2>
    <p>The best way to understand L-FIT is to turn up to a class.</p>
    <a href="/join/#trial" class="btn">Get Your Free Trial Week</a>
  </div>
</section>
"""
write("about/index.html", page(
    "About L-FIT Liverpool &amp; L-FIT Kids | Bootle, Liverpool",
    "L-FIT Liverpool is a strength & conditioning gym in Bootle running adult classes and powering L-FIT Kids, a fitness programme for ages 5-16.",
    "/about/", "/about/", about_body
))

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
contact_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">Get In Touch</div>
    <h1>Let's talk.</h1>
    <p class="hero-lede">Questions about adult classes, membership, or booking your child onto L-FIT Kids &mdash; message, call, or drop by.</p>
  </div>
</section>

<section class="tight">
  <div class="container two-col">
    <div>
      <div class="info-row">
        <div class="ic">&#128205;</div>
        <div><h4>Location</h4><p>Bootle, Liverpool, L20</p></div>
      </div>
      <div class="info-row">
        <div class="ic">&#128222;</div>
        <div><h4>Phone</h4><p><a href="tel:+447490730237">07490 730237</a></p></div>
      </div>
      <div class="info-row">
        <div class="ic">&#128172;</div>
        <div><h4>Adults</h4><p>DM <a href="https://www.instagram.com/lfit_liverpool/" target="_blank" rel="noopener">@lfit_liverpool</a> on Instagram</p></div>
      </div>
      <div class="info-row">
        <div class="ic">&#129466;</div>
        <div><h4>Kids</h4><p>DM <a href="https://www.instagram.com/lfit_kids/" target="_blank" rel="noopener">@lfit_kids</a>, or book directly via <a href="https://l-fit-kids.classforkids.io/" target="_blank" rel="noopener">ClassForKids</a></p></div>
      </div>
      <div class="social-row">
        <a href="https://www.instagram.com/lfit_liverpool/" target="_blank" rel="noopener" aria-label="L-FIT Liverpool Instagram">IG</a>
        <a href="https://www.instagram.com/lfit_kids/" target="_blank" rel="noopener" aria-label="L-FIT Kids Instagram">KID</a>
      </div>
    </div>
    <div class="form-card">
      <form id="contact-form">
        <p style="display:none"><label>Don't fill this out: <input name="bot-field"></label></p>
        <div class="field">
          <label for="c-name">Full name</label>
          <input type="text" id="c-name" name="name" required>
        </div>
        <div class="field">
          <label for="c-email">Email</label>
          <input type="email" id="c-email" name="email" required>
        </div>
        <div class="field">
          <label for="c-message">Message</label>
          <textarea id="c-message" name="message" required></textarea>
        </div>
        <button type="submit" class="btn block">Send Message</button>
        <p id="contact-form-status" style="margin-top:12px;font-size:.9rem"></p>
      </form>
    </div>
  </div>
</section>

<script>
(function () {
  var form = document.getElementById('contact-form');
  var status = document.getElementById('contact-form-status');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]');
    btn.disabled = true;
    status.style.color = 'var(--muted)';
    status.textContent = 'Sending...';
    var data = {
      name: form.name.value,
      email: form.email.value,
      message: form.message.value,
      'bot-field': form['bot-field'].value
    };
    fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
      .then(function (res) { return res.json().then(function (body) { return { ok: res.ok, body: body }; }); })
      .then(function (result) {
        btn.disabled = false;
        if (result.ok) {
          status.style.color = 'var(--teal)';
          status.textContent = "Thanks \u2014 we've got your message and will get back to you soon.";
          form.reset();
        } else {
          status.style.color = '#ff6b6b';
          status.textContent = (result.body && result.body.error) || 'Something went wrong. Please try again or message us on Instagram.';
        }
      })
      .catch(function () {
        btn.disabled = false;
        status.style.color = '#ff6b6b';
        status.textContent = 'Something went wrong. Please try again or message us on Instagram.';
      });
  });
})();
</script>
"""
write("contact/index.html", page(
    "Contact L-FIT Liverpool &amp; L-FIT Kids | Bootle",
    "Get in touch with L-FIT Liverpool and L-FIT Kids in Bootle, Liverpool L20. Call 07490 730237 or message us on Instagram.",
    "/contact/", "/contact/", contact_body
))

print("ALL PAGES WRITTEN")

# ---------------------------------------------------------------------------
# PRIVACY / TERMS (minimal, real stubs)
# ---------------------------------------------------------------------------
privacy_body = """
<section class="hero tight">
  <div class="container">
    <div class="eyebrow">Legal</div>
    <h1>Privacy Policy</h1>
  </div>
</section>
<section class="tight">
  <div class="container" style="max-width:760px">
    <p style="color:var(--muted)">L-FIT Liverpool ("we", "us") collects the information you give us through our contact and free-trial forms (name, email, phone, class preference) to respond to your enquiry and get you booked onto a class. We don't sell your data or share it with third parties beyond what's needed to run the gym.</p>
    <h3>Payments</h3>
    <p style="color:var(--muted)">Adult membership payments are processed by Stripe. We never see or store your card details &mdash; Stripe handles payment data directly under its own security standards (PCI DSS Level 1).</p>
    <h3>Kids Bookings</h3>
    <p style="color:var(--muted)">L-FIT Kids bookings and payments are handled by ClassForKids, a third-party booking platform for kids' activity providers. Their own privacy policy applies to information you submit there.</p>
    <h3>Contact</h3>
    <p style="color:var(--muted)">Questions about your data? Call <a href="tel:+447490730237">07490 730237</a> or message <a href="https://www.instagram.com/lfit_liverpool/" target="_blank" rel="noopener">@lfit_liverpool</a>.</p>
    <p class="form-note">This is a plain-English summary rather than a full legal policy. If you need a formal GDPR-compliant privacy policy, it's worth having one drafted properly for the business.</p>
  </div>
</section>
"""
write("privacy/index.html", page(
    "Privacy Policy | L-FIT Liverpool",
    "How L-FIT Liverpool handles your data.",
    "/privacy/", "", privacy_body
))

terms_body = """
<section class="hero tight">
  <div class="container">
    <div class="eyebrow">Legal</div>
    <h1>Terms &amp; Conditions</h1>
  </div>
</section>
<section class="tight">
  <div class="container" style="max-width:760px">
    <h3>Membership</h3>
    <p style="color:var(--muted)">Adult memberships are billed monthly via Stripe and renew automatically until cancelled. Cancel any time from your confirmation email or by contacting us directly &mdash; cancellation stops future billing, it doesn't refund the current period.</p>
    <h3>Free Trial</h3>
    <p style="color:var(--muted)">The free trial week is available to new members only, once per person, and doesn't require payment details.</p>
    <h3>Classes</h3>
    <p style="color:var(--muted)">Class spaces are limited and offered on a first-come basis. We may occasionally need to change timetable slots or coaches &mdash; we'll let members know via the WhatsApp community group.</p>
    <h3>Kids Bookings</h3>
    <p style="color:var(--muted)">L-FIT Kids bookings, payments and cancellations are governed by ClassForKids' own terms, since bookings are made and paid for on their platform.</p>
    <p class="form-note">This is a plain-English summary rather than a full legal terms document. Worth having formal terms drafted for the business.</p>
  </div>
</section>
"""
write("terms/index.html", page(
    "Terms &amp; Conditions | L-FIT Liverpool",
    "L-FIT Liverpool membership and class terms.",
    "/terms/", "", terms_body
))
