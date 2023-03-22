# Maior e Menor valor

a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))

menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print('O menor valor digitado foi {}'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O maior valor digitado foi {}'.format(maior))