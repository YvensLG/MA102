#fazer bubble sort nos anos(lista[i][1]) e depois meses(lista[i][0])
def ordenaranos(lista):
    n = len(lista)
    for _ in range(n-1):
        for i in range(n-1):
            if((lista[i][1] > lista[i+1][1]) or (lista[i][1] == lista[i+1][1] and lista[i][0] > lista[i+1][0])):
                aux = lista[i]
                lista[i] =lista[i+1]
                lista[i+1] = aux

    return lista
    
#fazer bubble sort nos meses(lista[i][0]) e depois anos(lista[i][1])
def ordenarmeses(lista):
    n = len(lista)
    for _ in range(n-1):
        for i in range(n-1):
            if((lista[i][0] > lista[i+1][0]) or (lista[i][0] == lista[i+1][0] and lista[i][1] > lista[i+1][1])):
                aux = lista[i]
                lista[i] =lista[i+1]
                lista[i+1] = aux

    return lista

#fazer bubble sort na temperatura(lista[i][2]) (maior para menor)
def ordenartemp(lista):
    n = len(lista)
    for _ in range(n-1):
        for i in range(n-1):
            if(lista[i][2] < lista[i+1][2]):
                aux = lista[i]
                lista[i] =lista[i+1]
                lista[i+1] = aux

    return lista

#valor absoluto
def absoluto(n):
    if(n>=0):
        return n
    else:
        return -n

#fazer raiz pela aproximação de Newton
def raiz(n):
    aprox = n/2
    for i in range(25):
        aprox = (aprox*aprox+n)/(2*aprox)
    return aprox

#fazer a media das temperaturas (lista[2])
def media(lista):
    media = 0.0
    
    for i in lista:
        media+=i[2]

    return media/len(lista)

#fazer o desvio padrão das temperaturas (lista[2])
def desvio(lista):
    soma = 0.0
    m = media(lista)

    for i in lista:
        soma+=(i[2]-m)*(i[2]-m)
    
    soma=raiz((soma/(len(lista))))

    return soma
