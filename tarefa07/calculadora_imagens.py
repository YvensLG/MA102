import funcoes

def main():
    while(True):
        #Caso acabem os inputs, o programa acaba
        try:
            funcao = input().split(" ")
        except EOFError:
            break

        #Analisar qual função deve ser executada
        if(funcao[0]=="carregar"):
            funcoes.carregar(funcao[1])

        elif(funcao[0]=="normalizar"):
            funcoes.normalizar(int(funcao[1]))

        elif(funcao[0]=="binarizar"):
            funcoes.binarizar(int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="multiplicar"):
            funcoes.somamult(0, int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="somar"):
            funcoes.somamult(1, int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="AND"):
            funcoes.operador(0, int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="OR"):
            funcoes.operador(1, int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="XOR"):
            funcoes.operador(2, int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="SUB"):
            funcoes.operador(3, int(funcao[1]), int(funcao[2]))

        elif(funcao[0]=="filtrar"):
            funcoes.filtrar(int(funcao[1]), funcao[2])

        elif(funcao[0]=="gravar"):
            funcoes.gravar(funcao[1], int(funcao[2]))

main()