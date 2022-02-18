while True:
    print('-' * 35)
    tab = int(input('Quer ver a tabuada de qual valor? [0 para encerrar] '))
    print('-' * 35)
    if tab == 0:
        break
    print(f'Tabuada do {tab}')
    for cont in range(1, 11):
        resul = tab * cont
        print(f'{tab} x {cont} = {resul}')
print('Programa tabuada Encerrado,\nVolte sempre!')
