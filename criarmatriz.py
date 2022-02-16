m = []

l1 = []

l2 = []

l3 = []

n = int(input("Quer adcionar quantos itens nas listas dentro da matriz ?"))

for c in range(0,n):
    num = int(input("Digite um número para a lista 1:"))
    l1.append(num)
    if c == 4:
        for c in range(0,n):
            num = int(input("Digite um número para a lista 2:"))
            l2.append(num)
            if c == 4:
                for c in range(0,n):
                    num = int(input("Digite um número para a lista 3:"))
                    l3.append(num)
                    if c == 4:
                        for c in range(0,3):
                            while c == 0:
                                m.append(l1)
                                break
                            while c == 1:
                                m.append(l2)
                                break
                            while c == 2:
                                m.append(l3)
                                break

print("Sua matriz é :{}".format(m))