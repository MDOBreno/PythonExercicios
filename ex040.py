'''
Exercicio 040
'''


primeiro = float(input('Digite a primeira nota: '))
segundo = float(input('Digite o segunda nota: '))
media = (primeiro + segundo) / 2

print(f'A média é {media}')
if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

