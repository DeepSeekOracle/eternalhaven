"""Room pages, second batch: entropy harness, resonance, and the music door."""

PAGES = []


def room(d):
    PAGES.append(d)


room({
    "path": "/BiometricEntropyHarness.html",
    "nav": "",
    "kicker": "Room &#183; randomness from a body",
    "h1": "The Biometric Entropy Harness",
    "lede": "Where do keys come from when you do not trust the machine's own randomness? This demo harvests timing from a human hand, measures it, and shows you the audit.",
    "byline": "Room guide &#183; updated 6 November 2026 &#183; about an eight-minute read",
    "crumb_parts": [("/", "Home"), (None, "Biometric Entropy Harness")],
    "title": "Biometric Entropy Harness — timing as entropy, explained | Eternal Haven",
    "ogtitle": "Biometric Entropy Harness — timing as entropy, explained",
    "description": "What the Biometric Entropy Harness demonstration does: collecting keystroke and pointer timing as entropy, measuring it honestly, and the limits of a browser demo.",
    "ogtype": "website",
    "schema": {
        "@type": "WebPage",
        "name": "The Biometric Entropy Harness",
        "url": "https://eternalhaven.ca/BiometricEntropyHarness.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "about": {"@type": "WebApplication", "name": "Biometric Entropy Harness", "url": "https://deepseekoracle.github.io/lygo-protocol-stack/BiometricEntropyHarness.html"},
    },
    "body": """
<p>Cryptography has a quiet dependency that most people never think about: every key starts as a random number, and a computer is bad at being random. It is a deterministic machine doing arithmetic. So every serious system harvests randomness from the physical world &#8212; disk timing, network jitter, a hardware chip that measures thermal noise &#8212; and then measures how much randomness it actually got.</p>
<p>This harness is a demonstration of the human version. A person's hand is a physical process: keystroke intervals, the tiny pause before a decision, the arc of a pointer. None of it is deterministic. The page collects that timing, runs it through a conditioning step, and shows you the audit, so you can see the difference between "we collected some numbers" and "we collected enough entropy to seed a key".</p>
<p>The live demo is <a href="https://deepseekoracle.github.io/lygo-protocol-stack/BiometricEntropyHarness.html">the interactive harness</a>. This page is the honest manual, including the part where I tell you what it cannot do.</p>
<h2>What it measures</h2>
<p>Three streams, all of them timing rather than content. Inter-key intervals while you type a phrase. Pointer path deviations, which carry small motor corrections nobody consciously controls. And pause distributions, which are the closest thing to a signature a human hand has.</p>
<p>There is a reason the harness never asks for a fingerprint and never records what you type (beyond the phrase it gives you). A biometric system that stores the biometric is a liability; a system that measures the <em>timing</em> of a hand and immediately reduces it to a hash is not storing anything about you that survives. That distinction is the difference between an authentication product and a demo worth publishing.</p>
<h2>What the audit shows</h2>
<p>Raw timing is not uniform. Human pauses cluster; intervals have a heavy tail. Feeding raw measurements into a key derivation function gives you a weak key with a confident face. So the harness runs a conditioning step and then estimates min-entropy &#8212; the conservative version of "how many bits do we really have". You can watch the estimate climb as you type and stall when you stop, which is a better intuition pump than any diagram.</p>
<p>The demo also shows the failure mode on purpose. Mash a key with a metronome, or let an automated script type, and the entropy estimate flattens. That is the lesson: the source is only as good as the unpredictability of the process behind it, and a human who is trying to be random is worse than a human who is not.</p>
<h2>What it does not prove</h2>
<p>It does not prove that a browser is a secure environment. JavaScript timing is coarse, a hostile page can pollute measurements, and no demo should be used to generate a key that protects something real. The demo is a teaching instrument: it makes visible a step that production systems hide.</p>
<p>It is also not a medical device and does not diagnose anything. The word "biometric" makes people assume health, and I would rather say plainly that this measures intervals, not bodies. If a page ever claims to read your physiology from typing speed, close it.</p>
<h2>Why publish a security demo at all</h2>
<p>Because the alternative is a paragraph of assurance. A page that says "we use strong randomness" is unfalsifiable. A page that shows you the collection, the conditioning, and the entropy estimate can be argued with, and being arguable is the point. This is the same policy as the rest of the workshop: publish the receipt, not the adjective.</p>
<p>The fiction's version of this idea is the seal &#8212; a guarantee that can be pointed at later. The <a href="/books/world.html">world page</a> explains seals and chains; this page is the same argument with numbers instead of dragons.</p>
<p>If you want the general rule, read <a href="/blog/systems-that-break-early.html">Systems that break early</a>. If the vocabulary is thick, the <a href="/glossary.html">glossary</a> defines seal, hash, and dual ledger in one line each.</p>
""",
    "related": [
        ("/SovereignLatticeMesh.html", "The Sovereign Lattice Mesh"),
        ("/HavenStarChart.html", "The Star Chart"),
        ("/glossary.html", "Glossary"),
        ("/lygo-hub.html", "The systems hub"),
    ],
})


