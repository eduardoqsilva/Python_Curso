from math import factorial
num = int(input("Digite um número para calcular o fatorial: "))
ftr = factorial(num)
while num != 0:
    print(f"\033[0:32:40mO fatorial de {num}! é {ftr}.\033[m")
    print("Digite 0 para sair.")
    num = int(input("Digite um número para calcular o fatorial: "))
    ftr = factorial(num)
print("Obrigado!")