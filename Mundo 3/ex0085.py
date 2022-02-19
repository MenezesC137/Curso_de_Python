num = [[], []]
linha = '-' * 30
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(linha)
num[1].sort()
num[0].sort()
print(f'''Os valores pares digitados foram: {num[0]}
Os valores ímpares digitados foram: {num[1]} ''')
