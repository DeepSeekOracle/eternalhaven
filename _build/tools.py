"""The tools room — a map of the free tools in this house. Ad-free by design."""

PAGES = []

PAGES.append({
    "path": "/tools.html",
    "nav": "tools",
    "kicker": "Tools",
    "h1": "The tools room",
    "lede": "Free, no account, no upload where it can be avoided. What each tool does, what it does not do, and where the honest limits are.",
    "byline": "Guide &#183; updated 6 November 2026 &#183; about an eight-minute read",
    "crumb_parts": [("/", "Home"), (None, "Tools")],
    "title": "Tools — free browser tools from the LYGO workshop | Eternal Haven",
    "ogtitle": "Tools — free browser tools from the LYGO workshop",
    "description": "The free tools built in this workshop: an ASCII art studio, a live seal chart, a public-feed witness, a globe, and the BPM and music tools next door.",
    "schema": {
        "@type": "CollectionPage",
        "name": "The tools room",
        "url": "https://eternalhaven.ca/tools.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "hasPart": [
            {"@type": "WebApplication", "name": "LYGO ASCII Art Studio", "url": "https://eternalhaven.ca/lygo-ascii-art.html"},
            {"@type": "WebApplication", "name": "Eternal Haven Star Chart", "url": "https://eternalhaven.ca/starchart/"},
            {"@type": "WebApplication", "name": "Public witness", "url": "https://eternalhaven.ca/witness/"},
        ],
    },
    "body": """
<p>Every tool in this room follows one rule: the tool is the product, not the funnel. No account, no newsletter wall, no "sign in to save". Where something needs a key, the page says so before you click. Where a tool could upload your file, it works in the browser instead.</p>
<h2>In this house</h2>
<p><strong>The ASCII art studio.</strong> <a href="/lygo-ascii-art.html">/lygo-ascii-art.html</a> turns a photo into letters, numbers, and symbols. It runs entirely in your browser, which means the picture you drop on it never leaves your machine. Density, character set, and width are adjustable. It is a toy with a real use: a poster, a terminal banner, a portrait that survives being pasted into a plain-text file.</p>
<p><strong>The Star Chart.</strong> <a href="/starchart/">/starchart/</a> is a live view of anchored seals: what has been recorded, when, and under which root. It is a public ledger page, so treat it as <em>reference</em>: a number you can check, not a claim you have to believe. The glossary defines <a href="/glossary.html">Merkle root</a> if the vocabulary gets thick.</p>
<p><strong>The witness.</strong> <a href="/witness/">/witness/</a> watches public feeds &#8212; weather, seismic, orbital &#8212; and shows what they say without editorial. The point is not prophecy. The point is a page that will tell you the feed is down instead of showing you a stale number with a confident font.</p>
<p><strong>God's Eye.</strong> <a href="/godseye/">/godseye/</a> is the same idea on a globe. One map instead of nine tabs. It is named with a deliberate amount of irony; a globe is not an authority, and the page says so.</p>
<p><strong>The lattice kernel.</strong> <a href="/lattice/">/lattice/</a> is the workshop's self-audit room: a local monitor that reports rather than acts. It exists because a system that cannot describe its own state is a system you have to trust blindly, and I would rather not.</p>
<!--NOAD-->
<h2>Next door, on the other domains</h2>
<p>The workshop is spread across several domains because each one was built for one job. The tools that are not on this domain:</p>
<ul>
<li><a href="https://bpmfinder.ca/tools.html">BPMfinder tools</a> &#8212; tap tempo, BPM detection, and the small utilities around them. This is the tool hub for the music side.</li>
<li><a href="https://asiancoastline.com/listen.html">Asian Coastline</a> &#8212; the free listen player for the Excavationpro catalog. No account, no preview wall.</li>
<li><a href="https://excavationpro.ca/image-studio.html">The image studio</a> &#8212; the workshop's picture tool, with provider health shown honestly instead of a spinner and a promise.</li>
<li><a href="https://chatagent.ca/games/">The arcade</a> &#8212; the browser games that used to live on this domain. The <a href="/games/">games page</a> here explains the move.</li>
</ul>
<h2>What these tools are not</h2>
<p>They are not products with a roadmap meeting. None of them stores your work on a server, sells your inputs, or asks for an email. That is not a marketing position; it is a maintenance decision. A tool that keeps no data is a tool I can leave running for years without a privacy incident, a breach notice, or a compliance page written by a lawyer at midnight.</p>
<p>The flip side is scope. These are small tools built by one person. They break when a browser changes something, and the repair is not instant. If one is broken, <a href="/contact.html">tell me</a>; the contact page is the bug tracker.</p>
<h2>Why give them away</h2>
<p>Because a tool that costs nothing to run and asks nothing of you is the closest thing to a gift the web still allows. The essays explain the economics at length; the short version is that the books pay for the hosting and the tools pay for themselves in usefulness. No advertisement runs inside a tool screen in this house. That is deliberate, and it is also why the <a href="/tools.html">tools page</a> you are reading is the only place an ad could sit without ruining the thing it sits on &#8212; so it does not.</p>
<h2>How to suggest a tool</h2>
<p>Ask for something small and specific: "a page that takes a CSV and prints the column widths" is a request I can honour. "An AI platform" is not. The workshop's rule is that a tool ships when it can be described in one sentence and verified in one sitting. If you want the longer argument, <a href="/blog/systems-that-break-early.html">Systems that break early</a> is the essay that set the policy.</p>
""",
    "related": [
        ("/start.html", "Start here"),
        ("/starchart/", "Star Chart"),
        ("/witness/", "Witness"),
        ("/lygo-hub.html", "The systems hub"),
    ],
})
