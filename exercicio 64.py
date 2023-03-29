#Tratando Vários Valores

cont = contx =0

n = int(input('Dígite um numero [999 para parar]:'))

while n != 999:
    cont += n
    contx += 1
    n = int(input('Dígite um numero [999 para parar]:'))
print('Você digitou {} e a soma entre eles é de {}'.format(contx,cont))
