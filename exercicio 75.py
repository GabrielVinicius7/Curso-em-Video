# Análise de dados em um tupla

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número :'))
n3 = int(input('Digite mais um número :'))
n4 = int(input('Digite o último número :'))

armazenamento = (n1,n2,n3,n4)

print(f'Você digitou os valores {armazenamento}')


print(f'\n\nO valor 9 apareceu {armazenamento.count(9)} vezes.')
if armazenamento == 3:
    print(f'O número 3 foi digitado na posição {armazenamento.index(3) + 1}°')
else:
    print('O número 3 não foi digitado!')

print(f'Os números pares foram : ',end= '')

for p in armazenamento:
    if p % 2 == 0:
        print(p,end=' ')
