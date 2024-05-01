def fac(n):
    prod=1
    for i in range(1, n+1):
        prod*=i
    
    return prod

def main():
    for i in range(1, 21):
        print(f"{i}: {fac(i)}")

main()