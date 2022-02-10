capmaxima = int(input("Digite a quantidade máxima de clientes que pode receber:"))
clientes_iniciais = int(input("Quantos clientes acabaram de chegar no estabelecimento ?"))
start_clientes = clientes_iniciais
while start_clientes < capmaxima:
    num_clientes = int(input("Quantos clientes chegaram agora ?:"))
    if start_clientes <= capmaxima:
        print("Já temos {} clientes".format(start_clientes + num_clientes))
    start_clientes += num_clientes
    if start_clientes > capmaxima:
        print(f"Você teria agora {start_clientes} clientes")
        print(f'''Não podemos aceitar esses clientes,pois a capacidade máxima excederá em {start_clientes - capmaxima} clientes a mais !! ''')
    else:
        if start_clientes == capmaxima:
            print("Restaurante Lotou!!")
