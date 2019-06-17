'''
Exercicio 033
'''

a = int(input('Me informe um primeiro numero: '))
b = int(input('Me informe um segundo número: '))
c = int(input('Me informe um terceiro número: '))

maior = a if (a > c and a > b) else (b if b > c else c)
menor = a if (a < c and a < b) else (b if b < c else c)

print(f'O maior é {maior}')
print(f'O menor é {menor}')

