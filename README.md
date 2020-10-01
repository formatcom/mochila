~~~
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
~~~

~~~
W = [  2,  5,  1,  6,  2]
U = [ 28, 33,  5, 12, 20]

N = len(W)  # numero de objetos
M = 5       # peso maximo


[ 1 1 ] 2  0 -1 28  0 False  True
[ 1 2 ] 2  0  0 28  0  True  True
[ 1 3 ] 2  0  1 28  0  True  True
[ 1 4 ] 2  0  2 28  0  True  True
[ 1 5 ] 2  0  3 28  0  True  True
[ 2 1 ] 5 28 -4 61  0 False  True
[ 2 2 ] 5 28 -3 61 28 False  True
[ 2 3 ] 5 28 -2 61 28 False  True
[ 2 4 ] 5 28 -1 61 28 False  True
[ 2 5 ] 5  0  0 33 28  True  True
[ 3 1 ] 1  0  0  5  0  True  True
[ 3 2 ] 1  0  1  5 28  True False
[ 3 3 ] 1 28  2 33 28  True  True
[ 3 4 ] 1 28  3 33 28  True  True
[ 3 5 ] 1 28  4 33 33  True False
[ 4 1 ] 6  5 -5 17  5 False  True
[ 4 2 ] 6 28 -4 40 28 False  True
[ 4 3 ] 6 33 -3 45 33 False  True
[ 4 4 ] 6 33 -2 45 33 False  True
[ 4 5 ] 6 33 -1 45 33 False  True
[ 5 1 ] 2 33 -1 53  5 False  True
[ 5 2 ] 2  0  0 20 28  True False
[ 5 3 ] 2  5  1 25 33  True False
[ 5 4 ] 2 28  2 48 33  True True
[ 5 5 ] 2 33  3 53 33  True True

[0, 0,  0,  0,  0,  0]
[0, 0, 28, 28, 28, 28]
[0, 0, 28, 28, 28, 33]
[0, 5, 28, 33, 33, 33]
[0, 5, 28, 33, 33, 33]
[0, 5, 28, 33, 48, 53]

53
~~~
