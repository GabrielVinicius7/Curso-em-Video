# Simulador de caixa eletrônico

print('--' * 11)
print('   BANCO DO BRASIL')
print('--' * 11)

nota50 = nota20 = nota10 = nota1 = 0

sacar = int(input('Que valor você quer sacar ?'))
total = sacar

while True:



    if total >= 50:
        total -= 50
        nota50 += 1

    if total < 50 and total >= 20:
        total -= 20
        nota20 +=1

    if total < 20 and total >= 10:
        total -= 10
        nota10 += 1

    if total < 10 and total >= 1:
        total -= 1
        nota1 += 1


    if total == 0:
        break

if nota50 >= 1:
    print(f'Total de {nota50} cédulas de R$50,00')
if nota20 >= 1:
    print(f'Total de {nota20} cédulas de R$20,00')
if nota10 >= 1:
    print(f'Total de {nota10} cédulas de R$10,00')
if nota1 >= 1:
    print(f'Total de {nota1} cédulas de R$1,00')


print('--' * 11)
print('    VOLTE SEMPRE!')
print('--' * 11)
