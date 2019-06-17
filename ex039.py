'''
Exercicio 039
'''

from datetime import date

nascimento = int(input('Digite o ano de seu nascimento: '))

hoje = date.today().year
idade = hoje - nascimento

if idade<18:
    print(f'Voce ainda vai se apresentar ao alistamento militar, e ainda falta {18 - idade} ano(s).')
elif idade==18:
    print('Está na hora de você se apresentar ao alistamento militar')
else:
    print(f'Voce já se apresentou(ou devia ter se apresentado) ao alistamento militar, a {idade - 18} ano(s) atrás.')


