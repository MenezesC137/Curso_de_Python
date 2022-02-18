print('{:=^40}'.format('LOJA'))
preco = float(input('Preço das compras: R$ '))
print('''Formas de pagamento
      [ 1 ] à vista dinheiro/cheque.
      [ 2 ] à vista no cartão.
      [ 3 ] 2x no cartão.
      [ 4 ] 3x ou mais no cartão.''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desc = preco * 0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desc))
elif opcao == 2:
    desc = preco * 0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desc))
elif opcao == 3:
    print('Na compra em 2x de {:.2f}, o valor sai o da preço original {:.2f}.'.format(preco/2 , preco))
elif opcao == 4:
    parc = int(input('Quantas vezes deseja parcelas? '))
    juros = preco * 1.2
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, juros / parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, juros))
else:
    print('Escolha uma opção valida.') 