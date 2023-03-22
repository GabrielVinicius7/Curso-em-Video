# Progressão Aritmética v2.0

print('Gerador de P.A')
print('-='*10)

p = int(input('Primeiro termo:'))
r = int(input('Razão da P.A:'))

p1 = p

n = 10

print('{}'.format(p),end='')
while n != 0:
    print('{}'.format(' -> '),end='')
    if n > 1:
        p1 += r
        print('{}'.format(p1),end='')
    else :
        print('FIM!')
    n -= 1



