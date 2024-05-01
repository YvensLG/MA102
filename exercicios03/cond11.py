import math

a, b, c = input().split()

a=float(a)
b=float(b)
c=float(c)

print(f"Média Aritmética: {(a+b+c)/3}\n")
print(f"Média Ponderada: {(3*a+3*b+4*c)/10}\n")
print(f"Média Harmônica: {3/(1/a+1/b+1/c)}\n")
print(f"Média Geométrica: {(a*b*c)**(1./3.)}\n")