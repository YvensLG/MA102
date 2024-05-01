def roman(n):
    assert n <= 50 and n>=0
    if n==0: return

    if n>=50:
        print("L", end='')
    
    elif n>=40:
        print("XL", end='')
        roman(n-40)
    
    elif n>=30:
        print("XXX", end='')
        roman(n-30)
    
    elif n>=20:
        print("XX", end='')
        roman(n-20)
    
    elif n>=10:
        print("X", end='')
        roman(n-10)

    elif n==9:
        print("IX", end='')
        return 

    elif n>=5:
        print("V", end='')
        roman(n-5)

    elif n==4:
        print("IV", end='')
        return 
    
    elif n<=3:
        print("I", end='')
        roman(n-1)

def main():
    n = int(input())
    roman(n)
    print()

main()