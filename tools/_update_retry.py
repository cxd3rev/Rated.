from pathlib import Path

path = Path("tools/retry_failed_artists.py")
text = path.read_text(encoding="utf-8")
start = text.index("RETRY = [")
end = text.index("]", start) + 1
names = [
    "De La Soul",
    "Cam'ron",
    "Kodak Black",
    "Sematary",
    "Saweetie",
    "Warren G",
    "Too Short",
    "City Girls",
    "Jim Jones",
    "UGK",
    "Juvenile",
    "Kurupt",
]
lines = ["RETRY = ["]
for name in names:
    lines.append(f"    {name!r},")
lines.append("]")
path.write_text(text[:start] + "\n".join(lines) + text[end:], encoding="utf-8")
print("retry list updated", len(names))
