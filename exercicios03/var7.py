import math

a = int(input())
b = math.sqrt(a)
c = str(b)

n1=-1
n2=-1

for i in range(0, len(c)):
    if(c[i]=="."):
        if(i>=3):
            n1=int(c[i-3])
        else:
            n1=0
        
        if(i+3>=len(c)):
            n2=0
        else:
            n2=int(c[i+3])

print(f"{n1} {n2}")