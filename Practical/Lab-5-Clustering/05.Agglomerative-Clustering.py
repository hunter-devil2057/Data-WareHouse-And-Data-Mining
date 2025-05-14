import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

# Given data
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Reshaping data into a 2D array (each point as a (x, y) pair)
data = np.array(list(zip(x, y)))

# Creating the linkage matrix for the dendrogram
Z = linkage(data, 'ward')

# Now performing Agglomerative Clustering for the given number of clusters (let's assume 3 clusters)
clustering = AgglomerativeClustering(n_clusters=3)
labels = clustering.fit_predict(data)

# Visualizing the clustered points
plt.scatter(x, y, c=labels, cmap='viridis', s=100)
plt.title("Agglomerative Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Visualizing the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Dendrogram for Agglomerative Clustering")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

