a = 1
b = 1
c = 0

n = int(input())

for i in range(3, n+1):
    c=a+b
    b=a
    a=c
    c=0

print(f"{a}\n")