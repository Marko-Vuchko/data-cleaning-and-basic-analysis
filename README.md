# FitTrackr — Fitness Data Cleaning & Analysis

Lightweight Python project demonstrating structured data cleaning and exploratory analysis on fitness app activity logs.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

---

## Overview

This project cleans a messy fitness tracking export and extracts actionable summary metrics for product and engagement analysis. Each row represents one logged activity with duration, calories, mood, and user demographics.

| Task | Business question | Method |
|------|-------------------|--------|
| **1** | Are activity labels consistent for reporting? | Text normalization & mapping |
| **2** | What is typical session duration? | Mean duration after parsing |
| **3** | Which mood follows workouts most often? | Mode on Mood column |
| **4** | How variable is calorie burn? | Standard deviation |
| **5** | What is the core user age band? | IQR on Age |

---

## Repository structure

```
.
├── data/
│   └── fit_trackr_data.csv     # Raw activity export
├── docs/
│   └── sample_output.txt       # Example console output
├── src/
│   └── fit_trackr.py           # Cleaning and summary script
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Quick start

```bash
git clone https://github.com/Marko-Vuchko/data-cleaning-and-basic-analysis.git
cd data-cleaning-and-basic-analysis
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
python src/fit_trackr.py
```

---

## Methodology

1. Parse numeric values from text fields (`Duration`, `Calories`).
2. Remove duplicate rows and records without usernames.
3. Standardize activity names via a canonical mapping dictionary.
4. Compute summary statistics: average duration, dominant mood, calorie variability, and age IQR.

See [`docs/sample_output.txt`](docs/sample_output.txt) for example output.

---

## Tech stack

**Python:** pandas

---

## Author

**Marko Vučković** — Data Analyst & Developer  
[GitHub](https://github.com/Marko-Vuchko) · [Email](mailto:markovucko12@gmail.com)

---

## License

This project is released under the [MIT License](LICENSE).
