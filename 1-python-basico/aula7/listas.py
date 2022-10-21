"""
Listas em Python
fatiamnento
append, insert, pop, del, clear, extend +
min, max
range
"""

lista = list(range(2,35,2))
print(lista)
lista2 = [3,3,2,3,3]

lista3 = lista2 + lista


lista.extend(lista2)
print(lista)

print(lista)
print((lista[0:11:3]))

lista.append('fim')
del(lista[4:9])
print(lista)

lista.insert(0,'inicio')
print(lista)

lista.pop(5)
print(lista)

lista.clear()
print(lista)

lista