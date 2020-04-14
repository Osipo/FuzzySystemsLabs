from DataScienceExamples.FunctionalFun.Distributions import binominal
from DataScienceExamples.FunctionalFun.Distributions import normal_cdf
from DataScienceExamples.FunctionalFun.Distributions import bernoulli_trial
from matplotlib import pyplot as plt
from collections import Counter
import mpmath
def make_list(p,n,num_points):
    data = [binominal(n,p) for _ in range(num_points)]
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in list(histogram.keys())],
            [v/num_points for v in  list(histogram.values())]
            ,0.8,color='0.75')
    mu = p * n
    sigma = mpmath.sqrt(n * p * (1 - p))
    xs = range(min(data),max(data)+1)
    ys = [normal_cdf(i+0.5,mu,sigma) - normal_cdf(i-0.5,mu,sigma) for i in xs]
    plt.plot(xs,ys)
    plt.title('Binominal and Normal Distribution')
    plt.show()
make_list(0.75,100,10000)