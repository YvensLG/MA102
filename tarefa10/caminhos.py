def caminhos(x, y, memo):
    #se der retorna a memorização
    if memo[x][y] != -1:
        return memo[x][y]
    
    #acha as dimensões da matriz
    m = len(memo)
    n = len(memo[0])

    #atualiza a memorização para o valor correto
    if(x!=m-1 and y!=n-1):
        memo[x][y] = caminhos(x+1, y, memo) + caminhos(x, y+1, memo)

    elif(x!=m-1):
        memo[x][y] = caminhos(x+1, y, memo)
    
    else:
        memo[x][y] = caminhos(x, y+1, memo)

    #retorna a memorização
    return memo[x][y]


def main():
    #lê a entrada
    m, n = [int(i) for i in input().split()]
    p = int(input())

    #define a matriz de memorização
    memo = [[-1]*(n) for _ in range(m)]
    
    #atualiza a matriz de forma que as pedras tenham valor 0
    for _ in range(p):
        x, y = [int(i)-1 for i in input().split()]
        memo[x][y] = 0
    
    #estando no objetivo, sempre há exatamente uma forma de chegar
    memo[m-1][n-1]=1

    #imprime as formas de chegar no objetivo a partir de (0, 0)
    print(caminhos(0, 0, memo))

main()