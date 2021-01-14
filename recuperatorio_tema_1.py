# Recuperatorio del Segundo Parcial
# Alumno : 

from pyrecord import Record
import numpy as np
import random

# Estructura
Evaluacion = Record.create_type("Evaluacion","legajo","nombre", "trabajo_practico","presentacion","exposicion","calidad",
                        legajo = 0,nombre = '',trabajo_practico = 0,presentacion = 0, exposicion = 0, calidad = 0)


# Procedimientos y Funciones Accesorias
def imprimir_vector(vector, elementos):
    print('{0:>4s} {1:6s} {2:15s} {3:^5s} {4:>12s} {5:>12s} {6:>12s}'.format("#","Legajo","Nombre", "TP","Presentación","Exposición","Calidad"))
    print('     --------------------------------------------------------------------')
    for i in range(elementos):
        if(vector[i]!= None):
            print('{0:4d} {1:6d} {2:15s} {3:5d} {4:12d} {5:12d} {6:12d}'.format(i + 1, vector[i].legajo,vector[i].nombre,vector[i].trabajo_practico,
                                                                     vector[i].presentacion,vector[i].exposicion,vector[i].calidad))

#Generar datos aleatorios
def cargar_datos(vector,alumnos):
    registro = 0
    tps = [8,5,6,4,1,3,2,7]
    for i in range(alumnos):
        legajo = random.randint(1,alumnos)
        nombre = "Estudiante " + str(legajo).zfill(2)
        for tp in range(random.randint(3,8)):
            vector[registro] = Evaluacion()
            vector[registro].legajo = legajo
            vector[registro].nombre = nombre
            vector[registro].trabajo_practico = tps[tp]
            vector[registro].presentacion = random.randint(1,10)
            vector[registro].exposicion = random.randint(1,10)
            vector[registro].calidad = random.randint(1,10)
            registro += 1
    return registro 

# ------ INSERTAR AQUI SU RESOLUCION --------

# ------ punto 1 --------

def  insertar_en(vector, value, pos, cant_elementos):
    #len(vector) < 
    if(cant_elementos and pos >= 0):
        #vector.insert(pos,value) Modo Correcto
        for i in range(1, pos, -1):
            vector[i] = vector[i - 1]
            vector[pos] = value
        #nueva_cantidad = cant_elementos + 1
        #return  nueva_cantidad
    else:
        print("no se pueden insertar mas de " + str(cant_elementos) + " registros")

# ------ punto 2 --------

def promedio_notas(vector, length):
    i = 0
    while i < length and vector[i] != None:
        nombre = vector[i].nombre
        tp = vector[i].trabajo_practico
        promedio = 0
        while  i < length and vector[i] != None and vector[i].nombre == nombre and vector[i].trabajo_practico == tp:
            promedio = (vector[i].presentacion + vector[i].exposicion + vector[i].calidad) / 3
            i+= 1
            if(vector[i] != None):
                print("Legajo: ",str(vector[i].legajo)," ",vector[i].nombre)
                print("TP N° ",tp, " Promedio ",promedio) 

# ------ punto 3 --------

# ------ punto 4 --------

# -------------------------------------------

# Procedimiento Principal
def main():
    max_elementos = 1000
    notas = np.empty([max_elementos,], dtype=Evaluacion)
    cant_real = cargar_datos(notas,30)
    imprimir_vector(notas,10)

    #Paso el registro
    registro = Evaluacion()
    registro.legajo = 1234
    registro.nombre = 'Alvaro'
    registro.trabajo_practico = 2
    registro.presentacion = random.randint(1,10)
    registro.exposicion = random.randint(1,10)
    registro.calidad = random.randint(1,10)
    insertar_en(notas, registro, 10, max_elementos)
    promedio_notas(notas, max_elementos)
    imprimir_vector(notas, max_elementos)
    # ------ INSERTAR AQUI LOS LLAMADOS A SU RESOLUCION ---





    # -----------------------------------------------------
    

if __name__ == "__main__":
    main()