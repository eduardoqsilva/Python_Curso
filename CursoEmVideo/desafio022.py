#desafio022
nome = input(str("digite seu nome completo: ")).strip()
up = nome.upper()
donw = nome.lower()
sep = nome.split()
junt = "".join(sep)
print("Capslock ligado: {}, tudo minúsculo: {}, quantas letras sem contar "
      "os espaços: {}, quantas letras só o primeiro nome {}".format(up, donw, len(junt), len(sep[0])))
