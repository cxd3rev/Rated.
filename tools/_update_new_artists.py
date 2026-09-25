from pathlib import Path

path = Path("tools/add_new_artists.py")
text = path.read_text(encoding="utf-8")
start = text.index("NEW_ARTISTS = [")
end = text.index("]", start) + 1
names = [
    "Public Enemy",
    "N.W.A",
    "Eazy-E",
    "Eric B. & Rakim",
    "Gang Starr",
    "De La Soul",
    "Mos Def",
    "Talib Kweli",
    "The Pharcyde",
    "Bone Thugs-N-Harmony",
    "Twista",
    "Tech N9ne",
    "Too $hort",
    "E-40",
    "Scarface",
    "UGK",
    "Juvenile",
    "Cam'ron",
    "Jadakiss",
    "Redman",
    "Immortal Technique",
    "Sean Price",
    "Kodak Black",
    "French Montana",
    "Dave East",
    "AJ Tracey",
    "Giggs",
    "Loyle Carner",
    "$uicideboy$",
    "Sematary",
    "D. Savage",
    "UnoTheActivist",
    "SahBabii",
    "Glokk40Spaz",
    "Benji Blue Bills",
    "Young M.A",
    "Saweetie",
    "City Girls",
    "Fabolous",
    "Jim Jones",
    "Xzibit",
    "Kurupt",
    "Warren G",
    "Mystikal",
    "Geto Boys",
    "Digable Planets",
    "Black Moon",
    "Jeru the Damaja",
    "R.A. the Rugged Man",
    "Nav",
]
lines = ["NEW_ARTISTS = ["]
for name in names:
    lines.append(f'    {name!r},')
lines.append("]")
new_list = "\n".join(lines)
path.write_text(text[:start] + new_list + text[end:], encoding="utf-8")
print("updated", len(names), "artists")
