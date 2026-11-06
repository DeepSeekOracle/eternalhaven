"""New long-form essays for Eternal Haven, November 2026."""

PAGES = []
D = "2026-11-06"


def essay(d):
    PAGES.append(d)


essay({
    "path": "/blog/how-a-book-gets-a-hash.html",
    "nav": "essays",
    "kicker": "Craft",
    "h1": "How a book gets a hash",
    "lede": "An ISBN names a book. A hash proves it is still the book. One is paperwork; the other is a receipt, and a small catalog needs both.",
    "byline": "6 November 2026 &#183; about a nine-minute read",
    "crumb_parts": [("/", "Home"), ("/blog/", "Essays"), (None, "How a book gets a hash")],
    "title": "How a book gets a hash — Eternal Haven Essays",
    "ogtitle": "How a book gets a hash",
    "description": "Justin Helmer on hash-anchoring an ebook: what SHA-256 proves, what it does not, and why a small press should publish the number next to the file.",
    "schema": {
        "@type": "BlogPosting",
        "headline": "How a book gets a hash",
        "datePublished": D,
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "url": "https://eternalhaven.ca/blog/how-a-book-gets-a-hash.html",
        "about": {"@type": "Book", "name": "The Unwritten Seal"},
    },
    "body": """
<p>When <em>The Unwritten Seal</em> went live as an ebook, I did two pieces of paperwork. The first was an ISBN, because a book needs a name a store can order. The second was a SHA-256, because a book needs a way to prove that the file you are holding is the file I wrote. The first one I filled in on a form. The second one I typed into a terminal at one in the morning, and it has done more for my peace of mind than the form did.</p>
<p>This essay is the plain-language version of that second piece of paperwork, written for writers rather than engineers. If you already know what a hash is, skip to the section about what it cannot do. That section is the only one I would defend in an argument.</p>
<h2>What a hash actually is</h2>
<p>A hash is a fingerprint computed from the bytes of a file. Feed the file into a function and you get back a fixed-length string of letters and numbers. Change one character in the file and the string changes completely. You cannot work backwards from the string to the file, and no one has ever found a practical way to make two different files with the same string on purpose.</p>
<p>That is it. That is the whole technology. It is not a blockchain, it is not a signature, and it does not prove authorship. A hash only proves one thing: the bytes you have now are the bytes that produced that number. If you also trust the source that published the number, you have something useful.</p>
<h2>Why a small press should bother</h2>
<p>Three reasons, in order of how much they matter.</p>
<p>First, edition control. Every store re-packages an ebook. Some add tracking pages, some re-flow the CSS, some strip the cover. If I publish one number and the store's edition does not match it, that is information, not a scandal. It tells me the file has been through a packaging step, and I can decide whether that step changed anything that matters.</p>
<p>Second, an end to a specific argument. Every writer eventually meets someone who claims a different edition is the original, or that a paragraph was removed, or that the book they have is the "real" one. With a published hash, that argument takes thirty seconds: compute, compare, done. Without it, the argument is about memory and vibes, and I lose either way.</p>
<p>Third, it changes my own habit. Writing down a number forces me to freeze a file. A lot of small-press chaos comes from never deciding when a book is finished, then editing it in four places forever. A hash is a small ceremony: this is the text. Future edits get a new number and a note in the changelog.</p>
<!--AD-->
<h2>What a hash cannot do</h2>
<p>It cannot prove I wrote the book. Anyone can hash a file. The hash is a receipt for a copy, not a birth certificate for an idea.</p>
<p>It cannot prove the text is unchanged across formats. An EPUB on one store and a PDF on another produce different bytes and different hashes for the same novel. If you want to compare the <em>reading experience</em>, you compare extracted text, not file bytes. The number protects the artifact, not the meaning.</p>
<p>It cannot survive a re-typeset with a new line break and still match. This is the part that annoys people. A perfectly innocent process &#8212; a retailer's re-flow, a corrected typo, a new font &#8212; changes the hash and looks, to a suspicious reader, exactly like tampering. So the number has to come with a sentence: <em>this is the file I published on this date</em>, not <em>this is the only legitimate form of this book</em>.</p>
<p>And it cannot be checked by a reader who does not know how to compute it. That is a real barrier, and pretending otherwise is how honest technical writing turns into a smug little club. Which is why the next section exists.</p>
<h2>How a normal person checks it</h2>
<p>On Windows, open PowerShell in the folder that holds the file and run <code>Get-FileHash .\\book.epub -Algorithm SHA256</code>. On a Mac or Linux machine, <code>shasum -a 256 book.epub</code>. Both print a long string. Compare it, character by character, to the number published with the listing.</p>
<p>It is not fun. It takes ten seconds. You will almost always find that the numbers match, and that is the point: a small, boring ceremony that makes a quiet guarantee real. The alternative is trusting a file because it has the right name, which is how people end up quoting a book that no longer exists.</p>
<h2>The wider habit</h2>
<p>I have started doing this for audio and for images too, because the same problem appears everywhere. A WAV gets re-encoded by every platform and the "same" track is suddenly three different waveforms. A cover image gets resized until the type is mush. A hash does not stop any of that. It just ends the argument about <em>what changed</em>, which is the only argument worth having.</p>
<p>If you write, publish one number per book. If you publish music, publish one per master. Put it somewhere that does not move: a page on your own domain, next to the download, with the date. Then never change it quietly. The number is the cheapest form of integrity available to a person with no legal department, and it costs nothing but attention.</p>
<p>The practical version for this house is in <a href="/books/the-unwritten-seal.html">The Unwritten Seal</a>, where the ISBN and the file live together. The philosophy is <a href="/blog/empty-beats-fake.html">Empty beats fake</a>: name what you actually have.</p>
""",
    "related": [
        ("/books/the-unwritten-seal.html", "Book V — The Unwritten Seal"),
        ("/blog/empty-beats-fake.html", "Empty beats fake"),
        ("/glossary.html", "Glossary: hash, Merkle root, seal"),
        ("/blog/", "All essays"),
    ],
})


