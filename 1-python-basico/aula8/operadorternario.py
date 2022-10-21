"""
OPERADOR TERNÁRIO EM PYTHON
"""

# logged_user = False
# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
# print(msg)

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    de_maior = (idade >= 18)
    msg = 'pode acessar.' if de_maior else 'não pode acessar.'
    print(msg)