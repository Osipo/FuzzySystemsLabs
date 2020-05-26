from DataScienceExamples.FunctionalFun.Vectors import distance
from DataScienceExamples.FunctionalFun.Vectors import vector_mean
from DataScienceExamples.FunctionalFun.Vectors import squared_distance
from matplotlib import pyplot as plt
from _functools import partial
import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
class KMeansImpl:
    def __init__(self,k):
        self.k = k # nums of clusters
        self.means = None #centroids
        self.sums = [0 for i in range(0,k)] # sum of squared distances of samples to the nearest cluster centre.
        self.ccards = [0 for i in range(0,k)]
        self.a = [] # a(i) = mean(sum_of_distances between i and other points of cluster_i)
        self.b = [] # b(i) = min(1/card(cluster_j)*sum(dist(i,j) for j in cluster_j)
        self.clusters = [] # points in clusters.
        self.sil = [] #silhouette_score for each point i.

    #return indexOf cluster by min distance.
    def classify(self,input):
        return min(range(self.k),key=lambda i:distance(input,self.means[i]))

    def train(self,input):
        if not(isinstance(input,list)):
            try:
                input = input.tolist()
            except:
                input = list(input)
        j = 0
        self.means = list(random.sample(input,self.k))
        assignments = None
        while True:
            j+=1
            n_assignments = list(map(self.classify,input)) #clusters of points
            if assignments == n_assignments:
                break
            assignments = n_assignments
            # self.a = [] # list of distances between point_i and other points in cluster which they are belong.
            # self.clusters = [] # list of points in cluster_i (clusters[i])
            for i in range(self.k):
                i_points = [p for p,a in zip(input,assignments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)

        for i in range(self.k):
            i_points = [p for p,a in zip(input,assignments) if a == i]
            if i_points:
                dist = partial(squared_distance,self.means[i])
                self.sums[i] = sum(list(map(dist,i_points)))  # assign sum of squared distances of samples to the cluster which they are belong.
                self.ccards[i] = len(i_points)
                for p in i_points:
                    d = partial(distance, p)
                    self.a.append((1 / (self.ccards[i] - 1)) * sum(list(map(d, i_points))) if
                                  self.ccards[i] > 1 else 0)
                self.clusters.append(i_points)

        print('reached')
        self.compute_b()
        i = 0
        if(self.k > 1):
            for c in self.clusters:
                for p in c:
                    self.sil.append((self.b[i] - self.a[i])/max(self.b[i],self.a[i]) if len(c) > 0 and self.a[i] > 0 and self.b[i] > 0 else 0)
                    i+=1

    def compute_b(self):
        if(self.k < 2):
            return
        m = []
        for i in self.clusters:
            for p in i:
                l = [c for c in self.clusters if c != i]
                d = partial(distance,p)
                for ci in range(len(l)):
                    l_j = l[ci] # list of points in j cluster.
                    m.append(sum(list(map(d,l_j)))*(1/len(l_j)))
                self.b.append(min(m))





PN = []; jj = 0 # PN are random data
while jj < 50:
    jj+=1
    PN.append([random.randrange(0,100),random.randrange(0,100),random.randrange(100,200),random.randrange(100,200)])
random.seed(0)

X = pd.read_csv('datasets/heart.csv')
cats = ['sex','fbs','exang','target','restecg','slope','cp','thal','ca']
for col in cats:
    dummies = pd.get_dummies(X[col], prefix=col)
    X = pd.concat([X, dummies], axis=1)
    X.drop(col, axis=1, inplace=True)
mms = MinMaxScaler()
mms.fit(X)
data_transformed = mms.transform(X)


ssd = []
print('---data---')
silscores = []
K = range(1,10)
for k in K:
    km = KMeansImpl(k) # initiate k clusters
    km.train(data_transformed) # train on data
    ssd.append(sum(km.sums)) # sum of the each cluster.
    if(k > 1):
        silscores.append(sum(km.sil))
print('\n---- end ----\n')


#Elbow metrics & si
plt.plot(K, ssd, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

plt.plot(K[1:],silscores,'bx-')
plt.xlabel('k')
plt.ylabel('Silhouette_score')
plt.title("Silhouette method")
plt.show()