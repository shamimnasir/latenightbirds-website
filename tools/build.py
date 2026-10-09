#!/usr/bin/env python3
"""Generates the static site: home, blog index, post pages, redirects, sitemap, 404.

Run from the repo root:  python3 tools/build.py
Source data for posts lives in tools/posts.json (exported from the old WordPress site).
"""
import json, html, math, os, re, struct
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from articles import ARTICLES, COVER, RELATED

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://latenightbirds.com"
EMAIL = "mail@latenightbirds.com"
YEAR = datetime.now().year
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&'
         'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&display=swap" rel="stylesheet">')


def nodash(s):
    """Remove em/en dashes from copy."""
    s = re.sub(r"(\d)\s?[–—]\s?(\d)", r"\1-\2", s)
    s = re.sub(r"\s[–—]\s", ", ", s)
    s = re.sub(r"[–—]", "-", s)
    return s


# ---------- posts ----------
def img_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


def clean_post(raw):
    h = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    h = re.sub(r"<hr[^>]*/?>", "", h)
    h = re.sub(r'\s(class|decoding|loading)="[^"]*"', "", h)
    h = h.replace("&nbsp;", " ")
    h = re.sub(r"<(/?)h3", r"<\1h2", h)

    def fig(m):
        block = m.group(0)
        src = re.search(r'src="([^"]+)"', block)
        if not src:
            return re.sub(r"</?figure[^>]*>", "", block)
        base = os.path.basename(re.sub(r"^https://web\.archive\.org/web/\d+im_/", "", src.group(1))) if src else ""
        f = ROOT / "blog" / "img" / base
        if not f.exists():
            return ""
        alt = re.search(r'alt="([^"]*)"', block)
        wh = img_size(f)
        dims = f' width="{wh[0]}" height="{wh[1]}"' if wh else ""
        return f'<figure><img src="/blog/img/{base}" alt="{alt.group(1) if alt else ""}"{dims} loading="lazy"></figure>'

    h = re.sub(r"<figure.*?</figure>", fig, h, flags=re.S)
    h = re.sub(r"<table", '<div class="tablewrap"><table', h)
    h = h.replace("</table>", "</table></div>")
    h = re.sub(r'\sstyle="[^"]*"', "", h)
    return nodash(h)


def load_posts():
    data = json.load(open(ROOT / "tools" / "posts.json"))
    posts = []
    for p in data:
        title = nodash(html.unescape(p["title"]["rendered"]))
        body = clean_post(p["content"]["rendered"])
        text = html.unescape(re.sub(r"<[^>]+>", " ", body))
        text = re.sub(r"\s+", " ", text).strip()
        first = re.search(r"<p>(.*?)</p>", body, flags=re.S)
        lead = html.unescape(re.sub(r"<[^>]+>", "", first.group(1))) if first else text
        excerpt = lead if len(lead) > 90 else text[:200]
        if len(excerpt) > 175:
            excerpt = excerpt[:172].rsplit(" ", 1)[0].rstrip(",;:") + "..."
        feat = os.path.basename(p["_embedded"]["feat"][0]) if p["_embedded"]["feat"] else ""
        dt = datetime.fromisoformat(p["date"])
        posts.append(dict(
            slug=p["slug"], title=title, body=body, excerpt=excerpt, img=feat,
            date=dt, pretty=dt.strftime("%B %-d, %Y"), iso=dt.date().isoformat(),
            mins=max(1, math.ceil(len(text.split()) / 230)),
        ))
    for a in ARTICLES:
        dt = datetime.fromisoformat(a["date"])
        body = nodash(a["body"].strip())
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).strip()
        posts.append(dict(
            slug=a["slug"], title=nodash(a["title"]), body=body, excerpt=nodash(a["excerpt"]),
            img=f"cover-{a['slug']}.svg", date=dt, pretty=dt.strftime("%B %-d, %Y"), iso=dt.date().isoformat(),
            mins=max(1, math.ceil(len(text.split()) / 230)),
            takeaways=[nodash(t) for t in a["takeaways"]],
            faqs=[(nodash(q), nodash(v)) for q, v in a["faqs"]],
        ))
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts


