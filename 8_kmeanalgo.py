import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

points = np.array([
    [1, 1],
    [1, 2],
    [4, 3],
    [5, 4],
    [9, 8],
    [10, 8]
], dtype=float)

label_names = [f"({int(x)},{int(y)})" for x, y in points]

kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)
kmeans.fit(points)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_

print("Centroids:")
for i, c in enumerate(centroids):
    print(f"C{i+1}: ({c[0]:.2f}, {c[1]:.2f})")

print("\nAssignments (points -> cluster):")
for name, lab in zip(label_names, labels):
    print(f"{name} -> C{lab+1}")

print(f"\nInertia: {inertia:.4f}")

plt.figure()

# Scatter plot of points colored by cluster
plt.scatter(points[:, 0], points[:, 1], c=labels, s=80, label="Points")

# Scatter plot of centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, marker="X", c="red", label="Centroids")

# Annotate points with their names
for i, txt in enumerate(label_names):
    plt.annotate(txt, (points[i, 0] + 0.1, points[i, 1] + 0.1), fontsize=9)

plt.title("K-means (k=2) Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.tight_layout()
plt.show()