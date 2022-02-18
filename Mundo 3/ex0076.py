lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25)
linha = '-' * 35
print(linha)
print(f'{"Listagem de preços":^35}')
print(linha)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<27}', end='')
    if pos % 2 == 1:
        print(f'R$ {lista[pos]:>5.2f}')
print(linha)
