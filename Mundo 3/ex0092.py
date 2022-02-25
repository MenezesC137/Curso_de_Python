from datetime import datetime
linha = '-' * 30
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['Carteira'] = int(input('Carteira de Trabalho (0 se não possuir): '))
if pessoa['Carteira'] == 0:
    print(linha)
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
if pessoa['Carteira'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + 35
    print(linha)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')
