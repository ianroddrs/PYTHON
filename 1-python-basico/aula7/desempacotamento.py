"""
DESEMPACOTAMENTO DE LISTAS EM PYTHON
"""

lista = ['nome1','nome2', 'nome3', 1,2,3,4,5,6,7,8,9,1000]

n1,n2,n3, *restante, ultimo = lista #*_ indica que os outros elementos nçao serão utilizados

print(n1, n2, restante)
print(ultimo)