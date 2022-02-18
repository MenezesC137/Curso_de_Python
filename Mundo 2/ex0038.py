num1 = int(input('Digite o Primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 < num2:
    print('O número {} é maior que {}, logo o Segundo número é maior.'.format(num2, num1))
elif num1 > num2:
    print('O número {} é maior que {}, logo o Primeiro número e maior.'.format(num1, num2))
else:
    print('Ambos os números são iguais.')
