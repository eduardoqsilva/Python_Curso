c = 0
num = 0
maior = 0
menor = 0
continua = ''
acumula = 0
while continua != "N":
    num = int(input("Digite um número: "))
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    acumula += num
    continua = str(input("Continua [S] ou [N]: ")).strip().upper()
print(f"A média é {acumula/c :.2f}, o maior número foi {maior} eo menor foi {menor}, foram digitados {c} números.")
