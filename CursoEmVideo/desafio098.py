from time import sleep

def contador(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print("=-" * 20)
    print(f"De {i} a {f} de {p} em {p}:")
    cont = i
    if i < f:
        while cont <= f:
            print(f"{cont} ", end="")
            cont +=p
            sleep(0.5)
        print("Fim!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="")
            cont -= p
            sleep(0.5)
        print("Fim!")


contador(1, 10, 1)
contador(10, 0, 2)
print("=-" * 20)
contador(i=int(input("Início: ")), f=int(input("Fim: ")), p=int(input("Passo: ")))
