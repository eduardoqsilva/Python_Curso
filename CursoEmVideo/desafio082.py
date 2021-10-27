lista = []
pares = []
impares = []
while True:
    lista.append(int(input("Digite um valor: ")))
    c = str(input("Continuar [S/N]: ")).upper().strip()[0]
    if c == "N":
        break
for j in lista:
    if j % 2 == 0:
        pares.append(j)
    else:
        impares.append(j)
print(f"Os valores digitados são: {lista}.")
print(f"Os valores pares são {pares}.")
print(f"Os valores ímpares são {impares}.")
