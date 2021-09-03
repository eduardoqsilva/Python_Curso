num = int(input("Digite um número inteiro: "))
print("1* para BINÁRIO.\n2* para OCTAL.\n3* para HEXADECIMAL.")
escolha = int(input("Escolha uma opção: "))
if escolha == 1:
    print(f"O número {num} convertido em Binario é {bin(num)[2:]}.")
elif escolha == 2:
    print(f"{num} convertido para octal é {oct(num)[2:]}.")
elif escolha == 3:
    print(f"{num} convertido em hexadecimal é {hex(num)[2:]}.")
else:
    print("Opção invalida")