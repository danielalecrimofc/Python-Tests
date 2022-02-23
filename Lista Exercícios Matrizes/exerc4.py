lista = []
vet_v = ["a","e","i","o","u"]
f = 0
lista_semv = []
for c in range(0,10):
    letras = str(input("Digite letras para serem adcioandas na lista:"))
    lista.append(letras)

    if len(lista) == 10:
        lista_semv = lista.copy()
        for x in range(0,5):
            if vet_v[x] in lista:
                f += lista_semv.count(vet_v[x])
                while lista_semv.count(vet_v[x]) > 0:
                    lista_semv.remove(vet_v[x])



print("Foram lidas {} consoantes".format(len(lista) - f))

print("As consoantes da lista são {}".format(lista_semv))