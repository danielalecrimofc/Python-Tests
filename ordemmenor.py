matriz = []

newmatriz = []

for i in range(0,3):
    for j in range(0,3):
        num = int(input("Digite um valor para a matriz:"))
        matriz.append(num)
        if len(matriz) == 9:
            matriz = sorted(matriz)

c = 0
while c<1:
    newmatriz.append(matriz[0:3])

    newmatriz.append(matriz[3:6])

    newmatriz.append(matriz[6:])

    c += 1

print("Sua matriz é :{}".format(newmatriz))


