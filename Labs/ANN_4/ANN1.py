from PIL import Image
from ANNs.LAB_1_Alphabetic.Vectors import *
from sklearn import datasets
import random
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
from keras.utils import np_utils
from Labs.ANN_4.PoliceData import X
# Resolver
def resolver(x): # sigmoid
    return 1 / ((1 + math.exp(-x)))

def softMax(x):
    return sum(math.exp(xi)/(sum(math.exp(xi) for xi in x)) for xi in x)
def logMax(x):
    return sum(resolver(xi) for xi in x)

# Neuron_output.
def neuron_output(W,X):
    return resolver(dot(W,X))

def neuron_output2(W,X):
    return softMax(vector_mul(W,X))

# Returns outputs from all layers.
def feed_forward(network, input):
    Y = []
    input_with_offset = input + [1]
    for layer in network:
        output = [neuron_output(neuron,input_with_offset) for neuron in layer] # for each neuron compute output.
        Y.append(output)

        input_with_offset = output

    return Y

# Get result
def predict(net,x):
    return feed_forward(net,x)[-1]


def backpropagate(net,input,targets):
    hidden_outputs, outputs = feed_forward(net,input)
    output_deltas = [output * (1 - output) * (output - target) for output,target in zip(outputs,targets)]

    for i, oneuron in enumerate(net[-1]):
        for j, h in enumerate(hidden_outputs + [1]):
            oneuron[j] -= output_deltas[i] * h

    hidden_deltas = [hidden_output *
                        (1 - hidden_output) *
                        dot(output_deltas, [n[i] for n in net[-1]]) for i, hidden_output in enumerate(hidden_outputs)]

    for i, hneuron in enumerate(net[0]):
        for j, x in enumerate(input + [1]):
            hneuron[j] -= hidden_deltas[i] * x

t_attr = 'race'

# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(X[t_attr].values) # make them in vector form [0,0,0,0,1,0,0] class 4
X.drop(t_attr,axis=1,inplace=True)
Y = dummy_y

XD = X.values
l, il = XD.shape;
print(str(l)+" , "+str(il))
print("+++++++++++++++++++  PREDICTING ++++++++++++++++++++++++++++")
XTAR = Y
tp = 0
targets = [[1 if i == j else 0 for i in range(0,7)] for j in range(0,7)] # Correct output.
olen = 7
num_hidden = 8 # neurons in hidden layer
hidden_layer = [   [random.random() for _ in range(il + 1)] for _ in range(num_hidden)] # for each neuron add random weights.

# for each output neuron add random weights from each neuron of the hidden_layer
output_layer = [  [random.random() for _ in range(num_hidden + 1)] for _ in range(olen)]

network = [hidden_layer, output_layer]

print("=== Network is beign learned by inputs...===")
for iteration in range(0,1000):
    print(iteration + 1)
    for input_vector,target_vector in zip(XD,targets):
        backpropagate(network,input_vector,target_vector)


for i in range(0,l):
   ans = predict(network,XD[i])
   exp = np.where(XTAR[i] == 1)[0][0]
   real = ans.index(max(ans))
   print("Predicted: "+str(real)+"  Target: "+str(exp))
   if(real == exp):
       tp+=1
fp = l - tp
print("TP: "+str(tp))
print("FP: "+str(fp))
print("From: "+str(l))