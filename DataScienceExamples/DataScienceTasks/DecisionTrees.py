from collections import defaultdict
from functools import partial
from collections import Counter
import pandas as pd
import random
import math
def entropy(probabilities):
    return sum(-p * math.log(p,2) for p in probabilities if p)

def class_probabilities(labels):
    t_count = len(labels)
    return [count / t_count for count in Counter(labels).values()]


def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    total_count = sum(len(subsets[subset]) for subset in subsets)
    return  sum(data_entropy(subsets[subset]) * len(subsets[subset]) / total_count for subset in subsets)


def partition_by(inputs,attribute):
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]
        groups[key].append(input)
    return groups

def partition_entropy_by(inputs,attribute):
    partitions = partition_by(inputs,attribute)
    return partition_entropy(partitions)



def classify(tree,input):
    if tree in [True,False]:
        return tree
    attribute, subtree_dict = tree

    subtree_key = input.get(attribute)
    if subtree_key not in subtree_dict:
        subtree_key = None
    subtree = subtree_dict[subtree_key]
    return classify(subtree,input)


def build_tree_id3(inputs,split_candidates=None):
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues
    if num_trues == 0:
        return False
    if num_falses == 0:
        return True
    if not split_candidates:
        return num_trues >= num_falses
    best_attribute = min(split_candidates, key=partial(partition_entropy_by,inputs))
    partitions = partition_by(inputs,best_attribute)
    new_candidates = [a for a in split_candidates if a!= best_attribute]
    subtrees = {attribute_value: build_tree_id3(subset,new_candidates) for attribute_value, subset in list(partitions.items())}
    subtrees[None] = num_trues > num_falses
    return (best_attribute,subtrees)



# create data_set
a1 = [0, 0.5, 1, 2, 4, 10]
a2 = ['yes','no']
a3 = ['Project Manager','Programmer','Tech support','Team leader','Tech administrator']
a4 = ['yes', 'no']
a5 = [0, 1, 2, 5, 7, 10]
a6 = [40000,60000,80000,100000]
a7 = [True, False]
for epo in range(0,10):
    data_set_labeled = []
    data_set_train = []
    for i in range(0,10000):
        s = {}
        random.shuffle(a1)
        random.shuffle(a2)
        random.shuffle(a3)
        random.shuffle(a4)
        random.shuffle(a5)
        random.shuffle(a6)
        random.shuffle(a7)
        c_exp = random.choice(a1)
        s['current_exp'] = c_exp
    #    s['tweets'] = random.choice(a2)
        s['job'] = random.choice(a3)
        s['Magister'] = random.choice(a4)
        exp = random.choice(a5)
        s['Experience'] = exp
        salary = random.choice(a6)
        s['Salary'] = salary
        item = (s, random.choice(a7)) if salary < 100000 and exp != 0 and c_exp >= 0.5 else (s, False)
        data_set_train.append(item)
        # data_set_labeled.append(item)
    for j in range(0,10000):
        s = {}
        random.shuffle(a1)
        random.shuffle(a2)
        random.shuffle(a3)
        random.shuffle(a4)
        random.shuffle(a5)
        random.shuffle(a6)
        random.shuffle(a7)
        c_exp = random.choice(a1)
        s['current_exp'] = c_exp
     #   s['tweets'] = random.choice(a2)
        s['job'] = random.choice(a3)
        s['Magister'] = random.choice(a4)
        exp = random.choice(a5)
        s['Experience'] = exp
        salary = random.choice(a6)
        s['Salary'] = salary
        item = (s, random.choice(a7)) if salary < 100000 and exp != 0 and c_exp >= 0.5 else (s, False)
        data_set_labeled.append(item)

    tree = build_tree_id3(data_set_train)
    correct = 0
    for item in data_set_labeled:
        answer = classify(tree,item[0])
        # print('Predicted: '+str(answer)+' --- Actual: '+str(item[1]))
        if item[1] == answer:
            correct = correct + 1
    print(str(epo)+':  Precision: '+str(correct / len(data_set_labeled))+' ( '+str(correct)+' from '+str(len(data_set_labeled))+' )')

    # print(tree)