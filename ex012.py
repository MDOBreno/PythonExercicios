'''
Exercicio 012
'''

preco = float(input('Qual é927 preço do produto? R$'))
desconto = 5
novo = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de {desconto}% vai custar R${novo:.2f}')

