def step(v,direction,step_size):
    return [v_i+direction_i*step_size for v_i,direction_i in zip(v,direction)]

def safe(f):
    def safe_f(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return float('inf')
    return safe_f

def minimize_batch(target_f,gradient_F,theta_0,tolerance=0.000001):
    step_sizes = [100,10,1,0.1,0.01,0.001,0.0001,0.00001]
    theta = theta_0
    target_f = safe(target_f)
    value = target_f(theta_0)

    while True:
        gradient = gradient_F
        next_thetas = [step(theta,gradient,-step_size) for step_size in step_sizes]

        next_theta = min(next_thetas, key=target_f)
        next_value = target_f(next_theta)
        if(abs(value-next_value)) < tolerance:
            return theta
        else:
            theta,value = next_theta,next_value

def negate(f):
    return lambda *args,**kwargs: -f(*args,**kwargs)
def negate_all(f):
    return lambda *args,**kwargs: [-y for y in f(*args,**kwargs)]
def maximize_batch(target_f,gradient_F,theta_0,tolerance=0.000001):
    return minimize_batch(negate(target_f),negate_all(gradient_F),theta_0,tolerance)
