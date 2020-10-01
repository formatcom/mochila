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
