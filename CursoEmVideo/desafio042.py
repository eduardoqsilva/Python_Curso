print("=>" * 20)
a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))
print("=>" * 20)
v = False
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima podem formar um triângulo",end=" ")
    if a == b == c:
        print("equilátero")
    elif a != b != c != a:
        print("escaleno!")
    else:
        print("isósceles")
else:
    print("Os segmentos acima não podem formar um triângulo")
