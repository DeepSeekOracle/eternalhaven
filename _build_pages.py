#!/usr/bin/env python3
"""Build Eternal Haven editorial pages from the content modules in _build/.

Every generated page shares one head (canonical, OG, X card, AdSense, JSON-LD),
one mast, one footer, one cookie banner and one workshop link block, so a page
cannot drift out of the network standard.  Run:

    python _build_pages.py            # rewrite every page
    python _build_pages.py books      # only one module
"""
from __future__ import annotations

import importlib
import json
import pathlib
import sys
from string import Template

ROOT = pathlib.Path(__file__).resolve().parent
SITE = "https://eternalhaven.ca"
PUB = "ca-pub-0646320966060599"

NAV = [
    ("/", "Home", "home"),
    ("/start.html", "Start", "start"),
    ("/books/", "Books", "books"),
    ("/blog/", "Essays", "essays"),
    ("/glossary.html", "Glossary", "glossary"),
    ("/music.html", "Music", "music"),
    ("/tools.html", "Tools", "tools"),
    ("/about.html", "About", "about"),
]

AD = """<div class="ad-slot" aria-label="Advertisement">
  <div class="ad-label">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-0646320966060599" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>"""

TEMPLATE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$description">
<meta name="author" content="Justin Helmer">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="$canonical">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/favicon.svg">
<link rel="stylesheet" href="/blog/blog.css">
<link rel="stylesheet" href="/assets/workshop-footer.css">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=IBM+Plex+Mono:wght@400&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<meta name="google-adsense-account" content="$pub">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=$pub" crossorigin="anonymous"></script>
<meta property="og:type" content="$ogtype">
<meta property="og:url" content="$canonical">
<meta property="og:title" content="$ogtitle">
<meta property="og:description" content="$description">
<meta property="og:site_name" content="Eternal Haven">
<meta property="og:image" content="$site/assets/og-home.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Eternal Haven — a library under a star vault">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@Excavationpro">
<meta name="twitter:creator" content="@Excavationpro">
<meta name="twitter:title" content="$ogtitle">
<meta name="twitter:description" content="$description">
<meta name="twitter:image" content="$site/assets/og-home.jpg">
<script type="application/ld+json">$schema</script>
<style>
$css
</style>
</head>
<body class="essay-site">
<header class="mast"><div class="mast-inner">
  <a class="mark" href="/">Eternal Haven</a>
  <nav>$nav</nav>
</div></header>
<article class="wrap">
  <p class="crumb">$crumb</p>
  <p class="kicker">$kicker</p>
  <h1>$h1</h1>
  <p class="lede">$lede</p>
  <div class="byline"><div class="avatar" aria-hidden="true">JH</div><div><strong>Justin Helmer</strong><br>$byline</div></div>
  <div class="prose">
$body
  </div>
$related
  <div class="author"><div class="avatar" aria-hidden="true">JH</div><div><h3>Justin Helmer</h3><p>Writes the Eternal Haven saga and the essays on this domain, publishes music as Excavationpro, and keeps the lantern on at <a href="/start.html">/start.html</a>.</p></div></div>
</article>
<footer class="foot"><div class="foot-inner">
  <nav><a href="/">Home</a> <a href="/start.html">Start here</a> <a href="/books/">Books</a> <a href="/blog/">Essays</a> <a href="/glossary.html">Glossary</a> <a href="/music.html">Music</a> <a href="/tools.html">Tools</a> <a href="/games/">Games</a> <a href="/contact.html">Contact</a> <a href="/privacy.html">Privacy</a> <a href="/terms.html">Terms</a> <a href="/editorial-standards.html">Standards</a></nav>
  <div class="workshop-nav">
    <p class="workshop-title" id="workshop-title">The workshop</p>
    <ul aria-labelledby="workshop-title">
      <li><a href="https://excavationpro.ca/">Excavationpro<span>music, essays, image studio</span></a></li>
      <li><a href="https://asiancoastline.com/">Asian Coastline<span>free listen player</span></a></li>
      <li><a href="https://bpmfinder.ca/">BPMfinder<span>tempo tools and guides</span></a></li>
      <li><a href="https://justinhelmer.ca/">Justin Helmer<span>author site</span></a></li>
      <li><a href="https://deepseekoracle.com/">DeepSeek Oracle<span>systems and whitepapers</span></a></li>
      <li><a href="https://chatagent.ca/">Chatagent<span>portal and arcade</span></a></li>
    </ul>
    <p class="workshop-tools"><a href="https://bpmfinder.ca/tools.html">All tools &rarr;</a><span class="sep" aria-hidden="true"> &middot; </span><a href="https://discord.gg/ktGcEkVN9" rel="noopener">Discord server</a></p>
  </div>
  <p>&copy; <span class="y"></span> Justin Helmer / Eternal Haven. Original writing. Empty beats fake.</p>
