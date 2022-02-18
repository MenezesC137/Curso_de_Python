soma = 0
cont = 0
for c in range(0, 6):
    var = int(input('Digite um número: '.format(c)))
    if var % 2 == 0:
        soma += var
        cont += 1
print('A soma do(s) {} número(s) pares é: {}.'.format(cont, soma))