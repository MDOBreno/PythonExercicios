'''
Exercicio 043
'''

altura = float(input('Qual a sua altura (m) ? '))
peso = float(input('Qual o seu peso (Kg) ? '))
imc = peso / (altura ** 2) #poderiamos arredondar para um int usando imc=round(valorFloat)
print(f'IMC={imc:.2f}')

if imc < 18.5:
    print('Abaxio do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

