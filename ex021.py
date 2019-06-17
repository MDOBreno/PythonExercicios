'''
Exercicio 021
'''

from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora que você escuta, é so inserir algo para parar a reprodução: ')

