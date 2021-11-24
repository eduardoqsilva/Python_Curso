dic = {}
li = []
tot = 0
dic['nome'] = str(input("Nome: "))
ptida = int(input(f"Quantas partidas {dic['nome']} jogou? "))
for c in range(0, ptida):
    gol = int(input(f"Quantos gols na partida {c}? "))
    tot += gol
    li.append(gol)
dic['gols'] = li
dic['total'] = tot
print("=-"*30)
print(dic)
print("=-"*30)
print(f"O campo nome tem valor {dic['nome']}.")
print(f"O campo gols tem valor {dic['gols']}.")
print(f"O campo total tem valor {dic['total']}.")
print("=-"*30)
print(f"O jogador {dic['nome']}  jogou {len(dic['gols'])} partidas.")
c = 0
for g in dic['gols']:
    print(f"=> Na partida {c}, fez {g} gols.")
    c += 1
print(f"Com um total de {dic['total']} gols.")
