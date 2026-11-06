"""Book pages for eternalhaven.ca — canon drawn from the Eternal Haven lore pack.

Each page describes one volume: where it begins, what it argues, how to read it,
and what to read next.  No invented plot, no fake store links.
"""

PAGES = []


def book(**kw):
    PAGES.append(kw)


BOOK_SCHEMA = {
    "@type": "Book",
    "name": "",
    "author": {"@type": "Person", "name": "Justin Helmer"},
    "bookSeries": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
    "inLanguage": "en",
    "url": "",
}

PAGES.append({
    "path": "/books/the-moonlit-slumber.html",
    "nav": "books",
    "ogtype": "book",
    "kicker": "Book I &#183; Volume I of the Silver Accord",
    "h1": "The Moonlit Slumber",
    "lede": "Night, a vow, and the first lantern. The book that starts the saga slowly on purpose.",
    "byline": "A site introduction &#183; updated 6 November 2026 &#183; about a nine-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "The Moonlit Slumber")],
    "title": "The Moonlit Slumber — Book I of Eternal Haven | Justin Helmer",
    "ogtitle": "The Moonlit Slumber — Book I of Eternal Haven",
    "description": "A reader's introduction to Book I of the Eternal Haven Chronicles: the First Seal, Arin of Elysun Vale, Serenya, Emberion, and the night the Accord began to crack.",
    "schema": {
        "@type": "Book",
        "name": "The Moonlit Slumber",
        "alternateName": "Volume I of the Silver Accord",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "bookSeries": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "inLanguage": "en",
        "url": "https://eternalhaven.ca/books/the-moonlit-slumber.html",
        "abstract": "The opening volume of the Eternal Haven Chronicles: the First Seal chooses a rider, an Accord is made, and the night that ends the prologue's quiet begins.",
    },
    "body": """
<p>Every saga has a door that looks like a wall until you are through it. <em>The Moonlit Slumber</em> is that door. It is not the loudest book in the series, and it is not meant to be. It is the one where a promise is made in front of witnesses who are still deciding whether they mean it.</p>
<p>If you have been handed this book by someone who said "start here," they were right, and they were also asking you for patience. The first hundred pages are a place, not a plot. Elysun Vale, the high eaves, pine and lark and watchfire. The reader who wants a battle by chapter four will be bored by a book that is busy teaching them what a vow costs.</p>
<h2>Where it begins</h2>
<p>The prologue is called <em>The Lullaby of Skylark</em>, and it does the thing I care most about in fantasy: it establishes a cosmology without turning it into a lecture. There was a dawn before the first dawn. In the quiet of that hour a song was woven, and the song became the First Seal. The old formula for it appears in the text as an equation — the integral of light and truth over the world — and the people of the Vale had a plainer name for it: the homeward sound.</p>
<p>The Seal chose a vessel. In those days it chose a young rider named Arin, whose laughter outran fear, and who grew up where the wind drinks the scent of pine and lark. That is the novel's first promise: the sacred is not abstract here, it is carried by someone with mud on his boots.</p>
<h2>What happens, without giving it away</h2>
<p>Fifteen chapters, and their titles are honest about the shape of the story. <em>Serenya and the Bronze Emberion</em>. <em>The Whispering Moon</em>. <em>The Call of Lyra</em>. <em>Illusions at Dusk</em>. <em>Corvath, the Fallen Dragon</em>. Then the middle of the book, where a community does its best and its worst: <em>Bonds in Trial</em>, <em>The Festival of Accord</em>, <em>Serenya's Temptation</em>, <em>The Haven's Secrets</em>, <em>Betrayal at Moonrise</em>.</p>
<!--AD-->
<p>The last movement is where the saga earns its name. <em>Emberion's Trial</em> tests the one character who has the most power and the least practice at restraint. <em>The Shattering of Accord</em> is the chapter that every later book is answering. <em>The Last Song of Lyra</em> is the one readers write to me about. <em>Emberion Ascends</em> sounds like triumph and is not simple. The final chapter, <em>The Moonlit Slumber</em>, gives the whole volume its title, and the epilogue asks a question with a question mark in it: <em>A New Accord?</em></p>
<p>What I will tell you is that no one in this book is a villain in their own head. Corvath is the closest thing to a monster, and the chapter that introduces him is careful with the word <em>fallen</em> — fallen from what, and by whose push.</p>
<h2>What the book is arguing</h2>
<p>Three arguments run under the plot. The first is that unity is a practice, not a mood. The Accord is not a vibe; it is sentences that people agreed to remember, and the book is interested in what happens when remembering becomes optional. The second is that moonlight is a clock. In the Haven, night is not decoration. It tells you who kept a watch and who sold the watch for a speech. The third is that power under constraint is the only interesting kind. Emberion begins in bronze and ends the book changed; the question the novel keeps asking him is the one I care about in every system I build: what do you do with capability after you have seen what it can break?</p>
<blockquote>"The elders say there was a dawn before the first dawn; a quiet hour when the world held its breath and listened."</blockquote>
<p>That is the first line of the prologue. It is also the thesis. A saga about listening is a strange thing to write in an era of clips, which is probably why I kept writing it.</p>
<h2>How to read it</h2>
<p>Slowly, and out loud if you can. The prose was built to be spoken. Names accumulate rather than dump on page one, so you do not need a glossary to start; you need to trust that the book will tell you who matters. If you are audio-first, the narrated edition exists and is listed from the <a href="/lygo-hub.html">hub</a>. If you are reading on a phone at midnight, one chapter at a time is the intended pace.</p>
<p>Do not skip to Book III because war sounds more exciting. The war is only expensive because of what was agreed in this book. A reader who starts at the siege has arrived at a funeral without knowing the person.</p>
<h2>Where the copy lives</h2>
<p>Two official doors, both mine, neither an affiliate link. Paper: <a href="https://www.lulu.com/shop/justin-helmer/the-eternal-haven/paperback/product-yvg9w9r.html" rel="noopener">The Moonlit Slumber, paperback on Lulu</a>. Audio: <a href="https://youtu.be/_WwSb4JlRBQ" rel="noopener">Book I, narrated, on YouTube</a>. The narration is mine, not a licensed reader's, so the voices are the ones I heard while writing.</p>
<p>I do not keep six storefronts on this domain pretending to be a shop. If a door is closed when you try it, <a href="/contact.html">write to me</a> and I will point you at the copy that is actually in print rather than the one a template says should exist. The other volumes are gathered on the <a href="/books/">shelf</a>.</p>
<p>Next: <a href="/books/the-shattered-accord.html">The Shattered Accord</a>, where the fracture in this book becomes the whole weather.</p>
""",
    "related": [
        ("/books/", "The shelf: all five books in order"),
        ("/books/the-shattered-accord.html", "Book II — The Shattered Accord"),
        ("/books/characters.html", "Who is who: a spoiler-light cast list"),
        ("/books/world.html", "Places and devices of the Haven"),
        ("/blog/reading-eternal-haven-in-order.html", "Reading Eternal Haven in order"),
    ],
})


