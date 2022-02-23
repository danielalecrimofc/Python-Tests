numers = []
media = 0
soma_notes = 0
for c in range(0,4):
    num = float(input("Digite a {}º nota do aluno:".format(c+1)))
    numers.append(num)

    soma_notes += numers[c]

    if len(numers) == 3:
        media = soma_notes/4

print("A média do aluno é {:.2}".format(media))


