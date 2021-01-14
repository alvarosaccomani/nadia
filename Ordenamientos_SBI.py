def ordenamiento_seleccion(arreglo,orden):
    for i in range(0,len(arreglo)): #recorro el arreglo
        #guardo la posicion actual 
        aux1= i
        for j in range(i+1,len(arreglo)): #recorro el arreglo buscando el menor
                if arreglo[j] < arreglo[aux1]: #comparo la actual con la siguiente buscando el menor
                    aux1= j #guardo la posicion del menor

        #realizo intercambio
        aux = arreglo[i]  
        arreglo[i] = arreglo[aux1]
        arreglo[aux1] = aux

def ordenamiento_insercion(arreglo,orden):
    for i in range(1,len(arreglo)): #RECORREMOS DE LA POSICION ACTUAL
        aux= arreglo[i] #AGARRO EL CONTENIDO DE LA POS ACTUAL
        j = i 
        while j>0 and arreglo[j-1]>aux: #COMPARO ACTUAL CON ANTERIOR
            arreglo[j]=arreglo[j-1] #REALIZO DESPLAZAMIENTO
            j = j-1 
        arreglo[j]=aux #INSERTO EL CONTENIDO DE LA POS ACTUAL EN LA CORRESPONDIENTE


def ordenamiento_burbuja(arreglo,orden):
    desordenado=True #boolenano para verificar si esta ordenado o no
    while desordenado:
        desordenado=False 
        for i in range(0, len(arreglo)-1): 
            if arreglo[i] > arreglo[i+1]: #comparo el actual con el siguiente
                desordenado=True
                # Intercambiamos los elementos de forma ascendente
                aux=arreglo[i]
                arreglo[i]=arreglo[i+1]
                arreglo[i+1]=aux


#ORDENAMIENTOS DE WALTER
def ordenar_burbuja_mejorada(vector,elementos): #WALTER
    intercambio = True
    while intercambio:   
        intercambio = False    
        for i in range(0,elementos - 1):      
            if vector[i] > vector[i + 1]:             
            intercambio = True             
            # intercambio             
            swap = vector[i]               
            vector[i] = vector[i + 1]
            vector[i + 1] = swap


def ordenar_insercion(vector,elementos):  #WALTER
for i in range(1,elementos):   #RECORREMOS DE LA POSICION ACTUAL
    j = i
    while (j > 0) and (vector[j - 1] > vector[j]): #COMPARAR LA POSICION ACTUAL CON LA POS ANTERIOR
        #REALIZA INTERCAMBIO (DESPLAZAMIENTO)    
        swap = vector[j]
        vector[j] = vector[j - 1]
        vector[j - 1] = swap
        j = j - 1 #EN CASO DE HABER DESPLAZAMIENTO EL PUNTERO SE PARA EN LA POSICION ANTERIOR (NUEVA ACTUAL)