from numpy import *
import scipy.optimize as op
import matplotlib.pyplot as plt

data = loadtxt('planetdistances.dat')
n = data[:,0]
a = data[:,1]

x = arange(0.0, 10.0, 0.10)

def distance(n, p, q):
  return p + q*2**n
  
seed = [0.0, 0.0]

par, cov = op.curve_fit(distance, n, a, seed)
p, q = par[0], par[1]
print p, q

plt.scatter(n, distance(n, p, q))
plt.plot(x,distance(x, p, q), 'r-')
plt.xlim(0.5, 10.0)
plt.ylim(0.0, 50.0)
plt.xlabel('planet index (n)')
plt.ylabel('distance from Sun (AU)')
plt.ticks(arange(0.5, 10.0, 1.0))
plt.show()
