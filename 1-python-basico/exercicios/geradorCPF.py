from random import randint
numero = str(randint(10000000000, 99999999999))
novoCPF = numero

def calcDigito(numcpf, c):
    soma = 0
    for i in numcpf:
        mult = int(i) * c
        soma += mult
        c -= 1
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return digito

cpfVAL = novoCPF[:-2]

digito = calcDigito(cpfVAL, 10)
cpfVAL += str(digito)

digito = calcDigito(cpfVAL, 11)
cpfVAL += str(digito)

print(cpfVAL)

