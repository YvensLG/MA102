import math

def meio(x, y, z):
    #devolve o número que não é o maior nem o menor
    return x+y+z - max(x, y, z) - min(x, y, z)

def criar_dict(nome, inicio, fim, THD):
    #cria o dicionário que será usado no problema
    D = {
        "nome": nome,
        "inicio": inicio,
        "fim": fim,
        "THD": THD,
    }
    return D

def imprimir(D):
    #imprime o dicionário no formato pedido do problema
    print("Grupo {}".format(D["nome"]))

    print("Motor(es): {} {}".format(D["inicio"], "até "+str(D["fim"]) if D["inicio"]!=D["fim"] else ""))

    print("THD: {:.2f} %\n".format(100*math.sqrt(D["THD"])/220))

def main():
    #define as variaveis e lê a entrada
    RMS = input().split()
    THD = []
    soma = 0
    n = len(RMS)
    
    #calcula cada THD (sem a parte da raiz e da divisão) e a soma de todos eles
    for i in range(n):
        THD.append(int(RMS[i])**2)
        soma += THD[i]

    #no primeiro caso, temos somente 0 no grupo A, somente 1 no grupo B e todos os outros motores no grupo C
    #no caso atual, os motores de A vão de 0 a p1, os de B de p1+1 a p2 e os de C de p2+1 a n-1
    p1=0
    p2=1

    #define as variáveis da soma de THD do caso que está sendo testado:
    a = THD[0]
    b = THD[1]
    c = soma-THD[1]-THD[0]

    #define as variáveis finais, o melhor caso que foi encontrado:
    A = criar_dict("A", 0, 0, a)
    B = criar_dict("B", 1, 1, b)
    C = criar_dict("C", 2, n-1, c)

    #testar o caso atual
    while(True):
        #se é possível melhorar o caso atual, o fazemos
        if(p1+1<p2 and max(a+THD[p1+1], b-THD[p1+1]) < max(a, b)):
            a+=THD[p1+1]
            b-=THD[p1+1]
            p1+=1
        elif(p2+1<n-1):
            b+=THD[p2+1]
            c-=THD[p2+1]
            p2+=1
        else:
            break
        
        #checa se o caso atual é melhor que o melhor caso anterior
        trocar = False
        if max(a, b, c) < max(A["THD"], B["THD"], C["THD"]):
            trocar = True

        elif max(a, b, c) == max(A["THD"], B["THD"], C["THD"]):
            if meio(a, b, c) < meio(A["THD"], B["THD"], C["THD"]):
                trocar = True

        #se for, atualiza-se o melhor caso
        if(trocar):
            A["THD"]=a
            B["THD"]=b
            C["THD"]=c

            A["fim"]=p1
            B["inicio"]=p1+1

            B["fim"]=p2
            C["inicio"]=p2+1

    #imprime o melhor caso
    imprimir(A)
    imprimir(B)
    imprimir(C)

main()