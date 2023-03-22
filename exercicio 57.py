# Validação de dados


sexo = str(input('Informe seu sexo : [M/F]')).upper().strip()[0 ]

while sexo not in 'FMmf':
    sexo = str(input('inválido, informe seu sexo : [M/F]')).strip().upper()[0]
print('Sexo preenchido : {}, obrigado!'.format(sexo))

