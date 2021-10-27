lista = []
text = "Não está"
while True:
    lista.append(int(input("Digite um valor: ")))
    v = str(input("Continuar [S/N]: ")).strip().upper()[0]
    if 5 in lista:
        text = "está"
    if v == "N":
        break
print(f"Foram digitados {len(lista)} números.")
print(f"A lista ordenada de maneira decrescente é: {sorted(lista, reverse=True)}")
print(f"O número 5 {text} na lista.")