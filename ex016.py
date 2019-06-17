'''
Exercicio 016
'''

from math import trunc

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua porção inteira é {trunc(num)}') # A linha abaixo faz exatamente a mesma coisa
print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}')
