from time import sleep
c = ('\033[m',  # 0 sem cor
     '\033[0;0;41m',  # 1 vermelho
     '\033[0;0;42m',  # 2 verde
     '\033[0;0;43m',  # 3 amarelo
     '\033[0;0;44m',  # 4 azul
     '\033[0;0;45m',  # 5 roxo
     '\033[7;40m'  # 6 branco
     )


def ajuda(comando, cor=0):
    titulo(f"Acessando o manual do \'{comando}\'", 4)
    print(c[6], end="")
    help(comando)
    print(c[0], end="")
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end='')
    sleep(1)


cmd = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    cmd = str(input("Função ou Biblioteca > "))
    if cmd.upper() == "FIM":
        break
    else:
        ajuda(cmd)
titulo("ATÉ LOGO!", 1)
