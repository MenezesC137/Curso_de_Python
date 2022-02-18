lista = str(input('Digite uma expressão: '))
pilha = []
for simb in lista:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('Expressão incorreta.')
