import gspread
from collections import defaultdict
import time
#https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf
gc = gspread.service_account(filename='academic-atlas-345823-ce14919e72bc.json')
sheets = \
    {'VENDAS':'https://docs.google.com/spreadsheets/d/1U1XDkHXGwVWOR78kJbSO82je6w4ooM94VSMuJiGymVc/edit?usp=sharing'}


def carregarTabelasBase():
    for planilha in sheets.values():
        time.sleep(3)
        sh = gc.open_by_url(planilha)
    dado = sh.worksheet('Página1')
    celula = dado.acell('F5').value
    com = defaultdict(list)
    dictmes = defaultdict(list)
    for c in range(5,23):
        if dado.find(dado.acell('F' + str(c)).value):
            fr = dado.acell('H' + str(c)).value
            f = fr.split()
            j = float(f[-1].replace(",00",""))
            com[dado.acell('F' + str(c)).value].append(j)
            l = dado.acell('A' + str(c)).value.replace("/","")
            dictmes['Comissões Mês ' + l[-5] + " " + dado.acell('F' + str(c)).value].append(j)
        time.sleep(3)
    for k,v in dictmes.items():
        v = str(sum(v))
        dictmes[k].append("Soma comissão desse mês = R$ " + v)

    print(f"Os valores das comissões  de cada funcionário é {com}")
    print(f"Valores das comissões de cada mês {dictmes}")
    print("Lendo a Planilha: ", celula)
carregarTabelasBase()