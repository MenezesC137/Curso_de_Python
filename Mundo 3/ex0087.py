matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = maior = somat = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}] '))
        if matriz[linha][coluna] % 2 == 0:
            somap += matriz[linha][coluna]
print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()
somat = matriz[0][2] + matriz[1][2] + matriz[2][2]
#for linha in range(0, 3):
#    somat += matriz[linha][2]
print('-' * 30)
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {somat}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
