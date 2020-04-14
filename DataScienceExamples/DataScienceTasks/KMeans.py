from DataScienceExamples.FunctionalFun.Vectors import distance
from DataScienceExamples.FunctionalFun.Vectors import vector_mean
from DataScienceExamples.FunctionalFun.Vectors import squared_distance
from matplotlib import pyplot as plt
import random
plt.ion()
plt.title("KMeans")
plt.xlabel("X")
plt.ylabel("Y")
class KMeans:
    def __init__(self,k):
        self.k = k
        self.means = None

    #return indexOf cluster by min distance.
    def classify(self,input):
        return min(range(self.k),key=lambda i:distance(input,self.means[i]))

    def train(self,input):
        j = 0
        self.means = list(random.sample(input,self.k))
        assignments = None
        while True:
            j+=1
            n_assignments = list(map(self.classify,input)) #clusters of points
            print("Iteraration "+str(j))
            print("A = "+str(assignments))
            print("NA = "+str(n_assignments))
            if assignments == n_assignments:
                return
            assignments = n_assignments
            for i in range(self.k):
                i_points = [p for p,a in zip(input,assignments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)
# P = [[12,33],[1,22],[10,5],[22,12],[7,7],[0,5],[5,0],[12,12],[22,16],[17,20],[22,11],[21,12],[13,15],[7,10],[24,12],[15,8]]
PN = []; jj = 0
while jj < 50:
    jj+=1
    PN.append([random.randrange(0,100),random.randrange(0,100)])
random.seed(0)
print("L = "+str(len(PN)))
cluster = KMeans(7) # FOR P = 4.
cluster.train(PN)
print(cluster.means)
for p in PN:
    plt.scatter(p[0],p[1],color='b')
for p in cluster.means:
    plt.scatter(p[0],p[1],color='r')
plt.show()