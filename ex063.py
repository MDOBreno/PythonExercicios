'''
Exercicio 063
'''

n=1
while n < 2:
    n = int(input('Digite um número inteiro maior ou igual a 2: '))
    if n < 2:
        print('Valor invalido, insira novamente')

b = 0
c = 1

if n >= 2:
    print(f'{b} → {c} → ', end='')
    n -= 2
    while n > 0:
        a = b
        b = c
        c = a + b
        print(f'{c}', end=' → ')
        n -= 1
print('ACABOU')




