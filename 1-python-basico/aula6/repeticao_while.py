"""
while em python
utilizando para realizar ações enquanto uma condição for verdadeira.
"""

# while True: #loop infinito
#     nome = input('Qual o seu nome?')
#     print(f'Olá {nome}!')

# -----------------------------------


x = 0
while x <= 100:
    print(x)
    x += 1



# -----------------------------------
# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         continue # volta para a parte de cima do loop
#     print(x)
#     x += 1
# print('acabou!')

# ----------------------------------
# x= 0
# while x < 10:
#     if x == 3:
#         x += 1
#         break # finaliza o loop
#     print(x)
#     x += 1
# print('acabou!')

# ---------------------------------
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1
print('acabou')