room({
    "path": "/LYGORESONANCE.html",
    "nav": "",
    "kicker": "Room &#183; image to sound",
    "h1": "LYGO Resonance",
    "lede": "Point it at a picture and it answers with a soundscape or a creative brief. Useful as a starting sketch; not a composer, and it says so.",
    "byline": "Room guide &#183; updated 6 November 2026 &#183; about a seven-minute read",
    "crumb_parts": [("/", "Home"), (None, "LYGO Resonance")],
    "title": "LYGO Resonance — turning an image into sound, honestly | Eternal Haven",
    "ogtitle": "LYGO Resonance — turning an image into sound, honestly",
    "description": "How LYGO Resonance reads an image (edges, colour, contour, texture) and turns it into a soundscape or a creative profile — plus what the output is not.",
    "ogtype": "website",
    "schema": {
        "@type": "WebPage",
        "name": "LYGO Resonance",
        "url": "https://eternalhaven.ca/LYGORESONANCE.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "about": {"@type": "WebApplication", "name": "LYGO Resonance", "url": "https://deepseekoracle.github.io/Excavationpro/LYGORESONANCE.html"},
    },
    "body": """
<p>There is a long tradition of turning pictures into music, and most of it is worse than the idea deserves. The usual failure is literal mapping: brightness becomes pitch, edges become rhythm, and the result sounds like a spreadsheet with a reverb. Resonance is an attempt to do the mapping with taste, and to be clear about where taste ends and the machine stops.</p>
<p>The live instrument is <a href="https://deepseekoracle.github.io/Excavationpro/LYGORESONANCE.html">LYGO Resonance</a>. What follows is what it actually does, in the order it does it.</p>
<h2>Reading the image</h2>
<p>First the picture is measured, not understood. Edges, contours, keypoints, dominant colours, the distribution of light across the frame, and a rough sense of texture from local contrast. None of this is semantic. The tool does not know it is looking at a face or a coastline; it knows density and direction and warmth.</p>
<p>That limitation is also the feature. A system that recognised "sunset" would produce the sunset it has seen in training. A system that measures an orange gradient and a low horizon produces something specific to <em>your</em> file, including the parts that are badly exposed. Specificity is worth more than recognition in a sketch.</p>
<h2>Building the sound</h2>
<p>The mapping is layered rather than one-to-one. A slow harmonic bed follows the large colour regions. A mid layer of filtered noise follows texture. Transient events &#8212; hard edges, bright points &#8212; trigger short percussive gestures. Contour direction sets the movement between layers, which is why two images with similar palettes can produce different pieces.</p>
<p>Then there is the profile mode. Instead of audio, the tool emits a structured description: mood words, tempo suggestions, instrumentation, a brief that a musician or a text-to-music model can start from. I use this more than the audio. A brief is easier to argue with, and arguing is how a sketch becomes a piece.</p>
<h2>What it is not</h2>
<p>It is not a composer. It does not develop a theme, resolve a phrase, or know when to stop. Left alone it will happily produce four minutes of texture with no argument in it. The output is a beginning: a bed to write over, a palette to steal from, a way to get past the blank page.</p>
<p>It is also not a substitute for listening. The most common mistake with a generative tool is to accept the first result because it exists. Play it twice. If the second listen is boring, the piece is boring, and no amount of visual justification fixes that. This is the same rule as <a href="/blog/empty-beats-fake.html">Empty beats fake</a>: a thing that sounds finished is not the same as a thing that is good.</p>
<h2>The audio question</h2>
<p>Everything here is generated locally in the browser or with a local model. Nothing you drop on the page is uploaded, which matters for pictures of people and pictures you do not own. If you are scoring something commercial, treat the output as a sketch you own the arrangement of, not as a sample library cleared for release.</p>
<h2>Why an image-to-sound tool belongs in a fiction house</h2>
<p>Because the books are built out of images that do not exist yet, and a saga needs a way to hear a scene before it is written. I have used this to find the tone of a chapter more than once: feed it a painting, listen to the bed, write toward it. That is not a workflow I would recommend to everyone. It is a workflow I would defend to anyone who has stared at a blank page at midnight.</p>
<p>If you want the music it feeds, the free player is <a href="https://asiancoastline.com/listen.html">asiancoastline.com</a> and the explanation is <a href="/music.html">Music in this house</a>. If you want the wider map of rooms, <a href="/tools.html">the tools room</a> is the door.</p>
""",
    "related": [
        ("/music.html", "Music in this house"),
        ("/tools.html", "The tools room"),
        ("/blog/empty-beats-fake.html", "Empty beats fake"),
        ("/lygo-hub.html", "The systems hub"),
    ],
})


