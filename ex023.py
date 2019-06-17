'''
Exercicio 023
'''

num = str(input('Informe um número: '))
len = len(num)
if len > 0:        # Este "switch" equivale ao metodo choice do modulo random
    print(f'Unidade: {num[len - 1]}')
    if len > 1:  # Este "switch" equivale ao metodo choice do modulo random
        print(f'Dezena: {num[len - 2]}')
        if len > 2:  # Este "switch" equivale ao metodo choice do modulo random
            print(f'Centena: {num[len - 3]}')
            if len > 3:  # Este "switch" equivale ao metodo choice do modulo random
                print(f'Milhar: {num[len - 4]}')
# --------------------------------------------------------------------------------

print()
num = int(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')



