import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load dataset
iris = load_iris()
X = iris.data   # features (sepal & petal measurements)
y = iris.target # target (species)

# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Normalize features (important for distance-based algorithms)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Create KNN model (try K=5)
knn = KNeighborsClassifier(n_neighbors=5)

# Step 6: Train the model
knn.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = knn.predict(X_test)

# Step 8: Evaluate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))
