'''
Exercicio 055
'''

from sys import float_info

maior = float(0)
menor = float_info.max

for c in range(0, 5):
    peso = float(input('Digite o peso de uma pessoa (Kg): '))
    maior = peso if peso>maior else maior
    menor = peso if peso<menor else menor
print(f'Maior={maior:.1f}Kg Menor={menor:.1f}Kg')

