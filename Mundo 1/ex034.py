n1 = float(input('Qual salário do funcionário? R$ '))
if n1 < 1250:
    n2 = (n1 * 15) / 100 + n1
    print('Quem ganha R${} passa a receber R${}.'
          .format(n1, n2))
else:
    n3 = (n1 * 10) / 100 + n1
    print('Quem ganha R${} passa a receber R${}.'
          .format(n1, n3))
