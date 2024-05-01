def intercalar(v1, v2, v):
    #caso base
    if(len(v1)==0 and len(v2)==0):
        return v

    #v pega o maior elemento dos conjuntos de um por um
    #no fim, v vai ficar com todos os elementos em ordem decrescente
    elif(len(v1)==0):
        v.append(v2.pop())

    elif(len(v2)==0):
        v.append(v1.pop())

    elif(v2[-1]>v1[-1]):
        v.append(v2.pop())
    
    else:
        v.append(v1.pop())
    
    return intercalar(v1, v2, v)

def main():
    #lê as duas entradas
    v1 = input().split()
    v2 = input().split()
    
    for i in range(len(v1)):
        v1[i] = int(v1[i])
    
    for i in range(len(v2)):
        v2[i] = int(v2[i])

    #define v auxiliar
    v=[]

    #atualiza v com o resultado
    v = intercalar(v1, v2, v)

    #imprime v do fim ao começo, pois ele está na ordem inversa
    for i in range(len(v)-1, -1, -1):
        print(v[i], end=" ")
    print()

main()