cont = 0
s = 0
for c in range(1, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        s += num
        cont += 1

print(f"voce informou {cont} pares, e a soma deles é {s} :")
