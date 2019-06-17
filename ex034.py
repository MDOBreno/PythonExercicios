'''
Exercicio 034
'''

f = int(input('Qual é o salário do funcionário? '))

aumento = f*0.10 if f>1250.00 else f*0.15
print(f'Ele acaba de receber um aumento de R${aumento:.2f}')
print(f'Quem ganhava R${f:.2f} passou a ganhar R${f+aumento:.2f}')



