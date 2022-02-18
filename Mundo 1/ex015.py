print('Aluguel de carro!')
d = int(input('Quantos dias de alugado? '))
k = float(input('Quantos km percorridos? '))
td = d * 60
tk = k * 0.15
tt = td + tk
print('O aluguel do carro ficou R${:.2f}'.format(tt))