PAGES.append({
    "path": "/books/the-shattered-accord.html",
    "nav": "books",
    "ogtype": "book",
    "kicker": "Book II &#183; The Eternal Haven Chronicles",
    "h1": "The Shattered Accord",
    "lede": "An accord is not a vibe. It is a sentence people agreed to remember. This is the book where remembering becomes optional.",
    "byline": "A site introduction &#183; updated 6 November 2026 &#183; about a nine-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "The Shattered Accord")],
    "title": "The Shattered Accord — Book II of Eternal Haven | Justin Helmer",
    "ogtitle": "The Shattered Accord — Book II of Eternal Haven",
    "description": "Book II of the Eternal Haven Chronicles: factions in the Vale, a seer in chains, Kaelion's trial, the fall of Elysun, and the night the Accord breaks.",
    "schema": {
        "@type": "Book",
        "name": "The Shattered Accord",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "bookSeries": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "inLanguage": "en",
        "url": "https://eternalhaven.ca/books/the-shattered-accord.html",
        "abstract": "The second volume: the fracture opened at the end of Book I widens into factions, trials, and the fall of a vale.",
    },
    "body": """
<p>The second book is the one that makes the saga feel like a history rather than a legend. It opens with a fracture, not a battle, and the fracture is in a room. The Circle of Haven stands above Aurethys as a crown of crystalline spires; the ceiling is woven from living light, threads of memory that move with the heartbeat of the world below. On the night the book begins, that current falters. Shadows bleed through the light.</p>
<p>That image is the whole novel in miniature. Nothing has been destroyed yet. Something that used to hold is holding less.</p>
<h2>The shape of the argument</h2>
<p>Book I asked what a promise costs. Book II asks who is allowed to interpret it. The word <em>accord</em> gets used by everyone in this book and means something different in every mouth: a treaty, an inheritance, a weapon, a memory of better people. The Council that was an ideal in the first volume becomes a decision body here, and decision bodies produce casualties even when everyone in the room means well. That is not cynicism. It is the least glamorous true thing I know about institutions.</p>
<h2>The chapters, and what they are for</h2>
<p>The prologue is <em>The Fracture in Haven</em>. Then <em>The Aftermath of the</em> &#8212; a title that breaks off mid-thought, which is deliberate; aftermath is a place where sentences do not finish. <em>Factions in the Vale</em> turns neighbours into positions. <em>The Seer in Chains</em> is where the book's cruelty becomes specific: prophecy is not a gift in this volume, it is a custody problem. <em>The First Forge</em> introduces the idea that mortals might make seals of their own rather than only receive them.</p>
<!--AD-->
<p>The middle chapters are the ones I am proudest of. <em>The Illusion Warband</em>, <em>The Fractured Choir</em>, and <em>Kaelion's Trial</em> are three different ways of asking whether a person can hold a structure together after the structure has been used against them. The choir matters more than it sounds. A single voice can be wrong; a choir can be corrupted. The book does not let harmony off the hook.</p>
<p>Then the floor gives way. <em>The Fall of Elysun</em> is not a set piece, it is an eviction. Part III is called <em>Betrayals</em>, and the chapters inside it earn the plural. <em>The Eclipse Ritual</em>, <em>The Betrayal in</em>, <em>The Duel of</em> &#8212; the saga starts refusing to finish its own titles, as if the language is being damaged in parallel with the world. Part IV, <em>The Moon's Shadow</em>, and Part V, <em>The Breaking of Haven</em>, are exactly as heavy as they sound. The book ends at <em>Haven's Gate</em>, <em>The Moonlit Battle</em>, <em>The Shattered</em>, and an epilogue called <em>A New Accord</em> that is not a resolution so much as a receipt.</p>
<h2>Why the middle book is the hard one</h2>
<p>Second volumes in a series usually stall: the first book spent the novelty, the last book is owed the payoff, and the middle is asked to hold the door. I wrote this one as the hinge instead. Everything that becomes a war in Book III is decided here, in rooms, by people who believe they are being reasonable. If you want to understand why the Ascension War happens, the answer is not in the war. It is in the trial and the choir and the fall of a vale.</p>
<p>It is also the book where the cast stops being an ensemble of archetypes and starts being a set of people with records. Serenya's compassion becomes a structural problem rather than a virtue. Kaelion's long game becomes visible as a series of lesser evils with receipts attached. And the dragon who was introduced as a fall in Book I is now a question about what a fallen thing is for.</p>
<h2>How to read it</h2>
<p>Do not read this one alone at a kitchen table if you can avoid it. It is the volume people message me about at 2 a.m., usually about the trial. Read Book I first; the fracture here is only legible if you saw the accord being made. If you have already read it and are returning, read the epilogue first and then the prologue. The book reads differently when you know what the new accord is going to cost in Book III.</p>
<h2>Where the copy lives</h2>
<p>Paper: <a href="https://www.lulu.com/shop/justin-helmer/eternal-haven-chronicles-book-ii-the-shattered-accord/paperback/product-578nykz.html" rel="noopener">The Shattered Accord, paperback on Lulu</a>. Audio: <a href="https://youtu.be/EC8GRmLG3Us" rel="noopener">Book II, narrated, on YouTube</a>. If a link has rotted, the <a href="/contact.html">contact page</a> is the repair route, and I answer faster than a storefront does.</p>
<p>The rest of the volumes are on the <a href="/books/">shelf</a>; the dense index of doors is in the <a href="/lygo-hub.html">hub</a>.</p>
<p>Next: <a href="/books/the-ascension-war.html">The Ascension War</a>, where the bill for this book comes due.</p>
""",
    "related": [
        ("/books/", "The shelf: all five books in order"),
        ("/books/the-moonlit-slumber.html", "Book I — The Moonlit Slumber"),
        ("/books/the-ascension-war.html", "Book III — The Ascension War"),
        ("/blog/four-books-and-a-long-road.html", "Four books and a long road"),
    ],
})


