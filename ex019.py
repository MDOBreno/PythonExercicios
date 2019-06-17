'''
Exercicio 019
'''

from random import randint, choice

a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2: '))
a3 = str(input('Nome do Aluno 3: '))
a4 = str(input('Nome do Aluno 4: '))
x = randint(1,4)
aluno = ''
if x == 1:        # Este "switch" equivale ao metodo choice do modulo random
    aluno = a1
elif x == 2:
    aluno = a2
elif x == 3:
    aluno = a3
else:
   aluno = a4
print(f'O aluno sorteado foi {aluno}')

lista = [a1, a2, a3, a4]
print(f'O escolhido foi {choice(lista)}')
