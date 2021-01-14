import menu_consola
import apareados
import punto_dos
import punto_cuatro
import ordenamiento_apareado

cantidad_maxima = 100
notas1 = [0] * cantidad_maxima
alumnos = [""] * cantidad_maxima
# matriz = [[0] * 3] * 1000
cant_real = apareados.leer_vector('alumnos.txt',alumnos,'T')
apareados.carga_aleatoria_int(notas1,cant_real,1,10)
opcion = 0

while opcion != 20:
    opcion = menu_consola.menu()
    if opcion == 1:
        apareados.mostrar_informacion(alumnos,notas1,cant_real)
    elif opcion == 2:
        # "- 2 - ¿Cuál fue la nota más alta?             "
        nota_alta = punto_dos.buscar_nota_mas_alta(notas1,cant_real)
        print("La nota mas alta fue : " + str(nota_alta))
    elif opcion == 3:
        # "- 3 - ¿Quienes obtuvieron una nota            "
        nota_alta = punto_dos.buscar_nota_mas_alta(notas1,cant_real)
        punto_dos.mostrar_alumnos_con_notas_mas_altas(nota_alta,alumnos,notas1,cant_real)

    elif opcion == 4:
        # "- 4 - ¿Cuál fue la nota de mayor frecuencia?  "
        nota_mayor_frecuencia = punto_cuatro.nota_mayor_frecuencia(notas1,cant_real)
        print("La nota que mas veces se repitió fue : ",nota_mayor_frecuencia)
        punto_dos.mostrar_alumnos_con_notas_mas_altas(nota_mayor_frecuencia,alumnos,notas1,cant_real)

        
    elif opcion == 5:
        # "- 5 - ¿Cuál fue la mediana de las notas?      "
        nota_mediana = ordenamiento_apareado.calcular_mediana(alumnos,notas1,cant_real)
        print(cant_real // 2)
        print("La nota mediana fue : ",nota_mediana)
        punto_dos.mostrar_alumnos_con_notas_mas_altas(nota_mediana,alumnos,notas1,cant_real)


    input("presione ENTER para continuar ....")

print("Gracias por usar el fabuloso programa!!!")