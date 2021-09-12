from random import randint
maior = 0
menor = 10
tupla = randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9);
print(f"os valores sorteados são: {tupla}")
for c in range(1, 5):
    if maior < tupla[c]:
        maior = tupla[c]
    if menor > tupla[c]:
        menor = tupla[c]
print(f"O maior valor é: {maior} o menor valor é: {menor}")
