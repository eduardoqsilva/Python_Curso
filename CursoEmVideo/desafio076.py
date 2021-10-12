tupla = ('Arroz', 25.99, 'Feijão', 7.99, 'Caneta', 1.99, 'Pizza', 20.99)
print(f'{"Listagem de preços":^30}')
print("="*30)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f"{tupla[pos]:.<20}", end="")
    else:
        print(f"R${tupla[pos]:>7.2f}")
print("="*30)
