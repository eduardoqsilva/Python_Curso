from random import randint
from time import sleep
megaSena = []
lista = []
print("=-" * 30)
print(f"GERADOR DE NÚMEROS MEGA SENA ".center(55))
print("=-" * 30)
n = int(input("Quantos jogos? "))
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    megaSena.append(lista[:])
    lista.clear()
    tot += 1
print("=-"*30)
tot = 1
for c in megaSena:
    print(f"Jogo {tot}: {c}")
    tot += 1
   # sleep(1)
print("=-"*30)
print("~~ < Boa sorte! > ~~".center(50))
print("=-"*30)
