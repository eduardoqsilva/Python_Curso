from math import tan, cos, sin, radians
a = int(input("digite o ângulo: "))
seno = sin(radians(a))
coseno = cos(radians(a))
tangente = tan(radians(a))
print("O seno é {:.2f} o cosseno é {:.2f} a tangente é {:.2f}".format(seno, coseno, tangente))
