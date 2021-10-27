lista = []
continua = ""
while continua != "N":
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor será adicionado!")
    else:
        print("Valor já existe e não será adicionado!")
    continua = str(input("Continua? [S/N]: ")).upper().strip()[0]
print(f"Você digitou os valores: {sorted(lista)}")
