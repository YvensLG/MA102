n = int(input())
M=0
F=0
PesoM=0
for i in range(n):
    peso, sexo, gravida, doacoes, dias = input().split()
    peso = float(peso)
    doacoes = int(doacoes)
    dias = int(dias)

    if(peso >= 50):
        if(sexo=="F"):
            if(gravida=="N" and doacoes<=3 and dias>90):
                F+=1
                PesoM+=peso
        if(sexo=="M"):
            if(doacoes<=4 and dias>60):
                M+=1
                PesoM+=peso

if(M+F!=0):
    PesoM=PesoM/(M+F)

print(f"Número de doadores aptos do sexo M: {M}")
print(f"Número de doadores aptos do sexo F: {F}")
print(f"Peso médio de doadores aptos: {PesoM:.1f}")