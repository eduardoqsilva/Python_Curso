lista = []
posicaoMaior = []
posicaoMenor = []

pos = 1
for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {c +1}: ")))
print()
print(f"O maior valor foi {max(lista)} nas posições:", end=' ')
for i in lista:
    if i == max(lista):
        print(f"{pos}", end="...")
    pos += 1
pos = 1
print()
print(f"E o menor valor é {min(lista)} na posições:", end=' ')
for i in lista:
    if i == min(lista):
        print(f"{pos}", end='...')
    pos += 1
