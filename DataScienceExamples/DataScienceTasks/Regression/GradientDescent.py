import random
from DataScienceExamples.FunctionalFun.Vectors import *
def step(v,direction,size):
    return [v_i + direction_i*size for v_i, direction_i in zip(v,direction)]

def safe(f):
    def safe_f(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return float('inf')
    return safe_f

def negate(f):
    return lambda *args, **kwargs: -f(*args,**kwargs)
def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args,**kwargs)]
def random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]

def minimaize_batch(target_f,gradient_f,theta_0,tolerance=0.00001):
    step_sizes = [100,10,1,0.1,0.01,0.001,0.0001,0.00001]
    theta = theta_0
    target_f = safe(target_f)
    value = target_f(theta)
    while True:
        gradient = gradient_f(theta)
        next_thetas = [step(theta,gradient,-size_i) for size_i in step_sizes]
        next_theta = min(next_thetas, key=target_f)
        next_value = target_f(next_theta)
        if(abs(value - next_value) < tolerance):
            return theta
        else:
            theta,value = next_theta,next_value

def minimaize_stohastic(target_f,gradient_f,x,y,theta_0,alpha_0=0.01):
    data = zip(x,y)
    theta = theta_0
    alpha = alpha_0
    min_theta,min_value = None,float("inf")
    iteration_with_no_improvement = 0
    while iteration_with_no_improvement < 100:
        value = sum(target_f(x_i,y_i,theta) for x_i,y_i in data)
        if value < min_value:
            min_theta,min_value = theta,value
            iteration_with_no_improvement = 0
            alpha = alpha_0
        else:
            alpha*=0.9
            iteration_with_no_improvement+=1
            for x_i,y_i in random_order(data):
                gradient_i = gradient_f(x_i,y_i,theta)
                theta = vector_sub(theta,vector_scalar_mul(alpha,gradient_i))
    return min_theta

def maximaize_batch(target_f,gradient_f,theta_0,tolerance=0.00001):
    return minimaize_batch(negate(target_f),
                           negate_all(gradient_f),
                           theta_0,tolerance)

def maximaize_stohastic(target_f,gradient_f,x,y,theta_0,alpha_0=0.01):
    return minimaize_stohastic(negate(target_f),
                           negate_all(gradient_f),
                           x,y,theta_0,alpha_0)
