def distancia_hamming(a, b):
    dist=0

    for i in range(len(a)):
        if a[i] != b[i]:
            dist+=1

    return dist

def minima_distancia(alvo, candidatos):
    minimo = len(alvo)+5

    for i in range(len(candidatos)):
        dist = distancia_hamming (alvo, candidatos[i])
        if(dist<minimo):
            minimo=dist
            melhor=candidatos[i]

    return [melhor, minimo]

def janela(sequencia, indice_inicial, tamanho_janela):
    final=''
    for i in range(indice_inicial, indice_inicial+tamanho_janela):
        final+=sequencia[i]
    
    return final


def distancia_janela(a, b, indice_inicial, tamanho_janela):
    x = janela(a, indice_inicial, tamanho_janela)
    y = janela(b, indice_inicial, tamanho_janela)
    
    return distancia_hamming(x, y)

def diferencas(a, b, tamanho_janela):
    lista=[]

    for i in range(len(a)//tamanho_janela):
        indice_inicial = tamanho_janela * i
        dist = distancia_janela(a, b, indice_inicial, tamanho_janela)

        if(dist >= tamanho_janela/3):
            lista.append(indice_inicial)
    
    return lista
