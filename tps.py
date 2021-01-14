nombre = input("Igrese el TP: ")

from random import seed
from random import randint

def carga_aleatoria():
    # seed random number generator
    seed(1)
    # generate some integers
    for _ in range(100):
        value = randint(0, 10)
        #print(value)

    res = filter(lambda x: x % 2 != 0, value)
    print(res)

carga_aleatoria()