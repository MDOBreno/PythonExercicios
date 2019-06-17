'''
Exercicio 059
'''

from time import sleep

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

operacao = 0
print('-=' * 10)
while operacao != 5:
    print('''Digite uma operação
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    operacao = int(input('Sua escolha: '))
    if operacao == 1:
        print(f'A soma:: {a} + {b} = {a + b}')
    elif operacao == 2:
        print(f'A multiplicação: {a} x {b} = {a * b}')
    elif operacao == 3:
        print(f'O maior entre {a} e {b} é:  {a if a > b else b}')
    elif operacao == 4:
        a = int(input('Digite o primeiro número: '))
        b = int(input('Digite o segundo número: '))
    print('-=' * 10)
    if operacao == 5:
        print('Finalizando...')
sleep(2)
print('Fim do programa! Atá a proxima')



