def mdc(a, b):
    #devolve o mdc usando o algoritmo de Euclides
    if(a == b):
        return a

    elif(a < b):
        return mdc(a, b-a)

    else:
        return mdc(a-b, b)

def main():
    #lê a entrada
    n, k = input().split()
    print(mdc(int(n), int(k)))

main()