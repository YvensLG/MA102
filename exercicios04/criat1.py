n = int(input("Digite o tamanho da lista: "))

lista = [0]*10

print("Digite os números da lista: ")

for i in range(0, n):
    lista[int(input())]+=1

maximo = max(lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9])

print("+---------+")

for i in range(0, maximo):
    print("|", end="")
    if(lista[1]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[2]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[3]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[4]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[5]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[6]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[7]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[8]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    if(lista[9]>=maximo-i): print("*", end="")
    else: print(" ", end="")
    print("|")

print("+---------+")
print(" 123456789 ")