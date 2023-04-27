# Extraindo dados de uma lista

total = []
cont = 0

while True:
    n = int(input('Digite um valor:'))
    cont += 1
    total.append(n)

    pergunta = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if pergunta == 'n' or pergunta != 'S':
        break







print('-=-'*20)
print(f'Você digitou {cont} elementos.')
total.sort(reverse=True)
print(f'Os valores em ordem descrente são{total}')
for c in (total):
    if c == 5:
        print('O valor 5 faz parte da lista!')