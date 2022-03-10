dados_jogador = {}

d = 0
qntgols = []
qntpart = 0
totalgols = 0
while d < 1:
    dados_jogador['nome'] = str(input("Digite o nome do jogador:"))
    dados_jogador['partidas'] = int(input("Digite quantas partidades ele jogou:"))
    qntpart = dados_jogador.get('partidas')
    if d == 0:
        i = 0
        while i < qntpart:
            numgols = int(input("Quantos gols o jogador fez na {}º partida".format(i+1)))
            qntgols.append(numgols)
            if i == qntpart - 1:
                f = 0
                while f < len(qntgols):
                    totalgols += qntgols[f]
                    if f == len(qntgols) - 1:
                        dados_jogador['gols'] = qntgols
                        dados_jogador['totaldegols'] = totalgols

                        for l,u in dados_jogador.items():
                            print(f"O campo {l} tem valor {u}!")

                        j = 0
                        for g in dados_jogador['gols']:
                            print(f"Na {j + 1}º partida o jogador fez {g} gols!")
                            j += 1
                    f += 1
            i += 1
    d += 1

print(dados_jogador)
