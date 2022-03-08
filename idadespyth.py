'''com base em duas datas digitadas pelo usuário informe a quantidade de dias entre elas'''
diasm = [31,28,31,30,31,30,30,31,31,30,31,30,31]


diai = int(input("Digite o dia da data inicial:"))
mesi = int(input("Digite o mês da data inicial:"))
anoi = int(input("Digite o ano da data iniciall:"))

diac = int(input("Digite o dia da data chegada:"))
mesc = int(input("Digite o mês da data chegada:"))
anoc = int(input("Digite o ano da data chegada:"))

diast = 0
contdiasm = 0
while anoi != anoc:
    diasdomesat = diasm[mesi-1]
    while diai < diasdomesat:
        diast += 1
        if diai == diasdomesat - 1:
            diai = 0

    mesi += 1
    if mesi == 13 :
        mesi = 1
        anoi += 1

    if diai == diac and mesi == mesc and anoi == anoc:
        break

print(diast)



'''07/03/1990
12/07/1990'''
