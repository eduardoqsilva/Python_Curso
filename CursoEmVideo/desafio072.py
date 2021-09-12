num = int(input("Digite um número de 0 a 20: "))
tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
         "oito", "nove", "dez", "onze", "doze", "treze", "quatorze ou catorze",
         "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    if 20 >= num >= 0:
        print(f"Você digitou {tupla[num]}.")
        break
    else:
        num = int(input("Digite um número de 0 a 20: "))
print("Obrigado!")
