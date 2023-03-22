 # Média

n1 = float(input('Primeira nota :'))
n2 = float(input('Segunda nota :'))

m = (n1+n2)/2

if m < 5:
     print('Tirando {} e {}, a média do aluno é {}'.format(n1,n2,m))
     print('O aluno está \033[31mREPROVADO!\033[m')
elif m >= 5 and m < 7:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, m))
    print('O aluno está \033[33mRECUPERÇÃO!\033[m')
else:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, m))
    print('O aluno está \033[34m APROVADO!\033[m')



