s = input()
letra = input()
r = ""

for i in range(0, len(s)):
    if(s[i]!=letra):
        r+=s[i]
    else:
        break

print(r)
