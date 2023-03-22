# Alistamento Militar

from datetime import date


a = int(input('Ano de nascimento :'))

ano = date.today().year

anos = (ano - a)

# n1 = diferença entre quantos anos tem e quantos anos prescisa para se alistar

n1 = 18 - anos

print('Quem nasceu em {} tem {} anos em {}.'.format(a,anos,ano))

if anos < 18:
    print('Ainda faltam {} anos para o alistamento !!'.format(n1))
    print('\033[7mSeu alistamento será em {}.\033[m'.format(ano + n1))
else :
    print('\033[31mVoce já deveria ter se alistado !!')
