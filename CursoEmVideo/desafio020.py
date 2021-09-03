import random
n = str(input("digite um nome: "))
n2 = str(input("digite outro nome: "))
n3 = str(input("digite outro: "))
n4 = str(input("digite mais um: "))
lista = [n, n2, n3, n4]
r = random.shuffle(lista)
print("a ordem é: {}".format(lista))
