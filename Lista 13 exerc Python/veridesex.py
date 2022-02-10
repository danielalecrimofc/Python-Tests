M_cont = 0
F_cont = 0
M_list = []
F_list = []
F_soma = 0
M_soma = 0
print("""==== Avaliando idade media dos grupos ====
==== Digite a seguir seu sexo e sua idade ====
==== Se for masculino digite 'M' ====
==== Se for feminino digite 'F' ====""")
for c in range(0,10):
    sex = str(input("Qual seu sexo:")).upper()
    if sex == 'M':
        idade = int(input("Qual sua idade:"))
        M_list.append(idade)
        M_cont+=1
    else:
        if sex == 'F':
            idade = int(input("Qual sua idade:"))
            F_list.append(idade)
            F_cont+=1
        else:
            print("Opção inválida!!")

for c in range (0,len(F_list)):
    F_soma += F_list[c]

for c in range (0,len(M_list)):
    M_soma += M_list[c]

print(f"A média de idade entre os homens é:{M_soma//M_cont} anos")
print(f"A média de idade entre as mulheres é:{F_soma//F_cont} anos")
print(f"A média de idade do grupo é:{(M_soma+F_soma)//10} anos")
