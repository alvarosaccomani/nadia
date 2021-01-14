def nota_mayor_frecuencia(notas,elementos):
    vector_de_fecuencias = [0] * 11
    for alumno in range(elementos):
        nota = notas[alumno]
        vector_de_fecuencias[nota] += 1
    
    maximo = 0
    posicion = 0
    for i in range(11):
        if (maximo < vector_de_fecuencias[i]):
            maximo = vector_de_fecuencias[i]
            posicion = i
    
    return posicion


