'''Entrada de atribuição da frase com tratament/transformando tudo que for atribuido a variável em letras maiúsculas e trocando os espaços em branco por vazio'''
frase = str(input("Digite uma frase :")).upper().replace(" ","")

'''Comparando se o inicio da frase até o final é igual ao final até o inicio'''
if frase[0:] == frase[::-1]:
    print("É  um palíndromo")
else:
    print("Não é um palíndromo")