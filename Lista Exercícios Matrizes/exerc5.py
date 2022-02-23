lista_20 = []

lista_pares = []

lista_impares = []

for c in range(0,20):
    num = int(input("Digite um número:"))
    lista_20.append(num)
    if len(lista_20) == 20:
        for c in range(0,20):
            if lista_20[c] % 2 == 0:
                lista_pares.append(lista_20[c])
            else:
                if lista_20[c] % 2 != 0:
                    lista_impares.append(lista_20[c])

print("Todos os números dentro da lista :{}".format(lista_20))
print("Números pares:{}".format(lista_pares))
print("Números impares:{}".format(lista_impares))
