from time import sleep
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
opcao = 0
maior = 0
while opcao != 5:
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    print("Carregando menu...")
    sleep(2)
    opcao = int(input('''Escolha a opção:
    [1]soma
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]Sair  '''))
    if opcao == 1:
        print(f"\033[4:31:40mA soma entre {num1} e {num2} é {num1 + num2}.\033[m")
    if opcao == 2:
        print(f"\033[4:31:40mA multiplicação entre {num1} e {num2} é {num1 * num2}.\033[m")
    if opcao == 3:
        print(f"\033[4:31:40mA o maior número  entre {num1} e {num2} é {maior}.\033[m")
    if opcao == 4:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
print("Obrigado!!!")
