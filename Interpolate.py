from numpy.lib.function_base import append
import numpy.linalg as la
import numpy as np
import math
from pprint import pprint
import matplotlib.pyplot as pl

def _interpolate(p):
    n = p.copy()
    z_i = []
    for i in range(len(n)):
        z_i.append(math.pow(n[i],i)) 
    return la.solve(np.vander(n), z_i)

intervalo = np.linspace(-1,1,101) #Un conjunto de 101 datos igualmente distribuidos entre -1 y 1 

pl.plot(intervalo, _interpolate(intervalo))
pl.show()
