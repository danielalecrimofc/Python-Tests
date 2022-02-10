cond = 0
num = int(input("Digte um número:"))
for c in range(1,100):
    if num % c == 0 or num / num == 0:
        cond += 1

if cond == 2:
    print("É número primo ")
elif num == 1 or num == 0:
    print("Não é número primo")
else:
    print("Não é número primo")

