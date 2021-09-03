velocidade = int(input("Digite a velocidade do carro:"))
if velocidade > 80:
    print("você ultrapassou o limite de velocidade permitido e recebera uma multa de R$ {:.2f} "
          "por estar a {} Km/h".format((velocidade - 80)* 7.00, velocidade))
else:
    print("Você está na velocidade permitida parabens continue assim!!")