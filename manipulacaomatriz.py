matriz = []
auxm = []
somaim = 0
somaultc = 0

for i in range(0,3):
    for j in range(0,3):
        num = int(input("Digite um número:"))
        auxm.append(num)
        if num % 2 != 0:
            somaim += num
        elif len(auxm) == 9:
            auxm.sort()
            c = 0
            while c < 1:
                matriz.append(auxm[0:3])

                matriz.append(auxm[3:6])

                matriz.append(auxm[6:9])

                c += 1
            for a in range(0,3):
                for b in range(0,3):
                    while b == 2:
                        somaultc += matriz[a][b]
                        break


print(matriz)
print(somaim)

print(somaultc)