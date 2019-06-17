'''
Exercicio 051
'''

prim = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razão da PA: '))

for c in range(prim, prim + 10*razao, razao):
    print(str(c), end=" → ")
print('ACABOU')
