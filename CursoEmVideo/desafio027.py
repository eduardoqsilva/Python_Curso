n = str(input("digite seu nome: ")).strip()
nome = n.split()
print("Óla prazer em te conhecer!!!")
print("seu primeiro nome é {}.".format(nome[0]))
print("seu último nome é {}.".format(nome[len(nome)-1]))