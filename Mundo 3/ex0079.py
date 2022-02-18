val = list()
linha = '-' * 30
while True:
    n = int(input('Digite um valor: '))
    if n not in val:
        val.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if sn == 'N':
        break
val.sort()
print(linha)
print(f'Você digitou os valores {val}')
