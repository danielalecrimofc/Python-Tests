lista = []
matriz = []

for c in range(0,3):
    for d in range(0,2):
        num = int(input("Digite um número:"))
        lista.append(num)
        if len(lista) == 6:
            j = 0
            k = 2
            for f in range(0,3):
                matriz.append(lista[j:k])
                j += 2
                k += 2
#By Daniel Sam cria qualquer matriz ;)
# Instruções:
# O primeiro e o terceiro for tem que ter o mesmo intervalo
# A variável j dentro do if será igual a 0 e o k igual ao número de colunas
# Na iteração do terceiro for as duas variáveis somam a quantidade do número de colunas mais ela mesmo

print(matriz)
