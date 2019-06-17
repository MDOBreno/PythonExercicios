'''
Exercicio 044
'''

print(f'{" LOJAS BRENO ":=^40}')

precoNormal = float(input('Insira o preço normal: \033[1;32mRS\033[m'))
print('''Metodos de pagamento
[ 1 ] Cartão à vista
[ 2 ] Cartão 2x
[ 3 ] Cartão 3x ou mais
[ 4 ] Dinheiro / Cheque''')
metodo = int(input('Sua escolha: '))

if not (str(metodo) in '1234'):
    print('Escolha inexistente')
else:
    valorASerPago = 0
    if metodo == 1:
        valorASerPago = precoNormal * 0.95
    elif metodo == 2:
        valorASerPago = precoNormal
    elif metodo == 3:
        valorASerPago = precoNormal * 1.20
    else:
        valorASerPago = precoNormal * 0.90
    print(f'O preço a ser pago é \033[1;32mR${valorASerPago:.2f}\033[m .')