PAGES.append({
    "path": "/books/the-ascension-war.html",
    "nav": "books",
    "ogtype": "book",
    "kicker": "Book III &#183; The Eternal Haven Chronicles",
    "h1": "The Ascension War",
    "lede": "Ascent is a flattering word. It sounds like light. It is often just altitude with a better press kit.",
    "byline": "A site introduction &#183; updated 6 November 2026 &#183; about a ten-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "The Ascension War")],
    "title": "The Ascension War — Book III of Eternal Haven | Justin Helmer",
    "ogtitle": "The Ascension War — Book III of Eternal Haven",
    "description": "Book III of the Eternal Haven Chronicles: Shadow's Throne, forgers of new seals, the return of Miralis, Serenya's grief, and the duel of Aetheris.",
    "schema": {
        "@type": "Book",
        "name": "The Ascension War",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "bookSeries": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "inLanguage": "en",
        "url": "https://eternalhaven.ca/books/the-ascension-war.html",
        "abstract": "The third volume: the war over who speaks truth into being, fought with seals forged from lived suffering.",
    },
    "body": """
<p>The war book is where I let ambition show its receipts. Not every climber is a villain. Not every villain thinks they are climbing. If you came for a clean banner and a side to cheer, this volume will annoy you, and I think that annoyance is a better teacher than a slogan.</p>
<h2>Where the third book stands</h2>
<p>The Accord lies shattered. The Eternal Haven has withdrawn into the void, and Aurethys stands abandoned beneath the Throne of Shadow. Corvath reigns in the broken Moon, and his illusions bleed endlessly across the world. The old guardians are not a united rescue force; the Ten Champions that remain are divided, some doubting their right to act, others faltering under guilt, still others whispering that mortals should stand alone.</p>
<p>So the book's premise is a subtraction. No functioning council, no intact heaven, no trustworthy prophecy. What is left is the idea that people can forge seals of their own &#8212; not echoes of Haven's equations, but things born from lived suffering, love, and hope. Imperfect seals, and alive. That sentence is the thesis of the novel and, honestly, of most of the software I build.</p>
<h2>The chapters</h2>
<p>It opens with <em>The Rise of Shadow's Throne</em> and moves into <em>Forgers of New Seals</em>, which is the most hopeful chapter in the volume and is placed second on purpose; hope that arrives after the war has started has to be made, not announced. <em>Haven's Doubt</em> and <em>The Return of Miralis</em> are a pair: the absence that everyone explained away comes back with inconvenient knowledge. <em>The Battle of Elysun Ashes</em> is the first time the book lets a set piece breathe.</p>
<!--AD-->
<p>Then the betrayals. <em>The Betrayal of Eternis</em> and <em>The Forgotten Seal</em> are about the same crime from two angles: what a structure does when it discovers it has been protecting the wrong thing. <em>Serenya's Grief</em> and <em>Emberion's Rage</em> sit next to each other because grief and rage are the same energy pointed at different targets. <em>The Siege of the Broken Moon</em> is the volume's largest movement, and <em>The Duel of Aetheris</em> is the smallest: two figures, one of whom used to be the guardian of vigilance, now serving the throne he was built to watch.</p>
<p>The last movement is <em>The Choir of Imperfection</em>, <em>The Heart of Shadow</em>, <em>The New Accord</em>, and <em>The Ascension War Ends</em>, with an epilogue called <em>The Seed of Tomorrow</em>. I will not tell you who wins. I will tell you that the book is more interested in what a victory is made of than in who receives the credit.</p>
<h2>What it is arguing</h2>
<p>First: the war is a battle of definition, not territory. Who speaks truth into being? The Haven-born, who erased imperfection to achieve harmony, or the scarred mortals whose seals are ugly and working? That question is not settled by force. It is settled by whichever side can survive being examined.</p>
<p>Second: an imperfect seal is not a lesser seal. A guarantee made by someone who has actually bled for it holds differently than a guarantee issued from a clean room. The novel calls these seals <em>alive</em>, and the word is doing work. Alive things can fail. Dead things can only be replaced.</p>
<p>Third: altitude is not virtue. Ascension is the title, and the book spends three hundred pages demonstrating that climbing is a bill with a due date. Corvath is the loudest example. Emberion is the quiet one. Aetheris is the one that hurts.</p>
<h2>How to read it</h2>
<p>This is the volume that rewards having read the first two. The trial in Book II explains the siege in Book III; the fall of Elysun explains the ashes. If you are reading the saga for the first time, resist the temptation to start here because the title is louder. If you are returning after Book IV, this is the book that changes most on a second pass, because you know which of its victories were actually loans.</p>
<p>Audio readers: the narrated edition is listed from the <a href="/lygo-hub.html">hub</a>, and the siege chapters work well spoken. Text readers: keep a scrap of paper for the seal names. The book does not stop to define them twice.</p>
<h2>Where the copy lives</h2>
<p>Paper: <a href="https://www.lulu.com/shop/justin-helmer/the-ascension-war/paperback/product-nvjgyme.html" rel="noopener">The Ascension War, paperback on Lulu</a>. Audio: <a href="https://youtu.be/kwrfjf2U0Qc" rel="noopener">Book III, narrated, on YouTube</a>. The siege chapters work well spoken; they were written to be heard in a room.</p>
<p>If a storefront has rotted, <a href="/contact.html">write</a> and I will point you at the copy that exists. The other volumes are on the <a href="/books/">shelf</a>.</p>
<p>Next: <a href="/books/eternal-haven-dawns.html">Eternal Haven Dawns</a>, where morning makes the mess visible.</p>
""",
    "related": [
        ("/books/", "The shelf: all five books in order"),
        ("/books/the-shattered-accord.html", "Book II — The Shattered Accord"),
        ("/books/eternal-haven-dawns.html", "Book IV — Eternal Haven Dawns"),
        ("/books/characters.html", "Who is who: a spoiler-light cast list"),
    ],
})


