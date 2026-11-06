# CHANGES — eternalhaven.ca

## 2026-11-06 (later still) — home page was hero + one paragraph + a video

The word count was there (923 prose words) but a reviewer never reached it: a full-viewport
**LYGO TV / Rumble embed** sat directly under the hero on `index.html`, pushing every article below
a screen-sized third-party video. On a phone the first screen was the hero, one paragraph, and six
stacked buttons.

- **Video embed removed from the homepage** (with its CSS/JS, ~12 KB). It existed only on this page;
  the live room is still linked from the music pages.
- Front page rebuilt **prose-first**: "Why this house exists" (six paragraphs, ~600 words) now starts
  immediately under the hero, before any card grid, media, or ad. Section order after that: books →
  essays → music → games and tools → how the site is kept → support.
- Hero CTAs cut from six to four; on phones they are a 2×2 grid instead of six full-width buttons.
- Mobile hero shortened to 76svh so the first line of the essay is on the opening screen.
- Home prose: **1,199 words** (was 923, and was 639 before this pass).

## 2026-11-06 (later) — footer rebuilt

The six-site cross-link block ("More from the workshop …") was a floating, unstyled paragraph
sitting between the article and the footer on 62 pages. It duplicated the footer's own link row,
matched neither the content column nor the footer grid, and on `games/index.html` it had drifted
into the middle of the page.

- `assets/workshop-footer.css` (new): "The workshop" is now a labelled six-column grid inside the
  footer, one line of context per site, 3 columns under 900 px, 2 under 520 px (descriptions
  dropped on phones so nothing overflows).
- The block moved inside `<footer>`, above the copyright line, on every page; the orphan
  paragraphs and the duplicated `.family` row are gone.
- `All tools` and `Discord server` share one line under the grid.
- `site-kit.js`: the floating Discord pill is hidden below 820 px — it was stacking on top of the
  sticky CTA bar and over footer links. Discord is now reachable from the footer on every page.
- The fixed cookie notice no longer covers the copyright line (body padding while it is shown).

## 2026-11-06 — full content pass (AdSense low-value-content repair)

AdSense declined the site for "low value content" after several review attempts. The measured
causes on this domain were structural, not stylistic: 57 pages, mean 400 prose words, ten pages
that were bare meta-refresh redirects, one book shelf with no per-book pages, and only seven
pages carrying an ad unit.

This pass adds substance and removes doorways.

### Added (20 pages, generated from `_build_pages.py` + `_build/*.py`)

| Page | Words | Ad |
|---|---:|---|
| `books/the-moonlit-slumber.html` | 943 | 1 |
| `books/the-shattered-accord.html` | 844 | 1 |
| `books/the-ascension-war.html` | 811 | 1 |
| `books/eternal-haven-dawns.html` | 855 | 1 |
| `books/the-unwritten-seal.html` | 791 | 1 |
| `books/characters.html` | 1,004 | 1 |
| `books/world.html` | 953 | 1 |
| `start.html` | 758 | 1 |
| `glossary.html` | 1,082 | 1 |
| `tools.html` | 677 | 0 (tool page, by policy) |
| `editorial-standards.html` | 863 | 1 |
| `blog/one-page-one-job.html` | 943 | 1 |
| `blog/how-a-book-gets-a-hash.html` | 1,019 | 1 |
| `blog/writing-a-saga-without-an-algorithm.html` | 955 | 1 |
| `blog/the-cost-of-a-quiet-website.html` | 824 | 1 |

### Rebuilt (5 pages that were bare redirects)

`HavenStarChart.html` (964), `SovereignLatticeMesh.html` (643), `BiometricEntropyHarness.html`
(729), `LYGORESONANCE.html` (703), `excavationpro-listen.html` (503). Each now explains the tool,
how to use it, and what it does not prove, then links the live surface. No tool screen carries an
ad unit.

### Site totals (quality gate, 2026-11-06)

72 pages · 43,748 prose words · mean 608 words · 32 pages at 700+ · 25 pages with an ad unit ·
15 pages under 300 words, all of them either `noindex` moved-page notes or ad-free tool demos.
Before this pass: 57 pages, mean ~400 words, 7 pages with ads.

### Expanded

`index.html` (start-here block, per-volume links, new-this-season), `about.html` (+biography,
maintenance, next), `contact.html` (+what to include, four self-serve answers, reply times),
`music.html` (+catalog numbers, public ledger, licensing), `games/index.html` (+scorecard honesty,
per-title status), `network/index.html` (+three audiences, what you can check), `privacy.html`
(+AdSense specifics, device storage, rights, retention), `terms.html` (+text licence, takedowns,
changes), `godseye/`, `lattice/`, `lygo-apps.html`, `lygo-eternal-lattice.html`,
`lygo-ascii-art.html`, `books/index.html`, `blog/index.html`,
`lygo-quantum-dots-whitepaper.html` (+1 ad on a 1,396-word page).

### Fixed

- 11 moved-page stubs: removed the AdSense script from redirect pages, replaced the one-line body
  with a titled, ad-free page that says what moved and where. Still `noindex, follow`.
- `sitemap.xml`: regenerated from an explicit list (60 URLs, `lastmod` 2026-11-06 on changed pages).
  noindex stubs and `thanks.html` are no longer listed.
- Music catalog: three broken `eternalhaven.html` links repointed; the advertised
  `data/excavationpro_music_ledger.json` now exists (extracted from the page's embedded ledger).
- `assets/site-kit.js`: the Discord button now clears the cookie banner (`:has()` rule) instead of
  sitting on top of it.
- `home.css`: the mobile nav is no longer hidden; it is a horizontally scrollable row.

### Not done, deliberately

- Nothing was pushed. Publishing is Justin's call.
- No page was deleted, redirected, or noindexed. Two pages that were already `noindex` stayed that
  way; only their ad script and body copy changed.
- AdSense review cannot be requested before 2026-11-08 (review-attempt limit).

## Verify

```
python projects/web-lattice/quality_gate.py --repo D:\LYGO_WEB\adsense-rollout\repos\eternalhaven --recursive
# 72/72 pages pass
```
