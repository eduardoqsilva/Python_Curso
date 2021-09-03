salario = float(input("digite seu sálario: "))

if salario > 1250.00:
    print("sálario reajustado com 12% é {:.2f}".format(((salario / 100)*12) + salario))
if salario == 1250.00 or salario < 1250.00:
    print("sálario reajustado com 15% é {:.2f}".format(((salario / 100)*15) + salario))
