print("~+."*15)
print("Sequência de fibonacci")
print("~+."*15)
c = int(input("Digite o número de termos: "))
t1 = 0
t2 = 1
contador = 3
print('~'*65)
print(f"{t1} ㋡ {t2}",end= " ")
while contador <= c:
    t3 = t1 + t2
    print(f' ㋡ {t3}',end= " ")
    contador += 1
    t1 = t2
    t2 = t3
    if c ==  contador:
        c = int(input("\nDigite o número de termos ou 0 para sair: "))
print(" -> Fim")