'''
Exercicio 031
'''

from termcolor import colored

n = int(input('Qual a distância da viagem em Km? '))
valorKm = 0.5 if n<=200 else 0.45
print(colored(f'O Preço da passagem é R${(n*valorKm):.2f}', 'green'))



