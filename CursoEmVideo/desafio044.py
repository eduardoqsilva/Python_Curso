ValorProd = float(input("Digite o valor do produto: "))
print("1* para pagamento a vista no cheque ou dinheiro.\n"
      "2* pagamento a vista no cartão.\n"
      "3* Dividir em 2x no cartão.\n"
      "4* dividir em 3x ou mais no cartão.\n")

sel = int(input("Escolha a opção: "))
if sel == 1:
    print(f"O produto custa R$ {ValorProd:.2f}, e com o desconto de 10% fica R$ {(ValorProd)-(ValorProd / 100)*10:.2f}")
elif sel == 2:
    print(f"O produto custa R$ {ValorProd:.2f}, e com o desconto de 5% fica R$ {(ValorProd)-(ValorProd / 100)*5:.2f}")
elif sel == 3:
    print(f"O produto custa R$ {ValorProd:.2f}")
elif sel == 4:
    p = float(input("Quantas parcelas? "))
    print(f"O produto custa R$ {ValorProd:.2f}, e com os juros de 20% fica R$ {(ValorProd) + (ValorProd / 100) * 20:.2f}, com parcelas de {((ValorProd) + (ValorProd / 100) * 20) / p:.2f}")
elif sel > 4 or sel < 1:
    print("Escolha uma opção valida")
