'''Entrada do Programa'''
print('==== Verificação nome da Cidade ====')
print('||||Se a Palavra (Santo) estiver no começo do nome da cidade será exibido a frase (true) caso contrário será exibido (false)||||')
cidade = str(input('Qual cidade você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')