# Grupo da Maioridade

from datetime import date

atual = date.today().year
menor = 0
maior = 0


for c in range(1,7):
    ano = int(input('Em que  ano a {}° pessoa nasceu ?'.format(c)))
    n = atual - ano
    if n >= 21:
        maior += 1

    else:
        menor += 1


print('O número de pessoas maiores de idade é {}'.format(maior))
print('O número de pessoas menores de idade é {}'.format(menor))