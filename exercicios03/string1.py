s = input()
s = s.replace(" ","")

for i in range(0, len(s)):
    if(s[i]!=s[len(s)-i-1]):
        print("Não é palíndromo\n")
        exit()

print("É palíndromo\n")