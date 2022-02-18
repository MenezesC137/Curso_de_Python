print('Desconto')
i = int(input('Valor do produto: '))
d = i * 5 / 100
f = i - d
print(' Comprando o produto no valor de {}$ com 5% de desconto sai por {}$, você acaba economizando {}$.'.format(i, f, d))

