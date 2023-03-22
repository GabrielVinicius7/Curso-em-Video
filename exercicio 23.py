# Separando digitos de um numero

n = int(input('Informe um numero :'))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o numero {}'.format(n))


print('unidade: {}\nDezena: {}\nCentena:{}\nMilhar: {}'.format(u,d,c,m))