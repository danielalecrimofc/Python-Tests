#Entrada do programa
def tela():
    print("""==== Calculadora ==== 
==== Adição (1) ====
==== Subtração (2) ====
==== Multiplicação (3) ====
==== Divisão (4) ==== 
==== Parar Programa (5) ====""")

def calculator():

    #Atribuição da váriavel global op
    global op

    #Atribuição da váriavel local cond
    cond = 0

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
                    while op > 4 or cond < 0 or op <= 0:
                        cond += 1
                        break

#Chamada da tela
tela()

# Atribuição da opção
op = int(input("Digite uma das opções acima:"))

# Atribuição do primeiro número
num1 = int(input("Digite o primeiro número:"))

# Atribuição do segundo número
num2 = int(input("Digite o  segundo número:"))
calculator()

#Atribuição da váriavel 'c' para o primeiro laço de repetição
c = 0

#Atribuição da variável 'f' para o segundo laço de repetição
f = 0

'''While com condicional para rodar constantemente até que a condição
seja estabelecida'''
while c != 10000:
    c += 1
    while op > 4 or f < 0 or op <= 0:
        f += 1
        break
    else:
        if op != 5:
            #Chamada da tela dentro da condicional
            tela()

            # Atribuição da opção dentro da condicional
            op = int(input("Digite uma das opções acima:"))

            # Atribuição do primeiro número dentro da condicional
            num1 = int(input("Digite o primeiro número:"))

            # Atribuição do segundo número dentro da condicional
            num2 = int(input("Digite o  segundo número:"))
            calculator()
