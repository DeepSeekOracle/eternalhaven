#!/usr/bin/env python3
"""Regenerate sitemap.xml. Only indexable pages are listed; noindex stubs are not."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = "2026-11-06"
OLD = "2026-08-31"
SEP = "2026-09-04"

# (path, lastmod, changefreq, priority)
URLS = [
    ("/", D, "weekly", "1.0"),
    ("/start.html", D, "monthly", "0.97"),
    ("/books/", D, "weekly", "0.96"),
    ("/blog/", D, "weekly", "0.96"),
    ("/network/", D, "daily", "0.95"),
    ("/about.html", D, "monthly", "0.95"),
    ("/books/the-moonlit-slumber.html", D, "monthly", "0.95"),
    ("/books/the-shattered-accord.html", D, "monthly", "0.94"),
    ("/books/the-ascension-war.html", D, "monthly", "0.94"),
    ("/books/eternal-haven-dawns.html", D, "monthly", "0.94"),
    ("/books/the-unwritten-seal.html", D, "monthly", "0.93"),
    ("/games/", D, "monthly", "0.94"),
    ("/music.html", D, "weekly", "0.92"),
    ("/lygo-quantum-dots-whitepaper.html", OLD, "monthly", "0.92"),
    ("/glossary.html", D, "monthly", "0.90"),
    ("/editorial-standards.html", D, "monthly", "0.88"),
    ("/tools.html", D, "monthly", "0.90"),
    ("/witness/", OLD, "daily", "0.90"),
    ("/starchart/", D, "daily", "0.90"),
    ("/lygo-hub.html", D, "weekly", "0.90"),
    ("/lattice/", D, "weekly", "0.88"),
    ("/skynet/", OLD, "daily", "0.88"),
    ("/godseye/", D, "weekly", "0.88"),
    ("/books/characters.html", D, "monthly", "0.85"),
    ("/books/world.html", D, "monthly", "0.85"),
    ("/lygo-ascii-art.html", D, "monthly", "0.85"),
    ("/HavenStarChart.html", D, "weekly", "0.82"),
    ("/excavationpro-listen.html", D, "weekly", "0.82"),
    ("/SovereignLatticeMesh.html", D, "monthly", "0.80"),
    ("/BiometricEntropyHarness.html", D, "monthly", "0.80"),
    ("/LYGORESONANCE.html", D, "monthly", "0.80"),
    ("/lygo-apps.html", D, "monthly", "0.78"),
    ("/lygo-eternal-lattice.html", D, "monthly", "0.78"),
    ("/lygo-music-license.html", D, "monthly", "0.78"),
    ("/lygo-turbo-models-whitepaper.html", OLD, "monthly", "0.78"),
    ("/excavationpro-music-catalog.html", D, "monthly", "0.75"),
    ("/excavationpro-sovereign-music-hub.html", D, "monthly", "0.75"),
    ("/blog/one-page-one-job.html", D, "monthly", "0.86"),
    ("/blog/how-a-book-gets-a-hash.html", D, "monthly", "0.86"),
    ("/blog/writing-a-saga-without-an-algorithm.html", D, "monthly", "0.86"),
    ("/blog/the-cost-of-a-quiet-website.html", D, "monthly", "0.86"),
    ("/blog/safety-layer-on-a-live-substrate.html", OLD, "monthly", "0.85"),
    ("/blog/harmony-of-human-and-machine.html", OLD, "monthly", "0.85"),
    ("/blog/quantum-dots-as-truth-anchors.html", OLD, "monthly", "0.85"),
    ("/blog/systems-that-break-early.html", OLD, "monthly", "0.85"),
    ("/blog/the-lantern-is-still-on.html", OLD, "monthly", "0.82"),
    ("blog/", D, "weekly", "0.0"),  # placeholder removed below
]

ESSAYS_OLD = [
    "why-the-homepage-got-quieter", "shipping-a-song-to-the-open-web",
    "reading-eternal-haven-in-order", "a-browser-golf-course-is-a-house",
    "ads-and-a-house-that-still-opens", "the-lantern-is-still-on",
    "lurk-friendly-radio", "empty-beats-fake", "tap-tempo-and-the-body",
    "four-books-and-a-long-road", "what-a-public-globe-is-for",
]
URLS = [u for u in URLS if u[0] != "blog/"]
for slug in ESSAYS_OLD:
    URLS.append((f"/blog/{slug}.html", SEP, "monthly", "0.80"))

URLS += [
    ("/contact.html", D, "yearly", "0.70"),
    ("/privacy.html", D, "yearly", "0.50"),
    ("/terms.html", D, "yearly", "0.40"),
]

parts = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, lastmod, freq, pri in URLS:
    parts.append(
        f"  <url><loc>https://eternalhaven.ca{path}</loc><lastmod>{lastmod}</lastmod>"
        f"<changefreq>{freq}</changefreq><priority>{pri}</priority></url>"
    )
parts.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(parts) + "\n", encoding="utf-8")
print(f"sitemap.xml: {len(URLS)} urls")
