num = int(input('Digite um número para\nCalcular o seu Fatorial: '))
c = num
fator = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    fator *= c
    c -= 1
print('{}'.format(fator))
