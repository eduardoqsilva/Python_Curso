tent = 1
from random import randint
randNum = randint(0,10)
print('Tente adivinhar o que estou pensando...')
num = int(input("Vamos lá digite um número entre 0 a 10: "))
while num != randNum:
    print("tente novamente... ")
    if randNum > num:
        print("Quer uma dica? é maior!")
    else:
        print("O número é menor! tenta de novo!!!")
    num = int(input("Digite um número entre 0 a 10: "))
    tent += 1
print(f"Você acertou o número era {randNum} e você precissou de {tent} tentativa(s).")