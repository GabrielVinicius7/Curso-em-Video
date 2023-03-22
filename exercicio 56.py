#Analisador Completo

media = 0
idadeH = 0
nomeH = ''
mulherF = 0

for c in range (1,3):
    print('-'*5,c,'°','-'*5)
    nome = str(input('nome:'))
    idade = int(input('idade:'))
    media += idade
    sexo= str(input('[M/F]:'))
    if c == 1 and sexo in 'Mm':
        idadeH = idade
        nomeH = nome
    if sexo in 'Mm' and idade > idadeH:
        idadeH = idade
        nomeH = nome
    if sexo in 'Ff' and idade < 20:
        mulherF += 1
print('A média de idade do grupo é de {:.0f} anos.'.format(media/c))
print('O homem mais velho tem {} de idade e seu nome é {}'.format(idadeH,nomeH))
print('Ao todo são {} mulheres com menos de 20 anos '.format(mulherF))


