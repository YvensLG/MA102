sudoku = []
for i in range(9):
    linha=input().split()
    sudoku.append(linha)

s = True 
total = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(9):
    for j in range(9):
        sudoku[i][j]=int(sudoku[i][j])

for i in range(9):
    vazio = set()
    for j in range(9):
        vazio.add(sudoku[i][j])

    if(vazio!=total):
        s=False
        
for i in range(9):
    vazio = set()
    for j in range(9):
        vazio.add(sudoku[j][i])

    if(vazio!=total):
        s=False

for i in range(0, 9, 3):
    vazio = set()
    for j in range(0, 9, 3):
        for k in range(0, 3):
            for l in range(0, 3):
                vazio.add(sudoku[i+k][j+l])
                
    if(vazio!=total):
        s=False

if(s):
    print("é sudoku")
else:
    print("não é sudoku")


'''
9 5 3 4 8 6 2 7 1
1 2 7 9 3 5 8 4 6
6 8 4 7 1 2 9 3 5
5 6 8 3 9 1 4 2 7
4 9 1 2 6 7 3 5 8
3 7 2 8 5 4 1 6 9
7 4 9 5 2 8 6 1 3
2 3 6 1 7 9 5 8 4
8 1 5 6 4 3 7 9 2
'''