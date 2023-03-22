# maior e menor da sequencia

menor = 0
maior = 0


for c in range (1,6):
    peso = float(input('Peso da {}° pessoa:'.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {} KG'.format(maior))
print('O menor peso foi de {} KG'.format(menor))