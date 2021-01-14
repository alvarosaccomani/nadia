def factorial(n):
    #caso embrionario
    if n == 0:
        f = 1
    else:
        #parte recursiva
        f = n * factorial(n - 1)
    return f

# 0,1,1,2,3,5,8,13,21
def calcular_serie(n):
    if n == 0:
        fibo = 0
    elif n == 1:
        fibo = 1
    else:
        fibo = calcular_serie(n - 1) + calcular_serie(n - 2)
    return fibo


def multiplicar(n,m):

    # 5 x 4 = 5 + (5 x 3)
    # 5 x 3 = 5 + (5 x 2)
    # 5 x 2 = 5 + (5 x 1)
    # 5 x 1 = 5
    
    if (m == 1):
        multi = n
    else:
        multi = n + multiplicar(n, m - 1)
    return multi    


def main():
    print(factorial(6)) 
    fibo = calcular_serie(8)
    #fibo = calcular_el_fibonacci(5)
    print("El fiboncci : ",fibo)  
    ## Queda para despues
    fibo = calcular_serie(18)
    print("El fiboncci hasta : ",fibo)  

    multi = multiplicar(20,5)
    print(multi)

    

if _name_ == "_main_":
    main()