from datetime import date
contM = 0
contm = 0
anoAt = date.today().year
for c in range (0,7):
    anoNas = int(input("Digite o ano de nascimento: "))
    idade = anoAt - anoNas
    if idade >= 21:
        contM += 1
    else:
        contm += 1
print(f"O número de pessoas com menos de 21 anos é {contm}")
print(f"O número de pessoas com mais de 21 anos é {contM}")