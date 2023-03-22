# Números Primos

n = int(input('Dígite um Número:'))
cont = 0

for c in range (1,n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')


if cont > 2:
    print('\n \033[mO número {} foi divisivel {} vezes \n E por isso ele NÃO É PRIMO !'.format(n,cont))
else:
    print('\n \033[mO número {} foi divisivel {} vezes \n E por isso ele É PRIMO !'.format(n, cont))



















