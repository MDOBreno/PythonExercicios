'''
Exercicio 053
'''

from math import ceil

frase = str(input('Digite um frase: ')).replace(' ', '').upper()
len = int(len(frase))
meio = ceil(len / 2)
lenPar = True if len%2==0 else False

palindromo = True
for c in range(0, (meio if len else meio-1)):
    # print(f'c={c:>2} [len-c-1]={(len - c - 1):>2}')
    # print(f'frase[c]={frase[c]:>2} frase[len-c-1]={frase[len - c - 1]:>2}')
    if frase[c] != frase[len - c - 1]:
        palindromo = False
print('É Palindromo!' if palindromo else 'NÃO é Palindromo!')



