import math

def eh_primo(n):
    b = True

    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            b = False
            break

    return b

def maior_primo(n):
    assert n>1

    for i in range(n, 0, -1):
        if eh_primo(i):
            return i

def main():
    n = int(input())

    print(maior_primo(n))

main()