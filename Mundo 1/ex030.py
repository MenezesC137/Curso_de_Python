nu = int(input('Me diga um número qualquer: '))
re = nu % 2
if re == 0:
    print('O número {} é par.'
          .format(nu))
else:
    print('O número {} é ímpar.'
          .format(nu))
