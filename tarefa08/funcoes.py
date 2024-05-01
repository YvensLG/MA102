def criar_gerenciador():
    return []

def criar_arquivo():
    #nome do arquivo, texto contido, usuario que o fez, data da criação e conjunto de todas as palavras do texto
    arquivo = {
        "nome": "",
        "texto": [],
        "usuario": "",
        "palavras": set(),
    }

    return arquivo

def terminar():
    print("até mais!")
    return False

def entrar(usuario):
    print(f"{usuario} entrou!")

def procurar_arquivo(gerenciador, nome):
    #se houver arquivo com o nome, devolva-o, se não houver, devolva None
    for arquivo in gerenciador:
        if arquivo["nome"] == nome:
            return arquivo
    return None

def criar(usuario, gerenciador, nome):
    #definir o arquivo que será criado
    arquivo = criar_arquivo()
    arquivo["nome"] = nome
    arquivo["usuario"] = usuario
    i = procurar_arquivo(gerenciador, nome)

    #analisar se um arquivo com mesmo nome já existe
    if i is None:
        gerenciador.append(arquivo)
        print(f"{nome} criado")
    else:
        print(f"{nome} existente")

def procurar_indice(gerenciador, nome):
    #se houver arquivo com o nome, devolva o seu índice, se não houver, devolva None
    for i, arquivo in enumerate(gerenciador):
        if arquivo["nome"] == nome:
            return i
    return None

def carregar_arquivo(usuario, gerenciador, nome_local, nome):
    #carregar texto do arquivo local
    with open(nome_local) as arquivo:
        texto = arquivo.read()
    
    #definir o arquivo que será criado
    arquivo = criar_arquivo()
    arquivo["nome"] = nome
    arquivo["usuario"] = usuario

    #separar o texto em linhas
    texto = texto.split("\n")
    texto.remove('')

    #separar as linhas em palavras
    for i in range(len(texto)):
        texto[i] = texto[i].split()

    arquivo["texto"] = texto

    #adicionar palavras do texto no conjunto
    for linha in texto:
        for palavra in linha:
            arquivo["palavras"].add(palavra)

    gerenciador.append(arquivo)
    print(f"{nome_local} carregado como {nome}")

def digitar(gerenciador, nome, linha):
    #acha o arquivo no gerenciador
    i = procurar_indice(gerenciador, nome)
    arquivo = gerenciador[i]

    #adiciona o texto
    linha = linha.split()
    arquivo["texto"].append(linha)

    #adicionar palavras do texto no conjunto
    for palavra in linha:
        arquivo["palavras"].add(palavra)

    linhas = len(arquivo["texto"])

    print(f"{nome} modificado: {linhas} linhas")

def mostrar(gerenciador, nome):
    #acha o arquivo
    arquivo = procurar_arquivo(gerenciador, nome)

    #imprime seu texto
    print(f"--- início de {nome} ---")

    for linha in arquivo["texto"]:
        for palavra in linha:
            print(palavra, end = " ")
        print()

    print(f"--- final de {nome} ---") 

def substituir(gerenciador, nome, termo, substituto):
    #acha o arquivo
    i = procurar_indice(gerenciador, nome)
    arquivo = gerenciador[i]

    #adiciona variáveis
    texto = arquivo["texto"]
    tem = False

    #substituir no texto
    for i in range(len(texto)):
        for j in range(len(texto[i])):
            if(texto[i][j] == termo):
                arquivo["texto"][i][j] = substituto
                tem = True
           
    #se houver o termo, o removemos do conjunto e adicionamos seu substituto
    if(tem):
        arquivo["palavras"].add(substituto)
        arquivo["palavras"].remove(termo)

    linhas = len(arquivo["texto"])

    print(f"{nome} modificado: {linhas} linhas")

def organizado(gerenciador_principal):
    #essa função devolve o gerenciador_principal organizado, mas sem alterá-lo
    #para isso criamos uma cópia e fazemos bubble sort

    gerenciador = criar_gerenciador()
    for arquivo in gerenciador_principal:
        gerenciador.append(arquivo)

    n = len(gerenciador)
    for _ in range(n-1):
        for i in range(n-1):
            if((gerenciador[i]["nome"] > gerenciador[i+1]["nome"])):
                aux = gerenciador[i]
                gerenciador[i] = gerenciador[i+1]
                gerenciador[i+1] = aux

    return gerenciador

def listar(gerenciador, argumento):
    #se o argumentoi é -t, imprimimos normalmente, já que o gerenciador já está em ordem cronológica 
    if(argumento=="-t"):
        for arquivo in gerenciador:
            print(arquivo["nome"], end=" ")
            print(arquivo["usuario"])
    
    #se não, imprimimos o gerenciador organizado
    else: 
        gerenciador_aux = organizado(gerenciador)

        for arquivo in gerenciador_aux:
            print(arquivo["nome"], end=" ")
            print(arquivo["usuario"])

    print(f"{len(gerenciador)} arquivos existentes")

def buscar(gerenciador, termo):
    gerenciador_aux = organizado(gerenciador)
    total=0

    #busca dentre o conjunto de palavras de todos os arquivos e imprime quais têm tal termo
    for arquivo in gerenciador_aux:
        if termo in arquivo["palavras"]:
            nome=arquivo["nome"]
            print(f"{nome} contém {termo}")
            total+=1

    print(f"{total} arquivos encontrados")

def comparar(gerenciador, nome1, nome2):
    #achar os arquivos com os nomes dados
    arquivo1 = procurar_arquivo(gerenciador, nome1)
    arquivo2 = procurar_arquivo(gerenciador, nome2)

    #adicionar as variávies linhas
    linhas1 = arquivo1["texto"]
    linhas2 = arquivo2["texto"]

    #imprimir caso as linhas sejam distintas
    for i in range(len(linhas1)):
        if(linhas1[i]!=linhas2[i]):
            print(f"<", end = " ")
            for palavra in linhas1[i]:
                print(palavra, end = " ")
            print()
    
    print("---")

    #imprimir caso as linhas sejam distintas
    for i in range(len(linhas2)):
        if(linhas2[i]!=linhas1[i]):
            print(f">", end = " ")
            for palavra in linhas2[i]:
                print(palavra, end = " ")
            print()
