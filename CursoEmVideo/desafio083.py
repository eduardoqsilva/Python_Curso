lista = []
p1 = 0
p2 = 0
c = 0
erro = False
expressao = (str(input("Digite a expressão: ")))
for c in expressao:
    lista.append(c)
for j in lista:
    if j == ")" and p1 == 0:
        erro = True
    if j == "(":
        p1 += 1
    if j == ")":
        p2 += 1
if p1 == p2 and erro == False:
    print("Sua expressão está correta!")
else:
    print("Sua expressão está errada!")
