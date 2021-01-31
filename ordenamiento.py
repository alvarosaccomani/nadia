def ordenar_seleccion(vector,elementos):
    for i in range(elementos - 1,0,-1):
        posicion = 0
        mayor = vector[0]
        for j in range(1,i + 1):
            if vector[j] > mayor:
                mayor = vector[j]
                posicion = j
        swap = vector[posicion]
        vector[posicion] = vector[i]
        vector[i] = swap

def ordenar_burbuja_mejorada(vector,elementos):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(0,elementos - 1):
            if vector[i] > vector[i + 1]:
                intercambio = True
                # intercambio
                swap = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = swap


def ordenar_insercion(vector,elementos):
    for i in range(1,elementos):
        j = i
        while (j > 0) and (vector[j - 1] > vector[j]):
            # intercambio
            swap = vector[j]
            vector[j] = vector[j - 1]
            vector[j - 1] = swap
            j = j - 1