# Índice de masssa corporal

p = float(input('Qual o seu peso (KG) :'))
a = float(input('Qual é a sua altura (M) :'))

imc = p / (a**2)

if imc < 18.5:
    print('O IMC dessa pessoa é de {:.2f}'.format(imc))
    print('Abaixo do Peso')
elif imc < 26:
    print('O IMC dessa pessoa é de {:.2f}'.format(imc))
    print('Peso ideal')
elif imc < 31:
    print('O IMC dessa pessoa é de {:.2f}'.format(imc))
    print('Soprepeso')
elif imc < 41 :
    print('O IMC dessa pessoa é de {:.2f}'.format(imc))
    print('Obesidade')
else:
    print('O IMC dessa pessoa é de {:.2f}'.format(imc))
    print('Obesidade Mórbida')