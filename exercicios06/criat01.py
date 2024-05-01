def ordenar_time(lista_nomes, funcao_comparar, confrontos):
    n=len(lista_nomes)
    for _ in range(n-1):
        for i in range(n-1):
            if(funcao_comparar(lista_nomes[i+1], lista_nomes[i], confrontos)):
                aux=lista_nomes[i]
                lista_nomes[i]=lista_nomes[i+1]
                lista_nomes[i+1]=aux
    return lista_nomes

def comparar(time_x, time_y, confrontos):
    time0=0
    time1=0
    desempate=-1
    for i in confrontos:
        if time_x==i[0]:
            time0+=1
            if(time_y==i[1]):
                desempate=0
        if time_y==i[0]:
            time1+=1
            if(time_x==i[1]):
                desempate=1

    if(time0>time1):
        return True
    if(time0==time1):
        return desempate==0
    return False

def main():
    confrontos = [
        ("Estaleiro", "Mavista"),
        ("Estaleiro", "Manos"),
        ("Estaleiro", "São Saulo"),
        ("Mavista", "Manos"),
        ("Mavista", "São Saulo"),
        ("Mavista", "Tio de Janeiro"),
        ("Tio de Janeiro", "Estaleiro"),
        ("Tio de Janeiro", "Manos"),
        ("Manos", "São Saulo"),
        ("São Saulo", "Tio de Janeiro"),
    ]

    lista_nomes = ["Estaleiro", "Mavista", "Manos", "São Saulo", "Tio de Janeiro"]

    lista = ordenar_time(lista_nomes, comparar, confrontos)

    print(lista)

main()