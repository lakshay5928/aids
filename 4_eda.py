 # Experiment: Exploratory Data Analysis (EDA) on a Sample Iris Dataset
 # Objective: Perform basic EDA using pandas and seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 # Manually created sample data from Iris dataset
data = {
    'sepal_length': [5.1, 4.9, 4.7, 6.0, 5.4, 6.9, 6.2, 5.9, 6.7, 6.3],
    'sepal_width':  [3.5, 3.0, 3.2, 3.2, 3.9, 3.1, 2.9, 3.0, 3.1, 2.5],
    'petal_length': [1.4, 1.4, 1.3, 5.1, 1.7, 5.4, 4.3, 5.1, 5.6, 4.9],
    'petal_width':  [0.2, 0.2, 0.2, 1.5, 0.4, 2.1, 1.3, 1.8, 2.4, 1.5],
    'species': ['setosa', 'setosa', 'setosa', 'versicolor', 'setosa',
                'virginica', 'virginica', 'versicolor', 'virginica', 'versicolor']
}
 # Create DataFrame
df = pd.DataFrame(data)
 # Describe the dataset (summary statistics)
print("Descriptive Statistics:")
print(df.describe())
 # Pairwise visualization
print("Generating pairplot...")
sns.pairplot(df, hue='species')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()