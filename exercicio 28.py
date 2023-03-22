# Jogo da adivinhação

from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar ...')
print('-=-'*20)

n = int(input('Em que número eu pensei ?'))

print('PROCESSANDO...')
sleep(3)

sorteio = randint(1,5)

if n == sorteio:
    print('PARABÉNS! Voce conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(sorteio,n))




