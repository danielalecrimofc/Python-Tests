import gspread
from collections import defaultdict
gc = gspread.service_account(filename='academic-atlas-345823-ce14919e72bc.json')
sheets = \
    {'VENDAS':'https://docs.google.com/spreadsheets/d/1U1XDkHXGwVWOR78kJbSO82je6w4ooM94VSMuJiGymVc/edit?usp=sharing'}


def carregarTabelasBase():
    for planilha in sheets.values():
        sh = gc.open_by_url(planilha)
    dado = sh.worksheet('Página1')
    celula = dado.acell('F5').value
    com = defaultdict(list)
    for c in range(5,23):
        if dado.find(dado.acell('F' + str(c)).value):
            fr = dado.acell('H' + str(c)).value
            f = fr.split()
            j = float(f[-1].replace(",00",""))
            com[dado.acell('F' + str(c)).value].append(j)
    for y,z in com.items():
        z = str(sum(z))
        com[y].append("<- Comissões -> Soma das comissões = R$" + z)

    print(f"Os valores das comissões e a soma da comissão de cada funcionário é {com}")
    print("Lendo a Planilha: ", celula)
carregarTabelasBase()
