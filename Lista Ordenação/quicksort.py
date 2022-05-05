#para cada valor na lista
def quick_sort(lista):
    tamanho = len(lista)
    if tamanho <= 1:
        return lista
    else:
        pivo = lista.pop()

    
    valores_maiores = []
    valores_menores = []

    for valor in lista:
        if valor > pivo:
            valores_maiores.append(valor)

        else:
            valores_menores.append(valor)

    return quick_sort(valores_menores) + [pivo] + quick_sort(valores_maiores)
