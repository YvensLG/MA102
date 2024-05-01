import sequencias

n = int(input())
referencia = input()
variante = input()

contador=0

for indice_inicial in sequencias.diferencas(referencia, variante, n):
    contador+=1
    
    print(f"Diferença {contador}:")
    print(f"   Posição: {indice_inicial}")
    print(f"Referência: {sequencias.janela(referencia, indice_inicial, n)}")
    print(f"  Variante: {sequencias.janela(variante, indice_inicial, n)}")
    print(f" Distância: {sequencias.distancia_janela(referencia, variante, indice_inicial, n)}")