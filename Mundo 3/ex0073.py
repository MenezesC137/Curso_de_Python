time = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
        'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
        'Atléco-GO', 'Santos', 'Ceará', 'Internacional',
        'São Paulo', 'Athetico-PR', 'Cuiabá', 'Juventude',
        'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
linha = '-' * 30
print(linha)
print(f'Lista de times Brasileiros: {time}')
print(linha)
print(f'Os 5 primeiros são: {time[:5]}')
print(linha)
print(f'Os 4 últimos são: {time[16:]}')
print(linha)
print(f'Times em ordem alfabética: {sorted(time)}')
print(linha)
for pos, cont in enumerate(time):
    if cont == 'Chapecoense':
        print(f'O {cont} está na {pos + 1}ª posição.')
