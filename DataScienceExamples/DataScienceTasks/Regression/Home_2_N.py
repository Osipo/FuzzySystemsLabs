import random
import numpy as np
from sklearn.linear_model import LinearRegression

#bo = a, b1 = b.
# 2(b0+b1x - y) derived

#Minimization of sum((bo + b1*x_i - y_i)^2) min b1,b0
def dfb0(b0,b1,x,y):
	return 2*(b0+b1*x-y)
# 2x(b0+b1x - y) expr
def dfb1(b0,b1,x,y):
	return 2*x*(b0+b1*x-y)

#Gradient on x_i, y_i
def estimate_gradient(x,y,beta):
    a = beta[0]
    b = beta[1]
    return [dfb0(a,b,x,y),dfb1(a,b,x,y)]

def randomize(data,related):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    if related is not None and len(related)==len(data):
        for i in indexes:
            yield data[i],related[i]
    else:
        for i in indexes:
            yield data[i]


def stepForSGD(x_i,y_i,beta,eta,f):
    return [beta[0]-eta*f(x_i,y_i,beta)[0], beta[1]-eta*f(x_i,y_i,beta)[1]]

def SGD(x,y,fgrad,beta,eta=0.001,iters=10000):
    for i in range(iters):
        # x = randomize(x) # shuffle X
        # y = randomize(y) # shuffle Y
        data2 = list(randomize(x,y))
        # data = zip(x,y)
        for x_i,y_i in data2:
            beta = stepForSGD(x_i,y_i,beta,eta,fgrad)
    return beta
x=[10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]
beta = [0,1]
coef = SGD(x,y,estimate_gradient,beta)
print(coef)
def prediction(x_i,coefs):
    return coefs[0]+coefs[1]*x_i
y_p = []
for x_i in x:
    y_p.append(prediction(x_i,coef))

regr = LinearRegression()
X = np.array(x).reshape(-1,1)
regr.fit(X,y)
y_pred = regr.predict(X)
print('Coefficients : \n')
print('B0 '+str(regr.intercept_))
print('B1 '+str(regr.coef_))
print(coef)
print(list(y_pred))
print(y_p)
