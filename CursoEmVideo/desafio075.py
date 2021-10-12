tupla = (int(input("digite um valor: ")),
         int(input("Digite um valor: ")),
         int(input("Digite um valor: ")),
         int(input("digite um valor: ")))
print(f"O valor 9 apareceu {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"O valor 3 foi digitado na posição {tupla.index(3)+1}.")
else:
    print(f"O valor 3 não foi digitado.")
print(f"Os números pares são:")
for c in tupla:
    if c % 2 == 0:
        print(c, end=" ")