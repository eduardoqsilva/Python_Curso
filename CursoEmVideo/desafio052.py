tot = 0
num = int(input("Digite o número: "))
for c in range(1, num +1):
    if num % c == 0:
        tot += 1
if tot > 2:
    print(f"O número {num} não é um número primo pois foi divisivel {tot} vezes!")
elif tot == 2:
    print(f"O número {num} é primo pois só foi divisivel {tot} vezes!")
