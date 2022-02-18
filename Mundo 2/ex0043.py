peso = float(input('Qual é seu peso? (kg)'))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / (alt * alt)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Cuidado, está abaixo do peso recomendado!')
elif imc <= 25:
    print('Parabéns, está com o peso ideal!')
elif imc <= 30:
    print('Comece a se preocupar com a sua saúde, esta com sobre peso!')
elif imc <= 40:
    print('Entrou em estado de alerta, está na faixa de obesidade!')
elif imc > 40:
    print('Obesidade Mórbida, entre em contato com seu medico urgente!')