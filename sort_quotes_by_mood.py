import json
from pathlib import Path

FILE = Path("quotes.json")

with FILE.open("r", encoding="utf-8") as f:
    quotes = json.load(f)
    
MOOD_ORDER = {
    "chaos": 0,
    "pain": 1,
    "fun": 2,
    "wisdom": 3,
}

quotes.sort(key=lambda q: MOOD_ORDER.get(q.get("mood"), 99))

with FILE.open("w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)
    
print("🛎️ quotes.json has now sorted moods (in-place)")
