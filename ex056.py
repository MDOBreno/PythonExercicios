'''
Exercicio 056
'''

pessoas = 4

mediaIdade = 0
homemMaisVelhoIdade = 0
homemMaisVelhoNome = ''
mulheresMenosVinte = 0

for c in range(0, pessoas):
    nome = str(input('Informe o nome de uma pessoa: '))
    idade = int(input(f'Informe a Idade de {nome}: '))
    mediaIdade += idade
    sexo = int(input(f'{nome} é do sexo Masculino[1] ou Feminino[2]? '))
    if sexo==1:
        if idade > homemMaisVelhoIdade:
            homemMaisVelhoIdade = idade
            homemMaisVelhoNome = nome
    elif sexo==2:
        if idade < 20:
            mulheresMenosVinte += 1
    print()

mediaIdade = mediaIdade / pessoas

print(f'A idáde média é de {mediaIdade} anos')
print(f'O homem mais velho é {homemMaisVelhoNome}')
print(f'Existe(m) {mulheresMenosVinte} mulher(es) com menos de 20 anos')
