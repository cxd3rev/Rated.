import json
import re
from pathlib import Path

BASE = Path(r"C:\Users\Aron\Documents\RateYourHipHop")
raw = (BASE / "js" / "albums.js").read_text(encoding="utf-8")
albums = json.loads(raw.replace("const albums =", "", 1).strip().rstrip(";"))

# Inspect suspect artists
for name in ["City Girls", "Jim Jones", "Too $hort", "De La Soul", "Cam'ron", "Kodak Black", "Sematary", "Saweetie", "Warren G", "Warren G."]:
    rows = [a for a in albums if a["artist"] == name or name.lower() in a["artist"].lower()]
    print(f"=== {name} ({len(rows)}) ===")
    for a in rows[:8]:
        print(f"  {a['id']}: {a['title']} ({a['year']})")
