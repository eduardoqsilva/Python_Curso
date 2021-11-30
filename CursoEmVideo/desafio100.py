from random import randint
números = []

def sorteia():
    for c in range(0, 5):
        números.append(randint(1, 10))
def somaPar():
    soma = 0
    for c in números:
        if c % 2 == 0:
            soma += c
    print(soma)


sorteia()
print(f"Os números sorteados são: {números}")
print(f"Somando os valores pares temos: ", end="")
somaPar()
