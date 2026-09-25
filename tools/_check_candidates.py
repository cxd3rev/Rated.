import json
import re
from pathlib import Path

BASE = Path(r"C:\Users\Aron\Documents\RateYourHipHop")

def normalize(text):
    text = text.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()

raw = (BASE / "js" / "albums.js").read_text(encoding="utf-8")
raw = raw.replace("const albums =", "", 1).strip().rstrip(";")
albums = json.loads(raw)
existing = set()
for album in albums:
    for part in re.split(r"\s+&\s+", album["artist"]):
        existing.add(normalize(part))

candidates = [
    "Public Enemy", "N.W.A", "Eazy-E", "Eric B. & Rakim", "Gang Starr",
    "De La Soul", "Mos Def", "Talib Kweli", "The Pharcyde", "Bone Thugs-N-Harmony",
    "Twista", "Tech N9ne", "Too $hort", "E-40", "Scarface",
    "UGK", "Juvenile", "Cam'ron", "Jadakiss", "Redman",
    "Immortal Technique", "Sean Price", "Kodak Black", "French Montana", "Dave East",
    "AJ Tracey", "Giggs", "Loyle Carner", "$uicideboy$", "Sematary",
    "D. Savage", "UnoTheActivist", "SahBabii", "Glokk40Spaz", "Benji Blue Bills",
    "Young M.A", "Saweetie", "City Girls", "Fabolous", "Jim Jones",
    "Xzibit", "Kurupt", "Warren G", "Mystikal", "Geto Boys",
    "Digable Planets", "Black Moon", "Jeru the Damaja", "R.A. the Rugged Man", "Nav",
]
for name in candidates:
    key = normalize(name)
    mark = "DUP" if key in existing else "ok"
    print(f"{mark}\t{name}")
print("count", len(candidates))
print("dups", sum(1 for c in candidates if normalize(c) in existing))
