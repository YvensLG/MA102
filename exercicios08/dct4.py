time = {}
n = int(input("quantidade de partidas:\n"))
for _ in range(n):
    partida = input().split(" ")

    time1 = partida[0]
    gol1 = int(partida[1])
    time2 = partida[3]
    gol2 = int(partida[4])

    if(gol1 == gol2):
        pontos1 = 1
        pontos2 = 1
    elif(gol1 > gol2):
        pontos1 = 3
        pontos2 = 0
    elif(gol1 < gol2):
        pontos1 = 0
        pontos2 = 3

    if time1 in time:
        time[time1][0]+=pontos1
        time[time1][1]+=gol1-gol2
    else:
        time[time1] = [pontos1, gol1-gol2]

    if time2 in time:
        time[time2][0]+=pontos2
        time[time2][1]+=gol2-gol1
    else:
        time[time2] = [pontos2, gol2-gol1]

listatime=[]

for i in time:
    listatime.append([i, time[i][0], time[i][1]])


n = len(listatime)

for _ in range(n-1):
    for i in range(n-1):
        if((listatime[i][0] > listatime[i+1][0]) or (listatime[i][0] == listatime[i+1][0] and listatime[i][1] > listatime[i+1][1])):
                aux = listatime[i]
                listatime[i] =listatime[i+1]
                listatime[i+1] = aux

print("Time       Pontos      Saldo")
for i in listatime:
    print(f"{i[0]}     {i[1]}     {i[2]}")