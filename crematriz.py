lista1 = []
lista2 = []
matriz = []
op = 0

print("""==== Adcionar lista dentro de outra ====
==== Digite (0)/Para adcionar lista a outra ====
==== Digite qualquer número para sair ====""")

op = int(input("Digite uma opção:"))

if op == 0:
    for c in range(0,4):
        num = int(input("Digite um valor para a primeira lista:"))
        lista1.append(num)
        if c == 3:
            for d in range(0,4):
                numer = int(input("Digite um valor para a segunda lista:"))
                lista2.append(numer)
                if d == 3:
                    matriz.append(lista1)
                    matriz.append(lista2)
                    print("Sua matriz é:{}".format(matriz))
else:
  f = 0
  while f < 1:
    print("Opção errada")
    break
    f+=1
