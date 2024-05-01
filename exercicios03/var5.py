import math

print("Insira os lados do triângulo:")
a=int(input())
b=int(input())
c=int(input())

if(2*max(a, b, c) >= a + b + c):
    print("Isso não forma um triângulo")
else:
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Área: {A}")
