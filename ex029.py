'''
Exercicio 029
'''

from termcolor import colored

v = int(input('Qual a velocidade do carro em Km/h? '))
if v>80:
    print(colored('MULTADO! Você excedeu o limite permitido que é de 80km/h', 'red'))
    print(colored(f'Voce foi multado em R${((v-80)*7):.2f}', 'red'))
print(colored('Tenha um bom dia! Dirija com segurança!', 'yellow'))

