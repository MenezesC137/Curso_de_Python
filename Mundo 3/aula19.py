#.values()
#.keys()
#.items()
#pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['Sexo']
#pessoas['Nome'] = 'Leandro'
#pessoas['Peso'] = 98.5
#for key, val in pessoas.items():
#    print(f'{key} = {val}')

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'Rj'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'Sp'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[1]['uf'])

#estado = dict()
#brasil = list()
#for cont in range(0, 3):
#    estado['uf'] = str(input('Unidade Federativo: '))
#    estado['sigla'] = str(input('Sigla: '))
#    brasil.append(estado.copy())
#for e in brasil:
#    for key, valor in e.items():
#        print(f'O campo {key} tem valor {valor}.')
#    for v in e.values():
#        print(v, end=' ')
#    print()
