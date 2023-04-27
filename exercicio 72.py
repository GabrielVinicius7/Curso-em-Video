# Número por extenso

total = ('zero','um','dois','três','quatro','cinco','seis','sete',
         'oito','nove','dez','onze','doze','treze',
         'quatorze','quinze','dezesseis','dezesste',
         'dezoito','dezenove','vinte')


while True:
    n = int(input('Digite um número entre 0 e 20 :'))

    if n < 0 or n > 20:
        print('INCORRETO')
        break

    print(f'Você digitou o número {n} e ele por extenso é {total[n]}.')




