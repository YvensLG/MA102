a = input()
b = a[0]+a[1]
c = a[2]+a[3]

x=int(a)
y=int(b)
z=int(c)

if((y+z)**2 == x):
    print(f"{x} é especial")
else:
    print(f"{x} não é especial")