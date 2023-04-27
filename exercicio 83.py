# Valindando expressões matemáticas

cont_esquerdo = 0
cont_direito = 0

expressao = input('Digite uma expressão:')

print(expressao)

for c in expressao:
    if c == '(':
        cont_esquerdo += 1
    elif c == ')':
        cont_direito += 1

if cont_esquerdo != cont_direito:
    print('Espressão está errada!')
else:
    print('Expressão está Válida')

