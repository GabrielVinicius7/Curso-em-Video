# Jogo da adivinhação 2.0
from random import randint

print('Sou seu computador ...')

print('acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')

palpite = int(input('Qual é o seu palpite ?'))

sorteio = randint(0,10)

erro = 0

while palpite != sorteio:
    if sorteio > palpite:
        palpite = int(input('MAIS... Tente mais uma vez.'))
    elif sorteio < palpite:
        palpite = int(input('MENOS... Tente mais uma vez.'))

    erro += 1
print('ACERTOU!, e errou {} 5'
      'vezes.'.format(erro))