maior = 0
menor = 0
for cont in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior é {}Kg.'.format(maior))
print('O menor é {}Kg.'.format(menor))