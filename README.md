# FitTrackr — Data Cleaning & Basic Analysis

Lightweight Python project that demonstrates simple data cleaning and exploratory analysis on a small fitness dataset.

Files
- [fit_trackr.py](fit_trackr.py) — main script that loads and processes the dataset. Key symbols: [`df`](fit_trackr.py), [`mapping`](fit_trackr.py).
- [fit_trackr_data.csv](fit_trackr_data.csv) — raw CSV dataset used by the script.

Overview
- Reads the CSV dataset, normalizes textual fields, extracts numeric values from "Duration" and "Calories", removes duplicates and rows without usernames, and standardizes activity names.
- Prints basic summary metrics: average duration, most common mood, calories standard deviation, and age interquartile range.

Requirements
- Python 3.8+
- pandas

Quick start
1. Create a virtual environment (recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
