'''
Exercicio 026
'''

frase = str(input('Digite uma frase: ')).strip()
fraseUpper = frase.upper()
letra = 'A'
aparicoes = fraseUpper.count(letra)
print(f'A letra {letra} apareceu {aparicoes} vezes.')

if aparicoes>0 :
    primeiraPosicao = fraseUpper.find(letra)
    ultimaPosicao = len(fraseUpper[:primeiraPosicao])
    fraseUpper = fraseUpper[primeiraPosicao + 1:]
    aparicoes = aparicoes - 1
    print(f'A primeira aparição é na posição {primeiraPosicao}')

    while aparicoes>0:
        primeiraPosicao = fraseUpper.find(letra)
        ultimaPosicao = ultimaPosicao + len(fraseUpper[:primeiraPosicao]) + 1
        fraseUpper = fraseUpper[primeiraPosicao + 1:]
        aparicoes = aparicoes - 1
    print(f'A ultima aparição é na posição {ultimaPosicao}')

# -----------------------------------------------------------------------------

ultimaPosicao = frase.upper().rfind(letra)
print(f'A ultima aparição é na posição {ultimaPosicao}')










