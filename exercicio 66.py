# Vários Números com Flag

cont = total = 0

while True:
    n = int(input('Dígite um valor [999 para parar]:'))
    if n == 999:
        break
    cont += 1
    total += n
print(f'A soma dos {cont} valores foi {total}!')
