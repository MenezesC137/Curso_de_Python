num = int(input(' Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.\n'
      'Unidade {}.\n'
      'Dezena {}.\n'
      'Centena {}.\n'
      'Milhar {}.'
      .format(num, u, d, c, m,))
