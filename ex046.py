'''
Exercicio 046
'''

from time import sleep
import emoji

print(f'-=' * 20)
print(emoji.emojize('Ta na hora do Pipoco!! :bomb:', use_aliases=True))
print(f'-=' * 20)

print()
for timer in range(10, 0, -1):
    print(timer)
    sleep(1)
print(emoji.emojize(':collision:', use_aliases=True))
