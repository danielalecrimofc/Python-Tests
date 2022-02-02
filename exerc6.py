#Criação de tupla para guardar os valores strings dos meses do ano
meses = ("","Janeiro","Fevereiro","Março","Maio",
         "Abril","Junho","Julho","Agosto",
         "Setembro","Outubro","Novembro","Dezembro")

#Print exemplificando o que deve ser feito para o usuário
print("Digite sua data de nascimento nesse formato 'dd/mm/aaaa'")

#Laço de repetição while que ira receber o dia o mês e o ano e ira pegar o mes para fazer o tratamento dentro do if
while True:
    dia = int(input("insira o dia:"))
    mes = int(input("insira o mês:"))
    ano = int(input("insira o ano:"))
    # If para fazer o tratamento do mês verificando se ele está no intervalo entre 0 e 12
    if 0 <= mes <= 12:
        break
    print("Esse mês não existe.\n")

#Print mostrando o dia em númerico o mês em extenso e o ano em númerico
print(f'Você nasceu no dia {dia} do mês de {meses[mes]} de {ano}')