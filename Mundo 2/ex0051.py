print('=' * 30)
print('     10 Termos de uma PA    ')
print('=' * 30)
termo = int(input('Primerio termo: '))
razao = int(input('Razão: '))
decimo = termo + (11 - 1) * razao
for c in range(termo, decimo, razao):
    print('{}'.format(c), end=' > ')
print('Finish!')
