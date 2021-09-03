km = int(input("Quantos km é a viagem? "))
if km > 200:
    print("A viagem custará R$ {:.2f} e será percorrido {} Km.".format(km * 0.45, km))
else:
    print("A viagem custará R$ {:.2f} e será percorrido {} Km.".format(km * 0.50, km))
