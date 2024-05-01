print("Nome do doador(a): ")
nome = input()
print("Idade: ")
idade =int(input())

if idade<16 or idade>69:
    print("Doador não atende os requisitos de idade.")
else:
    if idade>60:
        print("Já realizou doação anterior (S/N)? ")
        if(input()=="S"):
            print("Idade da primeira doação: ")
            if(int(input())<=60):
                print("Doador apto. Encaminhar para a próxima etapa!")
            else:
                print("Doador não atende os requisitos de idade.")
        else:
            print("Doador não atende os requisitos de idade.")

    if(idade<18):
        print("Possui documento de autorização (S/N)?")
        if(input()=="S"):
            print("Doador apto. Encaminhar para a próxima etapa!")
        else:
            print("Doador não atende os requisitos de idade.")

    if(idade>=18 and idade<=60):
        print("Doador apto. Encaminhar para a próxima etapa!")
