lista = []
posicaoMaior = []
posicaoMenor = []
posiAtual = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {c}: ")))
for c in lista:
    if c == max(lista):
        posicaoMaior.append(posiAtual)
    if c == min(lista):
        posicaoMenor.append(posiAtual)
    posiAtual += 1
print(f"O maior valor foi {max(lista)} na posição {posicaoMaior},"
      f" e o menor valor é {min(lista)} na posição {posicaoMenor}.")
