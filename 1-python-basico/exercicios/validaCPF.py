# CPF = input('Digite um CPF (apenas números): ')
#
# M1 = 10; M2 = 11
# S1 = 0; S2 = 0
#
# for i in range(len(CPF)-2):
#     S1 += int(CPF[i]) * M1
#     S2 += int(CPF[i]) * M2
#     M1 -= 1
#     M2 -= 1
#
# D1 = 0 if (11 - (S1 % 11)) > 9 else (11 - (S1 % 11))
# D2 = 11 - (S2 % 11)
#
# print(D1, D2)
#
# if int(CPF[10]) == D2 and int(CPF[9]) == D1:
#     print('CPF VÁLIDO')
# else:
#     print('CPF INVÁLIDO')
#
# Loop infinito

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

cpf = input('Digite um CPF: ')
cpfVAL = cpf[:-2]

digito = calcDigito(cpfVAL, 10)
cpfVAL += str(digito)

digito = calcDigito(cpfVAL, 11)
cpfVAL += str(digito)

if cpf == cpfVAL:
    print('Válido')
else:
    print('Inválido')
