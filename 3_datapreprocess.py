# Experiment 3: Data Preprocessing - Handling Missing Values
# Objective: To learn techniques to handle missing data using pandas
import pandas as pd
import numpy as np
# Creating a DataFrame with missing values
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 29],
    'Score': [85, 90, np.nan, 88]
})
 # Display original data
print("Original Data:")
print(df)
 # Filling missing values with mean
print("\nFilling missing values with mean:")
# df['Age'].fillna(df['Age'].mean(),inplace=True)    # Replacing missing age
# df['Score'].fillna(df['Score'].mean(),inplace=True) # Replacing missing score
df.fillna({
    'Age': df['Age'].mean(),
    'Score': df['Score'].mean()
}, inplace=True)

 # Display updated data
print("\nUpdated Data:")
print(df)