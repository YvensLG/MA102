def bin(n, k):
    #devolve o binomial usando Stifel
    if(n < k):
        return 0
    if(k == 0 or k == n):
        return 1
    
    return bin(n-1, k-1) + bin(n-1, k)

def main():
    #lê entrada
    n, k = input().split()
    print(bin(int(n), int(k)))

main()