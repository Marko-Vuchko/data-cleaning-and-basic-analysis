import pandas as pd

df = pd.read_csv("fit_trackr_data.csv")

# Ekstrakcija numeričkih vrednosti iz kolona "Duration" i "Calories"
df["Duration"] = df["Duration"].str.replace("min", " ").str.strip()
df["Calories"] = df["Calories"].str.replace("kcal", " ").str.strip()
df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce")
df["Calories"] = pd.to_numeric(df["Calories"], errors="coerce")

# Uklanjanje duplikata
df = df.drop_duplicates()

# Uklanjanje redova koji u koloni "Username" nemaju vrednosti
df = df.dropna(subset=["Username"], how="any")

# Standardizacija kolone "Activity"
df["Activity"] = df["Activity"].str.lower().str.strip()
print("Unikatne vrednosti u koloni 'Activity' pre standardizacije:")
print(df["Activity"].value_counts())

mapping = {
    "walk": "walking",
    "swimm": "swimming",
    "swim": "swimming"
}

df["Activity"] = df["Activity"].replace(mapping)
print("\nUnikatne vrednosti u koloni 'Activity' nakon standardizacije:")
print(df["Activity"].value_counts())

# Prosečno trajanje aktivnosti
avg_duration = df["Duration"].mean()
print(f"\nProsečno trajanje aktivnosti: {avg_duration:.2f} minuta")

# Najčešće raspoloženje korisnika nakon aktivnosti
most_common_mood = df["Mood"].mode()[0]
print(f"\nNajčešće raspoloženje korisnika nakon aktivnosti: {most_common_mood}")

# Varijacija broja potrošenih kalorija
calories_variation = df["Calories"].std()
print(f"\nVarijacija broja potrošenih kalorija: {calories_variation:.2f} kcal")

# Tipična distribucija godina korisnika
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1

print(f"\nRazlika u godinama između 50% središnjih korisnika aplikacije: {Q1:.0f} - {Q3:.0f} godina")
print(f"Interkvartilni raspon: {IQR:.0f} godina")
