num = int(input("Digite um número "))
num2 = int(input("Digite outro número "))
num3 = int(input("Digite mais um "))

menor = num

if num2 < num and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num:
    menor = num3
print("O menor numero é {}".format(menor))

maior = num

if num2 > num and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num:
    maior = num3
print("O maior número é {}".format(maior))
