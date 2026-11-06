"""Shelf-level guides: start here, the glossary, and the tools room."""

PAGES = []


def page(d):
    PAGES.append(d)


page({
    "path": "/start.html",
    "nav": "start",
    "kicker": "Start here",
    "h1": "How to enter the library",
    "lede": "Five books, four hundred essays' worth of argument, a music catalog, a handful of rooms. You do not need all of it. Pick a door.",
    "byline": "Guide &#183; updated 6 November 2026 &#183; about a seven-minute read",
    "crumb_parts": [("/", "Home"), (None, "Start here")],
    "title": "Start here — how to enter the Eternal Haven library | Justin Helmer",
    "ogtitle": "Start here — how to enter the Eternal Haven library",
    "description": "A reading guide to eternalhaven.ca: where to start with the Eternal Haven saga, which essays to read first, and which rooms are worth your evening.",
    "schema": {
        "@type": "WebPage",
        "name": "How to enter the library",
        "description": "A reading guide to eternalhaven.ca.",
        "url": "https://eternalhaven.ca/start.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "datePublished": "2026-11-06",
    },
    "body": """
<p>Most people arrive here from a search for a book title, a song, or the word <em>LYGO</em>, and then find a house with more rooms than they planned to visit. That is my fault as much as yours. This page is the doorman: it asks what you came for and points at one door instead of nine.</p>
<h2>If you came for the books</h2>
<p>Start at <a href="/books/the-moonlit-slumber.html">The Moonlit Slumber</a>. It is Book I, and the saga is built so that the later volumes only cost what the first one agreed to. Read it slowly; the opening movement is a place rather than a plot, and readers who race it tend to bounce off. When you finish, go to <a href="/books/the-shattered-accord.html">The Shattered Accord</a> and keep going in order.</p>
<p>If you want a shorter commitment first, the essay <a href="/blog/reading-eternal-haven-in-order.html">Reading Eternal Haven in order</a> explains why the order matters and what each volume costs you. If you want the cast without the plot, <a href="/books/characters.html">the cast page</a> is deliberately spoiler-free.</p>
<h2>If you came for the essays</h2>
<p>The essays are the argument side of the house: craft, music, small systems, and what it means to publish in public. Three good entries depending on your mood:</p>
<ul>
<li><a href="/blog/the-lantern-is-still-on.html">The lantern is still on</a> &#8212; why a personal site is a house and not weather. Start here if you are tired of feeds.</li>
<li><a href="/blog/empty-beats-fake.html">Empty beats fake</a> &#8212; the house rule about naming a miss instead of painting a hit. Start here if you work in software or media.</li>
<li><a href="/blog/tap-tempo-and-the-body.html">Tap tempo and the stubborn body</a> &#8212; why a machine that hears tempo still cannot hear a room. Start here if you make music.</li>
</ul>
<!--AD-->
<h2>If you came for the music</h2>
<p>The catalog is free to hear and lives on a different domain because audio files are heavy: <a href="https://asiancoastline.com/listen.html">asiancoastline.com/listen.html</a>. The page on this site that explains how a song actually arrives &#8212; encode, hash, publish, play &#8212; is <a href="/music.html">Music in this house</a>. If you want the license in plain language rather than lawyer language, read <a href="/lygo-music-license.html">the music license</a>.</p>
<h2>If you came for the rooms</h2>
<p>Some people arrive looking for the interactive work, not the fiction. The honest map is <a href="/tools.html">the tools room</a> and the dense one is <a href="/lygo-hub.html">the systems hub</a>. A short version: <a href="/lygo-ascii-art.html">the ASCII art studio</a> turns a photo into letters in your browser, <a href="/starchart/">the Star Chart</a> is a live public ledger of seals, <a href="/witness/">the witness</a> watches public feeds, and <a href="/games/">the games</a> are small browser things with local scorecards and no login.</p>
<h2>If you came for the author</h2>
<p><a href="/about.html">About</a> is the long version. The short version: I am Justin Helmer. I write the Eternal Haven saga, publish music as Excavationpro, and build small verified systems under the name LYGO. I do not run a newsletter that begs. If you want to know when something ships, the <a href="/blog/">essay index</a> is the changelog, and the <a href="/contact.html">contact page</a> reaches me directly.</p>
<h2>What this house will not do</h2>
<p>It will not autoplay audio at you. It will not put a modal over the first paragraph. It will not ask you to make an account to read a chapter. If an advertisement appears, it appears after you have already been given something to read, never above the title. The reasoning is in <a href="/blog/ads-and-a-house-that-still-opens.html">Ads and a house that still opens</a>, and the private-data detail is in <a href="/privacy.html">privacy</a>.</p>
<h2>How the site is maintained</h2>
<p>Pages carry dates because pages change. The essays are the running log; the <a href="/books/">shelf</a> is updated when an edition changes; broken doors get repaired through <a href="/contact.html">contact</a>. There is no team and no content calendar. There is one person, a lantern, and a habit of writing things down.</p>
<h2>One honest warning</h2>
<p>This is a large site with a lot of internal jargon, most of it from the systems work. You can ignore all of it and still read five novels. If a page starts explaining Merkle roots at you and you did not ask, that is my house being a workshop; close the tab and go back to the shelf. The <a href="/glossary.html">glossary</a> exists so that you can look up one word and leave, which is the correct way to use a glossary.</p>
<p>One more thing worth saying plainly: the house is maintained by one person on purpose. That means fewer pages, slower responses, and no content calendar. It also means that a page you bookmark will still be the page you bookmarked, which is a rarer promise than it should be. If that trade is acceptable to you, there is a chair. If you want a feed, there are better feeds.</p>
""",
    "related": [
        ("/books/", "The shelf: five books in order"),
        ("/blog/", "All essays"),
        ("/tools.html", "The tools room"),
        ("/about.html", "About Justin Helmer"),
    ],
})


