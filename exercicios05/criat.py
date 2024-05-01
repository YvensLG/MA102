def numero_palavras(texto):
    contador = 0

    for i in texto.split():
        if i[-1]=='s':
            contador+=1

    return contador
        
def eh_plural(palavra):
    return palavra[-1]=='s'

def numero_palavras2(texto):
    contador = 0

    for i in texto.split():
        if eh_plural(i):
            contador+=1

    return contador

#palavra dada
#local inicio/fim
#interesse string que quero localizar

def eh_legal(palavra, local, interesse):
    if len(palavra)<len(interesse):
        return False

    if local=='inicio':
        for i in range(len(interesse)):
            if(interesse[i]!=palavra[i]):
                return False
        
        return True
    
    if local=='fim':
        for i in range(len(interesse)):
            if(interesse[-i-1]!=palavra[-i-1]):
                return False
        
        return True

def numero_palavras2(texto):
    contador = 0

    for i in texto.split():
        if eh_legal(i):
            contador+=1

    return contador