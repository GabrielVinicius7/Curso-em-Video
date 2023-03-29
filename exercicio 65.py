# Maior e Menor valor

cont = media = maior = menor = 0

q = "S"

while 'N' not in q:
    n = int(input('Digite um número:'))
    cont += 1
    media += n

    if cont == 1:
        menor = maior = n
    else:
        if n <= menor:
            menor = n
        if n > maior:
            maior = n


    q = str(input('Quer continuar? [S/N]')).upper().split()[0]

print(f'Você digitou {cont} números e a média foi de {(media/cont):.2f}')
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
