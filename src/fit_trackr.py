import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "fit_trackr_data.csv"

df = pd.read_csv(DATA_PATH)

# Extract numeric values from Duration and Calories columns
df["Duration"] = df["Duration"].str.replace("min", " ").str.strip()
df["Calories"] = df["Calories"].str.replace("kcal", " ").str.strip()
df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce")
df["Calories"] = pd.to_numeric(df["Calories"], errors="coerce")

# Remove duplicates
df = df.drop_duplicates()

# Drop rows without a username
df = df.dropna(subset=["Username"], how="any")

# Standardize Activity labels
df["Activity"] = df["Activity"].str.lower().str.strip()
print("Unique Activity values before standardization:")
print(df["Activity"].value_counts())

mapping = {
    "walk": "walking",
    "swimm": "swimming",
    "swim": "swimming",
}

df["Activity"] = df["Activity"].replace(mapping)
print("\nUnique Activity values after standardization:")
print(df["Activity"].value_counts())

avg_duration = df["Duration"].mean()
print(f"\nAverage activity duration: {avg_duration:.2f} minutes")

most_common_mood = df["Mood"].mode()[0]
print(f"Most common post-activity mood: {most_common_mood}")

calories_variation = df["Calories"].std()
print(f"Calories standard deviation: {calories_variation:.2f} kcal")

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1

print(f"\nAge range for middle 50% of users: {Q1:.0f} - {Q3:.0f} years")
print(f"Interquartile range: {IQR:.0f} years")
