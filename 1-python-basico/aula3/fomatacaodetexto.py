"""
Variáveis
    iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Ian Rodrigues'
idade = 21
altura = 1.71
e_maior = idade > 18
peso = 70
imc = 'temp'

imc = peso/altura**2

print(nome, 'tem', idade,'anos de idade e seu imc é:',imc)

# Formatação de texto

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')

print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc))

print('{2} tem {0} anos de idade e seu imc é: {1:.2f}'.format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu imc é: {im:.2f}'.format(n=nome, i=idade, im=imc))
