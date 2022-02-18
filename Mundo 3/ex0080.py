maior = menor = meio = 0
val = list()
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > val[-1]:
        val.append(n)
        print('Foi adicionado na última posição da lista.')
    else:
        pos = 0
        while pos < len(val):
            if n <= val[pos]:
                val.insert(pos, n)
                print(f'Foi adcionado na posição {pos} da lista.')
                break
            pos += 1
print('-' * 30)
print(f'Os valores são {val}')
 