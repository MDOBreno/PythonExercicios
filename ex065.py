'''
Exercicio 065
'''

from sys import float_info

media = 0.0
qtdNumeros = 0
maior = float_info.min
menor = float_info.max

n = 1
continuar = True
while continuar:
    n = int(input('Digite um número: '))
    media += n
    qtdNumeros += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continuar = str(input('Deseja continuar: [S/N] ')).upper() == 'S'

media = media / qtdNumeros
print(f'\nDeu uma media de {media}, dos {qtdNumeros} números digitados. ')
print(f'O menor={menor}, e o maior={maior}')
