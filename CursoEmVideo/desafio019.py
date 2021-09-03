from random import choice

n = str(input("digite o primeiro nome: "))
n2 = str(input("digite o segundo nome: "))
n3 = str(input("digite o terceiro nome: "))
n4 = str(input("digite o querto nome: "))
n5 = str(input("digite o quinto nome: "))
lista = [n, n2, n3, n4, n5]
r = choice(lista)
print("O escolhido foi: {}".format(r))

