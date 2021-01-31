from pyrecord import Record
import random
import numpy as np

# Define el registro como tipo de datos
Nota = Record.create_type("Nota","alumno","nota1","nota2", 
            "nota3",alumno = '',nota1 = 0,nota2 = 0,nota3 = 0)


def cargar(vector,archivo):
    archivo = open(archivo, 'r')
    contador_de_lineas = 0
    for linea in archivo:
        vector[contador_de_lineas] = Nota()
        carga_aleatoria(vector[contador_de_lineas],linea.rstrip('\n'))
        contador_de_lineas += 1
    archivo.close
    return contador_de_lineas,vector



def carga_aleatoria(registro, nombre):
    registro.alumno = nombre
    registro.nota1 = random.randint(1,10)
    registro.nota3 = random.randint(1,10)
    registro.nota2 = random.randint(1,10)

def mostrar_registro(registro):
    print("Nombre : ",registro.alumno, " | Nota 1 : ",registro.nota1," | Nota 2 : ",registro.nota2," | Nota 3 : ",registro.nota3, " |")

def mostrar_registro_2(registro,valor_adicional):
    print("Nombre : ",registro.alumno, " | Nota 1 : ",registro.nota1," | Nota 2 : ",registro.nota2," | Nota 3 : ",registro.nota3, " | ",valor_adicional, " | ")


def mostrar_en_rango(vector,minimo,maximo,elementos,etiqueta):
    print(" ------ Los que ",etiqueta," son ------------------------------")
    for n in range(elementos):
        promedio = (vector[n].nota1 + vector[n].nota2 + vector[n].nota3 ) / 3
        if (promedio >= minimo and promedio < maximo):
            mostrar_registro_2(vector[n],promedio)

def main():
    cantidad_maxima = 100
    cant_real = 0  

    # Define un vector de 100 elementos de tipo Nota pero vacio
    notas = np.empty([cantidad_maxima,], dtype=Nota)
    # Pedir que se cargue el vector con los datos del archivo
    cant_real,notas = cargar(notas,"alumnos.txt")
    # Mostrar el vector
    for i in range(cant_real):
        mostrar_registro(notas[i])

    # Calcular Quines quedaron Integrando
    mostrar_en_rango(notas,6,11,cant_real,"integran")

    # Calcular Quines quedaron Integrando
    #mostrar_regular(notas,cant_real)
    mostrar_en_rango(notas,4,6,cant_real,"quedan regulares")

    # Calcular Quines quedaron Integrando
    #mostrar_libres(notas,cant_real)
    mostrar_en_rango(notas,1,4,cant_real,"quedan libres")
    
    #dato_tipo_nota = Nota()
    #carga_aleatoria(dato_tipo_nota,"Juan Perez")
    #mostrar_registro(dato_tipo_nota)


main()





