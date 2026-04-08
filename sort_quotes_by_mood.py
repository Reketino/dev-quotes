import json
from pathlib import Path
from typing import TypedDict

# Path of the file if it tries to escape🏃🏻‍➡️
FILE = Path("quotes.json")

# Load in file, cuz why load it out?
with FILE.open("r", encoding="utf-8") as f:
    quotes = json.load(f)

# Defined mood order   
MOOD_ORDER = {
    "chaos": 0,
    "pain": 1,
    "fun": 2,
    "wisdom": 3,
}

# Quote class defined
class Quote(TypedDict, total=False):
    mood: str

#  List sorting
def mood_key(q: Quote):
    mood = q.get("mood") or ""
    mood_rank = MOOD_ORDER.get(mood, 99)
    text = q.get("text", "").lower()
    return (mood_rank, text)
quotes.sort(key=mood_key)


# Updates the same file, why write a new file? 
with FILE.open("w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)

# Terminal gives you confirmation, as he should
print("🛎️ quotes.json has now sorted moods (in-place)")
