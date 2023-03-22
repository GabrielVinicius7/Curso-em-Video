# Progressão Aritmética

print('='*28)
print('    10 TEMOS DE UM P.A     ')
print('='*28)

p = int(input('Primeiro termo :'))
r = int(input('Razão :'))

d = p + (11-1) * r

for c in range (p,d,2):
    print('{}'.format(c), end='->')
print('acabou')
