dic = {}
li = []
tot = 0
jogadores = []
print("=-" * 30)
while True:
    dic['nome'] = str(input("Nome: "))
    ptida = int(input(f"Quantas partidas {dic['nome']} jogou? "))
    for c in range(0, ptida):
        gol = int(input(f"Quantos gols na partida {c}? "))
        tot += gol
        li.append(gol)
    dic['gols'] = li[:]
    dic['total'] = tot
    tot = 0
    li.clear()
    jogadores.append(dic.copy())
    dic.clear()
    print("=-" * 30)
    cont = str(input("Continua [S/N]: ")).strip().upper()[0]
    if cont == 'N':
        break
cont = ''
c = -1
print("=-"*25)
print("Cod  nome      gols            total")
for j in jogadores:
    c += 1
    print(f"{c: <4} {j['nome']: <10} {j['gols']!s: <15s} {j['total']}")
print("-"*50)
while True:
    cod = int(input("Mostrar dados de que jogador? "))
    if cod == 999:
        break
    if cod > c or cod < 0:
        print("Digite o número correto!")
    else:
        print(f"LEVANTAMENTO DO JOGADOR {jogadores[cod]['nome'].upper()}:")
        jg = 0
        for j in jogadores[cod]['gols']:
            print(f"-No jogo {jg} ele fez {j} gols.")
            jg += 1
    print("-"*50)
print("=-"*25)
print("~FINALIZADO~".center(50))
