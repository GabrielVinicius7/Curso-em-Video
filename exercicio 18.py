#Seno, Cosseno e Tangente

from math import sin,tan,cos,radians

n = float(input('Digite o angulo que voce deseja :'))

seno = (sin(radians(n)))
cosseno = (cos(radians(n)))
tangente = (tan(radians(n)))

print('O angulo de {}° tem o seno de {:.2f}'.format(n,(seno)))
print('O angulo de {}° tem o cosseno de {:.2f}'.format(n,cosseno))
print('O angulo de {}° tem o tangente de {:.2f}'.format(n,tangente))