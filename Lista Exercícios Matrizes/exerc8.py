matriz = []
lista_id_alt = []
l = 0
m = 2
for c in range (0,5):
    for d in range(0,1):
        idade = int(input("Digite sua idade:"))
        altura = float(input("Digite sua altura:"))

        lista_id_alt.append(idade)
        lista_id_alt.append(altura)

        while l < 9 and m <= 10:
            matriz.append(lista_id_alt[l:m])

            l += 2
            m += 2
            break

matriz = sorted(matriz,reverse=True)

print(matriz)
