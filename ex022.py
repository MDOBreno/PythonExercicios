'''
Exercicio 022
'''

nome = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(" " ,"" ))} letras')
print(f'Seu primeiro nome é {(nome.split()[0])} e ele tem {len(nome.split()[0])} letras')

