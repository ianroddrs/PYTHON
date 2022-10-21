"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11; Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver 5 e 6 letras, escreva "Seu nome é
normal"; maior que 6 escreva "Seu nome é muito grande".
"""

def exercicios():
    resposta = 0
    while resposta != 4:
        resposta = menu()

def menu():
    print('Qual execício você gostaria de fazer?:')
    print('Ex.1 = 1')
    print('Ex.2 = 2')
    print('Ex.3 = 3')
    print('sair = 4')

    resposta = int(input())

    if resposta == 1:
        ex1()
    elif resposta == 2:
        ex2()
    elif resposta == 3:
        ex3()
    else:
        print('Você saiu do programa!')

    return resposta

#EXERCÍCIO 1
def ex1():
    numero = input('Digite um número inteiro: ')

    # isnumeric isdigit isdecimal

    if numero.isdigit():
        if int(numero) % 2 == 0:
            print(f'{numero} é PAR')
        else:
            print(f'{numero} é ÍNMPAR')
    else:
        print('Não foi digitado um número inteiro.')

#EXERCÍCIO 2
def ex2():
    hora = input('Digite a hora atual (0-23): ')
    if hora.isdigit():
        hora = int(hora)

        if hora < 0 or hora > 23:
            print('Horário deve estar entre 0 e 23.')
        else:
            if hora <= 11:
                print('Bom dia!')
            elif hora <= 17:
                print('Boa tarde!')
            else:
                print('Boa noite!')
    else:
        print('Por favor, digite um npumero entre 0 e 23.')

#EXERCÍCIO 3
def ex3():
    nome = input('Digite o seu primeiro nome: ')
    tamanho = len(nome)

    if tamanho <= 4:
        print("Seu nome é curto")
    elif tamanho <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")

exercicios()