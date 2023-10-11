import random

def eh_primo(num):
    for n in range(2,num):
        if (num % n) == 0:
            return False
    return True

def sao_primos_entre_si(n1, n2):
    rest = 1
    while n2 != 0:
        rest = n1 % n2
        n1 = n2
        n2 = rest
    if n1 == 1:
        return True
    else:
        return False


def  gerar_numero_primo():
    while True:
        x = random.randrange(0,100)
        if eh_primo(x):
            return x
def gerar_e (z):
    while True:
        e = random.randrange(2,z)
        if sao_primos_entre_si(e,z):
            return e
def gerar_d(e,z):
    while True:
        d = random.randrange(2,z)
        if e*d % z == 1:
            return d
def criptografar (txt,c_pub):
    n = c_pub[0]
    e = c_pub[1]
    msg_crip = []
    for i in range(len(txt)):
        letra = txt[i]
        k = ord(letra)
        x = (k ** e) % n
        msg_crip.append(x)
    return msg_crip
def decriptar(txt,c_priv):
    n = c_priv[0]
    d = c_priv[1]
    msg_original = ''
    for i in range(len(txt)):
        num = txt[i]
        x = (num**d) % n
        l = chr(x)
        msg_original += l
    return msg_original
if __name__ == '__main__':
    p = gerar_numero_primo()
    q = gerar_numero_primo()
    n = p * q
    z = (p-1) * (q - 1)
    e = gerar_e(z)
    d = gerar_d (e,z)
    c_pub = [n,e]
    c_priv = [n,d]

    txt = "meu nome é luffy e eu vou ser o rei dos piratas"

    txt_crip = criptografar(txt,c_pub)
    txt_orig = decriptar(txt_crip,c_priv)

    print(txt_crip)
    print(txt_orig)


