#algoritmo em python
quant = int(input("Quantidade: "))
prec = float(input("Preço da unidade: "))
tot = prec * quant
descont = (tot / 100) * 20
if quant > 10:
   print(f"A compra sem o desconto ficou: R$ {tot}")
   print(f"O valor da compra com o desconto é: R$ {tot - descont}")
   print(f"O valor do desconto é de: R$ {descont}")
else:
    print("É preciso comprar mais de 10 itens para obter o desconto!")
    print(f"A compra sem o desconto ficou: R$ {tot}")
