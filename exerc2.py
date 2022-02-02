# Entrada do nome com tratamento
nome = input("Digite seu nome:").upper().replace(" ","")

#Saida do nome com tratamento/mostrando ele ao contrário
print(f"Seu nome em maiúsculas de trás pra frente é : {nome[::-1]}")