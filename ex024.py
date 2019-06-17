'''
Exercicio 024
'''

cidade = str(input('Em que cidade você nasceu? '))
san = 'SANTO'

if cidade.upper().lstrip().find(san) == 0:
    print(f'A cidade {cidade} começa com o nome {san}.')
else :
    print(f'A cidade {cidade} não começa com o nome {san}.')






