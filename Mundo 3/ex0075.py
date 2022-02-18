cont = 0
n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite outro número: '))
n3 = int(input(f'Digite mais um número: '))
n4 = int(input(f'Digite o último número: '))
num = (n1, n2, n3, n4)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não aparece em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for duo in num:
    if duo % 2 == 0:
        print(duo, end='')

