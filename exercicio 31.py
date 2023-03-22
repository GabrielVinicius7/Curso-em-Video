# Custo da Viagem

d = int(input('Qual é a distancia da sua viagem ?'))

print('Voce esta prestes a começar uma viagem de {}KM.'.format(d))

longas = d * 0.45
curtas = d * 0.50

if (d > 200):
    print('E o preço da sua passagem será de R${:.2f}'.format(longas))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(curtas))
