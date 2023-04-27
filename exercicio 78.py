# Maior e Menor valores na lista

total = []
mai = men = 0

for c in range(0,4):
    total.append(int(input(f'Dígite um valor para a Posição {c+1}:')))
    if c == 0:
        mai = men = total[c]
    else:
        if total[c] > mai:
            mai = total[c]
        if total[c] < men:
            men = total[c]
print('=-'*25)

print(f'Você digitou os valores {total}')

print(f'O maior valor digitado foi {mai} na posição: ',end='')

for i,v in enumerate(total):
    if v == mai:
        print(f'{i+1}°...',end=' ')
print()

print(f'O menor valor digitado foi {men} na posição: ',end='')

for i,v in enumerate(total):
    if v ==men:
        print(f'{i+1}°...',end='')
print()


