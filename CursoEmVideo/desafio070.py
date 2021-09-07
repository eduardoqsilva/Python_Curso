print("="*20, "Lojas Preço Baixo", "="*20)
maisC = maisB = preco = tot = cont = 0
nomMaisB = nome = continua = ''
while True:
    nome = str(input("Qual o nome do produto? "))
    preco = float(input("Qual o preço do produto R$"))
    print("-" * 25)
    continua = str(input("Continua [S] ou [N]: ")).strip().upper()[0]
    tot += preco
    cont += 1
    if cont == 1:
        maisB = preco
        nomMaisB = nome

    if maisB > preco:
        maisB = preco
        nomMaisB = nome
    if preco > 1000:
        maisC += 1

    if continua == "N":
        break
print(f'''O total da compra foi R${tot}
Temos {maisC} Produtos que custam mais de R$ 1000.
O produto mais barato foi {nomMaisB} que custa R${maisB}''')
