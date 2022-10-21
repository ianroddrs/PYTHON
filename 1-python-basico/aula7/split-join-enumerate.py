"""
Split, Join, Enumerate em Python
*Split - divide uma string
*Join - Junta uma string
*Enumerate - Enumera elementos da

.strip() - tira o espaço do inicio e fim de uma string
"""
#SPLIT
# string = "O Brasil é o país do futebol, o Brasil é penta."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#     print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
# print(f'\nA palavra que apareceu mais vezes é {palavra} ({contagem}x)\n\n')
#
# for valor in lista_2:
#     print(valor.strip().capitalize())

#JOIN
#
# string = 'O Brsil é penta'
# lista = string.split(' ')
# string2 = '*//'.join(lista)
#
# print(string)
# print(lista)
# print(string2)

#ENUMERATE

string = 'O brasil é penta.'
lista = string.split()

for indice, valor in enumerate(lista, 10):
    print(indice, valor)
print(list(enumerate(lista)))