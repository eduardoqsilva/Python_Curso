from datetime import date
anoint = date.today().year
anoqnasceu = int(input("que ano você nasceu? "))
if (anoint - anoqnasceu) == 18:
    print("Você deve se alistar esse ano!")
elif (anoint - anoqnasceu) < 18:
    print("Ainda não possui idade.")
elif (anoint - anoqnasceu) > 18:
    print("Já se passaram {} anos do tempo de alistamento".format((anoint - anoqnasceu)-18))
