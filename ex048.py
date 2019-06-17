'''
Exercicio 048
'''

s = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        s += c
        print(f'c={c:>3} s={s:>5}')

print(f'\nA soma dará {s}')


