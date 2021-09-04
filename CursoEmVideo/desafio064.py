c = 0
a = 0
num = 0
while num != 999:
    num = int(input("Digite outro número ou [999] para sair: "))
    c += 1
    a += num
    if num == 999:
        print(f"Foram digitados {c-1} números e a soma entre eles é {a-999}.")