PAGES.append({
    "path": "/books/eternal-haven-dawns.html",
    "nav": "books",
    "ogtype": "book",
    "kicker": "Book IV &#183; The Eternal Haven Chronicles",
    "h1": "Eternal Haven Dawns",
    "lede": "Dawn is not a reset button. Morning light makes the mess visible, which is the only kind of morning worth writing toward.",
    "byline": "A site introduction &#183; updated 6 November 2026 &#183; about a ten-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "Eternal Haven Dawns")],
    "title": "Eternal Haven Dawns — Book IV of Eternal Haven | Justin Helmer",
    "ogtitle": "Eternal Haven Dawns — Book IV of Eternal Haven",
    "description": "Book IV of the Eternal Haven Chronicles: the Twelve at dawn, a world rewoven, the Council in flesh, and the Accord of Imperfect Light.",
    "schema": {
        "@type": "Book",
        "name": "Eternal Haven Dawns",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "bookSeries": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "inLanguage": "en",
        "url": "https://eternalhaven.ca/books/eternal-haven-dawns.html",
        "abstract": "The fourth volume: the gods walk the earth, the Council becomes flesh, and the saga settles on an imperfect light.",
    },
    "body": """
<p>The Broken Moon is gone. That is the first sentence of the book, more or less, and it is a strange way to begin a final volume: by removing the thing every cover promised. What is left is a sky remade, not in perfection but in scars that gleam like constellations. Aurethys stands under it. On a ridge where obsidian spires have cracked and softened into living stone, the Council of Twelve gathers &#8212; no longer eleven, because Corvath stands among them, not as an enemy but as a reconciled seal.</p>
<p>That image tells you what kind of book this is. The dragon is not defeated and forgotten. He is seated, wings folded, and the folding is the point.</p>
<h2>The five movements</h2>
<p>The book is built in parts. <em>When Gods Walk the Earth</em> opens the volume: a world rewoven, Serenya's silence, Kaelion's legacy. <em>The Weight of Memory</em> follows: the return of Miralis, Haven among mortals, the cracks of reverence. <em>The Living Accord</em> is the political centre: Emberion's doubt, the Council in flesh, the Pure Accord's coup. <em>The Forging of Haven on Earth</em> is the cost: Serenya's last song, Emberion's flight, the Council's choice. And <em>The Eternal Haven</em> closes it: the Accord of Imperfect Light, Serenya's legacy, the dawn without separation, and an epilogue called <em>The Lattice Beyond</em>.</p>
<p>I am aware of how that reads in a table of contents. It sounds like a triumph march. It is closer to a settlement conference held in a burned house.</p>
<!--AD-->
<h2>Why the gods have to walk</h2>
<p>A saga that keeps its heaven in the sky can only end with a rescue. I did not want a rescue. So the fourth book brings the divine down into the weather: gods and mortals sharing roads, arguments, and rent. That produces the volume's best comedy and its worst politics, because reverence is easier to maintain at a distance. Up close, a god is a neighbour with opinions.</p>
<p>The cracks of reverence are the real antagonist of this book. Not Corvath, who has already fallen and returned. Not the war, which is over. The antagonist is the impulse to build a pure version of the thing you just survived &#8212; and the Pure Accord's coup is where that impulse gets a name and a knife.</p>
<h2>The Accord of Imperfect Light</h2>
<p>This is the phrase the whole saga has been walking toward. It is not a compromise between good and evil; it is a refusal to pretend that a working arrangement is a clean one. Light in these books has never been omniscience. It is orientation. A person acting with partial information can still be pointed the right way. A council acting with total information can still be pointed at itself.</p>
<p>The chapter that carries the title is the one I rewrote most. The first drafts resolved too neatly: everyone forgave, the seals held, the choir sang in tune. That version was a lie about people, and it was also a lie about systems. What shipped is a settlement: some things are repaired, some are buried, and the document everyone signs has a clause nobody likes.</p>
<blockquote>"A dawn without separation" is what the last chapter promises, and it is a promise I mostly believe. Mostly is the honest word.</blockquote>
<h2>What happens to the cast</h2>
<p>Serenya's silence in the early part of the book is the hardest thing I have written her through; the woman whose compassion was a structural problem in Book II now has to decide whether speaking is a kindness or an imposition. Kaelion's legacy is not a statue. Miralis returns again, and this time the returning is not convenient. Emberion's doubt and flight are the last movement of a character who began in bronze and spent four books learning that the interesting question is not whether he can burn something but whether he should.</p>
<p>Corvath, seated among the Twelve, gets no redemption speech. He gets work. That felt truer than absolution.</p>
<h2>How to read it</h2>
<p>Last, and in order. This is not a volume that works as an entry point, not because it is complicated but because it is a settlement &#8212; and a settlement means nothing if you were not in the argument. If you have read the first three, take the last hundred pages slowly. The epilogue, <em>The Lattice Beyond</em>, is deliberately shorter than the ending deserves, because a saga that explains its own afterlife has stopped trusting the reader.</p>
<p>Then read <a href="/books/the-unwritten-seal.html">The Unwritten Seal</a>, which is the fifth door and does not undo this one.</p>
<h2>Where the copy lives</h2>
<p>Paper: <a href="https://www.lulu.com/shop/justin-helmer/etrnal-haven-dawns/paperback/product-dy8m9wd.html" rel="noopener">Eternal Haven Dawns, paperback on Lulu</a> (the store's own slug has the typo, not mine). Audio: <a href="https://youtu.be/KIOv53YBZg4" rel="noopener">Book IV, narrated, on YouTube</a>. The last hundred pages read differently out loud, which is the test I set for the ending.</p>
<p>If one of those has rotted, the <a href="/contact.html">contact page</a> reaches me directly. Every volume is on the <a href="/books/">shelf</a>.</p>
""",
    "related": [
        ("/books/", "The shelf: all five books in order"),
        ("/books/the-ascension-war.html", "Book III — The Ascension War"),
        ("/books/the-unwritten-seal.html", "Book V — The Unwritten Seal"),
        ("/blog/four-books-and-a-long-road.html", "Four books and a long road"),
    ],
})


