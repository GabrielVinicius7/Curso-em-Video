# Radar eletronico

v = float(input('Qual a velocidade atual do seu carro ?'))


if v > 80:
    print('MULTADO! Voce excedeu o limite permitido que é 80 km/h')
    print('Voce deve pagar uma multa de R${:.2f}!'.format(((v-80)*7)))
    print('Tenha um bom dia! Dirija com segurança!!')

print('Tenha um bom dia! Dirija com segurança!!')