lista = []

for c in range(0,5):
    num = int(input("Digite um número:"))
    lista.append(num)

def menor_num(lista):
    indice_m = 0
    menor_num = lista[indice_m]
    for d in range(0,len(lista)):
        if menor_num > lista[d]:
            menor_num = lista[d]
            indice_m = d
    return indice_m

def ordenacao(lista):
    lista_ord = []
    for e in range(0,len(lista)):
        indice_menor_valor = menor_num(lista)
        lista_ord.append(lista.pop(indice_menor_valor))

    return lista_ord

print(ordenacao(lista))