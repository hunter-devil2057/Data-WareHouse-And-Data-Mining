#Mini-Batch K-means Clustering
import time
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans

data=100*np.random.rand(100,2)
print(*data)
mbk=MiniBatchKMeans(n_clusters=5,init='random', batch_size=3000)
t0= time.time()
mbk.fit(data)
t1= time.time()
tt=t1-t0
print("Total Time:",tt)
cents = mbk.cluster_centers_
labels = mbk.labels_
print("Cluster Centers:",*cents)
print("Labels:",*labels)

colors = ["g","r","b",'y','m']
markers=["+","x","*",'.','d']
for i in range(len(data)):
    plt.plot(data[i][0], data[i][1], color=colors[labels[i]], marker=markers[labels[i]])
plt.scatter(cents[:, 0],cents[:, 1], marker = "o", s=50, linewidths = 5)
plt.show()
