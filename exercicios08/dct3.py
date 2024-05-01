texto = input()
palavras = texto.split()

dict1 = {}
dict2 = {}

for i in palavras:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1

for i in texto:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1

print(dict1)
print(dict2)