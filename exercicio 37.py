# Conversor de Bases númericas

a = int(input('\033[31mDígite um número inteiro : \033[m'))

print('Escolha uma das bases para conversão:')

print('[1] converter par BÍNARIO')
print('[2] converter par OCTAL')
print('[3] converter par HEXADECIMAL')

b = int(input('Sua opção :'))


if b == 1:
    a1 = bin(a)
    print('{} convertido para BINÁRIO é igual a {}'.format(a,a1[2::]))
elif b == 2:
    a2 = oct(a)
    print('{} convertido para BINÁRIO é igual a {}'.format(a,a2[2::]))
elif b == 3:
    a3 = hex(a)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(a,a3[2::]))
else:
    print('\033[31m OPÇÃO INVÁLIDA !! \033[m')