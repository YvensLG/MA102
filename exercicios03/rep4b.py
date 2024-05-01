a = 1
b = 1
c = 0

print("1: 1")
print("2: 1")
for i in range(3, 21):
    c=a+b
    b=a
    a=c
    c=0
    print(f"{i}: {a}")
