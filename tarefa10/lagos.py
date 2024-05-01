def lagos(x, y, matriz):
    #se é terra, não há lago
    if matriz[x][y] == '#':
        return 0
    
    #acha as dimensões da matriz
    m = len(matriz)
    n = len(matriz[0])

    #"secamos" a água daquele ponto, para não repetir
    matriz[x][y] = '#'
    total=1

    #conta o tamanho do lago
    if(x!=m-1):
        total += lagos(x+1, y, matriz)
    
    if(y!=n-1):
        total += lagos(x, y+1, matriz)

    if(x!=0):
        total += lagos(x-1, y, matriz)

    if(y!=0):
        total += lagos(x, y-1, matriz)

    #retorna o tamanho total do lago achado
    return total


def main():
    #lê as variáveis
    m, n = [int(i) for i in input().split()]
    matriz = []
    
    for _ in range(m):
        matriz.append(input().split())

    total = 0
    maior = 0

    #acha o maior lago e o total de lagos olhando cada ponto
    for i in range(m):
        for j in range(n):
            if(matriz[i][j] == '_'):
                maior = max(maior, lagos(i, j, matriz))
                total+=1
    
    #imprime o pedido
    print(f"Número de lagos: {total}")
    print(f"Tamanho do maior: {maior}")

main()