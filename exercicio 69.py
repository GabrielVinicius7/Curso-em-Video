# Analise de dados do grupo
from time import sleep

idade18 = homem = mulher20 = 0




while True:
    print('--' * 13)
    print('   CADASTRE UMA PESSOA')
    print('--' * 13)

    idade = int(input('Idade:'))
    if idade <= 0:
        print('IDADE ERRADA! MAIS UMA VEZ!')
        idade = int(input('Idade:'))
        print('--' * 13)
        if idade <= 0:
            print('Resposta incorreta! Finalizando ...')
            sleep(2)
            break

    if idade > 18:
        idade18 += 1


    sexo = str(input('Sexo: [M/F]')).upper().split()[0]
    print('--' * 13)
    if sexo != 'M' and sexo != 'F':
        print('LETRA ERRADA! MAIS UMA VEZ!')
        sexo = str(input('Sexo: [M/F]')).upper().split()[0]
        print('--' * 13)
        if sexo != 'M' and sexo != 'F':
            print('Resposta incorreta! Finalizando ...')
            sleep(2)
            break

    if 'M' in sexo:
        homem += 1
    if 'F' in sexo and idade < 20 :
        mulher20 += 1


    pergunta = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if pergunta != 'S' and pergunta != 'N':
        print('LETRA ERRADA! MAIS UMA VEZ!')
        pergunta = str(input('Quer continuar? [S/N]')).upper().split()[0]
        if pergunta != 'S' and pergunta != 'N':
            print('Resposta incorreta! Finalizando ...')
            sleep(2)
            break
    if 'N' in pergunta:
        break

print(f'\n\n\nTotal de pessoas com mais de 18 anos : {idade18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')