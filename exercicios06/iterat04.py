n = int(input())

lista = []

cont=1

for i in range(0, n):
    lista.append([])
    for j in range(0, n-cont):
        lista[i].append('.')
    for j in range(n-cont, n+cont-1):
        lista[i].append('*')
    for j in range(n+cont-1, 2*n-1):
        lista[i].append('.')
    cont+=1

for i in range(0, n):
    for j in range(0, 2*n-1):
        print(lista[i][j], end='')
    for j in range(0, 2*n-1):
        print(lista[i][j], end='')
    print()