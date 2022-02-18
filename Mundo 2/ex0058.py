from random import randint
pc = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número de 0 a 10.
Será que consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
    jogador = float(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!!!'.format(palpite))
