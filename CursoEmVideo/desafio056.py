idades =[]
sexos = []
nomes = []
idadeMedia = 0
HMvelho = 0
NMvelho = []
countM = 0
for c in range (0,4):
    if c == 0:
        print("==========Primeira Pessoa==========")
    if c == 1:
        print("==========Segunda Pessoa==========")
    if c == 2:
        print("==========Terceira Pessoa==========")
    if c == 3:
        print("==========Quarta Pessoa==========")
    nome = str(input("Nome: ")).strip()
    sexo = str(input("Sexo masculino/feminino [M]/[F]: ")).upper().strip()
    idade = int(input("Idade: "))
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    idadeMedia += idade
    if sexo == "F" and idade < 20:
        countM += 1
    if c == 0 and sexo == "M":
        HMvelho = idade
    else:
        if HMvelho < idade and sexo == "M":
            HMvelho = idade
            NMvelho = nome
print(f"A média de idade do grupo é {idadeMedia/4} anos, o homem mais velho é {NMvelho} e ele tem {HMvelho} anos, o número de mulheres com menos de 20 anos é {countM}.")