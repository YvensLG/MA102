import math

lista = input().split()

n = len(lista)

media=0.

for i in range (0, n):
    media+=float(lista[i])

media = media/n
soma = 0.

for i in range (0, n):
    soma += (float(lista[i])-media)**2

soma = soma/(n-1)

soma = math.sqrt(soma)

print(f"O desvio padrão corrigido é {soma}")