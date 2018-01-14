#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Feature agglomeration
=========================================================

These images how similar features are merged together using
feature agglomeration.
"""
print(__doc__)

# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import collections
import seaborn as sns
import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale


maxdifference=65
X = pd.read_csv('data.csv').drop(['country','source'],1)
dist = np.linalg.norm(X.iloc[0]-X.iloc[1])


#Cluster the data
#kmeans = KMeans(n_clusters=32, random_state=0).fit(X)
#labels = kmeans.labels_

#Glue back to originaal data
#X['clusters'] = labels
#clmns=list(X.columns)

#Lets analyze the clusters
#print X[clmns].groupby(['clusters']).mean()

#VISAULIZE
"""
reduced_data = PCA(n_components=2).fit_transform(X)
kmeans = KMeans(init='k-means++', n_clusters=4, n_init=10)
kmeans.fit(reduced_data)
print kmeans.predict(reduced_data[0])
# Step size of the mesh. Decrease to increase the quality of the VQ.
h = 20     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each

xx, yy = np.meshgrid(np.arange(-12180122.9165,2147405391.66,90128025), np.arange(-12180122.9165,2147405391.66,190128025))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
print centroids.min(),centroids.max()
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)

plt.show()
"""



