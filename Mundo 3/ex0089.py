ficha = list()
linha = '-' * 25
#variaveis
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
#1ªCondição de parada
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if sn == 'N':
        break
#Menu
print(linha)
print(f'{"No.":<4}{"Nome":<12}{"Média":>7}')
print(linha)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<12}{aluno[2]:>5.1f}')
#2ªCondição de parada
while True:
    print(linha)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]:'))
    if opc == 999:
        print('Finalizando...')
        break
#Mostrando os dados do aluno solicitado
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