# ---------- shared chrome ----------
def head(title, desc, path, og_type="website", extra=""):
    t = html.escape(title)
    d = html.escape(desc)
    url = SITE + path
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="LateNightBirds">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fffefd">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="/styles.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;else if(matchMedia('(prefers-color-scheme: dark)').matches)document.documentElement.dataset.theme='dark'}}catch(e){{}}</script>
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(active):
    def a(href, label, key):
        cls = ' class="active"' if active == key else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    return f'''<header class="header" id="hdr"><div class="header-in">
  <a class="brand" href="/" aria-label="LateNightBirds home"><img src="/assets/logo-mark.svg" alt="" width="34" height="34"><span>Late<b>Night</b>Birds<sup>®</sup></span></a>
  <button class="menu" id="menuBtn" aria-label="Menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  <nav class="nav" id="nav" aria-label="Primary">
    {a("/", "Home", "home")}
    {a("/#services", "Services", "services")}
    {a("/#process", "Process", "process")}
    {a("/#results", "Results", "results")}
    {a("/blog/", "Blog", "blog")}
    <button class="toggle" id="themeToggle" aria-label="Toggle dark mode"><span></span></button>
    <a class="btn btn-solid btn-sm" href="/#contact">Book a Call <i>→</i></a>
  </nav>
</div></header>
'''


def footer():
    return f'''<footer class="footer" id="contact">
  <div class="cta-band">
    <p class="eyebrow">Have an idea?</p>
    <h2>Let's build something <em>together.</em></h2>
    <a class="btn btn-solid big" href="mailto:{EMAIL}?subject=Free%20Growth%20Audit">Book a Free Growth Audit <i>→</i></a>
  </div>
  <div class="foot">
    <div>
      <a class="brand" href="/"><img src="/assets/logo-mark.svg" alt="" width="34" height="34"><span>Late<b>Night</b>Birds<sup>®</sup></span></a>
      <p>An AI marketing and automation agency. We build growth systems that keep working after the office lights go off.</p>
    </div>
    <div><h4>Explore</h4><a href="/#services">Services</a><a href="/#process">Process</a><a href="/#results">Results</a><a href="/blog/">Blog</a></div>
    <div><h4>Contact</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="/#top">Back to top ↑</a></div>
  </div>
  <div class="legal"><span>© {YEAR} LateNightBirds LLC. All rights reserved.</span><span>Made with <span class="heart">♥</span> after dark</span></div>
</footer>
<script src="/script.js"></script>
</body>
</html>
'''


def card(p, tag="h3"):
    return (f'<a class="post-card" href="/blog/{p["slug"]}/"><img src="/blog/img/{p["img"]}" alt="" loading="lazy" width="720" height="480">'
            f'<div><{tag}>{html.escape(p["title"])}</{tag}><p class="pmeta">{p["pretty"]} · {p["mins"]} min read</p></div></a>')


# ---------- pages ----------
BANNER = '''<svg viewBox="0 0 800 260" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--sky-top)"/><stop offset="1" stop-color="var(--sky-bot)"/></linearGradient></defs>
  <rect width="800" height="260" fill="url(#sky)"/>
  <g class="stars" fill="var(--star)">
    <circle cx="60" cy="40" r="1.6"/><circle cx="140" cy="90" r="1.2"/><circle cx="230" cy="30" r="1.8"/><circle cx="330" cy="70" r="1.2"/>
    <circle cx="430" cy="25" r="1.6"/><circle cx="520" cy="95" r="1.2"/><circle cx="610" cy="40" r="1.8"/><circle cx="700" cy="85" r="1.4"/>
    <circle cx="760" cy="30" r="1.2"/><circle cx="90" cy="150" r="1"/><circle cx="380" cy="140" r="1"/><circle cx="560" cy="150" r="1"/>
  </g>
  <circle cx="640" cy="78" r="30" fill="var(--moon)"/><circle cx="652" cy="70" r="27" fill="var(--sky-top)" opacity=".92"/>
  <g fill="none" stroke="var(--star)" stroke-width="2.2" stroke-linecap="round">
    <path class="bird b1" d="M300 110q10-12 20 0q10-12 20 0"/><path class="bird b2" d="M370 80q7-9 14 0q7-9 14 0"/><path class="bird b3" d="M250 60q6-8 12 0q6-8 12 0"/>
  </g>
  <g fill="var(--city)">
    <rect x="0" y="190" width="70" height="70"/><rect x="70" y="170" width="50" height="90"/><rect x="120" y="200" width="80" height="60"/>
    <rect x="200" y="160" width="46" height="100"/><rect x="246" y="195" width="90" height="65"/><rect x="336" y="175" width="54" height="85"/>
    <rect x="390" y="205" width="100" height="55"/><rect x="490" y="165" width="48" height="95"/><rect x="538" y="195" width="90" height="65"/>
    <rect x="628" y="178" width="60" height="82"/><rect x="688" y="200" width="112" height="60"/>
  </g>
  <g fill="var(--window)">
    <rect x="80" y="185" width="6" height="8"/><rect x="96" y="205" width="6" height="8"/><rect x="210" y="175" width="6" height="8"/>
    <rect x="224" y="195" width="6" height="8"/><rect x="346" y="190" width="6" height="8"/><rect x="500" y="180" width="6" height="8"/>
    <rect x="514" y="200" width="6" height="8"/><rect x="640" y="192" width="6" height="8"/>
  </g>
</svg>'''


