# CONDICIONAL IF
a = 33
b = 200
if b > a:
  print("b is greater than a")

# CONDICIONAL ELIF
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# CONDICIONAL ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# ELSE E ELIF

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# IF CURTO
if a > b: print("a is greater than b")

#IF ELSE CURTO
a = 2
b = 330
print("A") if a > b else print("B")

#IF ELSE CURTO COM MAIS DE 2 DECLARAÇÕES
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# IF ANINHADO
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# PASS
a = 33
b = 200

if b > a:
  pass

# OR CONDICIONAL
nome = input('Qual seu nome? ')

 if nome:
     print(nome)
 else:
     print('Você não digitou nada.')

print(nome or 'Você não digitou nada!')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print(variavel)