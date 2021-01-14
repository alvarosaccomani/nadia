# Repaso de Registros
# Ordenanamiento en Registros
# Ordenanamiento por dos claves
# Corte de control
from pyrecord import Record
import numpy as np
import random



Venta = Record.create_type("Venta","sucursal","vendedor","total_vendido",
                        sucursal = 0,vendedor = '',total_vendido = 0)
# Variables de control de longitud del vector
cantidad_maxima = 1000
cant_real = 0

# Definir un vector de tipo Venta
ventas_mes = np.empty([cantidad_maxima,], dtype=Venta)

# Cargamos el vector en forma aleatoria usando el archivo de alumnos y random
# para calcular sucursal y total
def carga_aleatoria(vector,nombre_archivo):
    indice = 0
    archivo = open(nombre_archivo,'r')
    for linea in archivo:
        vector[indice] = Venta()
        cargar_registro(vector[indice],linea.rstrip('\n'))
        indice += 1
    archivo.close()
    #registros = indice
    return indice #registros

def cargar_registro(registro,nombre_vendedor):
    registro.vendedor = nombre_vendedor
    registro.sucursal = random.randint(1,14)
    registro.total_vendido = random.random() * 10000

###########

def imprimir_venta(registro):
    print("Sucursal : ",registro.sucursal," | Vendedor : ",registro.vendedor, " | Venta del Mes : $ ","{0:.2f}".format(registro.total_vendido))

########## Burbuja Mejorada ###############
def ordenar_vector(vector,cantidad):
    se_hizo_un_cambio = True
    while se_hizo_un_cambio:
        se_hizo_un_cambio = False
        indice = 1
        while indice < cantidad:
            if vector[indice - 1].sucursal > vector[indice].sucursal:
                #swap 
                aux = vector[indice - 1]
                vector[indice - 1 ] = vector[indice]
                vector[indice] = aux
                se_hizo_un_cambio = True
            indice += 1

########## Burbuja Mejorada 2 Claves M ###############
def ordenar_vector_2M(vector,cantidad):
    se_hizo_un_cambio = True
    while se_hizo_un_cambio:
        se_hizo_un_cambio = False
        indice = 1
        while indice < cantidad:
            clave1 = str(vector[indice - 1].sucursal) + vector[indice - 1].vendedor
            clave2 = str(vector[indice].sucursal) + vector[indice].vendedor
            if clave1 > clave2:
                #swap 
                aux = vector[indice - 1]
                vector[indice - 1 ] = vector[indice]
                vector[indice] = aux
                se_hizo_un_cambio = True
            indice += 1

# 10PANESSI WALTER
# 1PANESSI WALTER

# 0001PANESSI WALTER
# 0010PANESSI WALTER

########## Burbuja Mejorada 2 Claves B ###############
def ordenar_vector_2B(vector,cantidad):
    se_hizo_un_cambio = True
    while se_hizo_un_cambio:
        se_hizo_un_cambio = False
        indice = 1
        while indice < cantidad:
            clave1 = str(vector[indice - 1].sucursal).zfill(4) + vector[indice - 1].vendedor.upper()
            clave2 = str(vector[indice].sucursal).zfill(4) + vector[indice].vendedor.upper()
            if clave1 > clave2:
                #swap 
                aux = vector[indice - 1]
                vector[indice - 1 ] = vector[indice]
                vector[indice] = aux
                se_hizo_un_cambio = True
            indice += 1

########## Burbuja Mejorada 2 Claves M ###############
def ordenar_vector_3M(vector,cantidad):
    se_hizo_un_cambio = True
    while se_hizo_un_cambio:
        se_hizo_un_cambio = False
        indice = 1
        while indice < cantidad:
            clave1 = vector[indice - 1].sucursal + vector[indice - 1].total_vendido
            clave2 = vector[indice].sucursal + vector[indice].total_vendido
            if clave1 > clave2:
                #swap 
                aux = vector[indice - 1]
                vector[indice - 1 ] = vector[indice]
                vector[indice] = aux
                se_hizo_un_cambio = True
            indice += 1

########## Burbuja Mejorada 2 Claves B ###############
def ordenar_vector_3B(vector,cantidad):
    se_hizo_un_cambio = True
    while se_hizo_un_cambio:
        se_hizo_un_cambio = False
        indice = 1
        while indice < cantidad:
            clave1 = str(vector[indice - 1].sucursal).zfill(4) + "{0:.2f}".format(vector[indice - 1].total_vendido).zfill(10)
            clave2 = str(vector[indice].sucursal).zfill(4) + "{0:.2f}".format(vector[indice].total_vendido).zfill(10)
            if clave1 > clave2:
                print(clave1)
                print(clave2)
                print()
                #swap 
                aux = vector[indice - 1]
                vector[indice - 1 ] = vector[indice]
                vector[indice] = aux
                se_hizo_un_cambio = True
            indice += 1

