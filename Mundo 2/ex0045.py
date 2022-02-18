from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Escolha uma das opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jog = int(input('Qual você escolhe? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('#' * 23)
print('O jogador jogou {}'.format(itens[jog]))
print('A Maquina jogou {}'.format(itens[pc]))
print('#' * 23)
if pc == 0:
    if jog == 0:
        print('Empate!')
    elif jog == 1:
        print('Jogador Vence!')
    elif jog == 2:
        print('Maquina vence!')
    else:
        print('Jogada Invalida!')
elif pc == 1:
    if jog == 0:
        print('Maquina vence!')
    elif jog == 1:
        print('Empate!')
    elif jog == 2:
        print('Jogador vence!')
    else:
        print('Jogada Invalida!')
elif pc == 2:
    if jog == 0:
        print('Jogador vence!')
    elif jog == 1:
        print('Maquina vence!')
    elif jog == 2:
        print('Empate!')
    else:
        print('Jogada Invalida!')