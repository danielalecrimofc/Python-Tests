'''Anos divisíveis pelo número 4 são considerados bissextos.
Anos divisíveis por 100 não são bissextos.
Anos divisíveis por 400 são bissextos.'''

'''com base em duas datas digitadas pelo usuário informe a quantidade de dias entre elas'''
diasm = [31,28,31,30,31,30,31,31,30,31,30,31]


diai = int(input("Digite o dia da data inicial:"))
mesi = int(input("Digite o mês da data inicial:"))
anoi = int(input("Digite o ano da data iniciall:"))

diac = int(input("Digite o dia da data chegada:"))
mesc = int(input("Digite o mês da data chegada:"))
anoc = int(input("Digite o ano da data chegada:"))

diaia = diai
mesia = mesi
anoia = anoi

diacb = diac
mescb = mesc
anocb = anoc

diaf = diac
mesf = 1
diast = 0
contdiasm = 0
while anoi != anoc:
    diasdomesat = diasm[mesi-1]
    for diai in range(diai,diasdomesat):
        diast += 1
        if diai == diasdomesat - 1:
            diai = 0


    mesi += 1

    if mesi == 13:
        mesi = 1
        anoi += 1


    if anoi == anoc:
        while mesf < mesc:
            diasdta = diasm[mesf - 1]
            for diai in range(diai,diasdta):
                diast += 1
                if diai == diasdta - 1:
                    diai = 0
            mesf += 1
            if mesf == mesc:
                diai = 1
                for diai in range(diai,diaf + 1):
                    diast += 1


print(f"Da data {diaia}/{mesia}/{anoia} até {diacb}/{mescb}/{anocb} passaram-se {diast} dias !")

