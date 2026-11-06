"""Room pages: the four tools that used to be bare redirects, plus the music door.

Each page explains what the room is, how to use it, and what it does not prove.
These are tool pages: no ad units, by policy.
"""

PAGES = []


def room(d):
    PAGES.append(d)


room({
    "path": "/HavenStarChart.html",
    "nav": "",
    "kicker": "Room &#183; the public sky",
    "h1": "The Eternal Haven Star Chart",
    "lede": "A live sky of anchored seals: names, roots, and a hash pulse you can watch. What it is for, and what a chart does not prove.",
    "byline": "Room guide &#183; updated 6 November 2026 &#183; about an eight-minute read",
    "crumb_parts": [("/", "Home"), (None, "Star Chart")],
    "title": "Haven Star Chart — how to read the public sky | Eternal Haven",
    "ogtitle": "Haven Star Chart — how to read the public sky",
    "description": "A guide to the Eternal Haven Star Chart: what the anchored seals are, how the hash pulse works, how to read a star, and what a public chart cannot prove.",
    "ogtype": "website",
    "schema": {
        "@type": "WebPage",
        "name": "Haven Star Chart",
        "url": "https://eternalhaven.ca/HavenStarChart.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "about": {"@type": "WebApplication", "name": "Eternal Haven Star Chart", "url": "https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChart.html"},
    },
    "body": """
<p>The Star Chart is the workshop's public sky. Each star is an anchor: a named piece of work whose file has been hashed and recorded, with the date and the root it belongs to. There are over thirteen hundred of them now, which is a number that means less than it sounds &#8212; many are small artifacts, and a count is not a quality. What matters is that a stranger can look at a star and check it.</p>
<p>This page was a redirect for a long time. If you landed here from a bookmark and expected to be moved, you still can be: the live chart is <a href="https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChart.html">the interactive sky</a>. What you are reading now is the explanation that should have been here, so that the room has a door with something behind it.</p>
<h2>What a star actually is</h2>
<p>A star is a record with three parts: a name, a digest, and a position in a tree. The digest is a hash of a file or a small pack of files. The position in the tree comes from a Merkle structure, which means a single root number stands for the whole set: change any file in the set and the root changes.</p>
<p>That structure is the reason the chart can be public without being a privacy problem. It publishes numbers and names, not contents. You can verify that a file you hold is the file that was anchored, without the chart ever storing the file. If you want the vocabulary, the <a href="/glossary.html">glossary</a> defines hash, Merkle root, and seal in the same plain language.</p>
<h2>The hash pulse</h2>
<p>The chart shows a live pulse: the current root recomputed on a schedule. It is a heartbeat, not a proof of liveness. A pulse that stops means the publisher stopped publishing, which is useful to know and also entirely expected when the publisher is one person with a laptop. I would rather show a pulse that can go quiet than a green dot that lies.</p>
<h2>Where the chart lives, and why</h2>
<p>The chart itself is hosted on GitHub Pages because it is a static page with a large data file and no server to keep alive. This domain, eternalhaven.ca, is the library: the place where the work is described and the argument is made. Splitting the two is not modesty. It is the same reason a printing press is not in the reading room.</p>
<p>There is also a room on this domain called <a href="/starchart/">the Star Chart room</a>, which explains the anchoring practice in more depth and links the live surface. If the two pages ever disagree, the live chart wins on numbers and this page wins on meaning. That is the canon-versus-reference distinction the house uses everywhere: a chart is a report, an essay is a claim.</p>
<h2>How to read a star</h2>
<p>Start with the name. If the name is a book, the digest is probably the manuscript or the ebook. If the name is a skill or a champion pack, it is a bundle of small files and the digest covers the pack, not each file. Then look at the date. A star is a snapshot: it says what the file was on that date, not what it is now. If an author keeps editing a file, the star stays true to the older version, which is the correct behaviour and surprises people.</p>
<p>Then check the root. If you are comparing two stars from the same pack, they should share a root. If they do not and the dates are the same, something in the set changed between the recordings. That is not necessarily a scandal; it might be a typo fix that re-ran the whole tree. But it is information, and information is the point.</p>
<h2>What the chart does not prove</h2>
<p>It does not prove the work is good. A hash is indifferent to quality; a terrible manuscript hashes as cleanly as a great one. It does not prove authorship beyond the publisher's own claim, and it does not prove that no other copy exists. It proves that a specific set of bytes was recorded at a specific time under a specific root &#8212; and in a world of quiet edits, that is most of what a reader needs.</p>
<p>It also does not survive a change of host gracefully. GitHub Pages URLs move; a page that anchors to one is only as durable as the account behind it. That is a known weakness of every public ledger run by an individual. The honest mitigation is redundancy: the numbers are published in more than one place, and the essays describe what they mean so that losing a host does not lose the meaning.</p>
<h2>Why keep it public at all</h2>
<p>Because a private receipt is a diary. The value of hashing a manuscript is not that I can prove it to myself; it is that you can check it without asking me. That is the difference between a claim and a record, and it is the only reason a small publisher can play the same game as a large one.</p>
<p>If you have a star you cannot read, <a href="/contact.html">write to me</a> with the name and I will explain what it covers. If you want the practice rather than the sky, read <a href="/blog/how-a-book-gets-a-hash.html">How a book gets a hash</a>.</p>
""",
    "related": [
        ("/starchart/", "The Star Chart room"),
        ("/glossary.html", "Glossary: hash, Merkle root, seal"),
        ("/blog/how-a-book-gets-a-hash.html", "How a book gets a hash"),
        ("/lygo-hub.html", "The systems hub"),
    ],
})


