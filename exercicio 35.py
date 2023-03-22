# Analisando triangulos v1.0

print('-=-' * 20)

print('Analisador de triangulos')

print('-=-' * 20)

a = int(input('Digite o primeiro lado :'))
b = int(input('Digite o segundo lado :'))
c = int(input('Digite o terceiro  lado :'))

if a < b + c and b < a + c and c < a + b:
    print('Os lados adicionadas podem formar um Triangulo !!')
else:
    print('Os lados adicionadas não podem formar um Triangulo !!')





