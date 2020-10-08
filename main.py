import numpy as np
import csv

# objectos
# W = [  2,  5,  1,  6,  2]
# U = [ 28, 33,  5, 12, 20]
# N = len(W)  # numero de objetos
# M = 5       # peso maximo


W = 0      # peso
U = 0      # utilidad
N = 0      # numero de objetos
M = 0      # peso maximo

with open('input.csv', 'r') as f:
    data = np.array(list(csv.reader(f, delimiter=',')), dtype=int)

    N = data[0][0]
    M = data[0][1]

    data = data[1:]

    U = data[:, 0]
    W = data[:, 1]


# buffer (N+1) x (M+1)
R = [[0 for m in range(M+1)] for i in range(N+1)]

"""
R[x] <- x es el numero de objetos que ha introducido en orden

ej:
    - R[0] ningun objeto, todos los pesos a 0
    - R[1] se analiza el primer objeto de la lista,

        se introduce a la lista si se cumple que el peso (m) es
        mayor al peso del primer objeto en la lista y ademas este
        objeto tiene mas utilidad que el objeto que ya esta guardado
        en esta posición.

        NOTA: el valor guardado es la utilidad del objeto mas la utilidad
        del peso restante guardado anteriormente. U[i-1] + R[i-1][m-W[i-1]].

    - R[N] todos los objetos de la lista analizados.


R[x][y] <- y almacena la utilidad por peso, deacuerdo a el valor de x

 esto quiere decir que en R[N][M] tenemos la mejor solución, pero podemos
ver otras alternativas como R[N][5] para todos los objetos con peso max 5
"""

for i in range(1, N+1):
    for m in range(1, M+1):

        if W[i-1] <= m and U[i-1] + R[i-1][m-W[i-1]] > R[i-1][m]:
            R[i][m] = U[i-1] + R[i-1][m-W[i-1]]
        else:
            R[i][m] = R[i-1][m]

print(R[N][M])
