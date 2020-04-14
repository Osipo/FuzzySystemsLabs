import mpmath
import random
"""Probability density function (pdf)
Is x in[0..1)"""
def uniform_pdf(x):
    return 1 if x>=0 and x<1 else 0

"""Cumulative distribution function (cdf)
P (X<=x)
"""
def uniform_cdf(x):
    if x<0: return 0
    elif x<1: return x
    else: return 1

"""Normal distribution function
mu = mean(x), sigma = sqrt(variance(x)) = Standard deviasion
"""
def normal_pdf(x, mu=0,sigma=1):
    pi2sqrt = mpmath.sqrt(2*mpmath.pi) #root 2pi
    return (mpmath.exp(-(x-mu)**2/2/sigma**2))/(pi2sqrt*sigma) # 1/(root 2pi*sigma) * e degree(-(x-u)^2 / 2*sigma^2)

"""Integral Distribution Function"""
def normal_cdf(x, mu=0,sigma=1):
    return(1+mpmath.erf((x-mu)/mpmath.sqrt(2)/sigma))/2

"""Inverse Integral Distribution Function"""
def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
    if mu!=0 or sigma!=1:
        return mu+sigma*inverse_normal_cdf(p,tolerance=tolerance)
    low_z,low_p = -10.0,0 # normal_cdf(-10)
    high_z,high_p = 10.0,1 # normal_cdf(10)

    while high_z-low_z > tolerance:
        midle_z = (low_z+high_z)/2
        mid_p = normal_cdf(midle_z)
        if mid_p < p:
            low_z,low_p = midle_z,mid_p
        elif mid_p > p:
            high_z,high_p = midle_z,mid_p
        else:
            break
    return midle_z

def bernoulli_trial(p): # 0 for p and 1 for 1-p.
    return 1 if random.random() < p else 0

def binominal(n,p):
    sum(bernoulli_trial(p) for _ in range(n))