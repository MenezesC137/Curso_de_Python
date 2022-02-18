from time import sleep
final = False
print('-' * 35)
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
while not final:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} + {} = {}'.format(primeiro, segundo, soma))
        print('-' * 35)
    elif opcao == 2:
        multi = primeiro * segundo
        print('A multiplicação entre {} * {} = {}'.format(primeiro, segundo, multi))
        print('-' * 35)
    elif opcao == 3:
        if primeiro > segundo:
            print('Entre {} e {} o maior é {}.'.format(primeiro, segundo, primeiro))
            print('-' * 35)
        elif primeiro < segundo:
            print('Entre {} e {} o maior é {}.'.format(segundo, primeiro, segundo))
            print('-' * 35)
        else:
            print('Ambos são iguais {}.'.format(primeiro))
            print('-' * 35)
    elif opcao == 4:
        print('-' * 35)
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        final = True
        print('Finalizando...')
        print('-' * 35)
        sleep(3)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção invalida!\nSelecione outra opção abaixo:')
        print('-' * 35)
