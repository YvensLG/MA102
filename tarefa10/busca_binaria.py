def busca_menor(v, n, max, min):
    #busca binária pelo MENOR índice i tal que v[i] = n
    mid = (max+min)//2

    if(min+1 == max):
        if(v[min]==n):
            return min
        elif(v[max]==n):
            return max
        else:
            return None

    if(v[mid] <= n):
        return busca_menor(v, n, mid, min)
    
    if(v[mid] > n):
        return busca_menor(v, n, max, mid)

def busca_maior(v, n, max, min):
    #busca binária pelo MAIOR índice i tal que v[i] = n
    mid = (max+min+1)//2

    if(min+1 == max):
        if(v[max]==n):
            return max
        elif(v[min]==n):
            return min
        else:
            return None

    if(v[mid] < n):
        return busca_maior(v, n, mid, min)
    
    if(v[mid] >= n):
        return busca_maior(v, n, max, mid)

def main():
    #lê entrada
    v = input().split()
    
    for i in range(len(v)):
        v[i] = int(v[i])
    
    n = int(input())

    #acha o menor e o maior índices
    maior = busca_maior(v, n, len(v)-1, 0)
    menor = busca_menor(v, n, len(v)-1, 0)

    #se não achar o índice printa 0
    if(menor == None):
        print(0)
        return

    #printa o tamanho do intervalo de n
    total = maior - menor + 1
    print(total)

main()