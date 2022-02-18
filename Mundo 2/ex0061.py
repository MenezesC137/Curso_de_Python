print('=' * 30)
print('     10 Termos de uma PA    ')
print('=' * 30)
primeiro = int(input('Primerio termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('Acabou!')
