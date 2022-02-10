num = []

for c in range(0,5):
    numer=int(input("Digite um número:"))
    num.append(numer)

menorNum = num[0]
mNumer = 0
for c in range(0,5):
    if num[c] < menorNum:
        mNumer = num[c]

print(menorNum)
