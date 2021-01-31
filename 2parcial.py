
from pyrecord import Record
import numpy as np
import random
import string

#ejercicio 1
#defino regisro
registro_Proyecto = Record.create_type("registro_Proyecto","identificador_Proyecto","cliente","dias_Presupuestado","costo","ancho","largo","profundidad","formato","legajo_Supervisor"
                        identificador_Proyecto = 0,cliente = '',dias_Presupuestado = 0, costo = 0, ancho = 0, largo = 0, profundidad = 0, formato = '', legajo_Supervisor = 0)

#----------------carga de nombres aleatoria

def carga_nombre ():
	cadena = ''
	for i in range(15):
 		cadena += random.choice(string.ascii_letters)
	return(cadena)

#-------------------- carga de formato aleatoria

def carga_formato ():
	x=random.randint(1,4)
	if x == 1:
		resul= "corazon"
	elif x == 2:
		resul= "rectangular"
	elif x == 3:
		resul= "riñon"
	elif x == 4:
		resul= "ovalada"

	return resul

#-------------------------carga aleatoria de registro

  
def carga_aleatoria(vector_registro,cantidad_real):
	indice=0

    for i in range cantidad_real:
    	veces = random.randint(1,6)
    	identificador = i+1
    		for v in range (veces):
        		vector_registro[indice] = registro_Proyecto()
       			 #llamada funcion clientes
        		cliente = carga_nombre()
        		dias = random.randint(1,30)
        		costo = random.randint(10000,100000)
        		#cargo medidas pileta
       			 ancho = random.randint(2,25)
        		largo = random.randint(2,50)
        		profundidad = random.randint(1,4)

        		formato= carga_formato()
        		legajo = random.randint(1,10)

       			cargar_registro (vector_registro[indice],identificador,clientes,dias,costo,ancho,largo,profundidad,formato,legajo)
        		indice +=1
    return indice 


#----------carga del registro
def cargar_registro(registro,identificador,clientes,dias,costo,ancho,largo,profundidad,formato,legajo):
    registro.identificador_Proyecto = identificador
    registro.cliente = cliente
    registro.dias_Presupuestado = dias
    registro.costo = costo
    registro.ancho = ancho
    registro.largo = largo
    registro.profundidad = profundidad
    registro.formato = formato
    registro.legajo_Supervisor = legajo


#--------Punto 1 Agregar proyecto
def agregar(vector_registro,valor,cantidad_real,cantidad_maxima):
 nueva_cantidad = cantidad_real
   if (cantidad_real < cantidad_maxima):
        vector_registro[cantidad_real] = cargar_proyecto(vector_registro)
        nueva_cantidad = cantidad_real + 1
   	return  nueva_cantidad

#cargo el proyecto a agregar manualmente 
def cargar_proyecto(vector_registro):
    vector_registro[i] = registro_Proyecto()
    identificador = i+1
    cliente = input('Ingrese el nombre del cliente: ')
    dias = input('Ingrese el numero de dias presupuestados: ')
    costo = input('Ingrese costo: ')
    ancho = input('Ingrese ancho de la pileta: ')
    largo = input('Ingrese largo de la pileta: ')
    prufundidad = input('Ingrese profundidad de la pileta: ')
    formato = input('Ingrese formato de la pileta: ')
    legajo = input('Ingrese el numero de legajo del supervisor: ')



#-------Punto 2 Desplazamiento

def desplazamiento(registro,identificador,desplazamiento):
    while identificador-1 - desplazamiento <0:
        desplazamiento= input("ingrese la cantidad de desplazamientos que desea generar: ")

    for i in range(desplazamiento, -1):
        aux = registro[identificador -1]
       	registro[identificador -1] = registro[identificador]
        registro[identificador] = aux


#----------Punto 3 y 4 etuqueta comenzado o finalizado
def comenzado_o_finalizado(vector_registro,minimo,maximo,cantidad_real,etiqueta):
  
    for i in range(cantidad_real):
        
        if (vector_registro[i].dias > minimo and vector_registro[i].dias <= maximo):
          print('El proyecto',identificador,'esta: ',etiqueta)


