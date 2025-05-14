import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

# Given data
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Reshaping data into a 2D array (each point as a (x, y) pair)
data = np.array(list(zip(x, y)))

# Using KMeans to simulate Divisive Clustering
# Start with 1 cluster (whole dataset)
kmeans = KMeans(n_clusters=1, random_state=42)
kmeans.fit(data)
labels = kmeans.labels_

# For simulating the divisive process, we iteratively split the largest cluster
# Divisive clustering usually splits the largest cluster into two smaller clusters
# Simulate 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)
labels = kmeans.labels_

# Perform hierarchical clustering for dendrogram visualization
Z = linkage(data, 'ward')

# Visualizing the data with the labels (clusters)
plt.scatter(x, y, c=labels, cmap='viridis', s=100)
plt.title("Divisive Clustering (Simulated with KMeans)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Visualizing the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Dendrogram for Divisive Clustering Simulation")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

