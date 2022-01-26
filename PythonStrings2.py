#Entrada do Programa
''' forma com string que ainda n da certo
print('=== Análise do número ===')
#Atribuição
num = input('Digite um número de 0 a 9999: ')
num = ' '.join(num)
dividido = num.split()
print(dividido)
print('unidade = {} '.format(dividido[3]))
print('dezena = {} '.format(dividido[2]))
print('centena = {} '.format(dividido[1]))
print('milhar = {} '.format(dividido[0]))'''

''' forma com matématica '''
num = int(input('Digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade = {} '.format(u))
print('dezena = {} '.format(d))
print('centena = {} '.format(c))
print('milhar = {} '.format(m))