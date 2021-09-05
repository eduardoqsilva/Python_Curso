from time import sleep
c = n = 0
n = int(input("\033[0:31:40mDigite Um número para exibir sua tabuada:\033[m "))
while True:
    c += 1
    if n < 0:
        break
    print(f"{n} x {c} = {n * c}")
    if c >= 10:
        c -= c
        sleep(2)
        n = int(input("\033[0:31:40mDigite Um número para exibir sua tabuada ou um número negativo para sair:\033[m  "))
print("Fim!")
