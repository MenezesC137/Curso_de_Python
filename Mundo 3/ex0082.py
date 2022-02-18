lista = list()
impares = list()
pares = list()
linha = '-' * 30
while True:
    lista.append(int(input('Digite um número: ')))
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if sn == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
lista.sort()
print(linha)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')
