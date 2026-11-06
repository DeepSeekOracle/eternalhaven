#!/usr/bin/env python3
"""Rebuild the moved-page stubs: noindex, ad-free, one honest sentence each."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

GAMES = {
    "games/lattice-swarm/index.html": ("Lattice Swarm", "https://chatagent.ca/games/lattice-swarm/",
        "A hex-grid command game: place a swarm, hold the line, and watch the grid answer back. The playable build is on the arcade."),
    "games/lattice-marines/index.html": ("Lattice Marines", "https://chatagent.ca/games/lattice-marines/",
        "An isometric island war with a short loop and a local ledger. The playable build is on the arcade."),
    "games/eternal-lattice/index.html": ("Eternal Lattice", "https://chatagent.ca/games/eternal-lattice/",
        "The champion card-battle experiment. The playable build is on the arcade."),
    "games/lattice-golf/index.html": ("Lattice Golf", "https://chatagent.ca/games/lattice-golf/",
        "Club choice, a full power bar, and named nines. The playable build is on the arcade."),
    "games/stock-market-masters/index.html": ("Stock Market Masters", "https://chatagent.ca/games/stock-market-masters/",
        "A market simulation, honest about what it imitates. The playable build is on the arcade."),
    "games/lattice-golf/ledger.html": ("Lattice Golf ledger", "https://chatagent.ca/games/lattice-golf/ledger.html",
        "The local score ledger for Lattice Golf, now hosted with the arcade build."),
    "games/lattice-marines/ledger.html": ("Lattice Marines ledger", "https://chatagent.ca/games/lattice-marines/ledger.html",
        "The local score ledger for Lattice Marines, now hosted with the arcade build."),
    "games/stock-market-masters/ledger.html": ("Stock Market Masters ledger", "https://chatagent.ca/games/stock-market-masters/ledger.html",
        "The local run ledger for Stock Market Masters, now hosted with the arcade build."),
    "games/stock-market-masters/disclaimer.html": ("Stock Market Masters disclaimer", "https://chatagent.ca/games/stock-market-masters/disclaimer.html",
        "The gambling disclaimer for Stock Market Masters. It is a game, not financial advice, and it moved with the build."),
}
LYGO = {
    "LYGO-Network/champions.html": ("LYGO champions", "https://deepseekoracle.github.io/Excavationpro/LYGO-Network/champions.html",
        "The champion index for the LYGO network, kept with the protocol stack."),
    "LYGO-Network/legacy-guardian-music.html": ("Legacy guardian music", "https://deepseekoracle.github.io/Excavationpro/LYGO-Network/legacy-guardian-music.html",
        "The legacy guardian music page, kept with the protocol stack."),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Moved: {name} | Eternal Haven</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<meta http-equiv="refresh" content="0;url={url}">
<script>location.replace("{url}");</script>
<style>
body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#0b0a0f;color:#f4eee6;
font:400 1rem/1.7 "IBM Plex Sans",system-ui,sans-serif;padding:2rem}}
.card{{max-width:34rem;border:1px solid rgba(244,238,230,.16);border-radius:16px;padding:1.6rem 1.5rem;background:#121018}}
h1{{font:500 1.6rem/1.2 "Cormorant Garamond",Georgia,serif;color:#d4b56a;margin:0 0 .6rem}}
p{{color:#a89b8c;margin:0 0 .9rem}}
a{{color:#8ec8e8}}
</style>
</head>
<body>
<main class="card">
  <h1>{name} has moved</h1>
  <p>{desc}</p>
  <p>This address now forwards to the build. If the forward does not fire, use the link:
  <a href="{url}">{url}</a></p>
  <p><a href="https://eternalhaven.ca/games/">The games page on Eternal Haven</a> explains what each title is and which one to open first.</p>
</main>
</body>
</html>
"""


def write(path, name, url, desc):
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEMPLATE.format(name=name, url=url, desc=desc), encoding="utf-8")
    print("wrote", path)


for p, (n, u, d) in {**GAMES, **LYGO}.items():
    write(p, n, u, d)
print("done")