essay({
    "path": "/blog/one-page-one-job.html",
    "nav": "essays",
    "kicker": "Craft",
    "h1": "One page, one job",
    "lede": "The rule that fixed two sites: every page answers exactly one question, in prose, before it asks for anything. It is not a growth tactic. It is a test.",
    "byline": "6 November 2026 &#183; about a ten-minute read",
    "crumb_parts": [("/", "Home"), ("/blog/", "Essays"), (None, "One page, one job")],
    "title": "One page, one job — Eternal Haven Essays",
    "ogtitle": "One page, one job",
    "description": "Justin Helmer on the editorial test behind two rebuilt sites: one question per page, prose before requests, and why thin pages sink a small domain.",
    "schema": {
        "@type": "BlogPosting",
        "headline": "One page, one job",
        "datePublished": D,
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "url": "https://eternalhaven.ca/blog/one-page-one-job.html",
    },
    "body": """
<p>A page can fail in a way that no screenshot reveals. It can load in half a second, look expensive, and still be a hole in the ground: nothing on it answers the question that brought the visitor. When an advertising review calls that "low value content," it is using crude language for a real observation. The page was a doorway with no room behind it.</p>
<p>I have now rebuilt two domains under one rule, and the rule is small enough to write on an index card. Every page answers exactly one question, in prose, before it asks for anything.</p>
<h2>The rule in practice</h2>
<p>Pick the question. For a book page it is "should I read this, and what is it?" For a tools page it is "which of these is worth my evening?" For a contact page it is "can I reach a human?" If you cannot say the question in one sentence, the page is two pages wearing one URL, and one of them is going to be thin.</p>
<p>Then answer it in paragraphs. Not bullets, not cards, not an accordion. Paragraphs, because a paragraph is where a claim has to survive contact with a reader. A card that says "AI-powered publishing workflow" can be produced by anyone in four seconds; a sentence that explains what happens when you press publish cannot.</p>
<p>Then, and only then, ask. Sign up, buy, play, contact. The order matters more than the design. A request made before the answer is a toll booth, and people correctly refuse to pay tolls for nothing.</p>
<h2>What it fixed</h2>
<p>The first domain I did this on had a music catalog. Every page was a shell with buttons: listen here, buy there, follow this. The prose lived nowhere. Rebuilding it meant writing introductions that only the artist could have written &#8212; what a track cost to make, why a licence is worded the way it is, which door is a backup and which is the front. The site got slower to build and much faster to trust.</p>
<p>The second domain is this one. It had essays already, and essays are not the problem. The problem was the scaffolding around them: ten pages that were only a redirect, a book section that listed five titles with no introduction, a contact page with an address and nothing else. The essays were a library; the front of the house was a corridor of doors that opened onto other buildings.</p>
<!--AD-->
<h2>The three failures the rule catches</h2>
<p><strong>The stub.</strong> A page whose whole content is a link to somewhere else. It exists so a URL does not 404, which is a legitimate technical need and an illegitimate reading experience. If the thing moved, say what it was and why it moved, then point at the door. That is a page. A meta-refresh is a shrug.</p>
<p><strong>The directory.</strong> A page that is a list of other pages. Useful once &#8212; a shelf, an index &#8212; and then it multiplies. A domain of directories is a maze with no rooms. Even a listing page should tell you how to choose, which is a sentence a directory cannot say.</p>
<p><strong>The duplicate.</strong> The same paragraph on four pages because it was easier than writing four paragraphs. Readers notice before crawlers do, and they notice as boredom. If a paragraph applies to everything, put it on one page and link to it from the others.</p>
<h2>What it costs</h2>
<p>Time, mostly, and the unpleasant experience of discovering that a page you were proud of has no job. Half the work of the rule is subtraction: closing a page into a redirect, or folding it into a better page, or admitting that a section was a mood rather than a subject.</p>
<p>It also costs the comfort of numbers. A directory page with forty links looks productive in a dashboard. A page that answers one question in nine hundred words looks like less until a human reads it. I have chosen the second kind of looking, because the first kind is how you end up with a site that a reviewer can describe in one word.</p>
<h2>How to test a page in sixty seconds</h2>
<p>Read the page out loud and stop after the first two paragraphs. Can you say what question it answers? If not, it is a stub. Could a different site have published those two paragraphs unchanged? If yes, it is filler. Does the page ask for something before it gives something? If yes, the order is wrong.</p>
<p>Then look at the link you would click next. If the page's only real content is that link, the page is a hallway and the room is elsewhere. Hallways are allowed in a house. A house that is only hallways is a maze, and mazes are what reviewers mean when they say a site has no value.</p>
<p>The rule is not a formula for winning a review. It is a formula for not wasting a reader's evening. Those two things overlap more than the industry admits. The <a href="/start.html">start page</a> is the test applied to this house: one page, one job, which is to send you to exactly one other page.</p>
""",
    "related": [
        ("/start.html", "Start here: the rule applied to this house"),
        ("/blog/why-the-homepage-got-quieter.html", "Why the homepage got quieter"),
        ("/blog/ads-and-a-house-that-still-opens.html", "Ads and a house that still opens"),
        ("/blog/", "All essays"),
    ],
})
