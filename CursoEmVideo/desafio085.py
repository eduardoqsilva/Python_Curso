I = []
P = []
lista = []
for c in range(1, 8):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
      P.append(num)
    else:
        I.append(num)
lista = sorted(P), sorted(I)
print(f"Os valores pares são: {lista[0]}")
print(f"Os valores ímpares são: {lista[1]}")
