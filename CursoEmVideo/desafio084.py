lista = []
pessoas = []
Nmaior = []
Nmenor = []
cont = 0
while True:
    pessoas.append(str(input("Nome: ")))
    pessoas.append(float(input("Peso: ")))
    lista.append(pessoas[:])
    pessoas.clear()
    continua = str(input("Continuar [S/N]: ")).strip().upper()[0]
    if continua == "N":
        break
for c in lista:
    if cont == 0:
        maior = c[1]
        menor = c[1]
    else:
        if c[1] > maior:
            maior = c[1]
        if c[1] < menor:
            menor = c[1]
    cont += 1
for j in lista:
    if j[1] == maior:
        Nmaior.append(j[0])
    if j[1] == menor:
        Nmenor.append(j[0])
print("=-"*20)
print(f"Ao todo você cadastrou {cont} pessoas.")
print(f"O maior peso foi {maior} de {Nmaior}")
print(f"O menor peso foi {menor} de {Nmenor}")
