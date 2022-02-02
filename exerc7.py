#Comando de atribuição da frase com tratamento/transformando tudo que for atribuido em letras minúsculas
frase = str(input("Digite uma palavra:")).lower()

#Saída/print mostrando quantos espaços em branco contém na frase
print("Na frase existem {} espaços em branco".format(frase.count(" ")))

#Saídas/prints mostrando quantas letras ('a','e','i','o','u') existem na frase
print( "A frase tem {} Letras a".format(frase.count('a')))
print( "A frase tem {} Letras e".format(frase.count('e')))
print( "A frase tem {} Letras i".format(frase.count('i')))
print( "A frase tem {} Letras o".format(frase.count('o')))
print( "A frase tem {} Letras u".format(frase.count('u')))