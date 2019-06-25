from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

dataset = pd.read_csv("data.csv")
X = np.array(dataset.drop(['artist','song_title','target', 'id'], axis=1))
print(X)
# kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
