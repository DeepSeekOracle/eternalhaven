"""Editorial standards and change log — the maintenance record a reviewer can read."""

PAGES = []

PAGES.append({
    "path": "/editorial-standards.html",
    "nav": "",
    "kicker": "House rules",
    "h1": "How this site is made, changed, and corrected",
    "lede": "One author, one rule per page, a date on every claim. This is the record of how the library is maintained and what happens when it is wrong.",
    "byline": "Standards and changelog &#183; updated 6 November 2026 &#183; about a ten-minute read",
    "crumb_parts": [("/", "Home"), (None, "Editorial standards")],
    "title": "Editorial standards and changelog — Eternal Haven",
    "ogtitle": "How this site is made, changed, and corrected",
    "description": "The editorial standard behind eternalhaven.ca: one job per page, prose minimums, ad placement rules, how corrections are handled, and a dated changelog.",
    "ogtype": "website",
    "schema": {
        "@type": "WebPage",
        "name": "Editorial standards and changelog",
        "url": "https://eternalhaven.ca/editorial-standards.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "datePublished": "2026-11-06",
        "dateModified": "2026-11-06",
    },
    "body": """
<p>Every page on this domain is written by one person, dated, and held to the same rules. Publishing the rules is not a boast; it is a way for a reader to check whether the site is being kept or merely left running. If a page breaks one of the rules below, the page is wrong and the rules are not negotiable.</p>
<h2>The rules</h2>
<p><strong>One page, one job.</strong> Every page answers exactly one question in prose before it asks the reader to do anything. If a page cannot be described in one sentence, it is two pages and one of them will be thin. The full argument is <a href="/blog/one-page-one-job.html">here</a>.</p>
<p><strong>Prose before requests.</strong> No advertisement, modal, or sign-up sits above the headline or inside the first two paragraphs. Ad units appear only on pages with substantial writing, only after a section has been delivered, and never inside a player or a tool screen.</p>
<p><strong>A real introduction.</strong> A title is not an introduction. Every page opens with a lead that says what the page is for, and a hero or header that a first-time visitor can read without knowing the site's internal vocabulary.</p>
<p><strong>Dates on claims.</strong> Pages that describe a state of the world carry a date. A page without a date is either permanently true or unmaintained, and very little is permanently true.</p>
<p><strong>No invented detail.</strong> If an edition does not exist, the page says it does not exist. If a feed is down, the page says it is down. If a tool is a demonstration, it is labelled a demonstration. The house phrase for this is <em>empty beats fake</em>, and it applies to book listings as much as to dashboards.</p>
<p><strong>No page that only points elsewhere.</strong> When work moves to another domain, the address keeps a page that explains what moved, why, and where it went. A meta-refresh with no sentence behind it is a shrug, and shrugs are not pages.</p>
<h2>How corrections work</h2>
<p>Corrections are made on the record. When a factual error is found, the page is fixed and its date changes; for a substantial error, the changelog below records what changed. I do not quietly rewrite a claim and hope nobody kept a copy, because the whole publishing argument on this site depends on the file being the file.</p>
<p>If you find an error, the <a href="/contact.html">contact page</a> is the route. Say what you read, what you expected, and where the URL is. Rights concerns are answered before anything else.</p>
<!--AD-->
<h2>What an advertisement is allowed to do here</h2>
<p>Advertising keeps the hosting paid, and it is the only commercial thing on the site. It is not allowed to interrupt reading, cover a paragraph, autoplay, or appear on a page that has not yet given the reader something. Tool screens stay ad-free on purpose: a tool that taxes its own use is a worse tool. Privacy pages, contact pages, and error pages carry no units at all.</p>
<p>This is also why some pages carry no ads despite being long. A whitepaper is a document; a licence is a reference; a glossary is a lookup. None of them benefits from a rectangle in the middle, and a reader who is looking something up is the least appropriate audience to interrupt.</p>
<h2>Changelog</h2>
<p><strong>6 November 2026.</strong> Largest single pass on the site. Added seven book and reference pages (five volumes, a cast list, a world page), four long essays, a start page, a glossary, a tools room, and an editorial standards page. Rebuilt four room pages that were bare redirects. Expanded the homepage, about, contact, music, games, network, privacy, and terms pages. Removed ad code from moved-page stubs, regenerated the sitemap so it lists only indexable pages, fixed three broken navigation links on the music catalog, and published the music ledger JSON the catalog page advertises.</p>
<p><strong>18 October 2026.</strong> AdSense head tag added to every page. Quality gate run across all pages; thin pages either expanded or marked noindex.</p>
<p><strong>4 September 2026.</strong> Homepage rebuilt as a publisher front door rather than a systems directory. Essay library reorganised, about and contact rewritten, books page given original introductions.</p>
<p><strong>31 August 2026.</strong> Essay batch: the lantern essay, the radio essay, empty beats fake, tap tempo, the four-books note, the globe essay, and the quantum-dots series.</p>
<h2>What is not here</h2>
<p>There is no comments section, no newsletter, and no analytics script. Those are absences with reasons: a comment system needs moderation I cannot staff, a newsletter needs a promise I do not want to make, and analytics would mean a third-party script that the <a href="/privacy.html">privacy page</a> would then have to explain. The site is measured by whether people come back, which I hear about in mail.</p>
""",
    "related": [
        ("/blog/one-page-one-job.html", "One page, one job"),
        ("/blog/the-cost-of-a-quiet-website.html", "What a quiet website costs"),
        ("/privacy.html", "Privacy"),
        ("/about.html", "About this house"),
    ],
})
