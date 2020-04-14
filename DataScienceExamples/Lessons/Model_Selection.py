import numpy as np
from sklearn import cross_validation
from sklearn import grid_search
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)
print(X_train)