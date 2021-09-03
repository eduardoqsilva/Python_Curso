from datetime import date
anoInt = date.today().year

anoQnasc = int(input("Digite o ano que você nasceu: "))
if anoInt - anoQnasc <=9:
    print("mirim}")
elif anoInt - anoQnasc <=14 >=10:
    print("infantil")
elif anoInt - anoQnasc <=19 >=15:
    print("junior")
elif anoInt - anoQnasc == 20:
    print("Sênior")
else:
    print("master")
print(anoInt - anoQnasc)



