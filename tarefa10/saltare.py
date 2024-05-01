def fib(n, memo):
    #retorna a variação de Fibonacci salvando os já encontrados na memória 
    if memo[n]!=0:
        return memo[n]

    memo[n] = fib(n-1, memo) + fib(n-3, memo)
    return memo[n]

def main():
    #lê a entrada
    n = int(input())

    #define o memo inicial
    memo = [0]*(max(n+1, 4))
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1

    #printa o resultado
    print(fib(n, memo))

main()