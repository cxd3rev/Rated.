import json, re
from pathlib import Path

BASE = Path(r"C:\Users\Aron\Documents\RateYourHipHop")
albums = json.loads((BASE/"js"/"albums.js").read_text(encoding="utf-8").replace("const albums =","",1).strip().rstrip(";"))

wanted = [
    "Public Enemy", "N.W.A", "Eazy-E", "Eric B. & Rakim", "Gang Starr",
    "De La Soul", "Mos Def", "Talib Kweli", "The Pharcyde", "Bone Thugs-N-Harmony",
    "Twista", "Tech N9ne", "Too $hort", "Too Short", "E-40", "Scarface",
    "UGK", "Juvenile", "Cam'ron", "Jadakiss", "Redman",
    "Immortal Technique", "Sean Price", "Kodak Black", "French Montana", "Dave East",
    "AJ Tracey", "Giggs", "Loyle Carner", "$uicideboy$", "Sematary",
    "D. Savage", "UnoTheActivist", "SahBabii", "Glokk40Spaz", "Benji Blue Bills",
    "Young M.A", "Saweetie", "City Girls", "Fabolous", "Jim Jones",
    "Xzibit", "Kurupt", "Warren G", "Warren G.", "Mystikal", "Geto Boys",
    "Digable Planets", "Black Moon", "Jeru the Damaja", "R.A. the Rugged Man", "R.A. The Rugged Man", "Nav", "NAV",
]

def normalize(text):
    text = text.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()

by_artist = {}
for a in albums:
    by_artist.setdefault(a["artist"], []).append(a)

print("UGK albums:")
for a in by_artist.get("UGK", []):
    print(" ", a["id"], a["title"], a["year"], len(a["songs"]))

print("\nArtist coverage:")
# map wanted to actual catalog artists via normalize
catalog_norms = {}
for artist, rows in by_artist.items():
    catalog_norms.setdefault(normalize(artist), []).append((artist, len(rows)))

missing = []
covered = []
for name in [
    "Public Enemy","N.W.A","Eazy-E","Eric B. & Rakim","Gang Starr","De La Soul","Mos Def","Talib Kweli","The Pharcyde","Bone Thugs-N-Harmony","Twista","Tech N9ne","Too Short","E-40","Scarface","UGK","Juvenile","Cam'ron","Jadakiss","Redman","Immortal Technique","Sean Price","Kodak Black","French Montana","Dave East","AJ Tracey","Giggs","Loyle Carner","$uicideboy$","Sematary","D. Savage","UnoTheActivist","SahBabii","Glokk40Spaz","Benji Blue Bills","Young M.A","Saweetie","City Girls","Fabolous","Jim Jones","Xzibit","Kurupt","Warren G","Mystikal","Geto Boys","Digable Planets","Black Moon","Jeru the Damaja","R.A. the Rugged Man","Nav"
]:
    key = normalize(name)
    hits = catalog_norms.get(key) or []
    # also try Too $hort
    if not hits and name == "Too Short":
        hits = catalog_norms.get(normalize("Too $hort")) or []
    total = sum(n for _, n in hits)
    labels = ", ".join(f"{a}:{n}" for a,n in hits)
    if total == 0:
        missing.append(name)
        print(f"EMPTY {name}")
    else:
        covered.append((name, total, labels))
        print(f"OK {name}: {total} ({labels})")

print("\ncovered", len(covered), "missing", len(missing))
print("total albums", len(albums))
