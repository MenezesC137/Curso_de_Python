plus = masc = fem = 0
while True:
    print('-' * 27)
    print('    Cadastre uma pessoa')
    print('-' * 27)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 27)
    if idade >= 18:
        plus += 1
    if sexo == 'M':
        masc += 1
    if idade < 20 and sexo == 'F':
        fem += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-' * 27)
print(f'''Total de pessoas com mais de 18 anos: {plus}
Ao todo temos {masc} homem(s) cadastrado(s)
E temos {fem} mulher(es) com menos de 20 anos''')
