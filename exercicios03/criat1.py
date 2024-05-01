x = int(input())
y = int(input())

#x=a, y=b
x=x+y
#x=a+b, y=b
y=x-y
#x=a+b, y=a+b-b=a
x=x-y
#x=a+b-a=b, y=a

print(f"{x} {y}")

#é confuso e faz mais sentido colocar uma variável auxiliar, acredito que seja por isso que não é recomendado