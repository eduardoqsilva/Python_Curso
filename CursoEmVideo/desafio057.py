sexo = str(input("Digite Seu Sexo M ou F: ")).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print("Digite M ou F dado invalido tente novamente!")
    sexo = str(input("Digite Seu Sexo M ou F: ")).strip().upper()[0]
print("Obrigado!")