def home(posts):
    desc = ("LateNightBirds LLC is an AI marketing and automation agency. AI-focused SEO, content, link acquisition "
            "and workflow automation built to attract, convert and scale.")
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "LateNightBirds LLC", "url": SITE,
           "logo": SITE + "/assets/logo-mark.svg", "email": EMAIL,
           "description": "AI marketing and automation agency"}
    extra = f'<script type="application/ld+json">{json.dumps(org)}</script>'
    out = head("LateNightBirds | AI Marketing & Automation Agency", desc, "/", extra=extra)
    out += header("home")
    out += f'''<main id="main"><div class="page" id="top"><div class="frame">
<section class="hero">
  <div class="banner" role="img" aria-label="Night sky with a crescent moon, stars and birds in flight over a quiet city">{BANNER}</div>
  <div class="hero-row">
    <div class="avatar"><img src="/assets/logo-mark.svg" alt="LateNightBirds logo" width="92" height="92"></div>
    <div class="cta-row">
      <a class="btn btn-solid" href="mailto:{EMAIL}?subject=Free%20Growth%20Audit">Book a Free Growth Audit <i>→</i></a>
      <a class="btn btn-ghost" href="#services">See Services <i>→</i></a>
    </div>
  </div>
  <div class="intro">
    <h1>AI marketing &amp; automation that <em>works the night shift.</em></h1>
    <p class="meta"><span class="dot"></span> AI Marketing &amp; Automation Agency · LateNightBirds LLC</p>
    <p class="lede">We build search, content and automation systems that attract, convert and scale, so your growth keeps compounding long after the office lights go off. No vanity metrics. No guesswork. Just revenue.</p>
  </div>
  <ul class="stats" aria-label="Agency highlights">
    <li><b data-count="20" data-suffix="+">20+</b><span>Years combined experience</span></li>
    <li><b data-count="350" data-suffix="+">350+</b><span>Happy clients</span></li>
    <li><b data-count="98" data-suffix="%">98%</b><span>Client satisfaction</span></li>
  </ul>
</section>

<section class="block reveal">
  <h2 class="eyebrow">Sound familiar?</h2>
  <p class="statement">Lots of businesses are <em>“doing marketing”</em> without growing. Content that doesn't convert. Ads that burn cash. Rankings below competitors who aren't even better.</p>
  <p class="sub">We replace the noise with clarity: AI-assisted systems engineered to attract, convert and scale.</p>
</section>

<section class="block reveal" id="services">
  <h2 class="eyebrow">What we do</h2>
  <div class="cards">
    <article class="card"><span class="num">01</span><h3>AI-Focused SEO</h3><p>Get found by customers already searching for what you offer. We build search visibility that compounds over time, from ecommerce to SaaS, instead of rankings that disappear.</p></article>
    <article class="card"><span class="num">02</span><h3>Content &amp; Ethical Link Acquisition</h3><p>Turn attention into authority. Content that educates, persuades and sells in the background, backed by links earned the right way.</p></article>
    <article class="card"><span class="num">03</span><h3>Marketing Automation</h3><p>AI workflows for lead capture, nurturing, reporting and follow-up. The repetitive work runs on its own so your team can focus on closing.</p></article>
    <article class="card"><span class="num">04</span><h3>Web Launch &amp; Growth</h3><p>Be present where your audience already lives. Strategy, design, content and implementation, launched properly and built to convert.</p></article>
  </div>
</section>

<section class="block reveal" id="process">
  <h2 class="eyebrow">How the night shift works</h2>
  <p class="sub left">Predictable growth comes from a repeatable system, not a lucky campaign.</p>
  <ol class="steps">
    <li><b>Audit</b><span>We map where your next customer comes from (search, social or content) and where budget leaks.</span></li>
    <li><b>Strategize</b><span>Data and buyer behavior shape a plan tailored to your business model. We don't chase trends.</span></li>
    <li><b>Automate</b><span>AI handles research, production and routine operations. Strategists guide judgment and quality.</span></li>
    <li><b>Compound</b><span>We measure, refine and scale what works, month after month.</span></li>
  </ol>
  <div class="grid-wrap" aria-hidden="true">
    <div class="grid-label">A day at LateNightBirds: automation runs while you sleep <span>(illustrative)</span></div>
    <div class="hours" id="hours"></div>
    <div class="legend"><span><i class="l1"></i>Your team</span><span><i class="l2"></i>Automation running</span></div>
  </div>
</section>

<section class="block reveal" id="results">
  <h2 class="eyebrow">Why LateNightBirds</h2>
  <div class="why">
    <div><h3>Proven strategies</h3><p>Know where your next customer is coming from each month, whether that is search, social or content.</p></div>
    <div><h3>Expertise &amp; promise</h3><p>Led by strategists who focus on data, behavior and long-term results.</p></div>
    <div><h3>Customized solutions</h3><p>We engineer predictable growth through SEO, content, social and automation built for your model.</p></div>
  </div>
</section>

<section class="block reveal">
  <h2 class="eyebrow">Trusted by brands that refuse to stay average</h2>
  <div class="quotes">
    <blockquote><p>“LateNightBirds transformed our digital marketing approach, helping us achieve results we never imagined possible. Highly recommended!”</p></blockquote>
    <blockquote><p>“A skilled team with real insight.”</p><cite>Michael Hover</cite></blockquote>
    <blockquote><p>“They refined our strategy effectively and efficiently.”</p><cite>Ella Ford</cite></blockquote>
  </div>
</section>

<section class="block reveal">
  <div class="section-head"><h2 class="eyebrow">From the blog</h2><a class="link-arrow" href="/blog/">All articles →</a></div>
  <div class="posts">{"".join(card(p) for p in posts[:3])}</div>
</section>
</div></div></main>
'''
    out += footer()
    return out


