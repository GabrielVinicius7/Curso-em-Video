# Aumento múltiplos

n = float(input('Dígite o seu salário :'))

if n > 1250:
    print(' Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(n,(((10*n)/100)+n)))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(n,(((15*n)/100)+n)))