#---------Punto 5 total
def total(vector_registro,minimo,maximo,cantidad_real):
	acumulador=0
	for i in range (cantidad_real):

		if (vector_registro[i].dias >= minimo and vector_registro[i].dias <= maximo):
			acumulador+=vector_registro[i].costo
	return (acumulador)





#principal

cantidad_maxima=100
cantidad_real=6
vector_registro = np.empty([cantidad_maxima,]*cantidad_real, dtype=registro_Proyecto)
carga_aleatoria(vector_registro,cantidad_real)
cargar_registro(vector_registro,identificador,clientes,dias,costo,ancho,largo,profundidad,formato,legajo)

# etiqueta de comenzado
comenzado_o_finalizado(vector_registro,3,10,cant_real,"comenzado")

# etiqueta de finalizado
comenzado_o_finalizado(notas,10,20,cant_real,"finalizado")
# total ganacias
total_ventas=total(vector_registro,4,20,cantidad_real)
print('El monto total de ventas es de: ',total_ventas)





#---------------------------------------------------
#ejercicio 2

from pyrecord import Record
import numpy as np
import random
import string
#defino registro
Pc = Record.create_type("Pc","marca","micro","ram", 
            "disco_rigido","numero_serie", marca = '',micro = '',ram = '',disco_rigido = '',numero_serie = '')



def carga_marca ():
	x=random.randint(1,5)
	if x == 1:
		resul = "Dell"
	elif x == 2:
		resul = "Mac"
	elif x == 3:
		resul = "Toshiba"
	elif x == 4:
		resul = "Asus"
	elif x == 5
		resul = "Lenovo"

	return resul


def carga_micro ():
	x=random.randint(1,5)
	if x == 1:
		resul = "Intel I9"
	elif x == 2:
		resul = "Intel I7"
	elif x == 3:
		resul = "Intel I5"
	elif x == 4:
		resul = "AMD Ryzen 7"
	elif x == 5
		resul = "AMD Ryzen 5"

	return resul


def carga_ram ():
	x=random.randint(1,3)
	if x == 1:
		resul = "4 GB"
	elif x == 2:
		resul = "8 GB"
	elif x == 3:
		resul = "16 GB"
	return resul

def carga_disco ():
	x=random.randint(1,3)
	if x == 1:
		resul = "SSD 250 GB"
	elif x == 2:
		resul = "SSD 450 GB"
	elif x == 3:
		resul = "SSD 1 TB"
	return resul



def carga_n_serie ():
	cadena = ''
	for i in range(3):
 		cadena += random.choice(string.ascii_letters)
	return(cadena)



#cargo vector
def carga_aleatoria(vector_registro2,cantidad_maxima):
    for i in elementos:
        vector_registro2[i] = Pc()
        marca = carga_marca()
        micro = carga_micro()
        ram = carga_ram()
        disco_rigido = cargar_disco()
        numero_serie =  carga_n_serie()+str(random.randint(10000,99999))


        #cargo valores de las variables en registro de cada posicion en vector
            cargar_registro_2(vector_registro2[i],marca,micro, ram,disco_rigido,numero_serie)



def cargar_registro_2(vector_registro2,marca,micro,ram,disco_rigido,numero_serie):
    registro.marca = marca
    registro.micro = micro
    registro.ram = ram
    registro.disco_rigido = disco_rigido
    registro.numero_serie = numero_serie

def mostrar_registros(registro):
    for i in range(20):
        print("marca : ",registro[i].marca," | micro : ",registro[i].micro, 
        " | RAM : $ ",registro[i].ram," | Disco Rigido : ",registro[i].disco_rigido," | Numero de serie : ",registro[i].numero_serie)



#principal ejercicio2
cantidad_maxima = 1500
cantidad_real = 20

# Definir un vector de tipo Venta
vector_registro2 = np.empty([cantidad_maxima,], dtype=Pc)

carga_aleatoria(vector_registro2,cantidad_maxima)
cargar_registro_2(vector_registro2,marca,micro,ram,disco_rigido,numero_serie)
mostrar_registros(vector_registro2)
