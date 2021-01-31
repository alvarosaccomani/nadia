import random
import mostrar


def carga_aleatoria_int(arreglo,cantidad_de_elementos,minimo,maximo):
    for i in range(cantidad_de_elementos):
        arreglo[i] = random.randint(minimo,maximo)

def leer_vector(nombre_archivo, vector,tipo):
    archivo = open(nombre_archivo, 'r')
    i = 0
    for linea in archivo:
        if tipo == 'N':
            vector[i] = int(linea)
        else:
            vector[i] = linea.rstrip('\n')
        print(vector[i])
        i += 1
    archivo.close()
    return i

def mostrar_informacion(arreglo1, arreglo2, cantidad_de_elementos):
    #mostrar el arreglo
    mostrar.mostrar_titulo("Listado de Estudiantes")
    print(mostrar.centar("ID",3) + " " + mostrar.izquierda("Estudiante",40) + " " + mostrar.derecha("Nota",5))
    print(mostrar.linea(78))
    for i in range(cantidad_de_elementos):
        print(mostrar.derecha(str(i + 1),3) + " - " + mostrar.izquierda(arreglo1[i],40) + " " + mostrar.derecha(str(arreglo2[i]),5))



