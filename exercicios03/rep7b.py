n = int(input())
total = 0

for i in range(1, n+1):
    total += i 
    print(f"{i}: {total}")

# Eu não usaria a fórmula fechada nesse caso, pois de qualquer maneira vamos ter que rodar o algoritmo n vezes
# então é mais fácil só imprimir as somas feitas do que repetir a fórmula várias vezes