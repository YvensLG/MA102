a = int(input())
if(a%15==0):
    print(f"{a} é divisível por 3 e 5")
elif(a%3==0):
    print(f"{a} é divisível somente por 3")
elif(a%5==0):
    print(f"{a} é divisível somente por 5")
else:
    print(f"{a} não é divisível nem por 3 e nem por 5")