from DataScienceExamples.FunctionalFun.Vectors import distance
from DataScienceExamples.FunctionalFun.Vectors import vector_mean
from DataScienceExamples.FunctionalFun.Vectors import squared_distance
from matplotlib import pyplot as plt
from _functools import partial
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
import random
from sklearn.preprocessing import MinMaxScaler

from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import pydotplus

# generate random samples.
# split data with M features and N instances into
# k samples with m randomly chosen features and N instances with repetitions.
# Then return k trees learned at these samples.
def randomForest(data,target,k,ts,mktreeimg):
    i = 0
    res = []
    while(i < k):
        cols = list(data.columns)
        D = pd.DataFrame(data=data[cols],columns=cols)
        I = np.random.choice(D.index.values,len(D.values),replace=True)
        D = pd.DataFrame(data=D.loc[I,cols],columns=cols)
        D_y = target[I]
        X_train, X_test, y_train, y_test = train_test_split(D, D_y, test_size=ts,random_state=1)
        i+=1
        tree = DecisionTreeClassifier(criterion='entropy', max_features='auto', random_state=17)
        if(mktreeimg is True):
            dot_data = StringIO()
            export_graphviz(tree, out_file=dot_data,
                            filled=True, rounded=True,
                            special_characters=True, feature_names=cols, class_names=['0', '1','2','3'])
            graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
            graph.write_png('tree_'+str(i)+'.png')
            Image(graph.create_png())
        tree.fit(X_train,y_train)
        yp = tree.predict(X_test)
        res.append((tree,metrics.accuracy_score(y_test,yp)))
    return res

def makeVotes(electors,X_test,Y_test):
    Xp = []
    i = 0
    for d in X_test.values:
        P_i = []
        for t in electors:
            P_i.append(t[0].predict([d])[0])
        # print(str(P_i)+' : '+str(max(set(P_i), key=P_i.count))+' : '+str(Y_test.values[i]))
        Xp.append(max(set(P_i), key=P_i.count))
        i+=1
    return metrics.accuracy_score(Y_test,Xp)

def estimatePrediction(clf,Xt,Yt,X_test,labels):
    clf.fit(Xt,Yt)
    Ans = clf.predict(X_test)
    a = metrics.accuracy_score(labels,Ans)
    return a

# read data and extract X, y.
X = pd.read_csv('datasets/train.csv') # classes: [0,1,2,3]. column: price_range
print('Features: '+str(len(X.columns)))
print(list(X.columns)) # 20 features (columns) + target feature.
target = X['price_range'] # y.
X.drop('price_range', axis=1, inplace=True) # drop y from X.
print(X.head())
print('\n')
print('Create fitted classifiers (trees)')

# scaling.
mms = MinMaxScaler()
mms.fit(X)
X = pd.DataFrame(mms.transform(X),columns=X.columns)


X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.3, random_state=1) # 70% training and 30% test
electors = randomForest(X,target,10,0.3,0)
score1 = 0
for t in electors:
    print(t[1])
    score1+=t[1]
score1 = score1/len(electors)

a = makeVotes(electors,X_test,y_test)

tree = DecisionTreeClassifier(criterion='entropy',random_state=0)
tree.fit(X_train,y_train)
a0 = metrics.accuracy_score(y_test,tree.predict(X_test))
print('Single tree accuracy: '+str(a0))
print('Accuracy of random forest: '+str(a))
print('Mean(score): '+str(score1))
print('\n')
print('Libraries methods:\n')
clf0 = DecisionTreeClassifier(criterion='entropy', random_state=0)
scores = cross_val_score(clf0,X,target,scoring='accuracy', cv=10)
print("Decision Tree: "+str(scores.mean()))
clf1 = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
scores = cross_val_score(clf1,X,target, scoring='accuracy', cv=10)
print("Random forest: "+str(scores.mean()))
clf2 = ExtraTreesClassifier(n_estimators=100, max_depth=None,min_samples_split=2, random_state=0)
scores = cross_val_score(clf2, X, target, scoring='accuracy', cv=10)
print("ExtraTree: "+str(scores.mean()))
clf3 = AdaBoostClassifier(n_estimators=25)
scores = cross_val_score(clf3,X,target, scoring='accuracy', cv=10)
print('AdaBoost: '+str(scores.mean()))



eclf = VotingClassifier( estimators=[('dt',clf0),('rf', clf1), ('et', clf2), ('adb', clf3)],voting='hard')
for clf, label in zip([clf0,clf1, clf2, clf3, eclf], ['Decision Tree','Random Forest', 'Extra tree', 'AdaBoost', 'Ensemble']):
    scores = cross_val_score(clf, X, target, scoring='accuracy', cv=10)
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))
    print('Accurancy_score: '+str(estimatePrediction(clf,X_train,y_train,X_test,y_test))+' :: '+label)
