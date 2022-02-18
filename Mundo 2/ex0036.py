casa = float(input('Valor da casa? R$'))
salario: float = float(input('Salário: R$'))
anos = int(input('Anos para pagar:'))
parcelas = casa / (anos * 12)
minimo = salario * 30 / 100
print('O valor da casa {:.2f} em {} anos, fica com parcelas de {:.2f}.'.format(casa, anos, parcelas))
if parcelas <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado.')