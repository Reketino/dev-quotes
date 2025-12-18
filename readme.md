# Dev Quotes – Mood Sorted

This folder contains a collection of developer quotes, each tagged with a
*mood* for use in OG images, widgets, or other fun UI elements.

## 📁 Files

- `quotes.json`  
  The main quotes file.  
  Each quote has a `text` and a `mood`.

- `sort_quotes_in_place.py`  
  A small Python utility that sorts `quotes.json` **in place** by mood.

## 🎭 Supported moods

Quotes are grouped in this order:

1. `chaos`
2. `pain`
3. `fun`
4. `wisdom`

## 🛠 How to sort the quotes

Make sure you are in the same directory as `quotes.json`, then run:

```bash
python sort_quotes_by_mood.py