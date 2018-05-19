import warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn import decomposition
from IPython.display import display
from sklearn import metrics # for evaluations
from sklearn.datasets import make_blobs, make_circles # for generating experimental data
from sklearn.preprocessing import StandardScaler # for feature scaling
from sklearn.cluster import KMeans 
from sklearn.cluster import DBSCAN
import csv
import pandas as pd
def silhouette_coefficient(dataSet):
    
        # List of number of clusters
    range_n_clusters = [2, 3, 4, 5, 6]
    X = dataSet
  #  pca = decomposition.PCA(n_components=2)
   # pca.fit(X)
   # X = pca.transform(X)
    # For each number of clusters, perform Silhouette analysis and visualize the results.
    for n_clusters in range_n_clusters:

        # Perform k-means.

        kmeans = KMeans(n_clusters=n_clusters, random_state=10)
        y_pred = kmeans.fit_predict(X)
        # Compute the cluster homogeneity and completeness.
        homogeneity = metrics.homogeneity_score(y_pred, y_pred)
        completeness = metrics.completeness_score(y_pred, y_pred)

        # Compute the Silhouette Coefficient for each sample.
        s = metrics.silhouette_samples(X, y_pred)

        # Compute the mean Silhouette Coefficient of all data points.
        s_mean = metrics.silhouette_score(X, y_pred)

        # For plot configuration -----------------------------------------------------------------------------------
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)

        # Configure plot.
        plt.suptitle('Silhouette analysis for K-Means clustering with n_clusters: {}'.format(n_clusters),
                     fontsize=14, fontweight='bold')

        # Configure 1st subplot.
        ax1.set_title('Silhouette Coefficient for each sample')
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")
        ax1.set_xlim([-1, 1])
        ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

        # Configure 2st subplot.
        ax2.set_title('Homogeneity: {}, Completeness: {}, Mean Silhouette score: {}'.format(homogeneity,
                                                                                            completeness,
                                                                                            s_mean))
        ax2.set_xlabel("Feature space for the 1st feature")
        ax2.set_ylabel("Feature space for the 2nd feature")

        # For 1st subplot ------------------------------------------------------------------------------------------

        # Plot Silhouette Coefficient for each sample
        y_lower = 10
        for i in range(n_clusters):
            ith_s = s[y_pred == i]
            ith_s.sort()
            size_cluster_i = ith_s.shape[0]
            y_upper = y_lower + size_cluster_i
            color = cm.spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_s,
                              facecolor=color, edgecolor=color, alpha=0.7)
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            y_lower = y_upper + 10

        # Plot the mean Silhouette Coefficient using red vertical dash line.
        ax1.axvline(x=s_mean, color="red", linestyle="--")

        # For 2st subplot -------------------------------------------------------------------------------------------
        #pca = decomposition.PCA(n_components=2)
        #pca.fit(X)
        #plot_X = pca.transform(X)
        # Plot the predictions
        colors = cm.spectral(y_pred.astype(float) / n_clusters)
        ax2.scatter(X[:,0], X[:,1], c=colors)
    return X