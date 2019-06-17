'''
Exercicio 062
'''

prim = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razão da PA: '))

desejaVerPAs = True
c = numerosRestantes = 10
while desejaVerPAs:
    while numerosRestantes != 0:
        print(f'{prim + (c - numerosRestantes) * razao}', end=' → ')
        numerosRestantes -= 1
    print('PAUSA')

    desejaVerPAs = str(input('Você quer ver a continuação das PA? [S/N] ')).upper() == 'S'
    if desejaVerPAs:
        prim = prim + c * razao
        c = numerosRestantes = int(input('Quantos números você deseja ver a mais? '))
    else:
        desejaVerPAs = False