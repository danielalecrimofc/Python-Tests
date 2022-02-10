n = 0
for c in range(0,10):
    num = int(input("Digite um número:"))
    if num >= 10 and num < 51:
        n += 1
    else:
        print("Número fora do intervalo!")

print("Existem {} números entre 10 e 50".format(n))