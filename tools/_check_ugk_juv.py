import json, urllib.request, urllib.parse
from pathlib import Path

BASE = Path(r"C:\Users\Aron\Documents\RateYourHipHop")
UA = {"User-Agent": "RateYourHipHop/1.0"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

# Check Juvenile albums on Deezer for id 3504
releases = get("https://api.deezer.com/artist/3504/albums?limit=50")
print("Juvenile 3504 sample:")
for r in (releases.get("data") or [])[:15]:
    print(" ", r.get("id"), r.get("title"), r.get("release_date"), "tracks", r.get("nb_tracks"))

# Search interweave
print("\nSearch Interweave:")
data = get("https://api.deezer.com/search/album?q=" + urllib.parse.quote("Interweave Juvenile") + "&limit=5")
for r in data.get("data") or []:
    art = (r.get("artist") or {}).get("name")
    print(" ", r.get("title"), "by", art, "id", r.get("id"))

# UGK check
print("\nUGK 387168 sample:")
releases = get("https://api.deezer.com/artist/387168/albums?limit=30")
for r in (releases.get("data") or [])[:20]:
    print(" ", r.get("id"), r.get("title"), r.get("release_date"), "tracks", r.get("nb_tracks"))

# Check WAKE UP album
print("\nWAKE UP album lookup via search:")
data = get("https://api.deezer.com/search/album?q=" + urllib.parse.quote("WAKE UP!IT'S ALREADY MORNING!") + "&limit=3")
for r in data.get("data") or []:
    art = (r.get("artist") or {}).get("name")
    print(" ", r.get("title"), "by", art)
