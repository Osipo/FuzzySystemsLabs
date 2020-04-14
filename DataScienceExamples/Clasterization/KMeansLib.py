from sklearn.cluster import KMeans
from DataScienceExamples.FunctionalFun.Vectors import distance
from DataScienceExamples.FunctionalFun.Vectors import vector_mean
from DataScienceExamples.FunctionalFun.Vectors import squared_distance
from matplotlib import pyplot as plt
from _functools import partial
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import random
from sklearn.metrics import silhouette_score
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
def calculate_WSS(points, kmax):
    sse = []
    for k in range(1, kmax + 1):
        kmeans = KMeans(n_clusters=k).fit(points)
        centroids = kmeans.cluster_centers_
        pred_clusters = kmeans.predict(points)
        curr_sse = 0
        # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
        for i in range(len(points)):
            curr_center = centroids[pred_clusters[i]]
            d = partial(squared_distance,curr_center)
            curr_sse += d(points[i])

        sse.append(curr_sse)
    return sse



PN = []; jj = 0 # PN are random data
while jj < 50:
    jj+=1
    PN.append([random.randrange(0,100),random.randrange(0,100),random.randrange(100,200),random.randrange(100,200)])
X = pd.read_csv('datasets/heart.csv')

cats = ['sex','fbs','exang','target','restecg','slope','cp','thal','ca']
for col in cats:
    dummies = pd.get_dummies(X[col], prefix=col)
    X = pd.concat([X, dummies], axis=1)
    X.drop(col, axis=1, inplace=True)
X.head()
mms = MinMaxScaler()
mms.fit(X)
data_transformed = mms.transform(X)
sil = []
sse = []
kmax = 10
# sse = calculate_WSS(data_transformed,kmax)
K = range(1,10)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data_transformed)
    sse.append(km.inertia_)

for k in range(2, kmax):
  kmeans = KMeans(n_clusters = k).fit(X)
  labels = kmeans.labels_
  sil.append(silhouette_score(X, labels, metric = 'euclidean'))

plt.plot(K,sse,'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title("Elbow method")
plt.show()

plt.plot(K[1:],sil,'bx-')
plt.xlabel('k')
plt.ylabel('Siloute_score')
plt.title("Silouhette method")
plt.show()