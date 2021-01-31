def ordenar_vectores(alumnos,notas,elementos):
    se_hizo_intercambio = True
    while se_hizo_intercambio:
        se_hizo_intercambio = False
        i = 1
        while (i < elementos):
            if (notas[i - 1] > notas[i]):
                #swap
                swap1 = notas[i - 1]
                notas[i - 1] = notas[i]
                notas[i] = swap1

                swap2 = alumnos[i - 1]
                alumnos[i - 1] = alumnos[i]
                alumnos[i] = swap2
                se_hizo_intercambio = True

            i += 1

def calcular_mediana(alumnos,notas,elementos):
    ordenar_vectores(alumnos,notas,elementos)
    return notas[elementos // 2]
