# Game : pedra, papel e tesoura.

from time import sleep
from random import randint

print('Suas  Opções :')

print('[ 1 ] PEDRA ')
print('[ 2 ] PAPEL ')
print('[ 3 ] TESOURA ')

n = int(input('Qual é a sua jogada ?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

sorteio = randint(1,3)

print('-=-'*8)

if sorteio == 2:
    print('Computador jogou Papel ')
elif sorteio == 1:
    print('Computador jogou Pedra')
else:
    print('Computador jogou Tesoura')

if n == 1:
    print('Jogador jogou Pedra')
elif n == 2:
    print('Jogador jogou Papel')
elif n == 3:
    print('Jogador jogou Tesoura')
else:
    print('jogada invalida')

print('-=-'*8)

if n == 1 and sorteio == 2:
    print('JOGADOR PERDEU')
elif n == 2 and sorteio == 1:
    print('JOGADOR VENCEU')
elif n == 3 and sorteio == 2:
    print('JOGADOR VENCEU')
elif n == 1 and sorteio == 3:
    print('JOGADOR VENCEU')
elif n == 2 and sorteio == 3:
    print('JOGADOR PERDEU')
elif n == 3 and sorteio == 1:
    print('JOGADOR PERDEU')
elif n == sorteio:
    print('EMPATE')









