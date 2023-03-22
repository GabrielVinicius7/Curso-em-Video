# Analisador de textos
import nome as nome

nome = str(input('Digite seu nome :')).strip( )
print('Analisando seu nome ...')
print('Seu nome em MAIUSCULAS é {}'.format(nome.upper()))
print('Seu nome me minusculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(" ")))

# Para encontrar o primeiro nome e quantidade de letras

primeiro = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras '.format(primeiro[0],len(primeiro[0])))