#Entrada do nome com tratamento/tirando todos os espaços a direita
nome = str(input("Digite seu nome:")).rstrip()

#Laço de repetição for com tratamento/mostrando o nome em formato de escada de modo decrescente
for x in range(0,len(nome)+1):
    print(nome[:x])
