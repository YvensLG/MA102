lista = input("Digite a lista: ").split()

anterior = int(lista[0])

atual=1
inicioatual=0

maior = 0
inicio = 0

for i in range(1, len(lista)):
    if(int(lista[i])>anterior):
        atual+=1
        anterior = int(lista[i])
    else:
        if atual>maior:
            maior=atual
            inicio=inicioatual

            inicioatual=i
            atual=1
            anterior=int(lista[i])

if atual>maior:
    maior=atual
    inicio=inicioatual

print(f"Uma maior subsequencia crescente é ", end="")

for i in range(inicio, inicio+maior):
    print(f"{lista[i]} ", end='')

print(f"e tem {maior} elementos")