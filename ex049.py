'''
Exercicio 049
'''

n = float(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{(n):.0f} x {c:2} = {(n * c):.0f}')
print('-' * 12)

