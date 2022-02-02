# entrada para a primeira e em seguida entrada para a segunda palavra
primWord = str(input("Digite a primeira pálavra:")).rstrip()
secoWord = str(input("Digite a segunda palavra:")).rstrip()

# print mostrando as palavras em si e a quantidade de letras que possuem
print('A primeira palavra é : {} e contém {} letras'.format(primWord,len(primWord)))
print('A segunda palavra é : {} e contém {} letras'.format(secoWord,len(secoWord)))

#print("A primeira palavra é igual a segunda palavra ?:{}".format(primWord in secoWord)) primeira possibilidade

#if para comparar as duas palavras
if primWord[0:] == secoWord[0:]:
    print("As duas palavras são iguais")
else:
    print("As palavras não correspondem")
