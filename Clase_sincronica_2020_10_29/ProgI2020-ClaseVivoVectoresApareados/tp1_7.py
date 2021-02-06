import random
import numpy as np
import string

ALPHABET = np.array(list(string.ascii_lowercase))


def generate_guess(elementos):
    return np.random.choice(ALPHABET, size=5)

def cargar(vector,elementos):
    for i in range(elementos):
        vector[i]=generate_guess(elementos)


def mostrar(vector,elementos):
    for i in range(elementos):
        print(vector[i],end= " | ")
    print(" ")

def frecuencia(vector,elementos):
    vector_de_fecuencias = [1] * 95
    for edades in range(elementos):
        edad = edad[edades]
        vector_de_fecuencias[edad] += 1
    
    maximo = 0
    posicion = 0
    for i in range(11):
        if (maximo < vector_de_fecuencias[i]):
            maximo = vector_de_fecuencias[i]
            posicion = i
    
    return posicion
pass
def main():

    elementos=4
    vector=[None]*elementos
    cargar(vector,elementos)
    mostrar(vector,elementos)



if __name__ == "__main__":
    main()