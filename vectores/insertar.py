
def insertar(arreglo,valor,posicion, cantidad_elementos,cantidad_maxima,valor_min,valor_max):
    nueva_cantidad = cantidad_elementos
    if (cantidad_elementos < cantidad_maxima and posicion >= 0 and posicion < cantidad_elementos and
            valor >= valor_min and valor <= valor_max):
        for i in range(cantidad_elementos,posicion,-1):
            arreglo[i] = arreglo[i - 1]
        arreglo[posicion] = valor
        nueva_cantidad = cantidad_elementos + 1
    return  nueva_cantidad