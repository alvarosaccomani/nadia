import mostrar

def buscar_nota_mas_alta(notas,elementos):
    nota_mas_alta = -1
    for alumno in range(elementos):
        if (notas[alumno] > nota_mas_alta):
            nota_mas_alta = notas[alumno]

    return nota_mas_alta

def mostrar_alumnos_con_notas_mas_altas(nota, alumnos, notas, cantidad_de_elementos):
    #mostrar el arreglo
    mostrar.mostrar_titulo("Estudiantes con la nota mas alta")
    print(mostrar.centar("ID",3) + " " + mostrar.izquierda("Estudiante",40) + " " + mostrar.derecha("Nota",5))
    print(mostrar.linea(78))
    for i in range(cantidad_de_elementos):
        if (nota == notas[i]):
            print(mostrar.derecha(str(i + 1),3) + " - " + mostrar.izquierda(alumnos[i],40) + " " + mostrar.derecha(str(notas[i]),5))