</div></footer>
<script>document.querySelectorAll(".y").forEach(function(n){n.textContent=new Date().getFullYear()});</script>
<script src="/assets/site-kit.js" defer></script>
<div class="cookie-banner" id="cookieBanner" role="dialog" aria-label="Cookie consent">
  <div>Ads may use cookies after you accept. <a href="/privacy.html">Privacy</a></div>
  <div><button type="button" class="ok" id="cookieOk">Accept</button><button type="button" class="no" id="cookieNo">Decline</button></div>
</div>
</body>
</html>
""")


def nav_html(current: str) -> str:
    out = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return " ".join(out)


def crumbs(parts: list[tuple[str, str]]) -> str:
    items = " &#183; ".join(
        f'<a href="{href}">{label}</a>' if href else label for href, label in parts
    )
    return items


def breadcrumb_schema(parts: list[tuple[str, str]]) -> dict:
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label,
             **({"item": SITE + href} if href else {})}
            for i, (href, label) in enumerate(parts)
        ],
    }


def render(page: dict) -> str:
    path = page["path"]
    canonical = SITE + path
    body = page["body"]
    if "<!--AD-->" in body:
        body = body.replace("<!--AD-->", AD)
    schema = {"@context": "https://schema.org", "@graph": [page["schema"]]}
    if "crumb_parts" in page:
        schema["@graph"].append(breadcrumb_schema(page["crumb_parts"]))
    related = ""
    if page.get("related"):
        links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in page["related"])
        related = ('<div class="related"><h2>Keep reading</h2><ul class="read-list">'
                   + links + "</ul></div>")
    html = TEMPLATE.substitute(
        title=page["title"],
        description=page["description"],
        canonical=canonical,
        pub=PUB,
        site=SITE,
        ogtype=page.get("ogtype", "article"),
        ogtitle=page.get("ogtitle", page["title"]),
        schema=json.dumps(schema, ensure_ascii=False, separators=(",", ":")),
        css=CSS,
        nav=nav_html(page.get("nav", "")),
        crumb=" &#183; ".join(
            f'<a href="{h}">{t}</a>' if h else t for h, t in page.get("crumb_parts", [])
        ),
        kicker=page["kicker"],
        h1=page["h1"],
        lede=page["lede"],
        byline=page["byline"],
        body=body,
        related=related,
    )
    return html


CSS = """.cookie-banner{position:fixed;left:12px;right:12px;bottom:16px;z-index:90;max-width:36rem;margin:0 auto;padding:.9rem 1rem;background:#121018;border:1px solid rgba(244,238,230,.16);border-radius:12px;color:#a89b8c;font:500 .88rem/1.45 system-ui,sans-serif;display:none;gap:.5rem;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
.cookie-banner.show{display:flex}
.cookie-banner a{color:#8ec8e8}
.cookie-banner button{cursor:pointer;border-radius:8px;padding:.45rem .85rem;font-weight:600;border:1px solid rgba(244,238,230,.16);background:transparent;color:#f4eee6}
.cookie-banner .ok{background:#d4b56a;color:#1a140c;border-color:#d4b56a}
"""


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.path.insert(0, str(ROOT))
    modules = ["books", "reference", "guides", "tools", "essays", "essays2", "rooms", "rooms2", "standards"]
    written = 0
    for name in modules:
        if only and only != name:
            continue
        try:
            mod = importlib.import_module(f"_build.{name}")
        except ModuleNotFoundError:
            print(f"skip _build.{name} (not written yet)")
            continue
        importlib.reload(mod)
        for page in mod.PAGES:
            out = ROOT / page["path"].lstrip("/")
            if not page["path"].endswith(".html"):
                out = out / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(page), encoding="utf-8")
            print(f"wrote {out.relative_to(ROOT)}")
            written += 1
    print(f"{written} page(s) written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
