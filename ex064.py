'''
Exercicio 064
'''

soma = qtdNumeros = n = 0
while n != 999:
    n = int(input('Digite um número diferente de 999: '))
    if n != 999:
        soma += n
        qtdNumeros += 1

print(f'Deu uma soma de {soma}, dos {qtdNumeros} números digitados. ')


