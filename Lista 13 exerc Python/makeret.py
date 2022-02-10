print("===== Criando um retângulo =====")
s_alt = "#"
s_larg = "#"
alt = int(input("Digite um número para a altura do retângulo:"))
largura = int(input("Digite um número para a largura do retângulo:"))

for c in range(0,1):
    print(f"{s_larg:#^{(largura * alt)+2}}")
for c in range(0,alt):
    print(f"{s_alt} {s_alt:>{largura * alt}}")
for c in range(0,1):
    print(f"{s_larg:#^{(largura * alt)+2}}")

