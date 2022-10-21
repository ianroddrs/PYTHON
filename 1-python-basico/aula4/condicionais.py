# validação de login

usuario = input('Nome de Usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Ian'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistemas.')
else:
    print('Usuário ou senha inválidos.')
