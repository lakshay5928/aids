import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Sample dataset: Yearly crop yields (tons per hectare) for multiple crops ---
data = {
    "Year": [2015,2016,2017,2018,2019,2020,2021,2022],
    "Wheat": [3.2, 3.5, 3.1, 3.8, 3.6, 3.9, 4.0, 4.1],
    "Rice":  [4.5, 4.6, 4.4, 4.7, 4.8, 4.9, 5.0, 5.2],
    "Maize": [2.8, 3.0, 3.2, 3.1, 3.3, 3.5, 3.6, 3.9],
    "Soy":   [1.6, 1.7, 1.9, 1.8, 2.0, 2.1, 2.2, 2.3]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# --- Basic descriptive analysis ---
print("Summary statistics (per crop):\n")
print(df.describe().T[['mean','std','min','max']])

# --- Year-over-year percentage change ---
pct_change = df.pct_change() * 100
print("\nYear-over-year % change (first rows will be NaN):\n")
print(pct_change.round(2))

# --- Rolling (3-year) average to smooth trends ---
rolling = df.rolling(window=3, min_periods=1).mean()

# --- Plots ---
plt.figure(figsize=(10,6))
for col in df.columns:
    plt.plot(df.index, df[col], marker='o', label=col)
plt.title("Crop Yield Trends (tons/ha)")
plt.xlabel("Year")
plt.ylabel("Yield (tons per hectare)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Plot rolling averages (smoother trend)
plt.figure(figsize=(10,6))
for col in rolling.columns:
    plt.plot(rolling.index, rolling[col], marker='o', linestyle='--', label=f"{col} (3-yr avg)")
plt.title("Smoothed Crop Yield Trends (3-year rolling average)")
plt.xlabel("Year")
plt.ylabel("Yield (tons per hectare)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart: Average yield by crop across the period
avg_yield = df.mean().sort_values(ascending=False)
plt.figure(figsize=(8,5))
plt.bar(avg_yield.index, avg_yield.values)
plt.title("Average Yield per Crop (2015-2022)")
plt.ylabel("Average yield (tons/ha)")
for i, v in enumerate(avg_yield.values):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.show()

# Optional: export processed results to CSV
df.to_csv("crop_yields_by_year.csv")
avg_yield.to_csv("avg_yield_per_crop.csv", header=["Average_Yield"])
print("\nSaved: crop_yields_by_year.csv and avg_yield_per_crop.csv")


