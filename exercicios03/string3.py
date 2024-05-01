t = input()
p = input()
contador=0

t=t.replace(".", "")
t=t.replace(",", "")
t=t.replace(";", "")

r = t.split()

for i in r:
    if(i==p):
        contador+=1

print(f"{contador}\n")

#não fiz a parte de imprimir a posição por que não entendi direito a contagem, se conta ou não espaços.