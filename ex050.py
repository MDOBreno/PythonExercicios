'''
Exercicio 050
'''

s = 0
for c in range(0, 6):
    inteiro = int(input(f'Digite um número inteiro: '))
    s += inteiro if inteiro%2==0 else 0
print(f'\nA soma dos pares dá igual a {s}.')






