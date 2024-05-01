#lê quantidade de alimentos
n = int(input())    

#define lista dos alimentos
lista = []

#colocar os alimentos e seus nutrientes em lista
for i in range(0, n):
    nome, proteina, carboidrato, gordura = input().split()
    listaaux = [nome, float(proteina), float(carboidrato), float(gordura)]
    lista.append (listaaux)

#lê alimentos consumidos em cada refeição
cafe = input().split()
almoco = input().split()
janta = input().split()

#junta alimentos em uma só lista
refeicao = cafe + almoco + janta

#cria variaveis dos totais de nutrientes
proteinaT = 0.
carboidratoT = 0.
gorduraT = 0.

#para todo alimento na lista vemos se ele aparece em refeicao, caso sim, somamos os nutrientes
for i in lista:
    for j in refeicao:
        if i[0]==j:
            proteinaT+=i[1]        
            carboidratoT+=i[2]
            gorduraT+=i[3]
    
#imprimir o que é pedido no problema
if(proteinaT>140):
    print(f"{proteinaT-140:.1f} gramas de proteína em excesso")
else:
    print(f"{-proteinaT+140:.1f} gramas de proteína em falta")

if(carboidratoT>210):
    print(f"{carboidratoT-210:.1f} gramas de carboidrato em excesso")
else:
    print(f"{-carboidratoT+210:.1f} gramas de carboidrato em falta")

if(gorduraT>56):
    print(f"{gorduraT-56:.1f} gramas de gordura em excesso")
else:
    print(f"{-gorduraT+56:.1f} gramas de gordura em falta")