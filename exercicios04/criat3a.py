n = int(input("Digite o número de lâmpadas: "))
k = int(input("Lâmpada que deve ser acesa: "))

if k==n:
    print(f"Acender lâmpada {k}")
else:
    print(f"Acender lâmpada {k+1}")
    print(f"Acender lâmpada {k}")