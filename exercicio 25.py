# Procurando uma string dentro de outra

nome = str(input('Qual é o seu nome completo ?')).lower()
silva = 'silva' in nome
print('Seu nome tem silva ? {}'.format(silva))
