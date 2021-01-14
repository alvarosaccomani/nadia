import os
import mostrar

def busqueda_secuencial(arreglo,valor_a_buscar,cantidad_de_elementos):
    #Busqueda secuencial
    i = 0 #Indice
    respuesta = -1
    while (i < cantidad_de_elementos) and (arreglo[i] != valor_a_buscar):
        i +=  1
    if (i < cantidad_de_elementos):
        #devolver posicion
        respuesta = i

    return respuesta

def menu():
    opcion = '0'
    opciones = ['1','2','3','4','5','20']

    while (busqueda_secuencial(opciones,opcion,len(opciones)) < 0):
        os.system("clear") #en Windows es "cls"
        mostrar.mostrar_titulo("Menú de Opciones")
        print("- " + mostrar.izquierda("¿ Que quieres hacer ?",75) + "-")
        print(mostrar.linea(78))
        print("- " + mostrar.izquierda("1 - Mostrar la información registrada",75) + "-")
        print("- " + mostrar.izquierda("2 - ¿Cuál fue la nota más alta?",75) + "-")
        print("- " + mostrar.izquierda("3 - ¿Quienes obtuvieron una nota ? ",75) + "-")
        print("- " + mostrar.izquierda("4 - ¿Cuál fue la nota de mayor frecuencia?",75) + "-")
        print("- " + mostrar.izquierda("5 - ¿Cuál fue la mediana de las notas?",75) + "-")
        print(mostrar.linea(78))
        print("- " + mostrar.izquierda("- 20 - Salir ",75) + "-")
        print(mostrar.linea(78))
        opcion = input("Dime tu opción : ")

    return int(opcion)
