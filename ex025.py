'''
Exercicio 025
'''

nome = str(input('Qual é o seu nome completo? '))
sil = 'SILVA'

if nome.upper().lstrip().find(sil) != (-1):
    print(f'O nome {nome} comtem o nome {sil}.')
else :
    print(f'O nome {nome} não comtem o nome {sil}.')

# ----------------------------------------------------

if sil in nome.upper():
    print(f'O nome {nome} comtem o nome {sil}.')
else :
    print(f'O nome {nome} não comtem o nome {sil}.')





