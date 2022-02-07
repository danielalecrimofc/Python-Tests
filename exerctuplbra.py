#Declaração da tupla
times = ('América-MG','Athletico','Atlético-GO','Atlético-MG','Bahia',
        'Bragantino','Ceará','Chapecoense','Corinthians','Cuiabá',
        'Fortaleza','Flamengo','Fluminense','Grêmio','Internacional'
        'Juventude','Palmeiras','Santos','São Paulo','Sport')

#Tabela com as opções para a escolha do úsuario
print('''==== Tabela 20 primeiros colocados campeonato Brasileiro ===="
      ==== Opção 1 (Ver os primeiros 5 colocados) ====
      ==== Opção 2 (Ver os últimos 4 colocados) ====
      ==== Opção 3 (Uma lista com os time em ordem alfábetica) ====
      ==== Opção 4 (Ver em que posição o time está na tabela) ====
      ==== Outra Opção(Opção inválida)===''')

#Entrada da opção
oP = int(input("Digite uma opção:"))

#Laço de repetição
for c in range(0,20):
    if oP == 1:
        print(f"Os cinco primeiros colocados são:{times[c:5]}")
        break
    else:
        if oP == 2:
            print(f"Os quatro últimos colocados são:{times[15:]}")
            break
        else:
            if oP == 3:
                y = list(times)
                print(f"Os time em ordem alfabética são {y}")
                break
            else:
                if oP == 4:
                    nome_time = str(input("Qual time quer saber a posição:"))
                    if nome_time in times[0:]:
                        print("O time {} está na posição {}".format(nome_time,c))
                    else:
                        print("Time não encontrado")
                else:
                    print("Opção inválida")
                    break
