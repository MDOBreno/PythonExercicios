'''
Exercicio 027
'''

nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()
print(f'primeiro={nomes[0]}')
print(f'ultimo={nomes[len(nomes) - 1]}')