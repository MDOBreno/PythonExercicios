'''
Exercicio 032
'''

from datetime import date

a = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if a==0:
    a = date.today().year
bissexto = ((a%4)==0 and not ((a%400)!=0) and (a%100)==0)
print(f'O ano {a} É Bissexto' if bissexto else f'O ano {a} Não é Bissexto')