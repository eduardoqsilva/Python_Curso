from datetime import date
data = date.today()
datAtual = int(data.strftime("%Y"))
dic = {}
dic["nome"] = str(input("Nome: "))
dic["nasceu"] = int(input("Ano de nascimento: "))
dic["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if dic["ctps"] != 0:
    dic["contratado"] = int(input("Ano de contratação: "))
    dic["salario"] = float(input("Salário: "))
    print("=-"*30)
    print(f"Nome tem valor {dic['nome']}")
    print(f"Idade tem valor {datAtual - dic['nasceu']}")
    print(f"CTPS tem valor de {dic['ctps']}")
    print(f"Salário tem valor de {dic['salario']}")
    print(f"Aposentadoria tem valor de {(dic['contratado'] - dic['nasceu']) + 35}")
else:
    print("=-"*30)
    print(f"Nome tem valor {dic['nome']}")
    print(f"Idade tem valor {datAtual - dic['nasceu']}")
    print(f"CTPS tem valor de {dic['ctps']}")
print("=-"*30)
