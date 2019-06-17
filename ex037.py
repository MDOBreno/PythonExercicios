'''
Exercicio 037
'''

decimal = int(input('Insira um número inteiro em decimal: '))
print('''Para qual base de conversão você deseja converter?
[ 1 ] Binario; 
[ 2 ] Octal; 
[ 3 ] Hexadecimal''')
base = int(input('Sua opção: '))
if base==1:
    print(f'O valor de {decimal} em Binário é {bin(decimal)[2:]}')
elif base==2:
    print(f'O valor de {decimal} em Octal é {oct(decimal)[2:]}')
elif base==3:
    print(f'O valor de {decimal} em Hexadecimal é {hex(decimal)[2:]}')
else:
    print('Escolha inexistente.')


