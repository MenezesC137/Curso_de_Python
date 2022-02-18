tab = int(input('Qual tabuada deseja realizar: '))
print('Tabuada do {}'.format(tab))
for cont in range(0, 11):
    resul = tab * cont
    print('{} x {} = {}'.format(tab, cont, resul))
