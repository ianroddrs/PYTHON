"""
ENTRADA DE DADOS
"""

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')

ano_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {ano_nascimento}.')