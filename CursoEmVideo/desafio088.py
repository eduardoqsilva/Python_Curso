from random import randint
from time import sleep
megaSena = []
print("=-" * 30)
print(f"GERADOR DE NÚMEROS MEGA SENA ".center(55))
print("=-" * 30)
n = int(input("Quantos jogos? "))
for c in range(0, n):
    list = [randint(1, 60), randint(1, 60), randint(1, 60),
            randint(1, 60), randint(1, 60), randint(1, 60)]
    megaSena.append(list[:])
    list.clear()
print("=-" * 30)
print(f"SORTEANDO {n} JOGOS!".center(50))
print("=-" * 30)
for c in range(0, n):
    print(f"Jogo {c+ 1}: {megaSena[c]}")
    sleep(1)
print("=-" * 30)
print("~~ < BOA SORTE! > ~~".center(50))
