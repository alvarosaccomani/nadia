# import random

# def carga_Aleatoria(vector,elementos):
#     for i in range(elementos):
#         vector[i]=random.randint(10,999)


# def centena(vector,elementos,n):
#     contador=0
#     for i in range (elementos):
#         menor=100*n
#         mayor=100*(n+1)
    
    
#         while vector[i]>=menor and vector[i]<mayor and i<=elementos:
#             contador+=1
#             i=i+1
#     return contador

# def mostrar(vector,elementos):
#         for i in range(elementos):
#             print('vector original '+str(vector[i]))
            




# elementos=10
# vector=[0]*elementos
# carga_Aleatoria(vector,elementos)
# mostrar(vector,elementos) 
# n=int(input('ingrese numero a buscar'))
# resultado=centena(vector,elementos,n)
# print('la cantidad es: ',resultado)



def carga_aleatoria(vector,elementos,vector_nombres):
    for linea in elementos:
        vector[linea] = Venta()
        sucursal = random.randint(1,14)
        nombre = vector_nombres[linea]
        monto_vendido = random.random() * 10000

        #cargo valores de las variables en registro de cada posicion en vector[linea]
        cargar_registro(vector[linea],nombre,sucursal, monto_vendido)

def cargar_registro(registro,nombre_vendedor,sucursal,monto):
    registro.vendedor = nombre_vendedor
    registro.sucursal = sucursal
    registro.total_vendido = monto

def imprimir_venta(registro,elementos):
    for i in range(elementos):
        print("Sucursal : ",registro.sucursal," | Vendedor : ",registro.vendedor, "| Venta del Mes : $ ","{0:.2f}".format(registro.total_vendido))

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



#el corte de control sirve 
def ventas_por_sucursal(vector,cantidad_de_registros):
    #total = vector[0].total_vendido  
    i = 0
    while i < cantidad_de_registros:
        sucursal = vector[i].sucursal
        total = 0
        while  i < cantidad_de_registros and vector[i].sucursal == sucursal:
            total += vector[i].total_vendido 
            i += 1
        print("-- El total vendido por la sucursal : ",sucursal,
            " es $ ","{0:.2f}".format(total))