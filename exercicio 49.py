# Tabuada V 2.0

t = int(input('Dígite um número para ver sua tabuada :'))

for c in range (0,11):
    print('{} X {:2} = {}'.format(t,c,t*c))