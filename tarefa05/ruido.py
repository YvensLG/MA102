import sequencias

alvo = input()

n = int(input())

candidatos = []

for i in range(n):
    candidatos.append(input())

par = sequencias.minima_distancia(alvo, candidatos)

print(f"Sequência mais próxima: {par[0]}")
print(f"Distância de Hamming: {par[1]}")