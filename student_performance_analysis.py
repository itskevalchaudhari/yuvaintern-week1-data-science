from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset" / "student-mat.csv"
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

# Original UCI file is semicolon-separated.
df = pd.read_csv(DATA, sep=";")

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nDescriptive statistics:")
print(df.describe())

print("\nMean G3 by studytime:")
print(df.groupby("studytime")["G3"].mean())

print("\nMean G3 by goout:")
print(df.groupby("goout")["G3"].mean())

print("\nMean G3 by Walc:")
print(df.groupby("Walc")["G3"].mean())

# 1. Final grade distribution
plt.figure(figsize=(8, 5))
df["G3"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribution of Final Grade (G3)")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(OUT / "g3_distribution_reproduced.png", dpi=180)
plt.show()

# 2. Study time vs final grade
plt.figure(figsize=(8, 5))
sns.boxplot(x="studytime", y="G3", data=df)
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig(OUT / "studytime_vs_g3.png", dpi=180)
plt.show()

# 3. Absences vs final grade
plt.figure(figsize=(8, 5))
sns.scatterplot(x="absences", y="G3", data=df)
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig(OUT / "absences_vs_g3.png", dpi=180)
plt.show()

# 4. Correlation heatmap
plt.figure(figsize=(10, 7))
numeric_cols = df.select_dtypes(include="number")
sns.heatmap(numeric_cols.corr(), annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUT / "correlation_heatmap.png", dpi=180)
plt.show()

# 5. Missing-value check
missing = df.isna().sum()
plt.figure(figsize=(10, 5))
missing.plot(kind="bar")
plt.title("Missing Values by Column")
plt.xlabel("Column")
plt.ylabel("Missing Values")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(OUT / "missing_values_reproduced.png", dpi=180)
plt.show()