room({
    "path": "/SovereignLatticeMesh.html",
    "nav": "",
    "kicker": "Room &#183; a mesh you can poke",
    "h1": "The Sovereign Lattice Mesh",
    "lede": "An interactive demonstration of three ways for small nodes to agree: Merkle sync, mycelium sharding, and harmonic vortex consensus. A demo, labelled as one.",
    "byline": "Room guide &#183; updated 6 November 2026 &#183; about a seven-minute read",
    "crumb_parts": [("/", "Home"), (None, "Sovereign Lattice Mesh")],
    "title": "Sovereign Lattice Mesh — the interactive demo explained | Eternal Haven",
    "ogtitle": "Sovereign Lattice Mesh — the interactive demo explained",
    "description": "What the Sovereign Lattice Mesh demo shows: Merkle sync, mycelium sharding, harmonic vortex consensus, and the honest limits of a simulation.",
    "ogtype": "website",
    "schema": {
        "@type": "WebPage",
        "name": "The Sovereign Lattice Mesh",
        "url": "https://eternalhaven.ca/SovereignLatticeMesh.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "about": {"@type": "WebApplication", "name": "Sovereign Lattice Mesh", "url": "https://deepseekoracle.github.io/lygo-protocol-stack/SovereignLatticeMesh.html"},
    },
    "body": """
<p>The mesh page is a toy in the honest sense: a working visualisation of three mechanisms, run in a browser, that lets you break things and watch what happens. It is not a network you can join and it is not a claim that any of this runs at scale. It is an argument you can click.</p>
<p>The live version is at <a href="https://deepseekoracle.github.io/lygo-protocol-stack/SovereignLatticeMesh.html">the interactive mesh</a>. This page is the manual, so that the click has a sentence behind it.</p>
<h2>Three mechanisms, one question</h2>
<p>Every distributed system answers a version of the same question: how do independent nodes agree on what is true without a referee? The demo shows three answers, each with a cost.</p>
<p><strong>Merkle sync.</strong> Two nodes compare a single root hash first, and only walk down the tree where the roots disagree. It is how you can synchronise a large catalog by sending a few hundred bytes. The cost is that a node must be willing to trust the hash function and must keep a tree in a shape that can be walked. In the demo you can desynchronise a node and watch the walk find the difference.</p>
<p><strong>Mycelium sharding.</strong> Split the catalog into shards that spread across nodes, so no single machine holds everything. The benefit is redundancy and the ability to run on cheap hardware. The cost is that a shard is only as durable as the number of places it lives, and healing after a node disappears takes time. The demo lets you remove nodes and watch availability degrade, which is a more useful lesson than a diagram.</p>
<p><strong>Harmonic vortex consensus.</strong> The house's name for a weighted agreement round: nodes converge on a value by pulling toward a weighting function rather than a single leader. It is the most speculative of the three and the one I would defend least in a production argument. In the demo it shows convergence and, more importantly, divergence when the weights are adversarial &#8212; which is the behaviour you actually want to study.</p>
<h2>What the demo is not</h2>
<p>It is not a blockchain. There is no token, no mining, no economic incentive, and no claim that a browser simulation is a secure network. It is also not a benchmark: the timings you see are JavaScript on your machine, not a network under load. Anyone who reads a latency number off a demo and puts it in a slide deck is doing the thing this page is trying to prevent.</p>
<p>What it is good for is building intuition. Watching a shard go unavailable because two of its three holders left is a lesson that a paragraph cannot deliver as well. Watching a consensus round stall when one node weights itself too heavily is the same lesson in a different register.</p>
<h2>Why this lives on a fiction publisher's domain</h2>
<p>Because the books are about seals, accords, and what happens when a guarantee outlives its guarantor, and the software is the same argument with worse prose. The <a href="/books/world.html">world page</a> explains the fiction's version of a seal chain. This page is the version with hashes. Keeping them in one house is not confusion; it is the entire point of building both.</p>
<p>If the jargon is too thick, the <a href="/glossary.html">glossary</a> is the short door. If you want the policy that governs what gets built here &#8212; small, verifiable, one sitting &#8212; read <a href="/blog/systems-that-break-early.html">Systems that break early</a>.</p>
""",
    "related": [
        ("/HavenStarChart.html", "The Star Chart"),
        ("/glossary.html", "Glossary"),
        ("/blog/systems-that-break-early.html", "Systems that break early"),
        ("/lygo-hub.html", "The systems hub"),
    ],
})
