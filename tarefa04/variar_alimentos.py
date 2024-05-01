#lê lista de alimentos e número de dias
alimentos = input().split()
dias = int(input())

#cria variáveis: lista dos cardápio; maximo de alimentos diferentes; dias do maximo
lista = []
maximo = -1
dia1 = -1
dia2 = -1

#adiciona cardápios à lista
for i in range(0, dias):
    listaaux = input().split()
    lista.append(listaaux)

#i e j variam em todas os pares possíveis de dias
#analisar número de alimetos distintos nos dois dias e ver se é o máximo
for i in range(0, dias):
    for j in range(i+1, dias):
        total=0
        for k in alimentos:
            if k in lista[i] or k in lista[j]:
                total+=1
        if total>maximo:
            maximo=total
            dia1=i
            dia2=j

#imprimir o que é pedido no problema
print(f"Juan pode comer {maximo} alimentos diferentes")

print(lista[dia1][0], end = ' ')
for k in lista[dia1]:
    if k in alimentos:
        print(k, end = ' ')

print("\n", end = '')

print(lista[dia2][0], end = ' ')
for k in lista[dia2]:
    if (k in alimentos):
        print(k, end = ' ')

print("\n", end = '')