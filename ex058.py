'''
Exercicio 058
'''

from random import randint
from time import sleep
from pygame import mixer

computador = randint(0, 10)                           # Faz o computador "PENSAR"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 10)
numChutes = 0
chute = 11
print('Em que número eu pensei? ', end='')
while computador != chute:
    chute = int(input(''))     # Jogador tenta adivinhar
    #print('PROCESSANDO...')
    #sleep(1)
    mixer.init()
    if computador==chute:
        print('Acertou mizeravi')
        mixer.music.load('ex028a.mp3')
    else:
        numChutes += 1
        print(f'Errouuuuuu!!! Tenta de novo: ', end='')
        mixer.music.load('ex028b.mp3')
    mixer.music.play()
    sleep(3)
    mixer.music.stop()
print(f'\nForam necessários {numChutes} chutes')