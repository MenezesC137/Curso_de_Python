num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze',
       'dezeseis', 'dezecete', 'dezoito', 'dezenove', 'vinte')
linha = '-' * 30
print('Contagem de número por extenso')
print(linha)
while True:
    dig = int(input('Digite um número entre 0 e 20: '))
    while 0 < dig > 20:
        print('Tente Novamente.')
        dig = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {num[dig]}.')
    print(linha)
    deseja = ' '
    while deseja not in 'SN':
        deseja = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if deseja == 'N':
        break
print('{:-^30}'.format(' Fim do Programa '))
