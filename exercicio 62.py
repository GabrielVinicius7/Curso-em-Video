# Super Progressão Aritmetica

print('Gerador de P.A')
print('-='*10)

p = int(input('Primeiro termo:'))
r = int(input('Razão da P.A:'))
p1 = p
n = 10
cont = 10

print('{}'.format(p),end='')


while n != 0:
    print('{}'.format(' -> '),end='')
    if n > 1:
        p1 += r
        print('{}'.format(p1),end='')
    else :
        print('PAUSA!')
    n -= 1



q = int(input('Quantos termos você quer mostrar a mais ?'))

while q != 0:
    print('{}'.format(' -> '), end='')
    if q > 1:
        p1 += r
        print('{}'.format(p1), end='')
        q -= 1
    else:
        print('{} -> PAUSA!'.format(p1+r))
        cont += 1
        q = int(input('Quantos termos você quer mostrar a mais ?'))
print('Esta foi a quantida de termos mostrada : {}'.format(cont))
