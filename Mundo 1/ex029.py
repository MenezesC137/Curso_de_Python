ve = float(input('Qual é a velocidade atual do carro? '))
if ve > 80:
    multa = (ve - 80) * 7
    print('MULTADO! você excedeu o limite permitido que é de 80Km/h\n'
          'Você deve pagar uma multa de R${:.2f}'
          .format(multa))
print('Tenha um bom dia! Dirija com segurança!')

