'''
Exercicio 057
'''

sexo = ''
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if (sexo != 'M') and (sexo != 'F'):
        print('Valor invalido, digite apenas [M] para masculino, ou [F] para feminino.')
print(f'Sexo {"Masculino" if sexo=="M" else "Feminino"} registrado com sucesso!')
















