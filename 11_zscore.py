import numpy as np
from scipy import stats
import pandas as pd

# Example dataset: e.g., model accuracy percentages or scores
data = [56, 45, 67, 49, 58, 62, 70, 66, 59, 52]

# Step 1: Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data)

print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")

# Step 2: Compute Z-scores manually
z_scores_manual = [(x - mean) / std for x in data]

# Step 3: Compute Z-scores using SciPy
z_scores_scipy = stats.zscore(data)

# Step 4: Display results
df = pd.DataFrame({
    "Data": data,
    "Z-Score (Manual)": z_scores_manual,
    "Z-Score (SciPy)": z_scores_scipy
})

print("\nZ-Score Table:")
print(df)
