# Gerenciador de Pagamento


print('\033[34m=\033[m'*11,'\033[31mLojas Gabriel\033[m','\033[34m=\033[m'*11)

c = float(input('Preço das compras : R$ '))

print('FORMAS DE PAGAMENTOS')
print('[ 1 ] À vista dinheiro/cheque.')
print('[ 2 ] À vista no cartão. ')
print('[ 3 ] 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')

o = int(input('Qual a melhor opção :'))

if o == 1:
    print(' Sua compra de  R${:.2f} vai custar  R${:.2f} no final.'.format(c,(c-((c*10)/100))))
elif o == 2:
    print(' Sua compra de  R${:.2f} vai custar  R${:.2f} no final.'.format(c,(c-((c*5)/100))))
elif o == 3:
    print(' Sua compra NÃO terá alteração, e o valor será de   R${:.2f} '.format(c))
elif o == 4:
    n1 = int(input('Quantas parcelas :'))
    print('sua compra será parcelada em {:.2f} de R$ {:.2f} com juros '.format(n1,((((c*20)/100)+c))/n1))
    print(('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(c,(((c*20)/100)+c))))
