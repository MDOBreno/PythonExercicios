'''
Exercicio 061
'''

prim = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razão da PA: '))

c = 0
while c != 10:
    print(f'{prim + c * razao}', end=' → ')
    c += 1
print('ACABOU')
