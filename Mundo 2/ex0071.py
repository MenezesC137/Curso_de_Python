linha = '=' * 30
print(linha)
print('{:^30}'.format('Banco'))
print(linha)
valor = int(input('Total a ser sacado: R$ '))
total = valor
cont = 0
cedula = 100
while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'O total de {cont} cédulas de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        cont = 0
        if total == 0:
            break
print(linha)
print('Volte sempre!')
