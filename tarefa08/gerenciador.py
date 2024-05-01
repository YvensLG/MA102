import funcoes

def main():
    #definir variaveis a serem usadas
    gerenciador = funcoes.criar_gerenciador()
    rodar=True
    usuario = ""
    while(rodar):

        #analisar qual funcao foi digitada
        aux = input().split(" ", 1)
        funcao = aux[0]

        if(len(aux)>1):
            entrada = aux[1]
        else:
            entrada = ""
        
        if(funcao == "terminar"):
            rodar = funcoes.terminar()

        elif(funcao == "entrar"):
            usuario = entrada
            funcoes.entrar(usuario)

        elif(funcao == "criar"):
            nome = entrada
            funcoes.criar(usuario, gerenciador, nome)

        elif(funcao == "carregar"):
            nome_local, nome = entrada.split(" ", 1)
            funcoes.carregar_arquivo(usuario, gerenciador, nome_local, nome)

        elif(funcao == "digitar"):
            nome, texto = entrada.split(" ", 1)
            funcoes.digitar(gerenciador, nome, texto)
        
        elif(funcao == "mostrar"):
            nome = entrada
            funcoes.mostrar(gerenciador, nome)

        elif(funcao == "substituir"):
            nome, termo, substituto = entrada.split(" ", 2)
            funcoes.substituir(gerenciador, nome, termo, substituto)
        
        elif(funcao == "listar"):
            argumento=entrada
            funcoes.listar(gerenciador, argumento)

        elif(funcao == "buscar"):
            termo=entrada
            funcoes.buscar(gerenciador, termo)

        elif(funcao == "comparar"):
            nome1, nome2 = entrada.split(" ", 1)
            funcoes.comparar(gerenciador, nome1, nome2)
main()