PAGES.append({
    "path": "/books/the-unwritten-seal.html",
    "nav": "books",
    "ogtype": "book",
    "kicker": "Book V &#183; the live continuation",
    "h1": "The Unwritten Seal",
    "lede": "The fifth door. An ebook with an ISBN, a hash, and a rule about not swapping the text later and calling it the same book.",
    "byline": "A site introduction &#183; updated 6 November 2026 &#183; about a seven-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "The Unwritten Seal")],
    "title": "The Unwritten Seal — Book V of Eternal Haven | Justin Helmer",
    "ogtitle": "The Unwritten Seal — Book V of Eternal Haven",
    "description": "Book V of the Eternal Haven Chronicles: the ebook, its ISBN, the content hash, and how to read it after Dawns without losing the thread.",
    "schema": {
        "@type": "Book",
        "name": "The Unwritten Seal",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "bookSeries": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "isbn": "978-1-0698232-9-8",
        "bookFormat": "https://schema.org/EBook",
        "inLanguage": "en",
        "url": "https://eternalhaven.ca/books/the-unwritten-seal.html",
        "abstract": "The fifth volume of the Eternal Haven Chronicles, published as an ebook with a content hash so a later file cannot quietly replace it.",
    },
    "body": """
<p>This page is about the book's release rather than its plot, on purpose. A fifth volume that explains itself on a marketing page is a fifth volume with nothing left to discover. What you should know before you buy is what the thing is, how it is published, and how to make sure the file you are reading is the file I wrote.</p>
<h2>What it is</h2>
<p><em>The Unwritten Seal</em> continues the saga after <em>Eternal Haven Dawns</em>. It is published as an ebook, ISBN 978-1-0698232-9-8, and it is not a prequel, a side story, or a deleted chapter dressed up as a novel. It is the fifth door. If you have not read the first four, the honest advice is to <a href="/books/">start at the shelf</a> and come back; the book assumes the settlement at the end of Dawns and does not re-litigate it.</p>
<p>The title is a joke about provenance. A seal is a guarantee, and an unwritten seal is the strange case where the guarantee is real before the document exists &#8212; a promise made by someone who has not yet said the words. That is a fair description of how a long series gets finished: the ending is committed to years before it can be written.</p>
<h2>Why a hash</h2>
<p>I planted a content hash for the file when the ebook went live. You do not need the hash to read. You need it on the day someone claims a different file is the original.</p>
<p>This is not paranoia about pirates. Pirates were never the threat to a small catalog. The threat is edits: a retailer re-flow, a "corrected" edition, a file with my name on it and a paragraph I did not write. A hash is a small, cheap answer. It says: this text has one identity, and here is the number. I wrote about the practice at length in <a href="/blog/how-a-book-gets-a-hash.html">How a book gets a hash</a>.</p>
<!--AD-->
<h2>How to check a copy</h2>
<p>Take the file you have. Compute a SHA-256 of it. Compare against the value published with the listing. If they differ, you have a different file &#8212; possibly a newer one with a fixed typo, possibly something worse. Neither possibility should be a mystery. That is the whole point of publishing the number.</p>
<p>Practical note: file bytes can change without the text changing, because every store re-packages an ebook. If a store's copy fails the hash but the chapter text matches, that is a packaging difference, not a fraud. The hash protects the text, not the zip. I would rather explain that limitation than pretend the number is stronger than it is.</p>
<h2>The store door</h2>
<p>The ebook is on Lulu: <a href="https://www.lulu.com/shop/justin-helmer/the-unwritten-seal/ebook/product-65kg2mr.html">The Unwritten Seal, ebook</a>. That is the publisher page, not an affiliate link, and I do not get paid for you clicking it &mdash; I get paid if you buy it, which is a different and more honest transaction.</p>
<p>Hardcopy does not exist yet. When print is actually ready I will say so here and on the shelf. I will not advertise a hardcover I cannot hold, because that is the kind of small lie that turns a catalog into a storefront.</p>
<h2>What the fifth book is for</h2>
<p>The first four books argue about accords, seals, and whether an imperfect light is enough. The fifth asks what happens when the guarantee outlives the guarantor. That is the question a series eventually has to face, and it is also the question this house faces: what happens to a story when the person who made it stops being able to keep every door open.</p>
<p>I did not write it as an ending. I wrote it as a continuation that could survive one. If that sounds like a strange thing to want from a novel, consider that most things people build are judged by whether they still work after the builder leaves the room.</p>
<h2>Where to go next</h2>
<p>If you have finished all five: the <a href="/glossary.html">glossary</a> is the reference shelf for names and devices, <a href="/books/characters.html">the cast page</a> is the spoiler-light index, and <a href="/blog/">the essays</a> are where I argue with my own books in public. If you want the argument about why a saga in 2026 is a bad business and a good life, read <a href="/blog/four-books-and-a-long-road.html">Four books and a long road</a>.</p>
""",
    "related": [
        ("/books/", "The shelf: all five books in order"),
        ("/books/eternal-haven-dawns.html", "Book IV — Eternal Haven Dawns"),
        ("/blog/how-a-book-gets-a-hash.html", "How a book gets a hash"),
        ("/glossary.html", "The Haven glossary"),
    ],
})
