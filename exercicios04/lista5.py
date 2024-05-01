lista = input("Digite uma lista ").split()
i = int(input("Digite o primeiro número "))
j = int(input("Digite o segundo número "))

soma=0

for k in range(i, j+1):
    soma+=int(lista[k])

print(f"{soma}")