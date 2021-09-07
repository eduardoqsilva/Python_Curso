valor = int(input("Digite o valor a ser sacado R$"))
cedula = 50
total = valor
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f"São {totcedula} notas de R${cedula}.")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
             break
print("Volte sempre!")