# Classificando Atletas

from datetime import date

a = int(input('Ano de nascimento :'))

ano = date.today().year

n = (ano - a)

if n < 10:
    print('O atleta tem {} anos. '.format(n))
    print('Classificação : MIRIM')
elif n < 15:
    print('O atleta tem {} anos. '.format(n))
    print('Classificação : INFANTIL')
elif n < 20:
    print('O atleta tem {} anos. '.format(n))
    print('Classificação : JUNIOR')
elif n < 26:
    print('O atleta tem {} anos. '.format(n))
    print('Classificação : SÊNIOR')
else:
    print('O atleta tem {} anos. '.format(n))
    print('Classificação : MASTER')

