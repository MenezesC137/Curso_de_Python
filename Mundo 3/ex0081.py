lista = list()
linha = '-' * 30
while True:
    lista.append(int(input('Digite um valor: ')))
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if sn == 'N':
        break
lista.sort(reverse=True)
print(linha)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista})')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('Não temos o valor 5 na lista!')
