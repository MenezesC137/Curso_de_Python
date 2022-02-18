from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print(f'Os valores sorteados fora: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'''\nO maior valor sorteado foi {max(num)}.
O menor número sorteado foi {min(num)}.''')
