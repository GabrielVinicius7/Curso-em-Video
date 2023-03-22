#calculando Descontos

n = (float(input('Qual é o preco do produto ? R$')))

print('O produto que custava R$ {}, na promoção com desconto de 5% vai custar R${:.2f} . '.format(n,(((5/100)*-n)+n)))