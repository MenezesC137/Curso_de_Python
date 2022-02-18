from random import randint
cont = 0
print('-=' * 12)
print('Vamos jogar Par ou Ímpar')
while True:
    print('-=' * 12)
    jogador = int(input('Diga um valor: '))
    pc = randint(1, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 24)
    print(f'Você jogou {jogador} e o Computador {pc}.\nTotal de {total} ', end='')
    print('Deu Par'if total % 2 == 0 else 'Deu Ímpar')
    print('-' * 24)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            cont += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            cont += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos Jogar novamente...')
print(f'Game over! Você venceu {cont} vezes.')
