texto = input()

texto = texto.replace(".", "")
texto = texto.replace(",", "")

lista = texto.split()

lista2 = []

for i in lista:
    if(len(i) <= 5 and not i in lista2):
        lista2.append(i.lower())

for i in lista2:
    print(f"{i} ")