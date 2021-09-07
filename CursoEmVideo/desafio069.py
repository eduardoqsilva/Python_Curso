Hmc = Mlhc = M18 = idade = 0
sex = continua = ''
while True:
    idade = int(input("Digite sua idade: "))
    sex = str(input("Digite seu sexo [M] ou [F]: ")).strip().upper()[0]
    while sex != "M" and sex != "F":
        sex = str(input("Digite seu sexo [M] ou [F]: ")).strip().upper()[0]
    continua = str(input("Quer continuar [S] ou [N]: ")).strip().upper()[0]
    while continua != "S" and continua != "N":
        continua = str(input("Quer continuar [S] ou [N]: ")).strip().upper()[0]
    if idade >= 18:
        M18 += 1
    if sex == "M":
        Hmc += 1
    if idade < 20 and sex == "F":
        Mlhc += 1
    if continua == "N":
        break
print(f'''TOTAl:
O número de pessoas com mais de 18 anos é {M18}.
Ao todo são {Hmc} homem(s) cadastrados.
E {Mlhc} mulher(es) com menos de 20 anos.''')
