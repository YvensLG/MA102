import math

def main():
    #define as variaveis e lê a entrada
    RMS = input().split()
    RMS[0] = int(RMS[0])
    THD = [0]
    n = len(RMS)

    #transforma as strings da lista RMS em inteiros
    #calcula o THD[i] em função de RMS[0], de RMS[i] e de THD[i-1]
    for i in range(1, n):
        RMS[i] = int(RMS[i])
        THD.append(math.sqrt(THD[i-1]*THD[i-1] + (RMS[i]*RMS[i])/(RMS[0]*RMS[0])))

    #olha todos os elementos de THD, em ordem, e acha o primeiro que satisfaz o que foi pedido no problema
    for i in range(1, n):
        if(THD[i] >= (80/100)*THD[n-1]):
            print(f"Número de harmônicos críticos: {i}")
            print(f"THD de harmônicos críticos: {THD[i]*100 :.2f} %")
            print(f"THD de todos os harmônicos: {THD[n-1]*100 :.2f} %")
            break

main()