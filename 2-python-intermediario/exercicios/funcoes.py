# # 1
# def cumprimento(saudacao, nome):
#     print(f'{saudacao}, {nome}')
# cumprimento('bom dia', 'ian')
# print()
#
# # 2
# def soma3(n1,n2,n3):
#     soma = n1+n2+n3
#     return soma
# n1 = int(input('n1: '))
# n2 = int(input('n2: '))
# n3 = int(input('n3: '))
# result = soma3(n1,n2,n3)
# print(f'resposta: {result}')
# print()
#
# # 3
# def somaporcen(val, perc):
#     total = val + (val*(perc/100))
#     return total
# valor = int(input('Valor: '))
# porcentagem = int(input('Porcentagem: '))
# resposta = somaporcen(valor, porcentagem)
# print(resposta)

# 4
def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return f'FizzBuzz'
    if num % 5 == 0:
        return f'Buzz'
    if num % 3 == 0:
        return f'Fizz'
    return num

me = fizzbuzz(int(input('numero: ')))
print(me)

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(fizzbuzz(aleatorio))