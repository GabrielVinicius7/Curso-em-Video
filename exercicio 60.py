# calculo de fatorial



print('Digite um número para ')
f = int(input('Calcular seu fatorial :'))
n = f
fat = 1

print('Calculando {}! = '.format(n),end='')
while n > 0:
    print('{}'.format(n),end='')
    print(" x " if n > 1 else " = ",end='')
    fat *= n
    n -= 1
print('{} '.format(fat))



