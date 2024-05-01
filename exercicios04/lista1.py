lista = input("Digite uma lista: ").split()

minimo=int(lista[0])
posicao=0

for i in range(1, len(lista)):
    if minimo > int(lista[i]):
        minimo=int(lista[i])
        posicao=i

print(f"Um menor elemento vale {minimo} e está na posição {posicao}.")