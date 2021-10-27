boletim = []
n = 0
while True:
    nome = str(input("Nome: "))
    nota = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    continua = str(input("Continuar [S/N]: ")).strip().upper()[0]
    lista = [nome, nota, nota2]
    boletim.append(lista[:])
    lista.clear()
    if continua == "N":
        break
print("=-"*30)
print("No. NOME                MÉDIA")
print("=-"*30)
for c in boletim:
    print(f"{n: <4}{c[0]: <20}{(c[1] + c[2]) / 2}")
    n += 1
print("-"*60)
while True:
    mostrar = int(input("Mostrar notas de que aluno? (999 interromper): "))
    if mostrar == 999:
        break
    print(f"As notas de {boletim[mostrar][0]} são: {boletim[mostrar][1]} e {boletim[mostrar][2]}")
    print("-"*60)
