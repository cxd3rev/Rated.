import json
from pathlib import Path

BASE = Path(r"C:\Users\Aron\Documents\RateYourHipHop")
path = BASE / "js" / "albums.js"
albums = json.loads(path.read_text(encoding="utf-8").replace("const albums =", "", 1).strip().rstrip(";"))
before = len(albums)
# Wrong City Girls (Chinese titles) and wrong Jim Jones (western/folk sounding)
bad_titles_city = {
    "lao shi you wen ti",
    "xia ri xuan yan",
    "nian qing bu yao liu bai",
    "la shou",
}
removed = []
kept = []
for album in albums:
    artist = album["artist"]
    title_key = "".join(ch if ch.isalnum() else " " for ch in album["title"].lower())
    title_key = " ".join(title_key.split())
    if artist == "City Girls" and title_key in bad_titles_city:
        removed.append(f"{artist} - {album['title']}")
        continue
    if artist == "Jim Jones":
        # all current Jim Jones rows are the wrong artist; drop them for retry
        removed.append(f"{artist} - {album['title']}")
        continue
    kept.append(album)
path.write_text("const albums = " + json.dumps(kept, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"removed {len(removed)}; albums {before} -> {len(kept)}")
for line in removed:
    print(" -", line)
