from random import randint
cont = maior = menor = 0
print(f'Os valores sorteados foram: ', end='')
for cont in range(0, 5):
    num = randint(0, 10)
    cont += 1
    print(num, end=' ')
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'''\nO maior valor sorteado foi {maior}.
O menor número sorteado foi {menor}.''')
