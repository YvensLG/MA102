#definir a lista de imagens
imagem = []

def carregar(nome):
    #ignorar as primeiras linhas do arquivo .pgm e salvar a matriz numérica que o representa
    with open(nome) as arquivo:
        arquivo.readline()
        arquivo.readline()
        largura, altura = arquivo.readline().strip().split(" ")
        largura=int(largura)
        altura=int(altura)
        arquivo.readline()
        matriz=[]

        for _ in range(altura):
            matriz.append([int(x) for x in arquivo.readline().strip().split(" ")])
    
    #imprimir o texto pedido    
    print(f"Carregado arquivo {nome} em imagem {len(imagem)}.")
    
    #Adicionar a matriz numérica na lista de imagens  
    imagem.append(matriz)

def normalizar(id):
    #definir as variáveis que serão usadas
    altura=len(imagem[id])
    largura=len(imagem[id][0])
    maximo=0
    minimo=255
    maiores=0

    #achar o maior e o menor valor de cada entrada da matriz imagem[id]
    for i in range(altura):
        for j in range(largura):
            if(maximo<imagem[id][i][j]):
                maximo=imagem[id][i][j]

            if(minimo>imagem[id][i][j]):
                minimo=imagem[id][i][j]

    #interpolar a matriz em relação ao maximo e ao minimo, além de contar quantos pixels são maiores que 0
    for i in range(altura):
        for j in range(largura):
            imagem[id][i][j]-=minimo
            imagem[id][i][j]=(imagem[id][i][j]*255)//(maximo-minimo)

            if(imagem[id][i][j]>0):
                maiores+=1

    #imprimir o texto pedido  
    print(f"Imagem {id} modificada: {maiores} pixels maiores que zero.")

def binarizar(id, limiar):
    #definir as variáveis que serão usadas
    altura=len(imagem[id])
    largura=len(imagem[id][0])
    maiores=0

    #contar pixels maiores que 0 e binarizar a matriz: se é maior que o limiar vira 255, caso contrário, vira 0
    for i in range(altura):
        for j in range(largura):
            if(imagem[id][i][j]<=limiar):
                imagem[id][i][j]=0
            else:
                imagem[id][i][j]=255
                maiores+=1

    #imprimir o texto pedido  
    print(f"Imagem {id} modificada: {maiores} pixels maiores que zero.")

#funções produto e media usadas na funcao somamult
def produto(a, b):
    return a*b

def media(a, b):
    return (a+b)//2

def somamult(op, id1, id2):
    #definir as variáveis que serão usadas
    altura=len(imagem[id1])
    largura=len(imagem[id1][0])
    maiores=0

    #se op=0, usaremos a função produto, e se op=1, a operação media 
    op = [produto, media][op]

    #contar pixels maiores que 0 e realizar a operação na matriz
    for i in range(altura):
        for j in range(largura):
            imagem[id1][i][j]=op(imagem[id1][i][j], imagem[id2][i][j])

            if(imagem[id1][i][j]>0):
                maiores+=1

    #imprimir o texto pedido 
    print(f"Imagem {id1} modificada: {maiores} pixels maiores que zero.")

#funções AND, OR, XOR, SUB usadas na funcao operador
#note que no problema, "255" é False (pixel branco) e "0" é True (pixel preto), por isso foram usados vários "not" nessas funções
def AND(a, b):
    return 255*(int(not((not a) and (not b))))

def OR(a, b):
    return 255*(int(not((not a) or (not b))))

def XOR(a, b):
    return 255*(int(not((not a) != (not b))))

def SUB(a, b):
    return 255*(int(not((not a) and b)))

def operador(op, id1, id2):
    #definir as variáveis que serão usadas
    altura=len(imagem[id1])
    largura=len(imagem[id1][0])
    maiores=0

    #se op=0, usaremos a função AND, se op=1, OR, se op=2, XOR, se op3, SUB 
    op = [AND, OR, XOR, SUB][op]

    #contar pixels maiores que 0 e realizar a operação na matriz
    for i in range(altura):
        for j in range(largura):
            imagem[id1][i][j]=op(bool(imagem[id1][i][j]//255), bool(imagem[id2][i][j]//255))

            if(imagem[id1][i][j]>0):
                maiores+=1

    #imprimir o texto pedido
    print(f"Imagem {id1} modificada: {maiores} pixels maiores que zero.")

def filtrar(id, filtro):
    #definir as variáveis que serão usadas
    altura=len(imagem[id])
    largura=len(imagem[id][0])
    maiores=0
    imagemaux=[]

    #criar uma matriz auxiliar com mesmas dimensões de imagem[id] e entradas 0, imagemaux
    for i in range(altura):
        lista=[]
        for j in range(largura):
            lista.append(0)

        imagemaux.append(lista)
        
    #definir os filtros do problema
    if(filtro=="Laplaciano"):
        filtro = [
            [-1, -1, -1],
            [-1,  8, -1],
            [-1, -1, -1]
        ]
    else:
        filtro = [
            [1,  4,  7,  4, 1],
            [4, 16, 26, 16, 4],
            [7, 26, 41, 26, 7],
            [4, 16, 26, 16, 4],
            [1,  4,  7,  4, 1]
        ]

    #definir "a" de forma que 2a+1 é a largura/altura do filtro
    a=(len(filtro)-1)//2

    #atualizar imagemaux para ser imagem[id] com o filtro aplicado, e contar os pixels maiores que 0
    for i in range(altura):
        for j in range(largura):
            #se não está na borda, aplique o filtro
            if(i>=a and j>=a and i<altura-a and j<largura-a):
                for k in range(-a, a+1):
                    for l in range(-a, a+1):
                        imagemaux[i][j]+=imagem[id][i+k][j+l]*filtro[a+k][a+l]

            if(imagemaux[i][j]>0):
                maiores+=1

    #imagem[id] recebe imagemaux (imagem[id] com filtro aplicado)
    for i in range(altura):
        for j in range(largura):
            imagem[id][i][j]=imagemaux[i][j]
    
    #imprimir o texto pedido 
    print(f"Imagem {id} modificada: {maiores} pixels maiores que zero.")

def gravar(nome, id):
    #definir as variáveis que serão usadas
    altura=len(imagem[id])
    largura=len(imagem[id][0])

    #salvar um arquivo .pgm com matriz imagem[id]
    with open(nome, "w") as arquivo:
        arquivo.write("P2\n")
        arquivo.write(f"# {nome}\n")
        arquivo.write(f"{largura} {altura}\n")
        arquivo.write("255\n")
        for i in range(altura):
            linha=""
            for j in range(largura):
                linha+=f"{imagem[id][i][j]} "
            linha+="\n"
            arquivo.write(linha)
    
    #imprimir o texto pedido 
    print(f"Gravado arquivo {nome} com imagem {id}.")
