'''
Exercicio 035
'''


print('-=-' * 20)
print('Analizador de triangulos')
print('-=-' * 20)

a = float(input('Me informe um primeiro segmento: '))
b = float(input('Me informe um segundo segmento: '))
c = float(input('Me informe um terceiro segmento: '))

formaTriangulo = True if ((a + b) > c and (a + c) > b and (c + b) > a) else False

print('Podem formar triângulo!' if formaTriangulo else 'Não podem formar triângulo!')




