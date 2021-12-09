def voto(anoNasc):
    from datetime import datetime
    data = datetime.now().year
    idade = data - anoNasc
    if idade < 16:
        return f"com {idade} anos o voto é negado!"
    elif 16 <= idade < 18 or idade > 65:
        return f"com {idade} anos o voto é opcional!"
    else:
        return f"com {idade} anos o voto é obrigatorio!"


resp = voto(int(input("Ano de nascimento: ")))
print(resp)
