# maior e menor valor em tuplas

from random import randint

sorteio = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))


print('Os valores sorteados foram : ',end='')

for n in sorteio:
    print(f'{n}',end=' ')

print(f'\nO maior número foi : {max(sorteio)}')
print(f'O menor número foi : {min(sorteio)}')


