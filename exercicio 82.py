# Divindindo valores em várias listas


total = []
pares = []
impares = []



while True:
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    total.append(n)

    pergunta = str(input('Quer continuar? [S/N]:')).upper().strip()[0]

    if pergunta == 'N' or pergunta != 'S':
        break

print(f'A lista completa é {total}')
print(f'A listade pares é {pares}')
print(f'A lista de Ímpares é {impares}')