jogador = dict()
gols = list()
total = 0
linha = '-' * 50
jogador['Nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for cont in range(1, part+1):
    gol = int(input(f'   Quantos gols na partida {cont}: '))
    gols.append(gol)
    total += gol
jogador['gols'] = gols
jogador['total'] = total
print(linha)
print(jogador)
print(linha)
for key, valor in jogador.items():
    print(f'O campo {key} tem o valor {valor} ')
print(linha)
ranking = sorted(jogador.items())
print(f'O jogador {jogador["Nome"]} jogou {part} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'  => Na partida {indice+1}, fez {valor} gols.')
print(f'Foi um total de {total} gols')
