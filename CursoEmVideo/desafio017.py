#desafio017
from math import pow, hypot
catad = float(input("digite o cateto adjacente:"))
catop = float(input("digite o cateto oposto:"))
hip = hypot(catad, catop)
print("a hipotenusa é {:.2f}".format(hip))

