km = float(input("quantos km vc andou? "))
dia = int(input("quantos dias vc usou o carro? "))
cust = (km * 0.15) + (dia * 60)
print("você usou o carro por {:.0f} dias e andou {:.2f}km. Com isso o total a pagar é: R$ {:.2f}".format(dia, km, cust))
