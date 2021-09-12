tabel_brasileirão = ("Atlético-mg", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", "Corinthias", "Fluminense",
"Atlético-go", "Athético-pr", "Ceará sc", "Cuibá", "Internacional", "Juventude", "Santos", "São paulo", "Bahia", "América-mg","Sport recife", "Grêmio", "Chapecoence")

print(f'''Os 5 primeiros colocados são: {tabel_brasileirão[0:5]}.
Os 4 últimos colocados da tabela são: {tabel_brasileirão[16:]}.
Em ordem alfabética {sorted(tabel_brasileirão)}.
O time chapecoence está na posição {(tabel_brasileirão).index("Chapecoence")+1}''')