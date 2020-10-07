El problema de interpolación: 

Dados n + 1 puntos (xi; yi) \in R^2; x_i \neq x_j, i, j = 0, 1, ..., n, existe un único polinomio de grado a lo más n tal que:

p(x) = c_0x^0 + c_1x^1 + ... + c_nx^n

para p(x_i) = y_i, i = 0, 1, ..., n. 

El problema de interpolación con puntos igualmente espaciados es un problema mal condicionado ya que su solución involucra a la matriz de
Vandermonde. Para esto, construya un sistema de ecuaciones lineales a partir de las condiciones de interpolación.
Escriba un programa en phyton para construir la matriz de coeficientes y resolver el sistema resultante.
