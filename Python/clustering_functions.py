
from sklearn.cluster import KMeans as kmeans
import numpy as np
import matplotlib.pyplot as plt
# Though the following import is not directly being used, it is required
# for 3D projection to work
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
def ClusterIndicesNumpy(clustNum, labels_array):
    return np.where(labels_array == clustNum)[0]
def getMaximumEmotions():
    ch = pd.read_csv('all_features.csv', sep=',', encoding = "ISO-8859-1")
    arr = ch.values
    indexes = []
    import operator
    with open('maximum_emotion.csv', 'w',  encoding="utf-8") as csvfile:
        sentiment_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sentiment_writer.writerow(["Artist", "Song Title", "verse_emotion","chorus_emotion","Genre","Tempo","Loudness","Energy","Danceability","Mode","Valence"])
        for i in range(len(ch.index)):
            index_verse, value_verse = max(enumerate(ch.loc[i][9:14]), key=operator.itemgetter(1))
            index_chorus, value_chorus = max(enumerate(ch.loc[i][14:19]), key=operator.itemgetter(1))
            sentiment_writer.writerow([ch.loc[i, 'Artist'],ch.loc[i, 'Song Title'],index_verse,index_chorus,ch.loc[i, 'Genre'],ch.loc[i, 'Tempo'],ch.loc[i, 'Loudness'],ch.loc[i, 'Energy'],ch.loc[i, 'Danceability'],ch.loc[i, 'Mode'],ch.loc[i, 'Valence']])

def cluster3d(X):
    # Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause
    np.random.seed(5)
    colors = ['r', 'g', 'b']
    iris = datasets.load_iris()
    estimators = [('k_means_iris_3', KMeans(n_clusters=3))]
    fignum = 1
    titles = ['3 clusters']
    for name, est in estimators:
        fig = plt.figure(fignum, figsize=(11, 10))
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=20, azim=140)
        est.fit(X)
        labels = est.labels_

        ax.scatter(X[:, 0], X[:,1], X[:, 2],
                   c=labels.astype(np.float), edgecolor='k')

        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel('Genre')
        ax.set_ylabel('Tempo')
        ax.set_zlabel('Valence')
        ax.set_title(titles[fignum - 1])
        ax.dist = 12
        fignum = fignum + 1
    plt.show()
def cluster2d(X):
    plt.scatter(X[:,3], X[:, 8], s=50);

    plt.scatter(X[:, 3], X[:, 8], c=labels, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 3], centers[:, 8], c='black', s=200, alpha=0.5);