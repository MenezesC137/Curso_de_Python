num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[m0 Número {} foi dividido {} vezes.'.format(num, total))
if total == 2:
    print('Portanto é primo!'.format(num))
else:
    print('Portanto não e primo!'.format(num))