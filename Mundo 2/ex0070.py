soma = mais = menor = pri = 0
barato = ' '
linha = '-' * 31
print(linha)
print('Casas Bahia'.center(31))
print(linha)
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    print(linha)
    pri += 1
    soma += preco
    if preco >= 1000:
        mais += 1
    if pri == 1 or preco < menor:
        menor = preco
        barato = prod
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('{:-^30}'.format(' Fim do Programa '))
print(f'''O total da compra foi R${soma:.2f}
Temos {mais} produto(s) custando mais de R$ 1000.00
O produto mais barato foi {prod} que custa R$ {menor:.2f}''')
