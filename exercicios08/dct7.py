tup = (1, "Oi", 1, 2, 3, 4)
tup = list(tup)
tup1 =[]

for i in range(len(tup)-1, -1, -1):
    tup1.append(tup[i])

tup1 = tuple(tup1)

tup2 = list(tup1)
tup2 = tuple(tup2[1:4])

print(tup1)
print(tup2)