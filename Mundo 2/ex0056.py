media = 0
soma = 0
maior = 0
velho = 0
totmu = 0
for cont in range(1, 5):
    print('-----{}ª Pessoa -----'.format(cont))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if cont == 1 and sexo in 'Mm':
         maior = idade
         velho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        totmu += 1
media = soma / 4
print('A média de idade do grupo é de {:.2f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmu))