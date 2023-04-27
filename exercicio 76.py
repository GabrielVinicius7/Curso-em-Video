# Lista de preços com Tuplas

mercadoria = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Caneta',2,'Livro',34.90)

print('-'*40)
print(F'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for c in range (0,len(mercadoria)):
    if c % 2 == 0:
        print(f'{mercadoria[c]:.<30}',end='')
    else:
        print(f'R$ {mercadoria[c]:7.2f}')
print('-'*40)


