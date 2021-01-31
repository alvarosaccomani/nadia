
import random

filas = 10
columnas = 10
matriz = [[0] * columnas for i in range(filas)]

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = random.randint(1,1500)

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c],end=" ")
    print("")


#Calcluar el punto de silla
#Un punto de silla es un maxima de una fila que es minimo en la columna





