def fat(n):
    #devolve o fatorial
    if(n==0):
        return 1
    else:
        return n * fat(n-1)

def main():
    #lê entrada
    n = int(input())
    print(fat(n))

main()