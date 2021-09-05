from random import randint
num = randnum = c = v = 0
d = " "
while True:
    num = int(input("Digite um número de 1 a 10: "))
    esclh = int(input("Digite 1 [Par] ou 2 [Ímpar] "))
    c += 1
    randnum = randint(1, 10)
    if (num + randnum) % 2 == 0:
        d = "PAR"
        if esclh == 1:
            print(f"\033[0:32:40m{num + randnum} é par você venceu!\033[m")
            v += 1
        if esclh == 2:
            print(f"\033[0:31:40m{num + randnum} é par Você perdeu!\033[m")
            break
    if (num + randnum) % 2 != 0:
        d = "ÍMPAR"
        if esclh == 2:
            print(f"\033[0:32:40m{num + randnum} é ímpar você venceu!\033[m")
            v += 1
        if esclh == 1:
            print(f"\033[0:31:40m{num + randnum} é impar e você perdeu!\033[m")
            break

print(f"\033[0:31:40mVocê escolheu {num} eo computador escolheu {randnum} com total de {randnum + num} que é {d}, o computador precisou {c} tentativa(s) para vencer!\033[m")
print(f"\033[0:31:40mGame Over com {v} vitorias\033[m")