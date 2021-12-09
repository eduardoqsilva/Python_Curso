def leiaInt(intt):
    while True:
        if intt.isnumeric():
            break
        else:
            print("ERRO DIGITE APENAS NÚMEROS!")
            intt = input("Digite um número: ")
    return intt

n = leiaInt(input("Digite um número: "))
print(f"Você digitou o número {n}")
