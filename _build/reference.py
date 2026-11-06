"""Reference and shelf pages: cast, world, start-here guide, glossary, tools."""

PAGES = []


def page(d):
    PAGES.append(d)


page({
    "path": "/books/characters.html",
    "nav": "books",
    "kicker": "Reference &#183; the cast, spoiler-light",
    "h1": "Who is who in the Haven",
    "lede": "A cast list for readers who met nine names in one chapter and want the short version. No deaths, no twists, no ending.",
    "byline": "Reference page &#183; updated 6 November 2026 &#183; about a nine-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "Characters")],
    "title": "Eternal Haven characters — a spoiler-light cast list | Justin Helmer",
    "ogtitle": "Eternal Haven characters — a spoiler-light cast list",
    "description": "Who is who in the Eternal Haven Chronicles: Arin, Serenya, Emberion, Kaelion, Miralis, Corvath, Aetheris, Eternis, the Council of Twelve, and the Accord itself.",
    "ogtype": "article",
    "schema": {
        "@type": "Article",
        "headline": "Who is who in the Haven",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "datePublished": "2026-11-06",
        "about": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "url": "https://eternalhaven.ca/books/characters.html",
    },
    "body": """
<p>This page exists because readers keep asking the same question in different words: <em>which one is the dragon again?</em> It is the short version, written by the author, kept deliberately free of outcomes. If you want the arguments the books are making, the <a href="/books/">shelf</a> and the individual volumes do that better. This is the map you keep in your hand while walking.</p>
<h2>Arin</h2>
<p>The rider from the high eaves of Elysun Vale, where the wind drinks the scent of pine and lark. He is the vessel the First Seal chooses in the prologue of Book I, and he is the reader's first pair of eyes. Arin's defining quality is not talent. It is that his laughter outran fear, which in the Vale is a form of navigation.</p>
<h2>Serenya</h2>
<p>The heart of the saga and its hardest problem. Her domain is compassion, and the books take that seriously as a <em>structural</em> fact rather than a personality trait: care given without accounting becomes a burden that other people have to carry. Book I gives her a temptation. Book II makes her kindness expensive. Book III asks what grief does to a person whose job was holding others. Book IV gives her a silence that is louder than any speech she makes earlier.</p>
<h2>Emberion</h2>
<p>Begins in bronze and becomes the saga's study in power under constraint. The question that follows him through four books is the one I care about most in any system I build: what do you do with capability after you have seen what it can break? His trial in Book I is a test of restraint, not strength. By Book IV his doubt is more dangerous than his rage ever was, because doubt is what a powerful person does when no one is grading them.</p>
<!--AD-->
<h2>Kaelion</h2>
<p>The strategist. He trades personal comfort for structural stability and is usually right about the arithmetic and wrong about the cost, which is the classic failure mode of a competent leader. Book II puts him on trial in a chapter named for it. Book IV asks what his legacy is when the structure he held together no longer needs him. He is not a villain and he is not a hero; he is the person who signs the thing nobody else will sign.</p>
<h2>Miralis</h2>
<p>The returning echo. Absent when most needed, back when everything has already changed, carrying knowledge that would have helped earlier. The books use Miralis to ask an uncomfortable question about memory: is old truth still true when it arrives too late to prevent the damage? The return appears in Book III and again, differently, in Book IV. Both times it is inconvenient, which is the point.</p>
<h2>Corvath</h2>
<p>The fallen dragon. Introduced in Book I as a fall, he becomes the saga's argument about the line between victim, weapon, and villain. He is not redeemed by a speech. In Book IV he stands among the Council of Twelve, seated and folded, and the folding is the character work. If you want to know what a fallen thing is for, he is the answer the series gives, and it is not a comfortable one.</p>
<h2>Aetheris</h2>
<p>A guardian of vigilance who ends up serving the throne he was built to watch. The duel in Book III that carries Aetheris's name is the smallest set piece in the volume and the one that hurts most, because it is about a protector whose protection got repurposed. If you have ever watched a safety system become a surveillance system without anyone deciding to do it, you already know this character.</p>
<h2>Eternis</h2>
<p>The betrayal in Book III is named for Eternis, and I will say only that: the name is attached to the chapter, and the chapter is about what a structure does when it discovers it has been protecting the wrong thing. To say more would spend the book's best turn.</p>
<h2>Lyra</h2>
<p>A name at both hinges of Book I: chapter three is <em>The Call of Lyra</em>, chapter thirteen is <em>The Last Song of Lyra</em>. I keep this entry short on purpose. Lyra is a song before she is a biography, and explaining her is a good way to ruin the first book for someone who has not read it. Read the chapters.</p>
<h2>The Council of Twelve</h2>
<p>Not a person, and not quite an organisation either: a decision body that begins as an ideal and becomes a room where reasonable people produce casualties. In Book IV the Council comes into flesh, which is a politer way of saying that governance stops being a metaphor and starts having to sit at a table with people it has harmed. Eleven becomes twelve when Corvath is seated. That arithmetic matters.</p>
<h2>The Accord</h2>
<p>The saga's most important character is a document. An accord is a sentence people agreed to remember, and the whole series is an experiment on that sentence: made, strained, shattered, re-forged, and finally written as the Accord of Imperfect Light. If you read the books as being about people, you will still enjoy them. If you read them as being about <em>agreements</em>, you will notice that every plot turn is a clause being tested.</p>
<h2>How to use this page</h2>
<p>Keep it open in a second tab while you read. It is deliberately incomplete: no fates, no reveals, no endings. If a name is missing and you think it should be here, <a href="/contact.html">tell me</a> and I will add it if adding it does not spoil the books. The <a href="/glossary.html">glossary</a> covers the places and devices; <a href="/books/world.html">the world page</a> covers geography and cosmology.</p>
""",
    "related": [
        ("/books/", "The shelf"),
        ("/books/world.html", "Places and devices of the Haven"),
        ("/glossary.html", "The Haven glossary"),
        ("/start.html", "Start here: how to enter the library"),
    ],
})


