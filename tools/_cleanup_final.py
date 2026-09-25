import json
import re
from pathlib import Path

BASE = Path(r"C:\Users\Aron\Documents\RateYourHipHop")
path = BASE / "js" / "albums.js"
albums = json.loads(path.read_text(encoding="utf-8").replace("const albums =", "", 1).strip().rstrip(";"))

def normalize(text):
    text = text.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()

remove_titles = {
    ("juvenile", "interweave 03"),
    ("juvenile", "intermission"),
    ("juvenile", "interweave 02"),
    ("juvenile", "nterweave"),
    ("ugk", "wake up it s already morning"),
    ("ugk", "16 21 l o c ep"),
}

kept = []
removed = []
for album in albums:
    artist_key = normalize(album["artist"])
    title_key = normalize(album["title"])
    # merge Too $hort -> Too Short
    if album["artist"] == "Too $hort":
        album = dict(album)
        album["artist"] = "Too Short"
    if (artist_key, title_key) in remove_titles or (
        artist_key == "juvenile" and "interweave" in title_key
    ) or (artist_key == "juvenile" and title_key == "intermission") or (
        artist_key == "juvenile" and title_key == "nterweave"
    ) or (artist_key == "ugk" and "wake up" in title_key) or (
        artist_key == "ugk" and "16 21" in title_key
    ):
        removed.append(f"{album['artist']} - {album['title']}")
        continue
    kept.append(album)

path.write_text("const albums = " + json.dumps(kept, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"removed {len(removed)}; albums now {len(kept)}")
for line in removed:
    print(" -", line)

# Fix Too Short photo
photos_path = BASE / "js" / "artistPhotos.js"
photos = json.loads(photos_path.read_text(encoding="utf-8").replace("const artistPhotos =", "", 1).strip().rstrip(";"))
# Drop bad Too $hort Presents key if present
bad_keys = [k for k in photos if "presents lil jon" in k.lower() or k == "Too $hort Presents Lil Jon, The Eastside Boyz & Many More"]
for k in bad_keys:
    print("drop photo key", k)
    photos.pop(k, None)
# Ensure Too Short has a photo; copy from Warren G style fetch if needed
import urllib.request, urllib.parse, time
UA = {"User-Agent": "RateYourHipHop/1.0"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

for name, artist_id in [("Too Short", 504125), ("Jim Jones", 288), ("City Girls", 68294032), ("Warren G", 712)]:
    data = get(f"https://api.deezer.com/artist/{artist_id}")
    pic = data.get("picture_xl") or data.get("picture_big") or ""
    if pic:
        photos[name] = pic
        print("photo", name)
    time.sleep(0.15)

photos_path.write_text(
    "const artistPhotos = " + json.dumps(photos, ensure_ascii=False, separators=(",", ":")) + ";\n",
    encoding="utf-8",
)
print("photos", len(photos))
