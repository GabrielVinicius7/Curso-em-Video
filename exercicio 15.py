# Aluguel de carros

n = (float(input('Quantos dias alugados ?')))
n2 = (float(input('Quantos KM rodados ?')))

valor = (n*60) + (n2*0.15)

print('O total a pagar é de R$ {:.2f}'.format(valor))