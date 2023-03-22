# Analisando triângulos V 2.0


a = int(input('Digite o primeiro lado :'))
b = int(input('Digite o segundo lado :'))
c = int(input('Digite o terceiro  lado :'))





if a < b + c and b < a + c and c < a + b:
    print('Os lados adicionadas podem formar um Triangulo ',end='')
    if a == b == c:
        print(' equilatero!')
    if a != b != c != a:
        print(' escaleno!')
    else:
        print('ISÓSCELES!')
else:
    print('Os lados adicionadas não podem formar um Triangulo !!')