import random
p = int(input("Digite:\n1* pedra. \n2* Tesoura. \n3* papel.\n"))
c = random.randint(1,3)

if c == p:
    print("Empate!")
elif c == 1 and p == 2:
    print("você perdeu o computador escolheu pedra!")
elif c == 1 and p == 3:
    print("você ganhou o computador escolheu pedra!")
elif c == 2 and p == 1:
    print("você ganhou o computador escolheu tesoura!")
elif c == 2 and p == 3:
    print("você perdeu o computador escolheu tesoura!")
elif c == 3 and p == 1:
    print("você perdeu o computador escolheu papel!")
elif c == 3 and p == 2:
    print("você ganhou o computador escolheu papel!")
else:
    print("Escolha entre pedra papel ou tesoura 1*, 2*, 3*.")
