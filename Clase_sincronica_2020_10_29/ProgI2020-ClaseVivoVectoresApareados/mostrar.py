def mostrar_titulo(titulo):
        print(linea(78))
        print("-" + centar("SISTEMA DE SEGUIMIENTO DE ESTUDIANTES",76) + "-")
        print(linea(78))
        print("-" + centar(titulo,76) + "-")
        print(linea(78))

def centar(mensaje,tamanio):
    espacio = " " * ((tamanio - len(mensaje)) // 2)
    texto = espacio + mensaje + espacio + " "
    return texto[:tamanio]

def izquierda(mensaje,tamanio):
    espacio = " " * (tamanio - len(mensaje))
    texto = mensaje + espacio
    return texto[:tamanio]


def derecha(mensaje,tamanio):
    espacio = " " * (tamanio - len(mensaje))
    texto = espacio + mensaje 
    return texto[:tamanio]

def linea(tamanio):
    return ("-" * tamanio)