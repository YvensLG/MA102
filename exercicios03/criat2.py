idade = int(input("Qual sua idade?"))
classificacao = input("Qual a classificação do filme?")
acompanhado = input("Você está acompanhado?") == "sim"

if(idade<16 and classificacao!="livre" and (classificacao!="moderado" or idade<14) and (classificacao!="violento" or idade<14 or not acompanhado)):
    print("não")
else:
    print("sim")