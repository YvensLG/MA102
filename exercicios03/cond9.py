a, b, c = input().split()

a=int(a)
b=int(b)
c=int(c)

d=b*b-4*a*c

if(d==0):
    print("raiz única")
elif(d>0):
    print("raízes distintas")
else:
    print("raízes imaginárias")