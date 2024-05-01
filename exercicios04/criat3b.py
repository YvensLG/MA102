n = int(input("Digite o número de lâmpadas: "))
m = int(input("Digite o número de lâmpadas que devem ficar acesas: "))

print("Lâmpadas que devem ser acesas:")

lista = []

for k in range(0, m):
    lista.append(int(input()))

lista.sort(reverse=True)

for k in lista:
    if k==n:
        print(f"Acender lâmpada {k}")
    elif(k+1 not in lista):
        print(f"Acender lâmpada {k+1}")
        print(f"Acender lâmpada {k}")
    else:
        print(f"Acender lâmpada {k}")
        print(f"Acender lâmpada {k+1}")