# Aprovando Empréstimo

c = float(input('Qual o valor da casa ?'))
s = float(input('Qual o seu salário ?'))
t = int(input('Em quantos anos tu quer pagar a casa ?'))

# p = parcela
# t1 = quantidade de meses no ano
# p1 = porcentagem em relação ao salário

t1 = (t * 12)
p = (c/t1)
p1 = (s * 30)/100

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R${:.2f}'.format(c,t,p))

if p1 > s:
    print('Empréstimo \033[31m NEGADO !!!!')
else:
    print('Empréstimo pode ser \033[34mCONCEDIDO !!')


