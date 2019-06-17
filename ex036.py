'''
Exercicio 036
'''

casa = float(input('Quanto custa a casa? \033[32mR$\033[m'))
salario = float(input('Quanto é o seu salário? \033[32mR$\033[m'))
anos = int(input('Em quantos anos você pretende pagar? '))

parcela = (casa / anos) / 12
if parcela <= (salario * 0.30):
    print(f'Credito liberado, e pagamento em parcelas de R${parcela:.2f}')
else:
    print(f'Credito nâo liberado, porque a parcelas seria de R${parcela:.2f}')











