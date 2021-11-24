dic = {}
dic['nome'] = str(input("Nome: "))
dic['média'] = float(input("Média: "))
if dic['média'] >= 7:
    dic['situação'] = "Aprovado"
elif 5 <= dic['média'] < 7:
    dic['situação'] = "recuperação"
else:
    dic['situação'] = "reprovado"
print("-="*20)
for k, v in dic.items():
    print(f"-{k} é igual a {v}")