def blog_index(posts):
    out = head("Blog | LateNightBirds", "Practical writing on SEO, blogging, search and AI-era marketing from the LateNightBirds team.", "/blog/")
    out += header("blog")
    rows = ""
    for p in posts:
        rows += (f'<a class="row" href="/blog/{p["slug"]}/"><div><h2>{html.escape(p["title"])}</h2>'
                 f'<p>{html.escape(p["excerpt"])}</p><p class="pmeta">{p["pretty"]} · {p["mins"]} min read</p></div>'
                 f'<img src="/blog/img/{p["img"]}" alt="" width="720" height="480" loading="lazy"></a>')
    out += f'''<main id="main">
<div class="blog-head"><p class="eyebrow">The LateNightBirds Blog</p><h1>Ideas for growth that works while you sleep.</h1><p>Practical writing on SEO, search, blogging and marketing in the age of AI.</p></div>
<div class="list">{rows}</div>
</main>
'''
    return out + footer()


def takeaways_html(p):
    items = p.get("takeaways")
    if not items:
        return ""
    lis = "".join(f"<li>{html.escape(t)}</li>" for t in items)
    return f'<aside class="takeaways" aria-label="Key takeaways"><p class="tk-label">Key takeaways</p><ul>{lis}</ul></aside>'


def related_html(p, by_slug):
    slugs = RELATED.get(p["slug"], [])
    items = [by_slug[s] for s in slugs if s in by_slug]
    if not items:
        return ""
    lis = "".join(f'<li><a href="/blog/{x["slug"]}/">{html.escape(x["title"])}</a></li>' for x in items)
    return f'<section class="related"><h2>Related reading</h2><ul>{lis}</ul></section>'


