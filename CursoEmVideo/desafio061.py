print('******** Os 10 termos de uma PA ********')
termo1 = int(input("Digite O primeiro termo: "))
razao = int(input("Digite a razão: "))
c = 10
valor = 0
while c != 0:
    valor += razao
    print(valor, '->', end=" ")
    c -= 1
print('Acabou!')
