import funcoes

def main():
    #definir variáveis
    dados = []
    dadosatual = []
    datasdiscrep = []
    tendencia = []
    dadosauxiliares = []
    ano = -1

    #ler as variáveis e colocar na lista de dados
    #dados[0] é mês, dados[1] é ano e dados[2] é temperatura
    with open(input()) as arquivo:
        for linha in arquivo:
            data, temperatura = linha.split(",")
            dados.append([int(data[0]+data[1]), int(data[3]+data[4]+data[5]+data[6]), float(temperatura)])

    #ordenar os dados pelos anos e adicionar um elemento para o próximo for iterar uma vez a mais
    dados=funcoes.ordenaranos(dados)

    #adicionar um elemento para o próximo for iterar uma vez a mais
    dados.append([-2, -2, -2])

    #Analisar os dados por cada ano
    #Calcular desvio do ano e achar os meses discrepantes
    ano = dados[0][1]
    for dado in dados:

        if(dado[1]==ano):
            dadosatual.append(dado)

        else:
            d = funcoes.desvio(dadosatual)
            m = funcoes.media(dadosatual)

            for j in dadosatual:
                if(m-3*d/2 <= j[2] and j[2] <= m+3*d/2):
                    dadosauxiliares.append(j)
                else:
                    datasdiscrep.append(j)

            tendencia.append([ano, funcoes.media(dadosauxiliares)])

            dadosauxiliares=[]
            dadosatual=[dado]
            ano=dado[1]

    #Imprimir Outliners (datas discrepantes)    
    print("Outliers:")
    for i in datasdiscrep:
        if(i[0]<10):
            print("0", end='')

        print(f"{i[0]}/{i[1]}")

    #Imprimir médias anuais sem as datas discrepantes
    print("\nTendência de média anual:")
    for i in tendencia:
        print(f"{i[0]}: {i[1]:.2f}")

main()
