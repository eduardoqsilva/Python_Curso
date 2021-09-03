casa = float(input("Qual o valor da casa? "))
slr = float(input("Quanto você recebe mensalmente? "))
anos = int(input("Em quantos anos quer pagar a casa? "))

if casa / (anos * 12) <= (slr/100) * 30:
    print("Você pode comprar a casa, com {} parcelas de {:.2f} "
          "reais mensais, durante {} anos.".format((anos * 12), (casa / (anos * 12)), anos))
else:
    print("Você não pode comprar, o emprestimo foi negado.")
