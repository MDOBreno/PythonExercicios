'''
Exercicio 052
'''

n = int(input('Digite um número inteiro: '))
e = "\n\033[35mÉ primo!"
naoE = '\n\033[35mNÃO é primo!'

if n > 1:
    primo = True
    for c in range(2, n):
        if n % c == 0:
            print(f'\033[33m{c}', end=' ')
            primo = False
            c = n
        else:
            print(f'\033[31m{c}', end=' ')
    print(e if primo else naoE, end=' ')
else:
    print(naoE)
