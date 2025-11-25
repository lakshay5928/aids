import pandas as pd
import numpy as np
from scipy import stats

# Sample player performance dataset (e.g., runs scored in matches)
data = {
    'Player': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Runs': [45, 67, 32, 89, 56, 73, 21, 64],
    'Strike Rate': [120.5, 135.2, 110.4, 150.8, 126.5, 140.3, 105.6, 130.2],
    'Average': [40.2, 48.6, 32.4, 55.7, 44.8, 50.1, 28.9, 46.3]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Player Performance Data:\n", df, "\n")

# Descriptive statistics using pandas
print("Descriptive Statistics (Pandas):\n")
print(df.describe(), "\n")

# Calculate individual descriptive measures
mean_runs = np.mean(df['Runs'])
median_runs = np.median(df['Runs'])
mode_runs = stats.mode(df['Runs'], keepdims=True)[0][0]
std_runs = np.std(df['Runs'])
var_runs = np.var(df['Runs'])
range_runs = np.max(df['Runs']) - np.min(df['Runs'])

# Display descriptive statistics for 'Runs'
print("Descriptive Analysis for Runs:")
print(f"Mean: {mean_runs:.2f}")
print(f"Median: {median_runs}")
print(f"Mode: {mode_runs}")
print(f"Standard Deviation: {std_runs:.2f}")
print(f"Variance: {var_runs:.2f}")
print(f"Range: {range_runs}")
