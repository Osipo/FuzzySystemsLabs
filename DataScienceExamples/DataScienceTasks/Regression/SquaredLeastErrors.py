from DataScienceExamples.FunctionalFun.Statistics import *
def predict(alpha,beta,x_i):
    return beta*x_i + alpha
def error(alpha,beta,x_i,y_i):
    return y_i - predict(alpha,beta,x_i)
def squared_error(alpha,beta,x_i,y_i):
    return error(alpha,beta,x_i,y_i) ** 2
def squared_error_gradient(x_i,y_i,theta):
    alpha,beta = theta
    return [-2 * error(alpha,beta,x_i,y_i),
            -2 * error(alpha,beta,x_i,y_i)*x_i]


def squared_error_sum(alpha,beta,x,y):
    return sum(error(alpha,beta,x_i,y_i) ** 2 for x_i, y_i in zip(x,y))

def total_sum_of_squares(y):
    return sum(v ** 2 for v in deviasion(y))

#R_SQUARED = DETERMINATION COEFFICIENT. How much is it real.
def r_squared(alpha,beta,x,y):
    return 1.0 - (squared_error_sum(alpha,beta,x,y)/total_sum_of_squares(y))

def least_squares_fit(x,y):
    beta = correlation(x,y)*standard_deviation(y)/standard_deviation(x)
    alpha = mean(y) - beta*mean(x)
    return alpha,beta

