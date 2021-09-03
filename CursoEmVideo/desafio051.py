print("=-"*20)
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
d = p + 10 * r
print("=-"*20)
for c in range(p, d, r):
    print(c, "→", end= " ")
print("acabou")