room({
    "path": "/excavationpro-listen.html",
    "nav": "music",
    "kicker": "Music &#183; the listen door",
    "h1": "Listen to the catalog",
    "lede": "No account, no preview wall, no countdown. The player lives on another domain because audio is heavy; this page tells you which door to use and what the deal is.",
    "byline": "Music guide &#183; updated 6 November 2026 &#183; about a six-minute read",
    "crumb_parts": [("/", "Home"), (None, "Listen")],
    "title": "Listen to the Excavationpro catalog — free, no account | Eternal Haven",
    "ogtitle": "Listen to the Excavationpro catalog",
    "description": "How to listen to the Excavationpro catalog without an account: the main player, the backup door, what the free listen covers, and what it does not.",
    "ogtype": "website",
    "schema": {
        "@type": "WebPage",
        "name": "Listen to the catalog",
        "url": "https://eternalhaven.ca/excavationpro-listen.html",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "about": {"@type": "MusicGroup", "name": "Excavationpro"},
    },
    "body": """
<p>The music lives on a different domain because a catalog of original audio is heavy, and this domain is a library with a small server bill. That is the whole explanation. There is no strategy in it, and nothing is being withheld here.</p>
<h2>The main door</h2>
<p><a href="https://asiancoastline.com/listen.html">asiancoastline.com/listen.html</a> is the browser player. Search, shuffle, album play, a queue, and a radio mode that keeps going without asking you to choose. No login. It works on a phone. It does not autoplay at you from a page you did not ask to play.</p>
<h2>The backup door</h2>
<p><a href="https://deepseekoracle.github.io/Excavationpro/excavationpro-listen.html">The GitHub Pages listen hub</a> is the second door, useful when a host is having a bad day or when you want a page that loads with almost nothing on it. Same catalog family, plainer room.</p>
<p>Stores exist too: <a href="https://open.spotify.com/artist/6CkZ4bN2xu3WRKbjEL3u2S">Spotify</a>, <a href="https://music.youtube.com/@Excavationpro">YouTube Music</a>, and <a href="https://audius.co/excavationpro">Audius</a> carry a subset. They are not the primary door, because a store can change its terms and a domain you own cannot be delisted by a policy update. If you already live in one of those apps, use it; the same recordings are there.</p>
<h2>What "free to listen" covers</h2>
<p>You may listen. You may download copies offered for personal listening. You may share an official link. You may not sell the tracks, use them as a beat pack, put them under a monetised video, or feed them to a model you intend to resell. The full wording is <a href="/lygo-music-license.html">the music license</a>, which is short and was written to be read rather than survived.</p>
<p>The distinction that matters is between access and ownership. Free listening is a gift of access. It is not a transfer of rights, and it never was. If you need a commercial sync, ask: <a href="/contact.html">contact</a> reaches me, and I answer those messages.</p>
<h2>How a song arrives here</h2>
<p>The long version is <a href="/music.html">Music in this house</a>. The short version: a track is mixed, mastered, encoded to a stream, given an identity, hashed, published, and then linked from a page that explains it. The hash is not decoration. It means the file you hear is the file that was published, which matters more for a small catalog than for a large one, because a small catalog has no legal department to argue for it.</p>
<h2>Live rooms</h2>
<p>When there is a live room, the links are on <a href="https://excavationpro.ca/">excavationpro.ca</a> and in the <a href="/lygo-hub.html">hub</a>. I do not embed a player that starts by itself on this page, because a page about listening should not make noise before you choose to listen.</p>
<p>One more practical note: the catalog is large, so the player loads a first page of results and then more as you scroll. If a search returns nothing, try a shorter phrase — the index matches titles and aliases, not lyrics. And if a track fails to start, the backup door above is the fastest test of whether the problem is the host or your browser.</p>
""",
    "related": [
        ("/music.html", "Music in this house"),
        ("/lygo-music-license.html", "The music license in plain language"),
        ("/LYGORESONANCE.html", "LYGO Resonance — image to sound"),
        ("/tools.html", "The tools room"),
    ],
})