page({
    "path": "/books/world.html",
    "nav": "books",
    "kicker": "Reference &#183; places, seals, and weather",
    "h1": "The world of the Haven",
    "lede": "Aurethys, Elysun Vale, the Circle, the Broken Moon, and the difference between a seal and a promise. Geography for readers, not a wiki.",
    "byline": "Reference page &#183; updated 6 November 2026 &#183; about a ten-minute read",
    "crumb_parts": [("/", "Home"), ("/books/", "Books"), (None, "The world")],
    "title": "The world of Eternal Haven — places, seals, cosmology | Justin Helmer",
    "ogtitle": "The world of Eternal Haven — places, seals, cosmology",
    "description": "Aurethys, Elysun Vale, the Circle of Haven, the Broken Moon, the First Seal, and the choir: a reader's guide to the world of the Eternal Haven Chronicles.",
    "schema": {
        "@type": "Article",
        "headline": "The world of the Haven",
        "author": {"@type": "Person", "name": "Justin Helmer"},
        "datePublished": "2026-11-06",
        "about": {"@type": "BookSeries", "name": "The Eternal Haven Chronicles"},
        "url": "https://eternalhaven.ca/books/world.html",
    },
    "body": """
<p>The saga does not open with a map of continents, and that was a decision rather than an omission. A map on page one tells a reader what the story thinks is important: borders. These books think the important thing is <em>altitude</em> &#8212; who is above whom, and what that does to the people below. So the geography arrives the way geography actually arrives: as places people are from.</p>
<h2>Aurethys</h2>
<p>The world under the Haven. By Book II it is described from above, as something the Circle glimmers over; by Book III it stands abandoned beneath the Throne of Shadow; by Book IV it stands under a sky remade, "not in perfection, but in scars that gleam like constellations of truth." That progression &#8212; seen from above, then emptied, then inhabited again &#8212; is the whole arc of the saga in a single noun. When characters say "the world," they usually mean Aurethys, and they usually mean it with a bad conscience.</p>
<h2>Elysun Vale</h2>
<p>The place the reader is from, whether or not the reader has ever been to a vale. High eaves, pine, lark, watchfires, cliff ledges. Arin learns his craft there. It is not a paradise, and it is not a village of simple folk waiting to be saved: it is a working place with a long memory of its own. When it falls in Book II, the saga loses its ability to pretend that the war is happening somewhere else.</p>
<h2>The Circle of Haven</h2>
<p>A crown of crystalline spires curving inward to form a council chamber that has endured for an age. The ceiling is rivers of living light &#8212; threads of memory weaving and unweaving with the heartbeat of the world below. On the night Book II begins, that current falters. If you want one image that explains why the series is about institutions rather than armies, it is that ceiling.</p>
<!--AD-->
<h2>The Broken Moon, and the Throne of Shadow</h2>
<p>Corvath's seat. The moon in these books is not a romantic object; it is a structure that can be occupied, fractured, and used. In Book I it is a clock. By Book III it is a fortress with illusions bleeding out of it. In Book IV it is gone, and rivers of silver light stream where its fractured body used to loom. A series that starts with moonlight and ends with moonlight streaming from an absence has been consistent about one thing: light in the Haven is a position, not a possession.</p>
<h2>The First Seal</h2>
<p>The seal woven in the quiet before the first dawn, when the world held its breath and listened. The old texts give it an equation &#8212; the integral of light and truth over the world yields the vessel &#8212; and the people of the Vale gave it a plainer name: the homeward sound. It chose Arin. Everything that follows is a consequence of a guarantee being made before anyone had worked out the terms.</p>
<h2>Seals and chains</h2>
<p>A seal is a localised guarantee: something that says <em>this holds</em>, and can be pointed at later. A chain is what you get when seals depend on each other, which is where the trouble starts. Break one and you do not break one promise; you invalidate every promise that was leaning on it. The saga uses this literally and politically. Book III's mortals forge seals of their own out of lived suffering, and the books insist those seals are <em>alive</em> &#8212; which means they can fail, unlike the dead perfection they are replacing.</p>
<p>I have written about why this is also the correct way to think about software in <a href="/blog/systems-that-break-early.html">Systems that break early</a>. In the fiction it is metaphysics. In the workshop it is a deployment policy.</p>
<h2>The choir</h2>
<p>Many voices. Councils, crowds, networks. The saga's rule about choirs is consistent and uncomfortable: a single voice can be wrong, and a choir can be corrupted. Harmony is not what you get when everyone agrees; it is what you get when disagreement is still legible. Book II's fractured choir and Book III's choir of imperfection are the same idea at two temperatures.</p>
<h2>Dawn and dusk</h2>
<p>Dusk is where nobody has the full picture. Dawn is not perfection; it is enough light to walk without lying about what you see. The fourth book is named for the second, and the chapter that closes the saga is called <em>The Dawn Without Separation</em> &#8212; a promise I mostly believe, and the word <em>mostly</em> is doing the work. If you take one thing from the cosmology, take the refusal of a perfect dawn. Perfect dawns are how you get a Pure Accord and a coup.</p>
<h2>The Lattice Beyond</h2>
<p>The epilogue of Book IV. Shorter than the ending deserves, deliberately. A saga that explains its own afterlife has stopped trusting the reader. If you want the plain-language version of what I think that epilogue is pointing at, the essay that comes closest is <a href="/blog/the-lantern-is-still-on.html">The lantern is still on</a>, which is about keeping a small light on for people who arrive late.</p>
<h2>Where to go next</h2>
<p>The <a href="/books/characters.html">cast list</a> is the companion to this page. The <a href="/glossary.html">glossary</a> holds the shorter definitions. <a href="/books/">The shelf</a> holds the volumes themselves, in order, with the honest note about which door has a book behind it.</p>
""",
    "related": [
        ("/books/characters.html", "Who is who: a spoiler-light cast list"),
        ("/books/", "The shelf"),
        ("/glossary.html", "The Haven glossary"),
        ("/blog/reading-eternal-haven-in-order.html", "Reading Eternal Haven in order"),
    ],
})
