num = []
desordNum = []
for c in range(0,5):
    numer = int(input("Digite um número:"))
    num.append(numer)
    desordNum.append(numer)


num.sort()

if num == desordNum:
    print("True")
else:
    print("False")
