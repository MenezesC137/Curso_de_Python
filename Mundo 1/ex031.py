vi = float(input('Qual a distância da viagem? '))
if vi < 200:
    n1 = vi * 0.50
    print('A viagem custará R${:.2f}.'
          .format(n1))
else:
    n1 = vi * 0.45
    print('A viagem custará R${:.2f}.'
          .format(n1))
