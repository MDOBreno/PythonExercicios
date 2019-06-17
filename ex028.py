'''
Exercicio 028
'''

from random import randint
from time import sleep
from pygame import mixer

computador = randint(0,5)                           # Faz o computador "PENSAR"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
chute = int(input('Em que número eu pensei? '))     # Jogador tenta adivinhar
#print('PROCESSANDO...')
#sleep(1)
mixer.init()
if computador==chute:
    print('Acertou mizeravi')
    mixer.music.load('ex028a.mp3')
else :
    print(f'Errouuuuuu!!! O valor era {computador}')
    mixer.music.load('ex028b.mp3')
mixer.music.play()
input('')