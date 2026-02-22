# Quran JSON Data Parser

Simple Python script to read and analyze Quran chapter metadata from a JSON file.

## 📂 Files

* `quran.json` — Quran chapter data
* `quran_json.py` — JSON parsing and analysis script

## 📄 JSON Structure

Each chapter object contains:

```json
{
  "id": 1,
  "name": "الفاتحة",
  "transliteration": "Al-Fatihah",
  "translation": "The Opener",
  "type": "meccan",
  "total_verses": 7
}
```

## ⚙️ Features

* Load JSON data using Python
* Print chapter names
* Export results to `.txt` or `.json`
* Calculate:

  * Total verses in the Quran
  * Number of Meccan and Medinan chapters
  * Total verses revealed in Makkah and Madinah

## ▶️ Run

```bash
python quran_json.py
```

## 🛠 Requirements

* Python 3.x
* Built-in `json` module

---