matriz = []
n = []
i = a = 0
for b in range(0, 9):
    n.append(int(input(f"Digite o valor para [{a},{b}]: ")))
    matriz.append(n[:])
    n.clear()
    if i == 2:
        a = 1
    if i == 5:
        a = 2
    i += 1
print("=-"*30)
print(f'''{matriz[0]} {matriz[1]} {matriz[2]}
{matriz[3]} {matriz[4]} {matriz[5]}
{matriz[6]} {matriz[7]} {matriz[8]}''')
