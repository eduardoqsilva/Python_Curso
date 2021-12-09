def notas(*n, sit=False):
    """
    :param n: Um ou mais números para calcular a média.
    :param sit: True ou False mostrar ou não a situção.
    :return: retorna os resultados.
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n) / len(n)
    if sit == True:
        if dic['média'] >= 7:
            dic['situação'] ="Boa"
        if 6 < dic['média'] < 7:
            dic['situação'] = "Razoavel"
        if dic['média'] < 6:
            dic['situação'] = "Ruim"
    return dic


resp = notas(3.5, 2, 6.5, 2, 7, 4)
print("-"*100)
print(resp)
print("-"*100)
