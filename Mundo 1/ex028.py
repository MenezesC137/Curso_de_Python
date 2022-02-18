from random import randint
from time import sleep
co = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jo = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jo == co:
    print('PARABÉNS! Você conseguir me vencer!')
else:
    print('Tente novamente mais tarde!')
