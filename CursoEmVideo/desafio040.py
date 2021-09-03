nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if (nota1 + nota2) / 2 >= 7.0:
    print("Aluno aprovado!")
elif (nota1 + nota2) / 2 < 5.0:
    print("Aluno de reprovado é a média é {}".format((nota1 + nota2) / 2))
else:
    print("aluno de recuperação é a média é {}".format((nota1 + nota2) / 2))


