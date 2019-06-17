
'''
Exercicio 017
'''

from math import sqrt, hypot

co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacente: '))
hi = sqrt((ca ** 2) + (co ** 2))    # Essa expressão equivale a funcao hypot(ca,co) do modulo math
print(f'A hipotenusa é: {hi:.2f}')
hi = hypot(ca,co)
print(f'A hipotenusa é: {hi:.2f}')
