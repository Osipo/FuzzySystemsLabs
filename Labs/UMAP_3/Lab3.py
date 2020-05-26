from matplotlib import pyplot as plt
from matplotlib.ticker import NullFormatter
from _functools import partial
from collections import OrderedDict
from time import time
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
import math
from math import nan
import pandas as pd
import random
from sklearn.metrics import silhouette_score
from umap import UMAP
import umap.plot
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split, GridSearchCV

import datashader.utils as utils
import datashader.transfer_functions as tf
import datashader as ds

# Map str unordered categorized attributes to numbers
uClassCount = 0

#Delete NaN values from DataFrame
def deleteNaN(X,replacement):
    if not(isinstance(replacement,int)):
        replacement = 0
    for col in X.columns:
        X[col] = X[col].fillna(replacement)
    return X

def mapUnorderedStrAttr(name_of_attr,X,enc):
    global uClassCount
    l = enc.fit_transform(X[name_of_attr].astype('str'))
    m = {label:index+uClassCount for index, label in enumerate(enc.classes_)}
    if not(m.pop('0',1) == 1):
        m['0'] = 0 # save NaN -> 0 mapped value.
    uClassCount += len(X[name_of_attr].unique())
    print(uClassCount)
    print(m)
    X[name_of_attr] = X[name_of_attr].replace(m)
    return X

def makeLabelColors(X,name_of_attr,m):
    return [m[l] for l in X[name_of_attr]]
def makeTarget(X,name_of_attr,classes):
    for c in classes.keys():
        X.loc[X[name_of_attr] == c,name_of_attr] = classes[c]
    return X

# Map date in format 'yyyy-mm-dd' to int number 'dddddddd' ('2015-02-15' -> 20150215)
def mapDateAttr(X):
    def _m(s):
        dp = s.split('-')
        if(len(dp) == 3):
            return int(str(dp[0] + dp[1] + dp[2]))
        else:
            return -1
    X['date'] = X['date'].apply(_m)
    return X

#Read and prepare data.
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
X = pd.read_csv('datasets/PoliceShooting2015.csv')
manners_of_dead = ['shot','shot and Tasered']
le = LabelEncoder()
print('Has NaN: '+str(X.isnull().values.any()))
X = deleteNaN(X,0)
X = mapUnorderedStrAttr('name',X,le)
X = mapUnorderedStrAttr('armed',X,le)
X = mapUnorderedStrAttr('city',X,le)
X = mapUnorderedStrAttr('state',X,le)
X = mapUnorderedStrAttr('gender',X,le)
X = mapUnorderedStrAttr('race',X,le)
X.drop('date',axis=1,inplace=True)
# sings_of_mental_illness AND body_camera are Boolean (0 or 1)
X['signs_of_mental_illness'] = X['signs_of_mental_illness'].replace({True: 1, False:0})
X['body_camera'] = X['body_camera'].replace({True:1,False:0})

X['manner_of_death'] = X['manner_of_death'].replace({'shot':0,'shot and Tasered':1})
X = mapUnorderedStrAttr('flee',X,le)
X = mapUnorderedStrAttr('threat_level',X,le)
# X = mapDateAttr(X)
print('Has NaN: '+str(X.isnull().values.any()))


print('Races')
print(X.groupby(['race'])['id'].count())
X.drop('id', axis=1, inplace=True)
print('Preprocessed X')
print(X.head()) #Total attributes: 13.
print("\n")

# {'A': 3486, 'B': 3487, 'H': 3488, 'N': 3489, 'O': 3490, 'W': 3491, '0': 0}
races = {0: 0,3486:1,3487: 2,3488:3,3489:4,3490:5,3491:6} # classify by race.
races_color = {3486: 'yellow',3487: 'brown',3488:'red',3489:'black',3490:'orange',3491:'gray',0:'blue'}
t_attr = 'race'
colors = makeLabelColors(X,'race',races_color)
X = makeTarget(X,'race',races)
print('X with classes for '+str(t_attr))
print(X.head())
print('Colors for Attr: '+str(t_attr))
print(colors)
print("\n")

reducers = [
    (TSNE, {"perplexity": 50}),
    (umap.UMAP, {"n_neighbors": 30, "min_dist": 0.2}),
]

Y = X['race'].values
X.drop('race',axis=1,inplace=True) # delete Y from X.
# scaling.
mms = MinMaxScaler()
mms.fit(X)
X = pd.DataFrame(mms.transform(X),columns=X.columns)
test_data = [
    (X,Y)
]
n_rows = len(test_data)
n_cols = len(reducers)
ax_index = 1
ax_list = []
dataset_names = ["Police-Fails"]
plt.figure(figsize=(10, 8))
plt.subplots_adjust(
    left=0.02, right=0.98, bottom=0.001, top=0.96, wspace=0.05, hspace=0.01
)

for data, labels in test_data:
    for reducer, args in reducers:
        start_time = time()
        embedding = reducer(n_components=2, **args).fit_transform(data)
        elapsed_time = time() - start_time
        ax = plt.subplot(n_rows, n_cols, ax_index)
        if isinstance(labels[0], tuple):
            ax.scatter(*embedding.T, s=10, c=labels, alpha=0.5)
        else:
            ax.scatter(*embedding.T, s=10, c=labels, cmap="Spectral", alpha=0.5)
        ax.text(
            0.99,
            0.01,
            "{:.2f} s".format(elapsed_time),
            transform=ax.transAxes,
            size=14,
            horizontalalignment="right",
        )
        ax_list.append(ax)
        ax_index += 1
plt.setp(ax_list, xticks=[], yticks=[])

for i in np.arange(n_rows) * n_cols:
    ax_list[i].set_ylabel(dataset_names[i // n_cols], size=16)
for i in range(n_cols):
    ax_list[i].set_xlabel(repr(reducers[i][0]()).split("(")[0], size=16)
    ax_list[i].xaxis.set_label_position("top")

plt.tight_layout()
plt.show()