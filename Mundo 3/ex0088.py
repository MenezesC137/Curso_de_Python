from random import randint
from time import sleep
linha = '-' * 37
lista = list()
jogos = list()
print(linha)
print('{:^37}'.format(' Jogos da mega cena '))
print(linha)
quant = int(input('Quantos jogos você deseja sortear? '))
print('{:^37}'.format(f' Sorteando {quant} jogos'))
print(linha)
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for indice, lis in enumerate(jogos):
    print(f'Jogo {indice+1}: {lis}')
    sleep(1)
print('{:-^37}'.format('Boa sorte'))
