import math

y = float(input("Digite um número: "))
n = int(input("Digite quantas aproximações: "))

x=y/2
print(f"x1 = {x}")
for i in range(2, n+1):
    x=(x**2+y)/(2*x)
    print(f"x{i} = {x}")

print(f"\n aproximacao python: {math.sqrt(y)}")