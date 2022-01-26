# Declarando a Lista de nomes
lista_nomes = []
# For para a contagem de 0 até 5
for c in range(0,5):
    nome = str(input('Digite seu nome :'))
# Função .append() usada para adcionar  os nomes salvos na var(nome) no final da lista (lista_nomes = [])    
    lista_nomes.append(nome)
# Print fora do laço para se referir as pessoas dentro da lista
print('Os nomes das pessoas na lista são:')   
# For com print dentro para mostrar os nomes das pessoas
for c in lista_nomes:
    print(c)