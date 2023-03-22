# Criando um Menu

n1 = int(input("Primeiro valor :"))
n2 = int(input("Segundo valor :"))

opcoes = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n>>>>> Qual é a sua opção ?\n'))


while opcoes != 5:
    if opcoes == 1:
        print('A soma entre {} e {} é {}.'.format(n1,n2,(n1+n2)))
    if opcoes == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1,n2,(n1*n2)))
    if opcoes == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é {}.'.format(n1,n2,(n1)))
        elif n2 > n1:
            print('O maior número entre {} e {} é {}.'.format(n1,n2,(n2)))
        elif n1 == n2:
            print('NÃO SE A DIFERENÇA!!')
    if opcoes == 4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
        opcoes = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n>>>>> Qual é a sua opção ?'))

    else:
        opcoes = int(input('\nDE NOVO,\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n>>>>> Qual é a sua opção ?'))

print('OBRIGADO!')

