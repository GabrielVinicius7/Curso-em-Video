# Soma dos pares

n1 = 0
cont = 0

for c in range (1,6+1):
    n = int(input('Digite o {}° valor:'.format(c)))
    if n % 2 == 0:
        n1 += n
        cont += 1
print('Você informou {} números e a soma foi {}.'.format(c,n1))
