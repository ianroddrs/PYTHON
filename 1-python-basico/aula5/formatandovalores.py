"""
Formatando valores com modificadores

:s - strings
:d - int
:f - float

:.{numero}f - Quantidade de casas decimais (float)
:{caractere}{> ou < ou ^}{quantidade}{tipo - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
div = num1 / num2
print('{:.2f}'.format(div))
print(f'{div:.2f}')
# ---------------------------
num1 = 1
print(f'{num1:0>10d}')

num2 = 1150
print(f'{num2:0^11}')

print(f'{num2:0>10.2f}')

# ---------------------------
nome = 'Ian Rodirgues'
print(f'{nome:#^50}')
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
nome_formatado = '{n}{n}{n}'.format(n = nome)
nome_formatado = '{n:0<20}'.format(n = nome)
print(nome_formatado)

# ---------------------------
nome = 'ian'
sobrenome = 'rodrigues'
nome_formatado = '{0:º^10}{1:¨^18}'.format(nome,sobrenome)
print(nome_formatado)

# ---------------------------
nome = 'ryan'
nome = nome.ljust(20,'#')
print(nome)
# ---------------------------
nome = 'Norberto Vanches baRfENiNG'
print(nome.lower()) #letras minusculas
print(nome.upper()) #letras maiusculas
print(nome.title()) #primeiras letras maiusculas