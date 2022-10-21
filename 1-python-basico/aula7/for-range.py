"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
#
# for n in range(100,49,-5):
#     print(n)
#
# print('##################')
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n

texto = 'Python'
nova_string = ''

# continue - pula para a proxima laço de iteração
# break - sai do laço de iteração

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)