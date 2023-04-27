# Estatísticas em Produtos

print('--' * 13)
print('   LOJA SUPER BARATÃO')
print('--' * 13)


compras = produto1000 = produto = cont = 0
maisbarato = ' '


while True:
    nome = str(input('Nome do Produto:'))
    preco = int(input('Preço do Produto:'))
    # decobrindo o valor total gasto.
    compras += preco
    cont += 1
    # descobrindo o produto de menor valor.
    produto = preco
    if cont == 1 or preco < produto:
        produto = preco
        maisbarato = nome
    # descobrindo produto acima dos 1000 reais
    if preco > 1000:
        produto1000 +=1

    continuar = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if continuar == 'N':
        print('OK!')
        break
    if continuar != 'N' and continuar != 'S':
        print('incorreto! ULTIMA CHANCE!')
        continuar = str(input('Quer continuar? [S/N]')).upper().split()[0]
        if continuar != 'N' and continuar != 'S':
            print('OK!')
            break

print(f'O total da compra foi de R$ {compras:.2f}')
print(f'Temos {produto1000} custando mais que R$ 1000,00')
print(f'O produto mais barato foi {maisbarato} que custa R${produto:.2f}')
