from random import randint
num = randnum = c = v = 0
d = " "
print("*"*20,"PAR OU ÍMPAR","*"*20)
while True:
    num = int(input("Digite um número de 1 a 10: "))
    while num > 10:
        num = int(input("Digite um número de 1 a 10: "))
    esclh = str(input("Digite [P] para par ou [I] para ímpar: ")).strip().upper()[0]
    while esclh != "P" and esclh != "I":
        esclh = str(input("Digite [P] para par ou [I] para ímpar: ")).strip().upper()[0]
    c += 1
    randnum = randint(1, 10)
    if (num + randnum) % 2 == 0:
        d = "PAR"
        if esclh == "P":
            print(f"\033[0:32:40m{num + randnum} é par você venceu!\033[m")
            v += 1
        if esclh == "I":
            print(f"\033[0:31:40m{num + randnum} é par você perdeu!\033[m")
            break
    if (num + randnum) % 2 != 0:
        d = "ÍMPAR"
        if esclh == "I":
            print(f"\033[0:32:40m{num + randnum} é ímpar você venceu!\033[m")
            v += 1
        if esclh == "P":
            print(f"\033[0:31:40m{num + randnum} é ímpar e você perdeu!\033[m")
            break

print(f"\033[0:31:40mVocê escolheu {num} eo computador escolheu {randnum} com total de {randnum + num} que é {d}, o computador precisou {c} tentativa(s) para vencer!\033[m")
print(f"\033[0:31:40mGame Over com {v} vitorias\033[m")
