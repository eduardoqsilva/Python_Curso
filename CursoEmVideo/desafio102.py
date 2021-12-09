print("-"*10)
print(" Fatorial")
print("-"*10)

def fatorial(num=1, show=False):
    """
    :param num: Digite um número para calcular seu fatorial.
    :param show: Parâmetro opcional o padrão é false, retorna a conta.
    :return: Retorna o fatorial de num.
    """
    f = 1
    sinal = "x"
    for c in range(num, 0, -1):
        f *= c
        if c == 1:
            sinal = "="
        if show == True:
            print(f"{c} {sinal} ", end="")
    return f

print("=-"*30)
print(fatorial(10, show=True))
print("=-"*30)
