import random

def embaralhar(lista):
    for i in range(len(lista)):
        numero = random.randint(0, len(lista)-1)
        aux=lista[i]
        lista[i]=lista[numero]
        lista[numero]=aux
    return lista

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(embaralhar(lista))