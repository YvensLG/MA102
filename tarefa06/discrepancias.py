import funcoes

def main():
    #definir variáveis
    dados = []
    dadosatual = []
    datasdiscrep = []
    datasfinal = []
    mes = -1

    #ler as variáveis e colocar na lista de dados
    #dados[0] é mês, dados[1] é ano e dados[2] é temperatura
    with open(input()) as arquivo:
        for linha in arquivo:
            data, temperatura = linha.split(",")
            dados.append([int(data[0]+data[1]), int(data[3]+data[4]+data[5]+data[6]), float(temperatura)])

    #ordenar os dados pelos meses
    dados=funcoes.ordenarmeses(dados)

    #adicionar um elemento para o próximo for iterar uma vez a mais
    dados.append([-2, -2, -2])

    #Analisar os dados por cada mês
    #Calcular desvio pelos meses e achar suas discrepâncias
    mes=dados[0][0]
    for dado in dados:

        if(dado[0]==mes):
            dadosatual.append(dado)

        else:
            d = funcoes.desvio(dadosatual)
            m = funcoes.media(dadosatual)

            for j in dadosatual:
                disc = funcoes.absoluto(j[2]-m)/d
                datasdiscrep.append([j[0], j[1], disc])

            dadosatual=[dado]
            mes=dado[0]

    datasdiscrep=funcoes.ordenartemp(datasdiscrep)
    
    for i in range(10):
        datasfinal.append(datasdiscrep[i])

    datasfinal=funcoes.ordenaranos(datasfinal)

    for i in datasfinal:
        if(i[0]<10):
            print("0", end='')

        print(f"{i[0]}/{i[1]}: {i[2]:.2f}")

main()