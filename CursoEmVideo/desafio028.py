print("**-"*20)
numeroescolhido = int(input("digite um número de 0 a 5  tente adivinha-lo: "))
from  random import randint
from time import sleep
randNumber = randint(0,5)
print("**-"*20)
print("PROCESSANDO...")
print("**-"*20)
sleep(3)

if randNumber == numeroescolhido:
    print("Você acertou {} era o número que eu escolhi!!!".format(numeroescolhido))
    print("**-" * 20)
else:
    print("Que pena você errou o número era {}, tenta de novo!!".format(randNumber))
    print("**-"*20)
