num_int = []
soma = 0
mult = 1
i = 0
while i < 5:
    num = int(input("Digite um número inteiro:"))
    num_int.append(num)
    i += 1
    if i == 5:
        j = 0
        while j < 5:
            soma += num_int[j]
            j += 1
            if j == 5:
                k = 0
                while k < 5:
                    mult *= num_int[k]
                    k += 1

print("A lista é {} | A soma dos números é = {} | a multiplicação é = {} ".format(num_int,soma,mult))


