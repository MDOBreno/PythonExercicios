'''
Exercicio 042
'''

print('-=-' * 20)
print('Analizador de triangulos')
print('-=-' * 20)

a = float(input('Me informe um primeiro segmento: '))
b = float(input('Me informe um segundo segmento: '))
c = float(input('Me informe um terceiro segmento: '))

formaTriangulo = True if ((a + b) > c and (a + c) > b and (c + b) > a) else False

if formaTriangulo:
    print(f'Os ')
    #if a == b and a == c:  # Se isso ocorrer então obviamente "b == c", por isso removi essa ultima comparacao.
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b and a != c and b != c:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Não existe esse Triângulo.')

