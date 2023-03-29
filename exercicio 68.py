# Jogo Par ou Impar

from random import randint
vitoria = 0

while True:
    print('-=-'*10)
    print('VAMOS JOGAR PAR OU IMPAR !')
    print('-=-' * 10)
    valor = int(input('Diga um valor:'))
    maquina = randint(0,10)
    soma = valor + maquina
    jogada = str(input('Par ou Ímpar? [P/I]')).upper().split()[0]
    if soma % 2 == 0:
        print(f'Você jogou {valor} e o computador jogou {maquina}. total deu {soma} DEU PAR!   ')
        if jogada == 'P':
            print('Você VENCEU !\nVamos jogar novamente...')
            vitoria += 1
        else:
            print('Você Perdeu!')
            print('-=-'*10)
            print(f'GAME OVER! Você venceu {vitoria} vezes')
            break

    if soma % 2 != 0:
        print(f'Você jogou {valor} e o computador jogou {maquina}. total deu {soma} DEU IMPAR!  ')
        if jogada == 'I':
            print('Você VENCEU !\nVamos jogar novamente...')
            vitoria += 1
        else:
            print('Você Perdeu!')
            print('-=-' * 10)
            print(f'GAME OVER! Você venceu {vitoria} vezes')
            break
    print('--'*15)


