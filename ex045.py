'''
Exercicio 045
'''

from random import randint
from builtins import print
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
print('''Qual será sua jogada?
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogada = int(input('Sua escolha: '))

print(f'\nJO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PO!!!!')

print(f'\n[Você]={itens[jogada-1]}     X     {itens[computador-1]}=[computador]')
if jogada>3 or jogada<1:
    print('Jogada invalida')
else:
    resutado = ''
    vitoria = 'VITORIA'
    derrota = 'DERROTA'
    empate = 'EMPATE'
    if (jogada + computador)==4 and jogada!=computador:
        resutado = vitoria if jogada==1 else derrota
    elif jogada==computador:
        resutado = empate
    else:
        resutado = vitoria if jogada>computador else derrota
    print(f'{resutado:^38}')
