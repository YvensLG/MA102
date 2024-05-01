def a():
    S=0
    for i in range(1, 51):
        S+=(2*i-1)/i
    
    print(S)

def b():
    S=0
    for i in range(1, 51):
        S+=(2**(51-i))/i
    
    print(S)

def c():
    S=0
    for i in range(1, 11):
        S+=((-1)**(i-1))*(i)/(i**2)
    
    print(S)

a()
b()
c()