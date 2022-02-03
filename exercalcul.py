#Entrada do programa
print("""==== Calculadora ==== 
==== Adição (1) ====
==== Subtração (2) ====
==== Multiplicação (3) ====
==== Divisão (4) ==== 
==== Opção Inválida (Other Number) ====""")

#Atribuição da opção
op = int(input("Digite uma das opções acima:"))

#Atribuição do primeiro número
num1 = int(input("Digite o primeiro número:"))

#Atribuição do segundo número
num2 = int(input("Digite o  segundo número:"))

#Condições para as opções
if op == 1:
    print("A soma dos dois números é igual a:{}".format(num1 + num2))
else:
    if op == 2:
        print("A subtração dos dois números é igual a:{}".format(num1 - num2))
    else:
        if op == 3:
            print("A multiplicação dos dois números é igual a:{}".format(num1 * num2))
        else:
            if op == 4:
                print("A divisão dos dois números é igual a:{}".format(num1 / num2))
            else:
                print("Opção inválida")
