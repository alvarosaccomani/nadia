import random 

def carga_aleatoria(vector_a,vector_b,elementos):
    for i in range (elementos):
        vector_a[i]=random.randint(1,12)
        vector_b[i]=random.randint(1,12)


def mostrar(vector,elementos):
    for i in range (elementos):
        print(vector[i],end=" | ")
    print(" ")

def producto_a_escalar(vector_a,vector_b,elementos):
    res=0
    for i in range (elementos):
        res+=vector_a[i]*vector_b[i]
    return(res)


def main():
    #DEFINO VARIABLE
    elementos=3
    vector_a=[None]*elementos
    vector_b=[None]*elementos

    #LLAMADO DE MODULOS
    carga_aleatoria(vector_a,vector_b,elementos)
    print("Vector A")
    mostrar(vector_a,elementos)
    print("Vector B")
    mostrar(vector_b,elementos)

   
    producto=producto_a_escalar(vector_a,vector_b,elementos)
    print("Producto a escalar "+str(producto))




if __name__ == "__main__":
    main()