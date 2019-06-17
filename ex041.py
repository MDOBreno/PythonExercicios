'''
Exercicio 041
'''

from datetime import date

nascimento = int(input('Qual o seu ano de Nascimento? '))
hoje = date.today().year
idade = hoje - nascimento
print(f'Sua idade é {idade}')

if idade <= 9:
    print('MIRIN')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')








