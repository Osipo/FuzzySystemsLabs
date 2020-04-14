from matplotlib import pyplot as plt
from DataScienceExamples.FunctionalFun.Distributions import normal_pdf
from DataScienceExamples.FunctionalFun.Distributions import normal_cdf
xs = [x / 10.0 for x in range(-50,50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu = 0, sigma = 1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'-',label='mu = 0, sigma = 2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],'-',label='mu = 0, sigma = 0.5')
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu = 0, sigma = 1')

plt.legend()
plt.title('DFR of normal Distribution')
plt.show()

plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu = 0, sigma = 1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'-',label='mu = 0, sigma = 2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],'-',label='mu = 0, sigma = 0.5')
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu = 0, sigma = 1')
plt.legend(loc=4)
plt.title('IFR of normal Distribution')
plt.show()