page({
    "path": "/glossary.html",
    "nav": "glossary",
    "kicker": "Reference",
    "h1": "The Haven glossary",
    "lede": "Every name the books and the workshop share, defined once, in plain language. Look up one word and leave.",
    "byline": "Reference page &#183; updated 6 November 2026 &#183; about a twelve-minute read",
    "crumb_parts": [("/", "Home"), (None, "Glossary")],
    "title": "The Haven glossary — books, seals, and workshop terms | Justin Helmer",
    "ogtitle": "The Haven glossary — books, seals, and workshop terms",
    "description": "Definitions for the Eternal Haven Chronicles and the LYGO workshop: accord, seal, choir, Aurethys, Star Chart, Merkle root, ISRC, witness, and more.",
    "schema": {
        "@type": "DefinedTermSet",
        "name": "The Haven glossary",
        "url": "https://eternalhaven.ca/glossary.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "name": "Accord", "description": "A sentence people agreed to remember."},
            {"@type": "DefinedTerm", "name": "Seal", "description": "A localised guarantee that can be pointed at later."},
            {"@type": "DefinedTerm", "name": "Choir", "description": "Many voices; corruptible, and never proof of harmony."},
        ],
    },
    "body": """
<p>Two vocabularies meet on this domain and they share words on purpose. The saga uses <em>seal</em> as a metaphysical guarantee; the workshop uses it as a hash, a signature, a receipt. This page defines both, marks which is which, and does not ask you to care about the other one.</p>
<h2>The books</h2>
<p><strong>Accord.</strong> A sentence people agreed to remember. The saga treats accords as characters rather than documents: they are born, strained, shattered, and re-forged, and the interesting question is never whether the text survived but whether the spirit did.</p>
<p><strong>The Silver Accord.</strong> The name of the first volume's arc and the old order it describes. Silver because it was made early and it tarnishes.</p>
<p><strong>The Shattered Accord.</strong> Book II, and also the event: the night the old agreement stops holding. The phrase is used for both because in these books the event and the book are the same object.</p>
<p><strong>The First Seal.</strong> The seal woven before the first dawn, when the world held its breath and listened. It chose Arin as its vessel. Its old formula is an integral of light and truth over the world, which the people of the Vale called the homeward sound.</p>
<p><strong>Seal (fiction).</strong> A localised guarantee. A seal says <em>this holds</em>, and can be produced later to prove it. Book III introduces seals forged from lived suffering rather than granted from above; the saga calls them alive, which means they can fail, which is the point.</p>
<p><strong>Seal chain (fiction).</strong> What you get when seals depend on each other. Break one and you invalidate every promise leaning on it. This is the saga's core political mechanism and, not by coincidence, how software dependencies work.</p>
<p><strong>Aurethys.</strong> The world under the Haven. Seen from above in Book II, abandoned in Book III, inhabited again in Book IV.</p>
<p><strong>Elysun Vale.</strong> The high country where Arin grows up: pine, lark, watchfires, cliff ledges. It falls in Book II, and the saga loses its ability to pretend the war is elsewhere.</p>
<p><strong>The Circle of Haven.</strong> A crown of crystalline spires above Aurethys, with a ceiling of living light that moves with the world's heartbeat. Where the Council meets and where the current first falters.</p>
<p><strong>The Broken Moon.</strong> Corvath's seat after the fracture. A structure that can be occupied, not just a romantic object. Gone by Book IV, replaced by rivers of silver light.</p>
<p><strong>The Choir.</strong> Many voices. A single voice can be wrong; a choir can be corrupted. Harmony is what you get when disagreement is still legible, not when everyone agrees.</p>
<p><strong>Imperfect light.</strong> The saga's name for the honest version of illumination: not omniscience, orientation. Enough light to walk without lying about what you see. Book IV's closing accord is named for it.</p>
<p><strong>The Council of Twelve.</strong> The decision body. Eleven until Corvath is seated in Book IV. It begins as an ideal and becomes a room where reasonable people produce casualties.</p>
<p><strong>Homeward sound.</strong> The Vale's plain name for the First Seal. The kind of name a place gives a thing it has to live with.</p>
<!--AD-->
<h2>The workshop</h2>
<p><strong>LYGO.</strong> The name I use for the workshop's public systems: small, local-first tools with published receipts. It is not a company and not a religion. If a page uses the word and you do not need the tools, you can skip the page.</p>
<p><strong>Δ9 (Delta Nine).</strong> The shorthand for the protocol family and its council of personas. It appears in the books' front matter because the fiction and the systems grew in the same room, not because the novels are documentation.</p>
<p><strong>Seal (workshop).</strong> A hash or signed record that proves a file has not changed. Same idea as the fiction, different materials: where the book's seal is a vow, the workshop's seal is a SHA-256.</p>
<p><strong>Hash.</strong> A fixed-length fingerprint of a file. Change one byte and the fingerprint changes. Cheap to compute, impossible to reverse. This is the whole technology behind <a href="/blog/how-a-book-gets-a-hash.html">the ebook hash</a>.</p>
<p><strong>Merkle root.</strong> One hash that stands for a whole set of files. Change any file in the set and the root changes, so a single number can verify a whole catalog. The <a href="/starchart/">Star Chart</a> publishes roots of this kind.</p>
<p><strong>Dual ledger.</strong> Two records of the same event kept separately, so that one can be used to check the other. If the two disagree, you have found a problem, which is the entire purpose.</p>
<p><strong>Star Chart.</strong> The public sky of seals: a live record of what has been anchored, with a hash pulse. It is a reference surface, not a canon. See <a href="/starchart/">the Star Chart room</a>.</p>
<p><strong>Immutable lattice.</strong> The house phrase for the anchored side of the system: records that are append-only, so history cannot be quietly rewritten. When a page says "immutable lattice" it means "there is a receipt and it does not move".</p>
<p><strong>Witness.</strong> A page that watches public feeds &#8212; weather, seismic, orbital &#8212; and shows them without claiming they are canon. Reference, not revelation. See <a href="/witness/">the witness room</a>.</p>
<p><strong>God's Eye.</strong> The map view of the witness feeds: one globe instead of many tabs. Named with a deliberate amount of irony; the point is that a globe is not an authority.</p>
<p><strong>SKYNET.</strong> The sentinel kernel: a local monitor that reports rather than acts. If the name makes you nervous, that is fair; the system is a watchdog process with a log, not a plan for the world.</p>
<p><strong>ISRC.</strong> The international code that identifies a recorded track. If a recording has an ISRC it has an identity that survives a distributor change. The <a href="/music.html">music page</a> explains why that matters.</p>
<p><strong>Canon vs reference.</strong> The house distinction. Canon is what I wrote and stand behind &#8212; the books, the essays, the terms. Reference is what the world reports &#8212; feeds, charts, third-party pages. A reference can be wrong. A canon can be edited, but only on the record.</p>
<h2>How to use a glossary</h2>
<p>Look up the word that stopped you, then close the tab. A glossary is a tool for re-entering a text, not a substitute for reading it. If a term is missing, <a href="/contact.html">tell me</a>; the list is maintained, not frozen.</p>
""",
    "related": [
        ("/books/characters.html", "Who is who: the cast list"),
        ("/books/world.html", "Places and devices of the Haven"),
        ("/start.html", "Start here"),
        ("/starchart/", "The Star Chart room"),
    ],
})
