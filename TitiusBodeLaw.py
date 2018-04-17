from numpy import *
import scipy.optimize as op
import matplotlib.pyplot as plt

data = loadtxt('planetdistances.dat')
n = data[:,0]
a = data[:,1]

def TitiusBode(n, p, q):
  return p + q*2**n
  
seed = [0.0, 0.0]

par, cov = op.curve_fit(TitiusBode, n, a, seed)
p, q = par[0], par[1]
print p, q

plt.scatter(n, TitiusBode(n, p, q))
plt.xlim(0.5, 10.0)
plt.ylim(0.0, 50.0)
plt.xlabel('planet index (n)')
plt.ylabel('distance from Sun (AU)')
plt.title('Modified Titius-Bode Law')
plt.ticks(arange(0.5, 10.0, 1.0))
plt.show()
