'''
Exercicio 004
'''

insercao = input('Digite algo: ')
print(f'O tipo primitivo de {insercao} é ', type(insercao))
print('Só tem espaço? ',insercao.isspace())
print('É um número? ', insercao.isnumeric())
print('É alfanbético? ', insercao.isalpha())
print('É alfanumerico? ', insercao.isalnum())
print('Está em maiúsculas? ', insercao.isupper())
print('Está em menúsculas? ', insercao.islower())
print('Está capitalizada? ', insercao.istitle())
