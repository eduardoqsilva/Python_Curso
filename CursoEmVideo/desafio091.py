from random import randint
from time import sleep
from operator import itemgetter
dic = {}
for c in range(1, 5):
    dic[f"jogador ({c})"] = randint(1, 6)
for k, v in dic.items():
    print(f"O {k} tirou: {v}")
    sleep(1)
print("=-"*30)
print(f"~Ranking dos jogadores~".center(50))
print("=-"*30)
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i + 1}ª lugar: {v[0]} com {v[1]}")
