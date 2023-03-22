# Soma ímpares múltiplos de três


n1 = 0
n2 = 0

for n in range (1,501):
    if n % 2 != 0 and n % 3 == 0:
        n1 += n
        n2 += 1
print('A soma dde todos os {} valores solicitados é {} .'.format(n2,n1))
