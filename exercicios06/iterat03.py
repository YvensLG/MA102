n = int(input())
cont=0

for i in range(1, n+1):
    for j in range(i):
        cont+=1
        print(f"{cont} ", end='')
    print()