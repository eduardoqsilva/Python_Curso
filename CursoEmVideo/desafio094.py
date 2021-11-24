lista = []
dic = {}
listaFem = []
listaMedia = []
cont = 0
idadeTot = 0
while True:
     dic['nome'] = str(input("Nome: "))
     dic['sexo'] = str(input("Sexo: ")).upper().strip()[0]
     dic['idade'] = int(input("Idade: "))
     lista.append(dic.copy())
     dic.clear()
     continua = str(input("Continuar [S/N] ? ")).upper().strip()[0]
     cont += 1
     if continua == "N":
         break
print("=-"*30)
for c in lista:
    idadeTot += c['idade']
    if c['sexo'] == "F":
        listaFem.append(c)
media = idadeTot / cont
for c in lista:
    if c['idade'] > media:
        listaMedia.append(c)
print(f"O grupo tem {cont} pessoas.")
print(f"A média de idade é de: {media:.2f}")
print("As mulheres cadastradas foram: ", end="")
for c in listaFem:
    print(c['nome'], end=" ")
print()
print(f"Lista das pessoas que estão acima da média: ")
for c in listaMedia:
    print(f"Nome = {c['nome']}; sexo = {c['sexo']}; idade = {c['idade']}")
print("=-" * 30)
print(f"~~ENCERRADO~~".center(50))
