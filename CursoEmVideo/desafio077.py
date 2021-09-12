palavras = ("Obrigado", "Abacate", "Escada", "Desenho", "Site", "Fazer", "Melhor", "Mundo")
for p in palavras:
    print(f"\nA palavra ({p.upper()}) possui essas vogais:",end=" ")
    for letra in p:
        if letra in "AaEeIiOoUu":
            print(letra, end=" ")
