matriz = []
n = []
i = a = soma = coluna = 0
for b in range(0, 9):
    n.append(int(input(f"Digite o valor para [{a},{b}]: ")))
    matriz.append(n[:])
    if i == 2:
        a = 1
    if i == 5:
        a = 2
    if n[0] % 2 == 0:
        soma += n[0]
    if i == 2 or i == 5 or i == 8:
        coluna += n[0]
    n.clear()
    i += 1
print("=-"*30)
print(f'''{matriz[0]} {matriz[1]} {matriz[2]}
{matriz[3]} {matriz[4]} {matriz[5]}
{matriz[6]} {matriz[7]} {matriz[8]}''')
print("=-"*30)
print(f"A soma  dos valores pares é {soma}.")
print(f"A soma dos valores da terceira coluna é {coluna}.")
print(f"O maior valor  da segunda  linha é {max(matriz[3], matriz[4], matriz[5])}.")