########## Burbuja Mejorada 2 Claves B ###############
def ordenar_vector_3C(vector,cantidad):
    se_hizo_un_cambio = True
    while se_hizo_un_cambio:
        se_hizo_un_cambio = False
        indice = 1
        while indice < cantidad:
            clave1 = str(vector[indice - 1].sucursal).zfill(4) + str(vector[indice - 1].total_vendido).zfill(20)
            clave2 = str(vector[indice].sucursal).zfill(4) + str(vector[indice].total_vendido).zfill(20)
            if clave1 > clave2:
                print(clave1)
                print(clave2)
                print()
                #swap 
                aux = vector[indice - 1]
                vector[indice - 1 ] = vector[indice]
                vector[indice] = aux
                se_hizo_un_cambio = True
            indice += 1

# Corte de Control
def ventas_por_sucursal(vector,cantidad):
    if cantidad > 0:
        sucursal = vector[0].sucursal
        total = vector[0].total_vendido    
        for i in range(1,cantidad):
            if vector[i].sucursal == sucursal:
                total += vector[i].total_vendido
            else:
                print("-- El total vendido por la sucursal : ",sucursal,
                      " es $ ","{0:.2f}".format(total))
                sucursal = vector[i].sucursal
                total = vector[i].total_vendido   
        print("-- El total vendido por la sucursal : ",sucursal,
                " es $ ","{0:.2f}".format(total))


# Corte de Control
def ventas_por_sucursal_mateo(vector,cantidad):
    if cantidad > 0:
        sucursal = vector[0].sucursal
        total = vector[0].total_vendido    
        for i in range(1,cantidad):
            if vector[i].sucursal == sucursal:
                total += vector[i].total_vendido
            else:
                print("-- El total vendido por la sucursal : ",sucursal,
                      " es $ ","{0:.2f}".format(total))
                sucursal = vector[i].sucursal
                total = vector[i].total_vendido   
            if i == cantidad - 1:
                print("-- El total vendido por la sucursal : ",sucursal,
                      " es $ ","{0:.2f}".format(total))

# Corte de Control CORRECTO!!!!
def ventas_por_sucursal_jp(vector,cantidad):
        #total = vector[0].total_vendido  
        i = 0
        while i < cantidad:
            sucursal = vector[i].sucursal
            total = 0
            while  i < cantidad and vector[i].sucursal == sucursal:
                total += vector[i].total_vendido  
                i += 1
            print("-- El total vendido por la sucursal : ",sucursal,
                " es $ ","{0:.2f}".format(total)) 

# 0: 1   100     sucursal = 1 / total = 100
# for
# 1: 1   200      total += 200  // total = 300
# 2: 1   105      total += 105  // total = 405
# 3: 2   108   Total de la sucursal 1 es 405 /// sucursal = 2 / Total = 108
# 4: 2   120      total += 120 // total = 228






cant_real = carga_aleatoria(ventas_mes,"alumnos.txt")
#print(' ------- Mostramos el vector ---------------')
#for i in range(cant_real):
#    imprimir_venta(ventas_mes[i])

# print(' ------- Mostramos Ordenado 1 ---------------')
# ordenar_vector(ventas_mes,cant_real)

# for i in range(cant_real):
#     imprimir_venta(ventas_mes[i])

print(' ------- Mostramos Ordenado 2 ---------------')
ordenar_vector_2B(ventas_mes,cant_real)

for i in range(cant_real):
    imprimir_venta(ventas_mes[i])

print(' ------- Calcular Ventas por Sucursal ---------------')
ventas_por_sucursal(ventas_mes,cant_real)


print(' ------- Calcular Ventas por Sucursal Mateo ---------------')
ventas_por_sucursal_mateo(ventas_mes,cant_real)


print(' ------- Calcular Ventas por Sucursal Juan Pablo ---------------')
ventas_por_sucursal_jp(ventas_mes,cant_real)

### EJERCICIO PARA HACER 
#Sucural 1
### Vendedor JUAN $ 1000 // mas de una vez en el vector
### Vendedor JOSE $ 1400
#Total = 2400
#Sucursal 2
### Vendedor Garcia $ 1000
### Vendedor Ignacio $ 1400
#Total = 2400




