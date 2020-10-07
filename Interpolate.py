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

intervalo = np.linspace(-1,1,101)
vander_matrix = np.vander(intervalo)


print("Número de condición 1: ", la.cond(vander_matrix,1))
print("Número de condición 2: ", la.cond(vander_matrix,2))
print("Número de condición infinito: ", la.cond(vander_matrix, np.infty))
pprint(vander_matrix)

pl.plot(intervalo, _interpolate(intervalo))
pl.savefig("interpolacion")
pl.show()
