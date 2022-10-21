# Declaração
thislist = ["apple", "banana", "cherry"]
print(thislist)

# métodos

#  index
lista = ['Carro', 'Casa', 'Hotel', 'Casa']
pos = lista.index('Casa')
print(f'O item desejado está na posição: {pos}')
# O item desejado está na posição: 1

# Count
lista = ['Carro', 'Casa', 'Hotel', 'Casa']
pos = lista.count('Casa')
print(f'O item desejado aparece: {pos}')
# O item desejado aparece: 2

#  append
lista = ['Python', 'Academy']
lista.append('adicionado')
print(lista)
# ['Python', 'Academy', 'adicionado']

# insert
lista = ['Python', 'Academy']
lista.insert(0, 'Blog')
print(lista)
#['Blog', 'Python', 'Academy']

# extend
sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']
sacola.extend(legumes)
print(sacola)
# ['Laranja', 'Banana', 'Xuxu', 'Batata']

# remove
lista = ['Blog', 'Python', 'Academy']
lista.remove('Blog')
print(lista)
# ['Python', 'Academy']

# del - outra forma
lista = [10, 20, 30, 40, 50]
del lista[2]
print(lista)
# [10, 20, 40, 50]

# pop
lista = ['Banana', 'limão', 'Carro', 'Laranja']
item = lista.pop(2)
print('Item:', item)
print('Lista: 'lista)

# clear
lista = [10, 20, 40, 50]
lista.clear()
print(lista)
# []

#  copy
lista = ['Python', 'Academy']
lista_copiada = lista.copy()
print(lista_copiada)
print(lista)

# reverse
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

#  sort
lista = [1, 4, 5, 2, 4]
lista.sort()
print(lista)