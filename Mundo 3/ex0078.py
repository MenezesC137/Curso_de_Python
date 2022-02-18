val = list()
linha = '-' * 30
for cont in range(0, 5):
    val.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(linha)
print(f'Foram digitados os seguintes valores: {val}')
maior = max(val)
menor = min(val)
print(f'O maior valor foi {max(val)} na posição ', end='')
for i, v in enumerate(val):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor foi {min(val)} na posição ', end='')
for i, v in enumerate(val):
    if v == menor:
        print(f'{i}... ', end='')
