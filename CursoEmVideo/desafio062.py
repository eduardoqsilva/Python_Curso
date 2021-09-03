print('******** Os termos de uma PA ********')
termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
e = int(input("Digite quantos termos você quer exibir: "))
valor = 0
while e != 0:
    valor += razao
    print(f"\033[0:33:40m{valor} ->", end=" \033[m")
    e -= 1
    if e == 0:
        e = int(input("\n\033[0:32:40mDigite o número de termos, ou [0] para sair: \033[m"))
print('***Acabou!***')