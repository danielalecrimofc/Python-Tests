lista_reais = []
lista_inversa = []
c = 0
"""for c in range(0,10):
    num = float(input("Digite um número:"))
    lista_reais.append(num)

    if c == 9:
        print(f"Seus números reais na ordem inversa são:")
        while c > 0:
            lista_inversa.append(lista_reais[c])
            c -= 1"""

while c < 10:
    num = float(input("Digite um número:"))
    lista_reais.append(num)

    c += 1
    if c == 10:
        i = 9
        while i >= 0:
            lista_inversa.append(lista_reais[i])
            i -= 1

print(f"A lista na ordem inversa é:{lista_inversa}")