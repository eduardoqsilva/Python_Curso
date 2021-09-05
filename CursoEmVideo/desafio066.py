c = 0
s = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    s += num
    c += 1
print(f"Você digitou {c}, e a soma entre eles é {s}")