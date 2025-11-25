import pandas as pd
import matplotlib.pyplot as plt

# Create simple healthcare data
data = {
    'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'blood_pressure': [120, 125, 130, 135, 140, 145, 150, 155, 160, 165],
    'cholesterol': [180, 190, 200, 210, 220, 230, 240, 250, 260, 270],
    'bmi': [22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    'diabetes': ['No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

print("=== HEALTHCARE DATA ANALYSIS ===")
print("\nBasic Info:")
print(df.head())
print(f"\nShape: {df.shape}")

print("\nStatistics:")
print(df.describe())

print("\nDiabetes Count:")
print(df['diabetes'].value_counts())

# Simple plots
plt.figure(figsize=(12, 8))

# Plot 1: Age distribution
plt.subplot(2, 2, 1)
plt.hist(df['age'], color='lightblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')

# Plot 2: Blood pressure vs Age
plt.subplot(2, 2, 2)
plt.scatter(df['age'], df['blood_pressure'], color='red')
plt.title('Blood Pressure vs Age')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')

# Plot 3: BMI distribution
plt.subplot(2, 2, 3)
plt.hist(df['bmi'], color='lightgreen', edgecolor='black')
plt.title('BMI Distribution')
plt.xlabel('BMI')

# Plot 4: Diabetes comparison
plt.subplot(2, 2, 4)
diabetic_bp = df[df['diabetes'] == 'Yes']['blood_pressure']
non_diabetic_bp = df[df['diabetes'] == 'No']['blood_pressure']
plt.bar(['Non-Diabetic', 'Diabetic'], [non_diabetic_bp.mean(), diabetic_bp.mean()], 
        color=['blue', 'red'])
plt.title('Average Blood Pressure by Diabetes Status')
plt.ylabel('Blood Pressure')

plt.tight_layout()
plt.show()

# Simple analysis
print(f"\nAverage age: {df['age'].mean():.1f} years")
print(f"Average blood pressure: {df['blood_pressure'].mean():.1f}")
print(f"Average cholesterol: {df['cholesterol'].mean():.1f}")
print(f"Average BMI: {df['bmi'].mean():.1f}")
