#Entrada do nome com tratamento/tirando todos os espaços a direita
nome = str(input("Digite seu nome:")).rstrip()

#Laço de repetição mostrando o nome letra por letra 
for x in nome:
    print(x)
