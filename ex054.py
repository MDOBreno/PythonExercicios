'''
Exercicio 054
'''

from datetime import date

hoje = date.today().year
s = 0
for c in range(0, 7):
    idade = hoje - int(input('Informe o ano de nascimento de uma pessoa: '))
    s += 1 if idade >= 21 else 0
print(f'Foram dadas as idáde de {s} pessoas na Maioridade, e {7-s} Menores de idade')










