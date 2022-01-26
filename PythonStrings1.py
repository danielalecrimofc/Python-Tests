#Entrada programa
print('=== Análise do nome ===')
#Input e atribuição do nome a variável 'nome'
nome = input('Qual é o seu nome ?').strip()
#print nome com todas as letras maiúsculas
print('Seu nome com todas as letras maiúsculas é : {}'.format(nome.upper()))
#print nome com todas as letras minúsculas
print('Seu nome com todas as letras minúsculas é : {}'.format(nome.lower()))
''' print mostrando quantas letras o nome tem ao todo sem 'considerar espaços' '''
#Comando len para mostrar a quantidade de caracteres que a string nome possui sem espaços
reparticao = nome.split()
#primeiro metódo
'''print('A frase tem ao todo {} caracteres sem considerar os espaços'.format(len(reparticao[0]+reparticao[1]+reparticao[2]+reparticao[3])))'''
#Metódo correto
print('A frase tem ao todo {} caracteres sem considerar os espaços'.format(len(nome) - nome.count(' ')))
#Quantas letras tem o primeiro nome da minha string
''' Metódo utilizando split e depois analisando a primeira lista formada '''
#Comando para dividir as plavras da minha string em novas listas
dividido = nome.split()
#Comando para pegar o primeiro nome e analisar quantas letras/caracteres ele tem
print('O primeiro nome da minha string é {} e ele tem {} caracteres'.format(dividido[0],len(dividido[0])))
''' Metódo utilizando o find encontrando o primeira palavra apartir do primeiro espaço'''
print('O primeiro nome da minha string tem {} caracteres'.format(nome.find(' ')))