def faq_html(faqs):
    if not faqs:
        return ""
    items = "".join(f'<div class="qa"><h3>{html.escape(q)}</h3><p>{html.escape(v)}</p></div>' for q, v in faqs)
    return f'<section class="faq"><h2>Frequently asked questions</h2>{items}</section>'


BY_SLUG = {}


def post_page(p, posts):
    url = f"/blog/{p['slug']}/"
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "datePublished": p["iso"],
          "image": f"{SITE}/blog/img/{p['img']}", "author": {"@type": "Organization", "name": "LateNightBirds"},
          "publisher": {"@type": "Organization", "name": "LateNightBirds LLC", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo-mark.svg"}},
          "mainEntityOfPage": SITE + url}
    faqs = p.get("faqs", [])
    if faqs:
        fq = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": v}} for q, v in faqs]}
    extra = (f'<meta property="article:published_time" content="{p["iso"]}">'
             f'<script type="application/ld+json">{json.dumps(ld)}</script>'
             + (f'<script type="application/ld+json">{json.dumps(fq)}</script>' if faqs else ""))
    out = head(f'{p["title"]} | LateNightBirds', p["excerpt"], url, og_type="article", extra=extra)
    out += header("blog")
    others = [x for x in posts if x["slug"] != p["slug"]][:3]
    out += f'''<main id="main"><article class="article">
<p class="crumbs"><a href="/blog/">← All articles</a></p>
<h1>{html.escape(p["title"])}</h1>
<div class="byline"><img src="/assets/logo-mark.svg" alt="" width="42" height="42"><div><b>LateNightBirds Team</b><span>{p["pretty"]} · {p["mins"]} min read</span></div></div>
<figure class="hero-img"><img src="/blog/img/{p["img"]}" alt="" width="720" height="480"></figure>
{takeaways_html(p)}<div class="prose">{p["body"]}</div>
{faq_html(faqs)}
{related_html(p, BY_SLUG)}
</article>
<div class="after"><div class="cta-card"><div><h3>Want this kind of thinking applied to your growth?</h3><p>Book a free growth audit with the LateNightBirds team.</p></div><a class="btn btn-solid" href="mailto:{EMAIL}?subject=Free%20Growth%20Audit">Book a Free Growth Audit <i>→</i></a></div></div>
<section class="more"><div class="section-head"><h2 class="eyebrow">More to read</h2><a class="link-arrow" href="/blog/">All articles →</a></div><div class="posts">{"".join(card(x) for x in others)}</div></section>
</main>
'''
    return out + footer()


def not_found():
    out = head("Page not found | LateNightBirds", "That page could not be found.", "/404")
    out += header("")
    out += '<main id="main"><div class="blog-head" style="text-align:center;padding:120px 24px"><p class="eyebrow">Error 404</p><h1>This page flew the coop.</h1><p>The page you are looking for does not exist or has moved.</p><p style="margin-top:28px"><a class="btn btn-solid" href="/">Back to home <i>→</i></a> <a class="btn btn-ghost" href="/blog/">Read the blog</a></p></div></main>'
    return out + footer()


def write(rel, content):
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")


def main():
    posts = load_posts()
    BY_SLUG.update({x["slug"]: x for x in posts})
    write("index.html", home(posts))
    write("blog/index.html", blog_index(posts))
    for p in posts:
        write(f"blog/{p['slug']}/index.html", post_page(p, posts))
    write("404.html", not_found())
    # keep old WordPress URLs alive
    redirects = [f"/{p['slug']}/ /blog/{p['slug']}/ 301" for p in posts]
    redirects += ["/about/ /#top 301", "/services/ /#services 301", "/contact/ /#contact 301", "/home/ / 301"]
    write("_redirects", "\n".join(redirects) + "\n")
    urls = ["/", "/blog/"] + [f"/blog/{p['slug']}/" for p in posts]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{SITE}{u}</loc></url>" for u in urls] + ["</urlset>"]
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    bad = [f for f in list(ROOT.glob("*.html")) + list(ROOT.glob("blog/**/*.html")) if re.search("[–—]", f.read_text())]
    print(f"built {len(posts)} posts; files containing long dashes: {[str(b) for b in bad]}")


if __name__ == "__main__":
    main()
