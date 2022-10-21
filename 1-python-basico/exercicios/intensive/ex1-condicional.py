# validação de login

usuario = input('Nome de Usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Rafa'
senha_bd = '1@2345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha incorretos.')