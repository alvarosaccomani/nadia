def eliminar_por_posicion(vector,posicion_a_borrar,cantidad_elementos):
    nuevo_tamanio = cantidad_elementos
    if posicion_a_borrar < cantidad_elementos and posicion_a_borrar >= 0:
        for i in range(posicion_a_borrar,cantidad_elementos - 1):
            vector[i] = vector[i + 1]
        nuevo_tamanio = nuevo_tamanio - 1


    return nuevo_tamanio