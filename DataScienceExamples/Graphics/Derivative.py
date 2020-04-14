from matplotlib import pyplot as plt
from DataScienceExamples.FunctionalFun.Vectors import difference_quotient
from functools import partial
def square(x):
    return x*x
def derivative(x):
    return 2 * x
derivative_estimate = partial(difference_quotient,square,h=0.00001)
xs = range(-10,10)
plt.plot(xs,[2*x for x in xs],'rx',label='Fact')
plt.plot(xs,[derivative(x) for x in xs],'b+',label='Mark')
plt.legend(loc=9)
plt.show()