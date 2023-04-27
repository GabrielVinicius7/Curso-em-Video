# Valores únicos em uma lista

#Iniciando as variaveis
n = []
total = []

# Començando o while true para realizar o questionario.

while True:

    # a variavel n foi iniciada para a entrada de dados, mas sem o append, para que não os valores se tornem um lista na variavel.
    n = (int(input('Digite um valor :')))
    # PONTO CHAVE: Onde ocorre a separação do dados para iniciar a variavel em lista (total).
    if n not in total:
        print('Valor adicionado com sucesso!')
        total.append(n)
    else:
        print('Valor duplicado! Não vou adicionar!')


    pergunta = str(input('Quer continuar ? [S/N]')).upper()[0]
    # Fazendo a separação dos dados (pergunta) com o if
    if pergunta == 'N':
        print('-=-'*30)
        print(f'Voce digitou os valores {total}.')

    if pergunta != 'S' and pergunta != 'N':
        print('INCORRETO! FINALIZANDO!')
        print(f'Voce digitou os valores {total}.')

        break






