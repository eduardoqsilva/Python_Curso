c = 0
a = 0
num = 0
num = int(input("Digite outro número ou [999] para sair: "))
while num != 999:
    c += 1
    a += num
    num = int(input("Digite outro número ou [999] para sair: "))
print(f"Foram digitados {c} números e a soma entre eles é {a}.")