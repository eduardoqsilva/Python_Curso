frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"Voçê digitou a frase {junto} o inverso é {inverso} e ela é um palíndromo")
else:
    print(f"Voçê digitou a frase {junto} o inverso é {inverso} e ela não é um palíndromo")