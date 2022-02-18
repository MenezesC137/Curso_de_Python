pessoa = list()
dado = list()
maior = menor =  0
linha = '-' * 30
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoa.append(dado[:])
    dado.clear()
    sn = ' '
    while sn not in "SN":
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if sn == 'N':
        break
print(linha)
print(f'Ao todo, você cadastrou {len(pessoa)} pessoas.')
print(f'O maior peso foi de {maior}Kg, ', end='')
for per in pessoa:
    if per[1] == maior:
        print(f'[{per[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg, ', end='')
for per in pessoa:
    if per[1] == menor:
        print(f'[{per[0]}] ', end='')
print()
