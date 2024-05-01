def prob(n, x, memo):
    #casos base
    if(x<0):
        return 0
    if(x==0):
        return 1
    if(n==0):
        return 0

    #se der, retorna o que tiver salvo
    if memo[n][x]!=-1:
        return memo[n][x]

    #calcula a probabilidade usando os anteriores
    memo[n][x] = 1/6*(prob(n-1, x-1, memo) + prob(n-1, x-2, memo) + prob(n-1, x-3, memo) + prob(n-1, x-4, memo) + prob(n-1, x-5, memo) + prob(n-1, x-6, memo))
    return memo[n][x]

def main():
    #lê a entrada
    n, x = input().split()
    n = int(n)
    x = int(x)

    #definie a memorização
    memo = [[-1]*(x+1) for _ in range(n+1)]

    #imprime o resultado
    print(f"{prob(n, x, memo) :.3f}")

main()