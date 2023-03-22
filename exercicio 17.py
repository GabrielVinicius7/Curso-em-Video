# Catetos e Hipotenusa

'''from math import hypot, trunc

n1 = float(input('Comprimento do cateto oposto :'))
n2 = float(input('Comprimento do cateto adjascente :'))

print('A hipotenusa vai medir {:.2f}'.format(hypot(n1,n2)))'''

from math import sqrt

n1 = float(input('Comprimento do cateto oposto :'))
n2 = float(input('Comprimento do cateto adjascente :'))

soma = ((n1)**2) + ((n2)**2)

raiz = sqrt(soma)


print('A hipotenusa vai medir {:.2f}'.format())