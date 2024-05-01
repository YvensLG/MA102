n = input()
m = ""

for i in n:
    if(i == i.upper()):
        m+=i.lower()
    else:
        m+=i.upper()

print(m)
