'''
Exercicio 060
'''

from math import factorial

num = n = int(input('Digite um número para saber seu fatorial: '))
f = 1
print(f'Calculando {n}! = {n}', end='')
while n > 1:
    f *= n
    n -= 1
    if n >= 1:
        print(f' x {n}', end='')
print(f' = {f}')

print(f'\nO fatorial é {factorial(num)}')



