print("Vamos calculara a media de 10 alunos")
''' matriz 10 / 4'''
lista = []
matriz = []
matriz_medias = []
receb = 0
j = 0

l = 0
m = 4

for c in range(0,10):
    j = 0
    while j < 4:
        nota = float(input("Digite a {}º nota:".format(j+1)))
        lista.append(nota)

        j+=1
        if len(lista) == 40:
            while l < 39 and m <= 40:
                matriz.append(lista[l:m])
                l += 4
                m += 4
                continue

f = 0
for a in range(0,10):
    for b in range(0,4):
        if a == f:
            receb += matriz[a][b]
        if b == 3:
            matriz_medias.append(receb/4)
            print("A media do {}º aluno é {}".format(a + 1,matriz_medias[a]))
            f += 1
            receb = 0

""" Fela da ****** resolvi kr********"""
print(receb)
print(matriz)
print(matriz_medias)


